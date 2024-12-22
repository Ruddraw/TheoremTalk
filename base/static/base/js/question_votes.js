document.addEventListener("DOMContentLoaded", function () {
  // Function to handle voting for questions or replies
  function handleVote(button, url, voteType) {
      const questionId = button.getAttribute('data-question-id');
      
      // Disable the button to prevent multiple clicks
      button.disabled = true;

      // Send AJAX request to upvote/downvote the question
      fetch(url, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
          },
          body: JSON.stringify({ vote_type: voteType }) // Send the vote type in the body
      })
      .then(response => {
          if (!response.ok) {
              return response.json().then(data => {
                  alert(data.error); // Alert user if they've already voted or another error
                  button.disabled = false;
                  return;
              });
          }

          return response.json();
      })
      .then(data => {
          if (data) {
              const upvotesSpan = button.closest('.question-votes').querySelector('.upvotes');
              const downvotesSpan = button.closest('.question-votes').querySelector('.downvotes');
              upvotesSpan.textContent = data.upvotes;
              downvotesSpan.textContent = data.downvotes;

              // Update button visibility and disable state
              const oppositeButton = button.closest('.question-votes').querySelector(voteType === 'upvote' ? '.downvote-question' : '.upvote-question');
              oppositeButton.style.display = 'none'; // Hide the opposite button after voting
              button.disabled = true; // Disable the voted button
          }
      })
      .catch(error => console.error('Error:', error));
  }

  // Add event listeners for upvote and downvote buttons
  const upvoteButtons = document.querySelectorAll('.upvote-question');
  upvoteButtons.forEach(button => {
      button.addEventListener('click', function () {
          handleVote(this, `/upvote_question/${this.getAttribute('data-question-id')}/`, 'upvote');
      });
  });

  const downvoteButtons = document.querySelectorAll('.downvote-question');
  downvoteButtons.forEach(button => {
      button.addEventListener('click', function () {
          handleVote(this, `/downvote_question/${this.getAttribute('data-question-id')}/`, 'downvote');
      });
  });
});
