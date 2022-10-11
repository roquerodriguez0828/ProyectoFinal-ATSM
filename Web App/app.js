const express = require("express")
const request = require("request");
const bodyParser = require("body-parser");

const app = express();

app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended:true}));


app.get("/",(req,res)=>{
    res.sendFile(__dirname+'/public/login.html');
});


app.post("/loginPost",(req,res)=>{

	const user = req.body.user
	const pass = req.body.pass

	if(user == "admin" && pass=="admin"){
		res.redirect("/app");
	}else{
		res.redirect("/");
	}

    
});

app.get("/app",(req,res)=>{
	res.sendFile(__dirname+'/public/main.html');
});

app.post("/formPost",(req,res)=>{
	console.log(req.body)
	
	var options = {
		'method': 'POST',
		'url': 'http://127.0.0.1:5000',
		'headers': {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
		    "text": req.body.text
		    ,"lang": req.body.lang
			,"method":req.body.method
			,"min":Number(req.body.min)
			,"max":Number(req.body.max)
		})

		}; 

	request(options, function (error, response) {
	  if (error) throw new Error(error);
	  res.send(response.body);
	});
});


app.listen(process.env.PORT || 3000,()=>{
    console.log("Server is running on port 3000");
});