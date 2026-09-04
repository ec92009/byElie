/* Web Signals browser beacon v1.1.0 — aggregate mode uses no visitor/session identifier. */
(function installWebSignals(window, document, navigator) {
  "use strict";

  try {
    const script = document.currentScript;
    if (!script) return;

    const config = {
      enabled: script.dataset.wstEnabled === "true",
      endpoint: script.dataset.wstEndpoint || "",
      siteId: script.dataset.wstSite || "",
      environment: script.dataset.wstEnvironment || "production",
      consentState: script.dataset.wstConsent || "unknown",
      synthetic: script.dataset.wstSynthetic === "true",
      sessionless: script.dataset.wstSessionless === "true",
    };
    const allowedConsent = new Set(["granted", "denied", "not_required", "unknown"]);
    const allowedEnvironment = new Set(["production", "preview", "staging", "development", "test"]);
    const allowedBrowserEvents = new Set(["page_view", "cta_press"]);
    const stableId = /^[a-z][a-z0-9._-]{1,63}$/;
    const siteId = /^[a-z][a-z0-9-]{2,47}$/;
    let pageViewSent = false;

    if (!config.enabled) return;
    if (!siteId.test(config.siteId) || !allowedEnvironment.has(config.environment)) return;
    if (!allowedConsent.has(config.consentState)) config.consentState = "unknown";
    if (navigator.globalPrivacyControl === true || navigator.doNotTrack === "1") config.consentState = "denied";

    const endpoint = new URL(config.endpoint, window.location.href);
    if (endpoint.protocol !== "https:" && endpoint.hostname !== "127.0.0.1" && endpoint.hostname !== "localhost") return;
    endpoint.search = "";
    endpoint.hash = "";

    function normalizePath(value) {
      const path = String(value || "/").split(/[?#]/, 1)[0].replace(/\/{2,}/g, "/");
      if (!path.startsWith("/")) return "/";
      const withoutDefault = path.replace(/\/index\.html$/i, "/");
      return withoutDefault.length > 1 ? withoutDefault.replace(/\/$/, "") : "/";
    }

    function isAllowedToSend() {
      return config.consentState === "granted" || config.consentState === "not_required";
    }

    function transmit(payload) {
      const body = JSON.stringify(payload);
      try {
        if (typeof navigator.sendBeacon === "function" && navigator.sendBeacon(endpoint.href, body)) return;
      } catch {
        // A blocked beacon must never affect the host site's interaction.
      }
      try {
        void window.fetch(endpoint.href, {
          method: "POST",
          body,
          keepalive: true,
          mode: "cors",
          credentials: "omit",
          headers: { "Content-Type": "text/plain;charset=UTF-8" },
        }).catch(() => {});
      } catch {
        // Analytics failure is deliberately silent and non-blocking.
      }
    }

    function track(eventName, eventProperties = {}) {
      if (!isAllowedToSend() || !allowedBrowserEvents.has(eventName)) return false;
      const properties = { path: normalizePath(window.location.pathname) };
      if (eventName === "cta_press") {
        if (!stableId.test(eventProperties.cta_id || "")) return false;
        properties.cta_id = eventProperties.cta_id;
      }
      transmit({
        schema_version: "wst.event.v1",
        event_id: window.crypto.randomUUID(),
        occurred_at: new Date().toISOString(),
        site_id: config.siteId,
        environment: config.environment,
        event_name: eventName,
        source: "browser",
        synthetic: config.synthetic,
        bot_classification: navigator.webdriver ? "known_bot" : "unknown",
        consent_state: config.consentState,
        properties,
      });
      return true;
    }

    document.addEventListener("click", (event) => {
      const target = event.target instanceof Element ? event.target.closest("[data-wst-cta]") : null;
      if (target) track("cta_press", { cta_id: target.dataset.wstCta });
    }, true);

    window.WebSignals = Object.freeze({ track });
    if (!pageViewSent && isAllowedToSend()) pageViewSent = track("page_view");
  } catch {
    // Installation failure must never break the host page.
  }
})(window, document, navigator);
