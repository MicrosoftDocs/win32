---
title: HTTP Cookies
description: HTTP cookies provide the server with a mechanism to store and retrieve state information on the client application's system.
ms.assetid: c3574592-572f-4fde-adfa-aed3e862f13f
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Cookies

HTTP cookies provide the server with a mechanism to store and retrieve state information on the client application's system. This mechanism allows web-based applications the ability to store information about selected items, user preferences, registration information, and other information that can be retrieved later.

## Cookie-Related Headers

There are two headers, Set-Cookie and Cookie, that are related to cookies. The Set-Cookie header is sent by the server in response to an HTTP request, which is used to create a cookie on the user's system. The Cookie header is included by the client application with an HTTP request sent to a server, if there is a cookie that has a matching domain and path.

### Set-Cookie Header

The Set-Cookie response header uses the following format:

``` syntax
Set-Cookie: <name>=<value>[; <name>=<value>]...
[; expires=<date>][; domain=<domain_name>]
[; path=<some_path>][; secure][; httponly]
```

One or more string sequences (separated by semicolons) that follow the pattern *name*=*value* must be included in the Set-Cookie response header. The server can use these string sequences to store data on the client's system.

The expiration date is set by using the format expires=*date*, where *date* is the expiration date in Greenwich Mean Time (GMT). If the expiration date is not set, the cookie expires after the Internet session ends. Otherwise, the cookie is persisted in the cache until the expiration date. The date must use the following format:

*DAY*, *DD*-*MMM*-*YYYY* *HH*:*MM*:*SS* GMT

<dl> <dt>

<span id="DAY"></span><span id="day"></span>*DAY*
</dt> <dd>

The day of the week (Sun, Mon, Tue, Wed, Thu, Fri, Sat).

</dd> <dt>

<span id="DD"></span><span id="dd"></span>*DD*
</dt> <dd>

The day in the month (such as 01 for the first day of the month).

</dd> <dt>

<span id="MMM"></span><span id="mmm"></span>*MMM*
</dt> <dd>

The three-letter abbreviation for the month (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec).

</dd> <dt>

<span id="YYYY"></span><span id="yyyy"></span>*YYYY*
</dt> <dd>

The year.

</dd> <dt>

<span id="HH"></span><span id="hh"></span>*HH*
</dt> <dd>

The hour value in military time (22 would be 10:00 P.M., for example).

</dd> <dt>

<span id="MM"></span><span id="mm"></span>*MM*
</dt> <dd>

The minute value.

</dd> <dt>

<span id="SS"></span><span id="ss"></span>*SS*
</dt> <dd>

The second value.

</dd> </dl>

Specifying the domain name, using the pattern domain=*domain\_name*, is optional for persistent cookies and is used to indicate the end of the domain for which the cookie is valid. Session cookies that specify a domain are rejected. If the specified domain name ending matches the request, the cookie tries to match the path to determine if the cookie should be sent. For example, if the domain name ending is .microsoft.com, requests to home.microsoft.com and support.microsoft.com would be checked to see if the specified pattern matches the request. The domain name must have at least two or three periods in it to prevent cookies from being set for widely used domain name endings, such as .com, .edu, and co.jp. Allowable domain names would be similar to .microsoft.com, .someschool.edu, and .someserver.co.jp. Only hosts within the specified domain can set a cookie for a domain.

Setting the path, using the pattern path=*some\_path*, is optional and can be used to specify a subset of the URLs for which the cookie is valid. If a path is specified, the cookie is considered valid for any requests that match that path. For example, if the specified path is /example, requests with the paths /examplecode and /example/code.htm would match. If no path is specified, the path is assumed to be the path of the resource associated with the Set-Cookie header.

The cookie can also be marked as secure, which specifies that the cookie can be sent only to https servers.

Finally, a cookie can be marked as HttpOnly (attributes are not case-sensitive), to indicate that the cookie is non-scriptable and should not be revealed to the client application, for security reasons. Within Windows Internet, this means that the cookie cannot be retrieved through the **InternetGetCookie** function.

### Cookie Header

The Cookie header is included with any HTTP requests that have a cookie whose domain and path match the request. The Cookie header has the following format:

``` syntax
Cookie: <name>=<value> [;<name>=<value>]...
```

One or more string sequences, using the format *name*=*value*, contain the information that was set in the cookie.

## Generating Cookies

There are three methods for generating cookies for Microsoft Internet Explorer: using Microsoft JScript, using the WinINet functions, and using a CGI script. All of the methods need to set the information that is included in the Set-Cookie header.

### Generating a Cookie Using the DHTML Object Model

Using the Dynamic HTML (DHTML) object model, cookies can be set by calling the **cookie** property of the document object, as shown in the following example.

``` syntax
<SCRIPT language="JavaScript">
<!--
    document.cookie = "SomeValueName = Some_Value";
-->
</SCRIPT>
```

### Generating a Cookie Using the WinInet Functions

Cookies can be created by applications using the [**InternetSetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetsetcookiea) function. For more information, see [Setting a Cookie](managing-cookies.md).

### Generating a Cookie Using a CGI Script

Cookies are generated by including a Set-Cookie header as part of a CGI script included in the HTTP response to a request.

The following example is a CGI script that includes a Set-Cookie header using Perl.

``` syntax
print "Set-Cookie:Test=test_value; 
      expires=Sat, 01-Jan-2000 00:00:00 GMT;
      path=/;"
```

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

 

 