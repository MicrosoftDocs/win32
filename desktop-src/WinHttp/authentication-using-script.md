---
description: This section demonstrates how to write script that uses the WinHttpRequest object to access data from a server that requires HTTP authentication.
ms.assetid: 9e46777c-4d79-4f9b-9b31-1280ed1e3289
title: Authentication Using Script
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Authentication Using Script

This section demonstrates how to write script that uses the [**WinHttpRequest**](winhttprequest.md) object to access data from a server that requires HTTP authentication.

-   [Prerequisites and Requirements](#prerequisites-and-requirements)
-   [Accessing a Web Site With Authentication](#accessing-a-web-site-with-authentication)
-   [Checking the Status Codes](#checking-the-status-codes)
-   [Related topics](#related-topics)

## Prerequisites and Requirements

In addition to a working knowledge of Microsoft JScript, this example requires the following:

-   The current version of the Microsoft Windows Software Development Kit (SDK).
-   The proxy configuration tool to establish the proxy settings for Microsoft Windows HTTP Services (WinHTTP), if your connection to the Internet is through a proxy server. See [Proxycfg.exe, a Proxy Configuration Tool](proxycfg-exe--a-proxy-configuration-tool.md) for more information.
-   A familiarity with [network terminology](network-terminology.md) and concepts.

## Accessing a Web Site With Authentication

**To create a script that demonstrates authentication, do the following:**

1.  Open a text editor such as Microsoft Notepad.
2.  Copy the following code into the text editor after replacing "\[authenticationSite\]" with the appropriate text to specify the URL of a site that requires HTTP authentication.

    ```VB
    // Load the WinHttpRequest object.
    var WinHttpReq = 
              new ActiveXObject("WinHttp.WinHttpRequest.5.1");

    function getText1( )
    {
      // Specify the target resource.
      WinHttpReq.open( "GET", 
                       "https://[authenticationSite]", 
                       false;

      // Send a request to the server and wait for a response.
      WinHttpReq.send( );

      // Display the results of the request.
      WScript.Echo( "No Credentials: " );
      WScript.Echo( WinHttpReq.Status + "   " + WinHttpReq.StatusText);
      WScript.Echo( WinHttpReq.GetAllResponseHeaders);
      WScript.Echo( );
    };

    function getText2( )
    {
      // HttpRequest SetCredentials flags
      HTTPREQUEST_SETCREDENTIALS_FOR_SERVER = 0;

      // Specify the target resource.
      WinHttpReq.open( "GET", 
                       "https://[authenticationSite]", 
                       false );

      // Set credentials for server.
      WinHttpReq.SetCredentials( "User Name", 
                                 "Password",
                                 HTTPREQUEST_SETCREDENTIALS_FOR_SERVER);

      // It might also be necessary to supply credentials 
      // to the proxy if you connect to the Internet 
      // through a proxy that requires authentication.

      // Send a request to the server and wait for 
      // a response.
      WinHttpReq.send( );

      // Display the results of the request.
      WScript.Echo( "Credentials: " );
      WScript.Echo( WinHttpReq.Status + "   " + WinHttpReq.StatusText );
      WScript.Echo( WinHttpReq.GetAllResponseHeaders( ) );
      WScript.Echo( );
    };

    getText1( );
    getText2( );
    ```

    

3.  Save the file as "Auth.js".
4.  From a command prompt, type "cscript Auth.js" and press ENTER.

You now have a program that requests a resource two different ways. The first method requests the resource without supplying credentials. A 401 status code is returned to indicate that the server requires authentication. The response headers are also displayed and should look similar to the following:

``` syntax
Connection: Keep-Alive
Content-Length: 0
Date: Fri, 27 Apr 2001 01:47:18 GMT
Content-Type: text/html
Server: Microsoft-IIS/5.0
WWW-Authenticate: NTLM
WWW-Authenticate: Negotiate
Cache-control: private
```

Although the response indicates that access to the resource was denied, it still returns several headers that provide some information about the resource. The header named "WWW-Authenticate" indicates that the server requires authentication for this resource. If there was a header named "Proxy-Authenticate", it would indicate that the proxy server requires authentication. Each authenticate header contains an available authentication scheme and sometimes a realm. The realm value is case-sensitive and defines a set of servers or proxies for which the same credentials should be accepted.

There are two headers named "WWW-Authenticate", which indicate that multiple authentication schemes are supported. If you call the [**GetResponseHeader**](iwinhttprequest-getresponseheader.md) method to find "WWW-Authenticate" headers, the method only returns the contents of the first header of that name. In this case, it returns a value of "NTLM". To ensure that all occurrences of a header are processed, use the [**GetAllResponseHeaders**](iwinhttprequest-getallresponseheaders.md) method instead.

The second method call requests the same resource, but first supplies authentication credentials by calling the [**SetCredentials**](iwinhttprequest-setcredentials.md) method. The following section of code shows how this method is used.


```VB
WinHttpReq.SetCredentials( "User Name", "Password",
                               HTTPREQUEST_SETCREDENTIALS_FOR_SERVER);
```



This method sets the user name to "UserName", the password to "Password", and indicates that the authorization credentials apply to the resource server. Authentication credentials can also be sent to a proxy.

When credentials are supplied, the server returns a 200 status code that indicates that the document can be retrieved.

## Checking the Status Codes

The previous example is instructional, but it requires that the user explicitly supply credentials. An application that supplies credentials when it is necessary and does not supply credentials when it is not necessary is more useful. To implement a feature that does this, you must modify your example to examine the status code returned with the response.

For a complete list of possible status codes, along with descriptions, see [**HTTP Status Codes**](http-status-codes.md). For this example, however, you should encounter only one of three codes. A status code of 200 indicates that a resource is available and is being sent with the response. A status code of 401 indicates that the server requires authentication. A status code of 407 indicates that the proxy requires authentication.

Modify the example you created in the last section by replacing the "getText2" function with the following code (replace "\[authenticationSite\]" with your own text to specifies the URL of a site that requires HTTP authentication):


```VB
function getText2() {
  WScript.Echo( "Credentials: " );

  // HttpRequest SetCredentials flags.
  HTTPREQUEST_SETCREDENTIALS_FOR_SERVER = 0;
  HTTPREQUEST_SETCREDENTIALS_FOR_PROXY = 1;

  // Specify the target resource.
  var targURL = "https://[authenticationSite]";
  WinHttpReq.open( "GET", targURL, false );

  var Done = false;
  var Attempts = 0;
  do
  {
    // Keep track of the number of request attempts.
    Attempts++;

    // Send a request to the server and wait for a response.
    WinHttpReq.send( );

    // Obtain the status code from the response.
    var Status = WinHttpReq.Status;

    switch (Status)
    {
      // A 200 status indicates that the resource was retrieved.
      case 200:
        Done = true;
        break;

      // A 401 status indicates that the server 
      // requires authentication.
      case 401:
        WScript.Echo( "Requires Server UserName and Password." );

        // Specify the target resource.
        WinHttpReq.open( "GET", targURL, false );

        // Set credentials for the server.
        WinHttpReq.SetCredentials( "User Name", 
                             "Password",
                              HTTPREQUEST_SETCREDENTIALS_FOR_SERVER);
        break;

      // A 407 status indicates that the proxy 
      // requires authentication.
      case 407:
        WScript.Echo( "Requires Proxy UserName and Password." );

        // Specify the target resource.
        WinHttpReq.open( "GET", targURL, false );

        // Set credentials for the proxy.
        WinHttpReq.SetCredentials( "User Name", 
                              "Password",
                              HTTPREQUEST_SETCREDENTIALS_FOR_PROXY );
        break;
    }
  } while( ( !Done ) && ( Attempts < 3 ) );

  // Display the results of the request.
  WScript.Echo( WinHttpReq.Status + "   " + WinHttpReq.StatusText );
  WScript.Echo( WinHttpReq.GetAllResponseHeaders( ) );
  WScript.Echo( );
};
```



Again, save and run the file. The second method still retrieves the document, but it only provides credentials when required. The "getText2" function executes the [**Open**](iwinhttprequest-open.md) and [**Send**](iwinhttprequest-send.md) methods as if authentication was not required. The status is retrieved with the [**Status**](iwinhttprequest-status.md) property and a switch statement responds to the resulting status code. If the status is 401 (server requires authentication) or 407 (proxy requires authentication), the [**Open**](iwinhttprequest-open.md) method is executed again. This is followed by the [**SetCredentials**](iwinhttprequest-setcredentials.md) method, which sets the user name and password. The code then loops back to the [**Send**](iwinhttprequest-send.md) method. If, after three attempts, the resource cannot be successfully retrieved, then the function stops execution.

## Related topics

<dl> <dt>

[Authentication in WinHTTP](authentication-in-winhttp.md)
</dt> <dt>

[WinHttpRequest](winhttprequest.md)
</dt> <dt>

[**SetCredentials**](iwinhttprequest-setcredentials.md)
</dt> <dt>

[HTTP/1.1 Request for Comments (RFC 2616)](https://www.ietf.org/rfc/rfc2616.txt)
</dt> </dl>

 

 



