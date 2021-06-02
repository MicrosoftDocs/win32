---
description: This topic explains the use of the Microsoft Windows HTTP Services (WinHTTP) proxy configuration tool, &\#0034;ProxyCfg.exe&\#0034;.
ms.assetid: f96adf59-59be-414e-ad6f-9eac05f4b975
title: Netsh.exe and ProxyCfg.exe Proxy Configuration Tools
ms.topic: article
ms.date: 05/31/2018
---

# Netsh.exe and ProxyCfg.exe Proxy Configuration Tools

**Windows Vista and Windows Server 2008:  **

ProxyCfg.exe has been deprecated. It is replaced by the [Netsh.exe winhttp](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731131(v=ws.10)) commands.

This topic explains the use of the [Microsoft Windows HTTP Services (WinHTTP)](about-winhttp.md) proxy configuration tool, "ProxyCfg.exe".

There are two ways to access HTTP and Secure Hypertext Transfer Protocol (HTTPS) servers through a proxy using Microsoft Windows HTTP Services (WinHTTP). First, you can specify proxy settings from within your WinHTTP application. Second, you can specify default proxy settings from outside your application using the proxy configuration utility located in the %windir%\\system32 directory.

You can programmatically set the proxy data from within your application or script. If you are writing an application using the WinHTTP API, use one of the following two techniques to change proxy settings.

-   Use the [**WinHttpOpen**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopen) function. Specify access type in the second parameter, the name of the proxy in the third parameter, and a bypass list in the fourth parameter. The following example shows how the [**WinHttpOpen**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopen) function can be used to set proxy data.

    ``` syntax
    hSession = WinHttpOpen( L"WinHTTP Example/1.0",  
                            WINHTTP_ACCESS_TYPE_NAMED_PROXY,
                            L"proxy_name", 
                            L"<local>", 
                            0);
    ```

-   Use the [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) function. The [**WINHTTP\_OPTION\_PROXY**](option-flags.md) flag enables you to specify proxy settings with a [**WINHTTP\_PROXY\_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_proxy_info) structure. The following example code shows how the [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) function can be used to set proxy data.

    ``` syntax
    WINHTTP_PROXY_INFO proxyInfo;
    proxyInfo.dwAccessType = WINHTTP_ACCESS_TYPE_NAMED_PROXY;
    proxyInfo.lpszProxy = L"proxy_name";
    proxyInfo.lpszProxyBypass = L"<local>";
        
    // Set the proxy information for this session.
    WinHttpSetOption( hSession, 
                      WINHTTP_OPTION_PROXY, 
                      &proxyInfo, 
                      sizeof(proxyInfo));
    ```

If you are writing a script or an application using the [**WinHttpRequest**](winhttprequest.md) object, use the following technique to change proxy settings.

-   Use the [**SetProxy**](iwinhttprequest-setproxy.md) method. Specify the access type in the first parameter, the name of the proxy in the second parameter, and a bypass list in the third parameter. The following example shows how the [**SetProxy**](iwinhttprequest-setproxy.md) method can be used in script to set proxy data.

    ``` syntax
    WinHttpReq.SetProxy( HTTPREQUEST_PROXYSETTING_PROXY, 
                         "proxy_server:80", 
                         "*.microsoft.com");
    ```

To specify default settings and eliminate the need to use either the [**SetProxy**](iwinhttprequest-setproxy.md) method or the [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) function, use the proxy configuration utility. Using this utility, you can specify that your application access a network either directly, through a proxy, or through a combination of direct and proxy access by specifying a bypass list. When you use the WinHTTP API, the proxy configuration tool only determines the settings when you pass the **WINHTTP\_ACCESS\_TYPE\_DEFAULT** flag to the [**WinHttpOpen**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopen) API. The [**WinHttpRequest**](winhttprequest.md) object uses the proxy configuration tool settings by default.

The proxy settings for WinHTTP are not the proxy settings for Microsoft Internet Explorer. You cannot configure the proxy settings for WinHTTP in the Microsoft Windows Control Panel. Using the WinHTTP proxy configuration utility does not alter the settings you use for Internet Explorer.

> [!Note]  
> If you attempt to open and send an HTTP request using WinHTTP and the proxy settings are incorrect, an error occurs.

 

## Command Line Parameters

The following table lists the command line parameters available for use with the ProxyCfg.exe tool.



| Parameter | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| none      | When no parameters are specified, the current WinHTTP proxy settings are displayed.                                                                                                                                                                                                                                                                                                                                               |
| ?         | Help information is displayed.                                                                                                                                                                                                                                                                                                                                                                                                    |
| d         | Specifies that WinHTTP applications access the network directly, without a proxy.                                                                                                                                                                                                                                                                                                                                                 |
| p         | Specifies the proxy server. You can also specify an optional list of servers that are accessed without a proxy.                                                                                                                                                                                                                                                                                                                   |
| u         | Specifies that WinHTTP applications use the current user's proxy settings for Internet Explorer. This parameter does not work if Internet Explorer is automatically detecting proxy settings, or if it is using an automatic configuration URL to set the proxy information.                                                                                                                                                      |
| i         | Specifies that WinHTTP applications use the current user's proxy settings for Internet Explorer. This only works when ProxyCfg.exe was not previously used. If ProxyCfg.exe is installed, specify that the "u" command line parameter use the manual settings. This parameter does not work if Internet Explorer automatically detects proxy settings, or if it uses an automatic configuration URL to set the proxy information. |



 

You can specify proxies in a space-delimited string. The proxy listings can contain the port number that is used to access the proxy. To list a proxy for a specific protocol, the string must follow the format, <protocol>=https://<proxy\_name>. The valid protocols are HTTP and HTTPS. For example, to list an HTTP proxy, a valid string is http=https://http\_proxy\_name:80, where http\_proxy\_name is the name of the proxy server and 80 is the port number that you must use to access the proxy. If the proxy uses the default port number for that protocol, then you can omit the port number. If a proxy name is listed by itself, you can use it as the default proxy for any protocols that do not have a specified proxy. For example, http=https://http\_proxy other\_proxy uses http\_proxy for any HTTP operations, while the HTTPS protocol uses the proxy named other\_proxy.

You can list locally known host names or IP addresses in the proxy bypass list. This list can contain wildcards, such as "\*", that cause the application to bypass the proxy server for addresses that fit the specified pattern, for example, "\*.microsoft.com" or "\*.org". Wildcard characters must be the left-most characters in the list. For example, "aaa.\*" is not supported. To list multiple addresses and host names, separate them with blank spaces or semicolons in the proxy bypass string. If you specify the <local> macro, the function bypasses any host name that does not contain a period.

> [!WARNING]
> After Proxycfg.exe runs, you cannot restore the previous proxy settings. However, you can remove the proxy settings entirely.

 

## Usage

To use the proxy configuration tool, open a command prompt window and run the proxy configuration utility with the appropriate command line parameters. The following section provides syntax examples.

## Example Syntax

### Example 1: Use a proxy only for external resources

The following is the most common use for Proxycfg.exe. This command specifies that both HTTP and HTTPS servers are accessed through the proxy server named "proxy\_server", except for host names that do not contain a period.

**proxycfg -p proxy\_server "<local>"**

### Example 2: Use a proxy for all resources

The following example specifies that both HTTP and HTTPS servers are accessed through the proxy server named "proxy\_server". No bypass list is specified.

**proxycfg -p proxy\_server**

### Example 3: Use a different proxy for secure resources

The following example specifies that HTTP servers are accessed through the http\_proxy proxy and HTTPS servers are accessed through https\_proxy. Local intranet sites and any site in the \*.microsoft.com domain bypass the proxy.

**proxycfg -p "http=http\_proxy https=https\_proxy" "<local>;\*.microsoft.com"**

## Removing ProxyCfg.exe

After using the proxy configuration tool, you cannot restore your original proxy settings. However, if necessary, you can remove the registry settings that the utility creates. To remove the registry entries that ProxyCfg.exe creates, you must delete the **WinHttpSettings** value from the following registry key.

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Internet Settings**\\**Connections**\\**WinHttpSettings**

Deleting the *WinHttpSettings* value removes all proxy configurations.

## ProxyCfg.exe and Authentication

The proxy configuration utility sets the default authentication policy. Because you should not perform NTLM authentication with untrusted hosts, by default, NTLM authentication only occurs automatically with hosts on the proxy bypass list. If there is no proxy, you can still use ProxyCfg.exe to specify a bypass list of hosts that you trust to perform NTLM authentication. A proxy name is required when using ProxyCfg.exe for this purpose, but you can use any valid string in place of a real proxy name.

For more information about the auto-logon policy, see [Automatic Logon Policy](authentication-in-winhttp.md).

 

 
