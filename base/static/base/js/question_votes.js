// question_votes.js

document.addEventListener('DOMContentLoaded', function () {
  // Upvote Question
  document.querySelectorAll('.upvote-question').forEach(button => {
    button.addEventListener('click', function () {
      const questionId = this.dataset.questionId;
      fetch(`/upvote/question/${questionId}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,  // CSRF token for safety
        },
      })
      .then(response => response.json())
      .then(data => {
        this.nextElementSibling.innerHTML = `Upvotes: ${data.upvotes}`;
        this.nextElementSibling.nextElementSibling.innerHTML = `Downvotes: ${data.downvotes}`;
      });
    });
  });

  // Downvote Question
  document.querySelectorAll('.downvote-question').forEach(button => {
    button.addEventListener('click', function () {
      const questionId = this.dataset.questionId;
      fetch(`/downvote/question/${questionId}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
      })
      .then(response => response.json())
      .then(data => {
        this.previousElementSibling.innerHTML = `Upvotes: ${data.upvotes}`;
        this.previousElementSibling.nextElementSibling.innerHTML = `Downvotes: ${data.downvotes}`;
      });
    });
  });

  // Upvote Reply
  document.querySelectorAll('.upvote-reply').forEach(button => {
    button.addEventListener('click', function () {
      const replyId = this.dataset.replyId;
      fetch(`/upvote/reply/${replyId}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
      })
      .then(response => response.json())
      .then(data => {
        this.nextElementSibling.innerHTML = `Upvotes: ${data.upvotes}`;
        this.nextElementSibling.nextElementSibling.innerHTML = `Downvotes: ${data.downvotes}`;
      });
    });
  });

  // Downvote Reply
  document.querySelectorAll('.downvote-reply').forEach(button => {
    button.addEventListener('click', function () {
      const replyId = this.dataset.replyId;
      fetch(`/downvote/reply/${replyId}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
      })
      .then(response => response.json())
      .then(data => {
        this.previousElementSibling.innerHTML = `Upvotes: ${data.upvotes}`;
        this.previousElementSibling.nextElementSibling.innerHTML = `Downvotes: ${data.downvotes}`;
      });
    });
  });
});
