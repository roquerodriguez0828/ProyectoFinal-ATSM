const express = require("express");
const request = require("request");
const bodyParser = require("body-parser");
const upload = require('express-fileupload')
const fs = require('fs');
const { text } = require("body-parser");


const app = express();

app.use(upload())

app.use(express.static("public"));
app.use('css',express.static(__dirname+'public/css'))
app.use('js',express.static(__dirname+'public/js'))
app.use('img',express.static(__dirname+'public/img'))


app.use(bodyParser.urlencoded({extended:true}));

app.set('view engine','ejs')
app.set('views','./views')


app.get("/",(req,res)=>{
    //res.sendFile(__dirname+'/public/login.html');
	res.render('index')
});

app.get("/signup",(req,res)=>{
	res.render('signup')
});


app.post("/signin",(req,res)=>{

	const email = req.body.user
	const password = req.body.pass

	/*

	if(user == "admin" && pass=="admin"){
		res.redirect("/app");
	}else{
		res.redirect("/");
	}
*/ 
});

app.get("/app",(req,res)=>{
	//res.sendFile(__dirname+'/public/main.html');
	params = {
		texto: "",
		resumen: ""
	}
	res.render('main',{params:params})
});

app.post("/formPost",(req,res)=>{
	//console.log(req.body)



	if(req.body.tipo == 'resumen'){

		var text = req.body.text

		if(req.body.text == '' && req.files){
			text = req.files.textfile.data.toString('utf8');
		}

		var options = {
			'method': 'POST',
			'url': 'http://127.0.0.1:5000',
			'headers': {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				"text": text
				,"lang": req.body.lang
				,"method":req.body.method
				,"min":Number(req.body.min)
				,"max":Number(req.body.max)
			})
	
		}; 
	
		request(options, function (error, response) {
		  if (error) {
			throw new Error(error);
		  }
		  else {
			summary = JSON.parse(response.body)
			params={
				texto:text,
				resumen: summary.response
			  }
			  res.render('main',{params:params});
		  }
		});
	}
	/*
	if(req.files){
		console.log(req.files.textfile.data.toString('utf8'));

	}
	*/

});


app.listen(process.env.PORT || 3000,()=>{
    console.log("Server is running on port 3000");
});


