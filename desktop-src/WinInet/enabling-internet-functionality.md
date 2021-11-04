---
title: Enabling Internet Functionality
description: Before using the WinINet functions, the application should attempt to make a connection to the Internet by using the InternetAttemptConnect function.
ms.assetid: 80747c0d-5a09-4ffa-a0ca-b051b82acbf8
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Internet Functionality

Before using the WinINet functions, the application should attempt to make a connection to the Internet by using the [**InternetAttemptConnect**](/windows/desktop/api/Wininet/nf-wininet-internetattemptconnect) function. This function calls the dial-up dialog box to initiate a connection to the Internet or check if a connection already exists. If this function fails, the application can enter offline mode, which allows it to access information that was cached during previous connections to the Internet.

Use the [**InternetCheckConnection**](/windows/desktop/api/Wininet/nf-wininet-internetcheckconnectiona) function to check the connection to the Internet. It attempts to ping the server designated by the URL that is passed to the function. If the FLAG\_ICC\_FORCE\_CONNECTION flag is set and the URL is **NULL**, the function checks to see if there is an entry in the server database for the nearest server. If one exists, the function pings that server.

Next, use the [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena) function to establish the characteristics of the Internet connection the client application is using. [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena) creates the root [**HINTERNET**](appendix-a-hinternet-handles.md) handle that is used to establish [http](http-sessions.md)[ftp](ftp-sessions.md) sessions. [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena) does not test the connection to the Internet to verify that the characteristics passed to the function are correct.

Use the [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) function to create a specific session. [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) initializes a session for the specified site using the arguments passed to it and creates an [**HINTERNET**](appendix-a-hinternet-handles.md) handle that is a branch off the root handle. [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) does not attempt to access or establish a connection to the specified site, except in the case of an FTP session. [**FtpFindFirstFile**](/windows/desktop/api/Wininet/nf-wininet-ftpfindfirstfilea), [**FtpOpenFile**](/windows/desktop/api/Wininet/nf-wininet-ftpopenfilea), and [**HttpOpenRequest**](/windows/desktop/api/Wininet/nf-wininet-httpopenrequesta) functions use the handle created by [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) to establish a connection to the specified site.

## Using InternetOpen

To enable a connection to the Internet, a root [**HINTERNET**](appendix-a-hinternet-handles.md) handle must be created by using [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena). Information about the user agent (the application calling the Internet functions), the type of access to the Internet, the proxy names, the hosts and addresses that bypass the proxy, and the behavior are passed to [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena).

### Setting the User Agent

The calling application should give a string that contains the name of the application or entity accessing the Internet to the *lpszAgent* parameter of [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena). This string is used as the user agent in the HTTP protocol. For example, Microsoft Internet Explorer uses "Microsoft Internet Explorer".

### Setting Access Types

[**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena) supports three access types:

-   Use INTERNET\_OPEN\_TYPE\_DIRECT if the system on which the application is running uses a direct connection to the Internet. The *lpszProxyName* and *lpszProxyBypass* parameters of [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena) are not used and should be set to **NULL**.
-   Use INTERNET\_OPEN\_TYPE\_PROXY if the system on which the application is running uses one or more proxy servers to access the Internet. [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena) uses the proxy servers indicated by *lpszProxyName* and bypasses the proxy for any host names or IP addresses specified by *lpszProxyBypass*.
-   Use INTERNET\_OPEN\_TYPE\_PRECONFIG to instruct your application to retrieve the configuration from the registry. This is typically the best choice, as most applications including web browsers use this option.

INTERNET\_OPEN\_TYPE\_PRECONFIG looks at the registry values **ProxyEnable**, **ProxyServer**, and **ProxyOverride**. These values are located under "HKEY\_CURRENT\_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings".

If **ProxyEnable** is zero, the application uses INTERNET\_OPEN\_TYPE\_DIRECT. Otherwise, the application uses INTERNET\_OPEN\_TYPE\_PROXY and uses the **ProxyServer** and **ProxyOverride** information.

The WinINet functions provide support for SOCKS type proxies only if Internet Explorer is installed. The installation of Internet Explorer includes the Wsock32n.dll file, which is needed to support SOCKS proxies. Wsock32n.dll is not redistributable.

### Listing Proxy Servers

WinINet recognizes two types of proxies: CERN type proxies (HTTP only) and TIS FTP proxies (FTP only). If Internet Explorer is installed, WinINet also support SOCKS type proxies. [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) assumes, by default, that the specified proxy is a CERN proxy. If the access type is set to INTERNET\_OPEN\_TYPE\_DIRECT or INTERNET\_OPEN\_TYPE\_PRECONFIG, the *lpszProxyName* parameter of [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena) should be set to **NULL**. Otherwise, the value passed to *lpszProxyName* must contain the proxies in a space-delimited string. The proxy listings can contain the port number that is used to access the proxy.

To list a proxy for a specific protocol, the string must follow the format ""&lt;protocol&gt;&lt;protocol&gt;://<proxy\_name>"". The valid protocols are HTTP, HTTPS and FTP. For example, to list an FTP proxy, a valid string would be ""ftp=ftp://ftp\_proxy\_name:21"", where ftp\_proxy\_name is the name of the FTP proxy and 21 is the port number that must be used to access the proxy. If the proxy uses the default port number for that protocol, the port number can be omitted. If a proxy name is listed by itself, it is used as the default proxy for any protocols that do not have a specific proxy specified. For example, ""http=https://http\_proxy other"" would use http\_proxy for any HTTP operations, while all other protocols would use other.

By default, the function assumes that the proxy specified by *lpszProxyName* is a CERN proxy. An application can specify more than one proxy, including different proxies for the different protocols. For example, if you specify ""ftp=ftp://ftp-gw HTTP=https://jericho:99 proxy"", FTP requests are made through the ftp-gw proxy, which listens at port 21, and HTTP requests are made through a CERN proxy called jericho, which listens at port 99. Otherwise, HTTP requests would be made through the CERN proxy called proxy, which listens at port 80. Note that if the application is only using FTP, for example, it would not need to specify ""ftp=ftp://ftp-gw:21"". It could specify just ""ftp-gw"". An application is only required to specify the protocol names if it is using more than one protocol per handle returned by [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena).

### Listing the Proxy Bypass

Host names or IP addresses that should not be sent to the proxy can be listed in the proxy bypass list. This list can contain wildcards, "\*", which cause the application to bypass the proxy server for addresses that fit the specified pattern. To list multiple addresses and host names, separate them with semicolons in the proxy bypass string. If the "&lt;local&gt;" macro is specified, the function bypasses the proxy for any host name that does not contain a period.

By default, WinINet will bypass the proxy for requests that use the host names "localhost", "loopback", "127.0.0.1", or "\[::1\]". This behavior exists because a remote proxy server typically will not resolve these addresses properly.

**Internet Explorer 9:** You can remove the local computer from the proxy bypass list using the "<-loopback>" macro.

The following example shows sample calls to [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena) using different proxy bypass strings. The comments above each call describe what effect the bypass string has on the host names that are accessed from the [**HINTERNET**](appendix-a-hinternet-handles.md) handle it creates.


```C++
HINTERNET hInternetRoot;

/* bypass the proxy for any host name that does not 
    contain a period */
hInternetRoot = InternetOpen(TEXT("WinInet Example"), 
    INTERNET_OPEN_TYPE_PROXY,TEXT("proxy"),TEXT("<local>"), 0);

/* bypass the proxy for any host name that starts with the 
    letters "ms" */
hInternetRoot = InternetOpen(TEXT("WinInet Example"), 
    INTERNET_OPEN_TYPE_PROXY,TEXT("proxy"),TEXT("ms*"), 0);

/* bypass the proxy for any host name that contains "int", 
    such as "internet" and "painter" */
hInternetRoot = InternetOpen(TEXT("WinInet Example"), 
    INTERNET_OPEN_TYPE_PROXY,TEXT("proxy"),TEXT("*int*"), 0);

/* bypass the proxy for the host name "example" and any 
    host name that contains "test" */
hInternetRoot = InternetOpen(TEXT("WinInet Example"), 
    INTERNET_OPEN_TYPE_PROXY,TEXT("proxy"),TEXT("example *test*"), 0);

/* Disable the loopback proxy bypass for localhost */
hInternetRoot = InternetOpen(TEXT("WinInet Example"), 
    INTERNET_OPEN_TYPE_PROXY,TEXT("127.0.0.1:8888"),TEXT("<-loopback>"), 0);
```



## Using InternetConnect

To begin a session, the [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) function must create a handle off the root handle returned by the [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena) function. [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) sets the server address, port number, user name, password, and type of service.

[**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) uses the root [**HINTERNET**](appendix-a-hinternet-handles.md) handle created by [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena) to establish a session handle. If the [INTERNET\_FLAG\_ASYNC](api-flags.md) flag was set in the call to [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena), the call to [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) should include a nonzero context value.

The server name can contain either the host name (for example, "www.servername.com") or IP number of the site in ASCII dotted-decimal format (for example, "10.0.1.45").

The server port is the Transmission Control Protocol/Internet Protocol (TCP/IP) port number to connect to on the server. [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) uses the default port for the selected service type if the INTERNET\_INVALID\_PORT\_NUMBER value is used. The following tables contain the server port defaults for WinINet.




| Value | Meaning | 
|-------|---------|
| INTERNET_DEFAULT_FTP_PORT | Use the default port for ftp servers (port 21). | 
| INTERNET_DEFAULT_GOPHER_PORT | Use the default port for gopher servers (port 70).<blockquote>[!Note]<br />Windows XP and Windows Server 2003 R2 and earlier only.</blockquote><br /> | 
| INTERNET_DEFAULT_HTTP_PORT | Use the default port for http servers (port 80). | 
| INTERNET_DEFAULT_HTTPS_PORT | Use the default port for https servers (port 443). | 
| INTERNET_DEFAULT_SOCKS_PORT | Use the default port for SOCKS firewall servers (port 1080). | 




 

### Defining the User Name and Password

The value of *lpszUsername* is the address of a **null**-terminated string that contains the name of the user who is logging on. If this parameter is **NULL**, the function uses an appropriate default, except for HTTP. A **NULL** parameter in HTTP causes the server to return an error. For the FTP protocol, the default is anonymous.

The value of *lpszPassword* is the address of a **null**-terminated string that contains the log-on password. If both *lpszUsername* and *lpszPassword* are **NULL**, the function uses the default anonymous password. In the case of FTP, the default anonymous password is the user's email name. If *lpszUsername* is not **NULL** and *lpszPassword* is **NULL**, the function uses a blank password. There are four possible settings of *lpszUsername* and *lpszPassword*, which produce the behaviors shown in the following table.



| *lpszUsername*      | *lpszPassword*      | User name sent to FTP server | Password sent to FTP server |
|---------------------|---------------------|------------------------------|-----------------------------|
| **NULL**            | **NULL**            | "anonymous"                  | User's email name           |
| Non-**NULL** string | **NULL**            | *lpszUsername*               | ""                          |
| **NULL**            | Non-**NULL** string | ERROR                        | ERROR                       |
| Non-**NULL** string | Non-**NULL** string | *lpszUsername*               | *lpszPassword*              |



 

This information can be changed by using the [**InternetSetOption**](/windows/desktop/api/Wininet/nf-wininet-internetsetoptiona) and [**InternetErrorDlg**](/windows/desktop/api/Wininet/nf-wininet-interneterrordlg) functions. [**InternetSetOption**](/windows/desktop/api/Wininet/nf-wininet-internetsetoptiona) changes the user name and password values, while [**InternetErrorDlg**](/windows/desktop/api/Wininet/nf-wininet-interneterrordlg) displays a dialog box that requests the proper user name and password.

### Defining the Session

To define the session that is being established, set the service type, flags, and context value for [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta).

There are two service types available to [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta): INTERNET\_SERVICE\_FTP and INTERNET\_SERVICE\_HTTP. INTERNET\_SERVICE\_HTTP is used for both HTTP and HTTPS sessions.

[INTERNET\_FLAG\_PASSIVE](api-flags.md) is the only service-specific flag used by the WinINet functions. This flag can be set when the service type is INTERNET\_SERVICE\_FTP in order to use passive FTP semantics.

For all synchronous operations, the value of *dwContext* should be set to zero. If asynchronous operations were established by setting the [INTERNET\_FLAG\_ASYNC](api-flags.md) flag in the call to [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena), a nonzero value should be supplied for *dwContext*. For more information on asynchronous operations, see [Setting Up Asynchronous Operations](common-functions.md).

For FTP sessions, [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) tries to establish a connection to the server on the Internet. For HTTP sessions, [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta) does not establish a connection until another function attempts to get information from the server.

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

 

