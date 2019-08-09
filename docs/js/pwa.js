window.addEventListener('beforeinstallprompt', (event) => {
    console.log('👍', 'beforeinstallprompt', event);
    event.preventDefault();
    // Stash the event so it can be triggered later.
    window.deferredPrompt = event;
    // Remove the 'hidden' class from the install button container
    document.querySelector("#pwa").classList.toggle('hidden', false);

    // listen for click event
    document.querySelector("#pwa").addEventListener('click', (e) => {
        // hide our user interface that shows our A2HS button
        document.querySelector("#pwa").classList.toggle('hidden', true);
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
    });

  window.addEventListener('appinstalled', (evt) => {
    document.querySelector("#pwa").classList.toggle('hidden', true);
  });


  