const print = (string) => {console.log(`${string}`)}

// const customer = require('./customer.json');

// print(customer.address);

const fs = require('fs');
const filePAth =  './node-js/stuff.json'
const newFilePath = './node-js/newData.json';

try {
    const stuff = fs.readFileSync('./node-js/stuff.json', 'utf-8');
    const stuffJSON = JSON.parse(stuff)
    print(stuffJSON)
} catch (err) {
    if (err instanceof SyntaxError && err.message.includes('Unexpected end of JSON input')) {
        console.error('Error: Invalid or incomplete JSON data.');

        // Create or overwrite a new JSON file with valid data
        const defaultData = {
            message: 'This is a new valid JSON file because the original was incomplete.'
        };
        
        fs.writeFileSync(newFilePath, JSON.stringify(defaultData, null, 2), 'utf8');
        print(`A new file "${newFilePath}" has been created with default data.`);

    } else {
        print('An error occurred:', err.message);
    }
}

// Read JSON data on file
const data = fs.readFileSync('./node-js/stuff.json', 'utf8');

// Parse JSON data
const jsonData = JSON.parse(data);

print(jsonData)

// Write JSON data to a file
fs.writeFileSync('./node-js/output.json', JSON.stringify(data, null, 2), 'utf8');

console.log("Data written successfully");