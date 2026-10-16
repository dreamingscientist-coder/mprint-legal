(() => {
  const languages = ['en', 'fr', 'vi'];
  const tabs = [...document.querySelectorAll('[role="tab"]')];
  const panels = [...document.querySelectorAll('[role="tabpanel"]')];
  const preferenceKey = 'mprint-language';
  let saved;
  try { saved = localStorage.getItem(preferenceKey); } catch (_) { /* Optional preference. */ }
  function select(language, focus = false) {
    if (!languages.includes(language)) language = 'en';
    for (const tab of tabs) {
      const active = tab.id === `tab-${language}`;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
      if (active && focus) tab.focus();
    }
    for (const panel of panels) panel.hidden = panel.lang !== language;
    document.documentElement.lang = language;
    document.title = document.getElementById(`panel-${language}`).dataset.title;
    try { localStorage.setItem(preferenceKey, language); } catch (_) { /* Tabs still work. */ }
    const url = new URL(location.href);
    url.searchParams.set('lang', language);
    history.replaceState(null, '', url);
  }
  for (const tab of tabs) {
    tab.addEventListener('click', event => {
      event.preventDefault();
      select(tab.lang);
    });
    tab.addEventListener('keydown', event => {
      const index = languages.indexOf(tab.lang);
      const targets = { ArrowRight: (index + 1) % 3, ArrowLeft: (index + 2) % 3, Home: 0, End: 2 };
      if (!(event.key in targets)) return;
      event.preventDefault();
      select(languages[targets[event.key]], true);
    });
  }
  const requested = new URL(location.href).searchParams.get('lang');
  select(requested || saved || 'en');
  document.documentElement.classList.remove('no-js');
})();
