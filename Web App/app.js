const express = require("express");
const request = require("request");
const bodyParser = require("body-parser");
const upload = require('express-fileupload');
const session = require('express-session');
const cookieParser = require('cookie-parser');
const fs = require('fs');
const { text } = require("body-parser");
const mongoose = require('mongoose');
const User = require('./model/user')
require("dotenv").config();


const mongo_uri = 'mongodb://localhost:27017/atsm'
const sgMail = require("@sendgrid/mail");

sgMail.setApiKey(process.env.SENDGRID_API_KEY);


const sendMail = async (msg) => {
	try{
		await sgMail.send(msg);
		console.log("Message sent successfully!");
	}catch(error){
		console.log(error);
		if(error.response){
			console.error(error.response.body);
		}
	}
};


mongoose.connect(mongo_uri,(err)=>{
	if(err){
		throw err;
	}else {
		console.log('Successfully connected to DB')
	}
});



const app = express();

app.use(upload())

app.use(express.static("public"));
app.use('css',express.static(__dirname+'public/css'))
app.use('js',express.static(__dirname+'public/js'))
app.use('img',express.static(__dirname+'public/img'))


app.use(bodyParser.urlencoded({extended:true}));


app.use(cookieParser());
app.use(session({
	resave:false,
	saveUninitialized:false,
	secret: 'secret-key',
	credentials: null
}));

app.set('view engine','ejs')
app.set('views','./views')


let credentials = {

	username: 1234,
	email: 'rrodriguezcabreja@outlook.com'
}

app.get("/",(req,res)=>{
    //res.sendFile(__dirname+'/public/login.html');
	res.render('index')
});

app.get("/signup",(req,res)=>{
	res.render('signup')
});


app.post("/signup", async (req,res)=>{
	console.log(req.body)
	const username = req.body.user;
	const password = req.body.password;
	const email = req.body.email;

	if (!username || typeof username !== 'string') {
		return res.json({ status: 'error', error: 'Invalid username' })
	}

	if (password.length < 5 ) {
		return res.json({ status: 'error', error: 'Password too small. Should be atleat 6 characters' })
	}


	try{
		const response = await User.create({
			username,
			email,
			password
		})

		console.log(response)
	}catch(error){
		if(error.code == 11000){
			return res.json({status: 'error', error: 'Username already in use.'})
		}
		throw error
	}
	//res.redirect("/")
});

app.post("/signin",(req,res)=>{

	const username = req.body.user
	const password = req.body.pass

	try{
		User.find({username},(err,result)=>{
			if(err){
				console.log(err);
			}else {
				if(result.length>0 && result[0].password == password){
					credentials.email = result[0].email;
					credentials.username = username;
					req.session.credentials = credentials;
					req.session.save();
					res.redirect("/app");
				}else {
					console.log("WRONG CREDENTIALS")
				}	
			}

		});
	}catch(error){
		console.log(error)
		throw error
	}

	/*
	if(user == "admin" && pass=="admin"){
		req.session.credentials = credentials;
		req.session.save();
		res.redirect("/app");
	}else{
		res.redirect("/");
	}*/
 
});

app.get("/logout",(req,res)=>{
	req.session.destroy();
	res.redirect('/')
});


app.get("/app",(req,res)=>{
	//res.sendFile(__dirname+'/public/main.html');
	//console.log(req.session);
	if(req.session.credentials == null ){
		res.redirect("/")
	}else {
		params = {
			texto: "",
			resumen: ""
		}
		res.render('main',{params:params})
	}
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

	if(req.body.tipo == 'correo'){
		sendMail({
			to: req.session.credentials.email,
			from: "ATSM <atsmpucmm@gmail.com>",
			subject: "Your Summary Has Arrived!",
			text: "Your summary:\n"+ req.body.summary
		})
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


