const list = document.getElementById('results')
let descendingName = false
let descendingPrice = false

const sortName = document.getElementById('sort-name')
sortName.onclick = () => {
    descendingName = !descendingName
    let switching = true
    while (switching) {
        switching = false
        const listItems = list.getElementsByTagName('tr')
        const itemNames = []
        for (let i = 0; i < listItems.length; i++) {
            itemNames.push(listItems[i].getElementsByClassName('name')[0].textContent)
        }
        for (let i = 0; i < listItems.length - 1; i++) {
            if (descendingName) {
                if (itemNames[i].toLowerCase() > itemNames[i + 1].toLowerCase()) {
                    listItems[i].parentNode.insertBefore(listItems[i + 1], listItems[i])
                    switching = true
                    break
                }
            }
            else {
                if (itemNames[i].toLowerCase() < itemNames[i + 1].toLowerCase()) {
                    listItems[i].parentNode.insertBefore(listItems[i + 1], listItems[i])
                    switching = true
                    break
                }
            }
        }
    }
}

const sortPrice = document.getElementById('sort-price')
sortPrice.onclick = () => {
    descendingPrice = !descendingPrice
    let switching = true
    while (switching) {
        switching = false
        const listItems = list.getElementsByTagName('tr')
        const itemPrices = []
        for (let j = 0; j < listItems.length; j++) {
            itemPrices.push(parseInt(listItems[j].getElementsByClassName('price')[0].textContent.substring(1)))
        }
        for (let i = 0; i < listItems.length - 1; i++) {
            if (descendingPrice) {
                if (itemPrices[i] > itemPrices[i + 1]) {
                    listItems[i].parentNode.insertBefore(listItems[i + 1], listItems[i])
                    switching = true
                    break
                }
            }
            else {
                if (itemPrices[i] < itemPrices[i + 1]) {
                    listItems[i].parentNode.insertBefore(listItems[i + 1], listItems[i])
                    switching = true
                    break
                }
            }
        }
    }
}