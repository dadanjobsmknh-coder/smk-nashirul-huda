import {loadShell} from './component-loader.js';import {initNavbar} from './navbar.js';import {initSearch} from './search.js';import {initModals} from './modal.js';import {initAccessibility} from './accessibility.js';
async function init(){await loadShell();initNavbar();initSearch();initModals();initAccessibility();document.querySelectorAll('[data-current-year]').forEach(el=>el.textContent=new Date().getFullYear());document.documentElement.classList.add('js-ready');}
init();
