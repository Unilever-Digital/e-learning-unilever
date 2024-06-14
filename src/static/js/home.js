const workview = document.querySelector('#work-view');

for (let i = 1; i <= 8; i++) {
    const container = document.createElement('div');
    container.classList.add('container-catalog');
    container.id = 'catalog' + i;
    container.textContent = "";
    container.addEventListener('click', handleClick);
    workspace.appendChild(container);
}

