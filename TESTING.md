# Testing

Back to [Readme file.](README.md)

## Table of Contents
- [Functionality Testing](#functionality-testing)
- [Browser Compatability](#browser-compatability)
- [Code Validation](#code-validation)
- [Performance Testing](#performance-testing)
- [User Stories Testing](#user-stories-testing)
- [Bugs](#bugs)

---
## Functionality Testing

---
## Browser Compatability

---
## Code Validation

---
## Performance Testing

---
## User Stories Testing

---
## Bugs

**Bug:** The dropdown menu for the "My Account" icon was not working with Bootstrap 5.

**Fix:** The solution was to add the following code JavaScript code:

```
<script 
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" 
    crossorigin="anonymous">
</script>
```

**Bug:** The Toast popups would not close when the 'X' button was clicked with Bootstrap version 5.

**Fix:** The solution was to: 

1. Firstly, change the 'data-toggle' attribute to 'data-bs-toggle'.

2. Secondly, add the following JavaScript code to the postloadjs block:

```
<script type="text/javascript">
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    var toastList = toastElList.map(function(toastEl) {
    // Creates an array of toasts (it only initializes them)
    return new bootstrap.Toast(toastEl); // No need for options; use the default options
    });
    toastList.forEach(toast => toast.show()); // This show them
</script>
```

**Bug:** There was an issue with horizontal scrolling associated with the footer on smaller screen sizes.

**Fix:** The solution was to make each column in the footer row take up the full width of the row on smaller screen sizes.