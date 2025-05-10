document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const hashtags = document.getElementById('hashtags').value.split(',');

    console.log({ username, password, hashtags });  // Add this line
    
    // Show the spinner
    const spinner = document.getElementById('spinner');
    spinner.style.display = 'block';

    fetch('/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password, hashtags })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Followers process initiated successfully!');
    })
    .catch((error) => {
        console.error('Error:', error);
    })
    .finally(() => {
        // Hide the spinner
        spinner.style.display = 'none';
    });
});
