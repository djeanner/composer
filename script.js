document.addEventListener('DOMContentLoaded', function() {
    fetch('composers.json')
        .then(response => response.json())
        .then(data => {
            const composerList = document.getElementById('composerList');
            data.composers.forEach(composer => {
                const composerLink = document.createElement('a');
                composerLink.href = composer.lastName.toLowerCase() + '.html';
                composerLink.innerText = composer.fullName;
                composerList.appendChild(composerLink);
                composerList.appendChild(document.createElement('br'));
            });
        });
});

