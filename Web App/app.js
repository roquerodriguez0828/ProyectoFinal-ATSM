const express = require("express")
const request = require("request");
const bodyParser = require("body-parser");

const app = express();

app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended:true}));


app.get("/",(req,res)=>{
    res.sendFile(__dirname+'/public/index.html');
});

app.post("/formPost",(req,res)=>{
	
	var options = {
		'method': 'POST',
		'url': 'http://127.0.0.1:5000',
		'headers': {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
		    "text": req.body.text
		    ,"lang": req.body.lang
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