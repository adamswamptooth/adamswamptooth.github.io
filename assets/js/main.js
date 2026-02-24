const menuToggle = document.querySelector('[data-menu-toggle]');
const menuOverlay = document.querySelector('[data-menu-overlay]');

if (menuToggle && menuOverlay) {
  const closeMenu = () => {
    menuOverlay.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
  };

  menuToggle.addEventListener('click', () => {
    const isOpen = menuOverlay.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', String(isOpen));
  });

  menuOverlay.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      closeMenu();
    }
  });
}
