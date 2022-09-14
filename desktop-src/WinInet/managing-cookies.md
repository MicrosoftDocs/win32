---
title: Managing Cookies
description: Under the http protocol, a server or a script uses cookies to maintain state information on the client workstation.
ms.assetid: c00279cf-9cdc-4caf-8549-af1851edfa25
ms.topic: article
ms.date: 05/31/2018
---

# Managing Cookies

Under the http protocol, a server or a script uses cookies to maintain state information on the client workstation. The WinINet functions have implemented a persistent cookie database for this purpose. They can be used to set cookies in and access cookies from the cookie database. For more information, see [HTTP Cookies](http-cookies.md).

The [**InternetSetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetsetcookiea) and [**InternetGetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetgetcookiea) functions can be used to manage cookies.

## Using Cookie Functions

The following functions allow an application to create or retrieve cookies in the cookie database.



| Function                                       | Description                                                      |
|------------------------------------------------|------------------------------------------------------------------|
| [**InternetGetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetgetcookiea) | Retrieves cookies for the specified URL and all its parent URLs. |
| [**InternetSetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetsetcookiea) | Sets a cookie on the specified URL.                              |



 

Note that these functions do not require a call to [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena). Cookies that have an expiration date are stored in the local users account under Users\\"username"\\AppData\\Roaming\\Microsoft\\Windows\\Cookies directory, and the Users\\"username"\\AppData\\Roaming\\Microsoft\\Windows\\Cookies\\Low directory for applications running under low privileges. Cookies that do not have an expiration date are stored in memory and are available only to the process in which they were created.

As noted in the [HTTP Cookies](http-cookies.md) topic, the [**InternetGetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetgetcookiea) function does not return cookies that have been marked by the server as non-scriptable with the "HttpOnly" attribute in the Set-Cookie header.

### Getting a Cookie

[**InternetGetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetgetcookiea) returns the cookies for the specified URL and all its parent URLs.

The following example demonstrates a call to [**InternetGetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetgetcookiea).


```C++
TCHAR szURL[256];         // buffer to hold the URL
LPTSTR lpszData = NULL;   // buffer to hold the cookie data
DWORD dwSize=0;           // variable to get the buffer size needed

// Insert code to retrieve the URL.

retry:

// The first call to InternetGetCookie will get the required
// buffer size needed to download the cookie data.
if (!InternetGetCookie(szURL, NULL, lpszData, &dwSize))
{
    // Check for an insufficient buffer error.
    if (GetLastError()== ERROR_INSUFFICIENT_BUFFER)
    {
        // Allocate the necessary buffer.
        lpszData = new TCHAR[dwSize];

        // Try the call again.
        goto retry;
    }
    else
    {
        // Insert error handling code.
    }
}
else
{
    // Insert code to display the cookie data.

    // Release the memory allocated for the buffer.
    delete[]lpszData;
}
```



### Setting a Cookie

[**InternetSetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetsetcookiea) is used to set a cookie on the specified URL. [**InternetSetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetsetcookiea) can create both persistent and session cookies.

Persistent cookies have an expiration date. These cookies are stored in the local users account under Users\\"username"\\AppData\\Roaming\\Microsoft\\Windows\\Cookies directory, and the Users\\"username"\\AppData\\Roaming\\Microsoft\\Windows\\Cookies\\Low directory for applications running under low privileges.

Session cookies are stored in memory and can be accessed only by the process that created them.

The data for the cookie should be in the format:

``` syntax
NAME=VALUE
```

For the expiration date, the format must be:

``` syntax
DAY, DD-MMM-YYYY HH:MM:SS GMT
```

DAY is the three-letter abbreviation for the day of the week, DD is the day of the month, MMM is the three-letter abbreviation for the month, YYYY is the year, and HH:MM:SS is the time of the day in military time.

The following example demonstrates two calls to [**InternetSetCookie**](/windows/desktop/api/Wininet/nf-wininet-internetsetcookiea). The first call creates a session cookie and the second creates a persistent cookie.


```C++
BOOL bReturn;

// Create a session cookie.
bReturn = InternetSetCookie(TEXT("https://www.adventure_works.com"), NULL,
            TEXT("TestData = Test"));

// Create a persistent cookie.
bReturn = InternetSetCookie(TEXT("https://www.adventure_works.com"), NULL,
           TEXT("TestData = Test; expires = Sat,01-Jan-2000 00:00:00 GMT"));

```



> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

 

 