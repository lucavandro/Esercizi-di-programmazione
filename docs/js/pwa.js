var divInstall = document.querySelector("#add-to-homescreen");
var btnAdd = document.querySelector("#install");
var btnClose   = document.querySelector("#add-to-homescreen .close");

window.addEventListener('beforeinstallprompt', (event) => {
    console.log('👍', 'beforeinstallprompt', event);
    event.preventDefault();
    // Stash the event so it can be triggered later.
    window.deferredPrompt = event;
    // Remove the 'hidden' class from the install button container
    divInstall.classList.toggle('hidden', false);
  });

  window.addEventListener('appinstalled', (evt) => {
    divInstall.classList.toggle('hidden', true);
  });


  btnAdd.addEventListener('click', (e) => {
    // hide our user interface that shows our A2HS button
    divInstall.classList.toggle('hidden', true);
    // Show the prompt
    deferredPrompt.prompt();
    // Wait for the user to respond to the prompt
    deferredPrompt.userChoice
      .then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('User accepted the A2HS prompt');
        } else {
          console.log('User dismissed the A2HS prompt');
        }
        deferredPrompt = null;
      });
  });


  btnClose.addEventListener('click', (e) => {
    divInstall.classList.toggle('hidden', true);
  });