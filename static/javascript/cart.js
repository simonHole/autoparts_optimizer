console.log('Hello World');

var updateButtons = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function () {
        var partID = this.dataset.product
        var action = this.dataset.action
        console.log(`Part ID: ${partID}, Action: ${action}`);
    })
}