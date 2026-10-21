/*
  for site search component. searches site/domain via Bing (Google is blocked in mainland China;
  Bing also works there).
*/

{
  // when user submits site search form/box
  window.onSiteSearchSubmit = (event) => {
    event.preventDefault();
    const engine = "https://www.bing.com/search?q=site:";
    const site = window.location.origin;
    const query = event.target.elements.query.value;
    window.location = engine + site + " " + query;
  };
}
