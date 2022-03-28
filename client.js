
const net = require("net");
const command=document.getElementById("command");
const sendButton=document.getElementById("sendButton");

const host = "127.0.0.1";
const port = 42069;

let InterBotClient=new net.Socket();

InterBotClient.connect(port,host, () => {
    console.log(`Successfully connected to ${host}:${port}`);
});

InterBotClient.on('data', (data) => {
    console.log(data.toString());
});

InterBotClient.on('close', () => {
    console.log("Connection closed.")
});

sendButton.addEventListener("click", () => {
    InterBotClient.write(command.textContent);
    console.log(`Sent: "${command.textContent}"`);
});
