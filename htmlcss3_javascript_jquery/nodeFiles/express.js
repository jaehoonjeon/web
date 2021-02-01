//npm install express@4.14
//모듈을 추출합니다.
const express = require('express')
const app = express()

//변수를 선언합니다.
const items = [{
    name: '우유',
    price: '2000'
},{
    name: '홍차',
    price: '5000'
},{
    name: '커피',
    price: '5000'
}]

//폴더에 있는 모든 내용을  Static으로 사용가능 (http://127.0.0.1:52273/index.html)
//public 폴더 안에 있는 index.html 을 / 루트로 접근하게 함
app.use(express.static('public')) 

//html 응답
app.get('/data.html', (request, response) =>{
    let output = ''
    output += '<!DOCTYPE html>'
    output += '<html>'
    output += '<head>'
    output += '     <title>Data HTML</title>'
    output += '</head>'
    output += '<body>'
    
    items.forEach(function (item){
        output += '<div>'
        output += '     <h1>' + item.name + '</h1>'
        output += '     <h2>' + item.price + '</h2>'
        output += '</div>'
    })

    output += '</body>'
    output += '</html>'


    response.send(output)
})

//JSON 응답
app.get('/data.json', (request, response) =>{
    
    response.send(items)
})

//XML 응답
app.get('/data.xml', (request, response) =>{
    var output = ''
    output += '<?xml version="1.0" encoding="UTF-8" ?>'
    output += '<products>'

    items.forEach(function (item){
        output += '<product>'
        output += '     <name>' + item.name + '</name>'
        output += '     <price>' + item.price + '</price>'
        output += '</product>'
    })

    output += '</products>'
    response.type('text/xml')
    response.send(output)
})


app.listen(52273, () => {
    console.log('Server Running at http://127.0.0.1:52273')
})

