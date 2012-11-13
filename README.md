community-crowdsource
=====================

Allows communities, neighborhoods, organizations, and really anybody to crowdsource geospatial information for free.

HTML5 and built for mobile browsers.

This project uses Google Fusion Tables as the backend geospatial database as well as Google App Engine for deployment.

Thanks to the other open-source libraries used in this project:
[Twitter Bootstrap](http://twitter.github.com/bootstrap/) for UI elements
[Google Maps Utility Library v3 geolocationmarker](http://google-maps-utility-library-v3.googlecode.com/svn/trunk/geolocationmarker/docs/reference.html)
[Font Awesome](http://fortawesome.github.com/Font-Awesome/)


Thanks to [NetCDN](http://www.bootstrapcdn.com/) for hosting the Twitter Bootstrap CDN and [Font Awesome](http://fortawesome.github.com/Font-Awesome/)
#Demo
See the [demo] (http://community-crowdsource.appspot.com)

#Setting it up

Clone the repo

##Create an App Engine project
First create an Google App Engine project [here](https://appengine.google.com/start/createapp?).

##Create a project on Google Code
Create a project in [Google Code here](https://code.google.com/apis/console/)

Enable the Fusion Tables API under "Services"

Under "API Access" click Create an OAuth 2.0 client ID...
Use Web Application as Application Type and use http://localhost for your site 

##Get your tokens
Run oauth_tokens.py from command line.  Note urllib2, urllib, and json packages are required.

Here you will input the client id, client secret and redirect url from the API console

If all goes as planned you will be returned with a access token and refresh token.  **Make sure to record these somewhere.**

##Create a Google Fusion Table
Create a Google Fusion table with the following columns: Address, Type, Notes, latLng, and Date Recorded. Make sure all are type text except latLng which should be location.  Make sure to set the table visable to the public.

##Setup ftclient.py
Paste in information from the previous steps to the following variables.  TableId is from the table you created in Fusion Tables and can be found by going to File -> About -> Encrypted ID

    client_id = ""
    client_secret = ""
    access_token = ""
    refresh_token = ""
    tableId = ''
    
##Add table ID to templates/main-map.html
Add the same table ID to line 84 of the main-map.html document located in the `templates` directory
