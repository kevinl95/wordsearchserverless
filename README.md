# Serverless Text to Word Search Generator

[Try it out now!](https://d3pmqgalyxt1nk.cloudfront.net/)

![Screenshot][screenshot]

This is a serverless application that runs in an AWS Lambda function with an AWS API Gateway instance sitting in front serving the page and input form.

It takes in a blob of text, like an article or story, and the number of words you want to be in the word search. It then uses the RAKE algorithm to generate a word search based on the top keywords identified in that text!

All libraries have been saved and bundled in the source directory, while the website itself can be found in the HTML directory. It should be deployed to Lambda as a zip since the dependencies need to be brought along with the function code itself.
