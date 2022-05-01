const list = document.getElementById('results')

const sortName = document.getElementById('sort-name')
sortName.onclick = () => {
    let switching = true
    while (switching) {
        switching = false
        const listItems = list.getElementsByTagName('li')
        const itemNames = []
        for (let i = 0; i < listItems.length; i++) {
            itemNames.push(listItems[i].getElementsByClassName('name')[0].textContent)
        }
        for (let i = 0; i < listItems.length - 1; i++) {
            if (itemNames[i].toLowerCase() > itemNames[i + 1].toLowerCase()) {
                listItems[i].parentNode.insertBefore(listItems[i + 1], listItems[i])
                switching = true
                break
            }
        }
    }
}

const sortPrice = document.getElementById('sort-price')
sortPrice.onclick = () => {
    let switching = true
    while (switching) {
        switching = false
        const listItems = list.getElementsByTagName('li')
        const itemPrices = []
        for (let j = 0; j < listItems.length; j++) {
            itemPrices.push(parseInt(listItems[j].getElementsByClassName('price')[0].textContent))
        }
        for (let i = 0; i < listItems.length - 1; i++) {
            if (itemPrices[i] > itemPrices[i + 1]) {
                listItems[i].parentNode.insertBefore(listItems[i + 1], listItems[i])
                switching = true
                break
            }
        }
    }
}