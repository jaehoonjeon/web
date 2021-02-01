//$ npm install express
//모듈을 추출합니다.
const express = require('express')
//$ npm install body-parser
const bodyParser = require('body-parser')
const app = express()
app.use(bodyParser.urlencoded({extended: false}))

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

// GET 데이터 모두 가져오기
app.get("/drink", (req, res) => {
    res.send(items)
})

// POST 데이터 넣기
app.post("/drink", (req, res) => {
    items.push({
        name:req.body.name,
        price:req.body.price
    })
    console.log(items)
    res.send(items[items.length - 1])
})

// GET 한개
app.get("/drink/:id", (req, res) => {
    const id = Number(req.params.id)
    res.send(items[id])
})

// PUT 수정
app.put("/drink/:id", (req, res) => {
    const id = Number(req.params.id)
    items[id].name = "수정테스트"
    items[id].price = 3000
    res.send(items[id])
})

// 삭제
app.delete("/drink/:id", (req, res) => {
    const id = Number(req.params.id)
    items.splice(id, 1)        
    res.send("success")
})


app.listen(52273, () => {
    console.log('Server Running at http://127.0.0.1:52273')
})

