# Welcome to this Weather API

##Here it will be explained how you can execute this piece of code

1. ###Installing and Setting Negrok
   1. You need to download ngrok by clicking on this link: 	[https://ngrok.com/download](https://ngrok.com/download)
   2. Unzip the dowloaded file (extension .exe) and put it inside the folder that you created your project
   3. You need to create an account on this website
   4. Follow the steps under "setup & installation", verify in your code if you created a .yml file for ngrok with your authtoken, otherwise create this file in the same folder that it is located your code and insert the authtoken code
2. ###Installing Flask
   1. In your terminal type 'pip install flask'
   2. A message will be displayed that the installation was successful
3. ###Running this code on Windows - Browser
   1. On WINDOWS: Go to your code in your IDE (Visual Studio Code, Pycharm, etc...) and run it
   2. Access your cmd in the admin mode:
      1. Move to the folder that your code is located (for windows you can press 'cd' + the folder path)
      2. Execute the following: ngrok http 5000
      3. It will be generated a https url, for example: https://2a0e-206-0-90-201.ngrok.io
         1. Pick the url address that starts with 'https'
      4. Copy it and paste in the URL address and do not forget to check the route that your code is. For example: https://2a0e-206-0-90-201.ngrok.io/weather
4. ###Inputing the Data
   1. It will be exhibited one key field, which is the city
   2. For City: 
      1. Type: String
      2. Put place that you would like to get data from
5. ###Getting the Result
   1. Hit "Submit" in browser
   2. It will be showed the current temperature, the min and the max temperature
