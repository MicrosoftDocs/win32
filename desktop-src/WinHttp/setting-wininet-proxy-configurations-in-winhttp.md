---
description: Applications that port from WinINet to WinHTTP may need to use the same autoproxy settings that they can retrieve under WinINet or Internet Explorer (IE).
ms.assetid: c3e867d8-9d67-4e6a-8551-1fa846e089ed
title: Setting WinINet Proxy Configurations in WinHTTP
ms.topic: article
ms.date: 05/31/2018
---

# Setting WinINet Proxy Configurations in WinHTTP

## Setting Automatic Proxy on WinHTTP 5.1

Applications that port from WinINet to WinHTTP may need to use the same autoproxy settings that they can retrieve under WinINet or Internet Explorer (IE). The WinHTTP version 5.1 API can retrieve and use these proxy settings. In general, WinHTTP specifies the proxy and proxy bypass servers on a per-session basis when the session is created. These settings can be overridden on a per-request basis.

To use the same proxy configuration as WinINet or IE, the WinHTTP client should set proxy settings for the session. In addition, if IE or WinINet are configured to use Web Proxy Auto-Discovery (WPAD), the WinHTTP client that uses those settings must set proxy settings on a per-request basis. The following sections describe how to specify the proxy settings for a session and a request:

-   [Setting the Proxy Configuration on a Session](#setting-the-proxy-configuration-on-a-session)
-   [Setting the Proxy Configuration on a Single Request](#setting-the-proxy-configuration-on-a-single-request)

## Setting the Proxy Configuration on a Session

## The Application is Running on a User Account

Before a session is created, the application calls [**WinHttpGetIEProxyConfigForCurrentUser**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser) to get the IE proxy settings. The application must be running as a user account to obtain these settings. The *pProxyConfig* parameter is a pointer to a [**WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG**](/windows/win32/api/winhttp/ns-winhttp-winhttp_current_user_ie_proxy_config) structure that contains the proxy name (*lpszProxy*) and proxy bypass (*lpszProxyBypass*) servers. The proxy name and proxy bypass values of the **WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG** structure are then used to initialize the WinHTTP session. The session is initialized by calling [**WinHttpOpen**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopen) with the *pwszProxyName* and *pwszProxyBypass* parameters obtained from the **lpszProxy** and **lpszProxyBypass** members of the **WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG** structure.

## The Application is Running as a Service

The application must ensure that the registry settings for an individual user are loaded into the registry before calling [**WinHttpGetIEProxyConfigForCurrentUser**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser). If these settings are not loaded into the registry, **WinHttpGetIEProxyConfigForCurrentUser** cannot obtain the proxy settings. Registry settings for an individual user can be loaded into the registry by calling the **LoadUserProfile** function. If loading the user's registry settings is not an option, the application can call [**WinHttpOpen**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopen) with the **WINHTTP\_ACCESS\_TYPE\_DEFAULT\_PROXY** specified in the *dwAcessType* parameter. Specifying the default proxy in the call to **WinHttpOpen** tells the WinHTTP API to retrieve the proxy configuration set by using the WinHTTP [**proxycfg.exe**](proxycfg-exe--a-proxy-configuration-tool.md) utility. After the registry settings for an individual user have been loaded, the application follows the steps outlined under [The application is running on a user account](#the-application-is-running-on-a-user-account) to set the proxy name and proxy bypass servers.

## Setting the Proxy Configuration on a Single Request

Before the session is created, the application calls [**WinHttpGetIEProxyConfigForCurrentUser**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser) to determine if WinINet and IE are configured to use WPAD. **WinHttpGetIEProxyConfigForCurrentUser** returns the [**WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG**](/windows/win32/api/winhttp/ns-winhttp-winhttp_current_user_ie_proxy_config) structure that contains the **fAutoDetect** member. A value of **TRUE** for this member indicates that WPAD is used, and the **lpszAutoConfigUrl** member contains the WPAD URL.

## Automatic Proxy Configuration Is Used

If WPAD is used, the application calls [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) to retrieve the proxy for the request. The *lpwszUrl* parameter contains the URL that the request is being sent to, and the *pAutoProxyOptions* parameter contains a pointer to the structure ([**WINHTTP\_AUTOPROXY\_OPTIONS**](/windows/win32/api/winhttp/ns-winhttp-winhttp_autoproxy_options)) that contains the autoproxy options. The application initializes the **WINHTTP\_AUTOPROXY\_OPTIONS** structure with the settings returned from the [**WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG**](/windows/win32/api/winhttp/ns-winhttp-winhttp_current_user_ie_proxy_config) structure in the call to [**WinHttpGetIEProxyConfigForCurrentUser**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser). The **WINHTTP\_AUTOPROXY\_CONFIG\_URL** flag is specified in the **dwFlags** member of the **WINHTTP\_AUTOPROXY\_OPTIONS** structure, and the **lpszAutoconfigUrl** member contains the proxy auto-configuration URL from the **WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG** structure. The **WinHttpGetProxyForUrl** function returns the proxy name and the proxy bypass list in the **lpszProxy** and **lpszProxyBypass** members of the [**WINHTTP\_PROXY\_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_proxy_info) structure.

After the proxy for the request is obtained from [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl), the application creates the request with [**WinHttpOpenRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopenrequest). Then [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) is called to set the proxy for the request by specifying the request handle in the *hInternet* parameter. The *dwOption* parameter in the call to **WinHttpSetOption** should be set to **WINHTTP\_OPTION\_PROXY** and the *lpBuffer* parameter is a pointer to a [**WINHTTP\_PROXY\_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_proxy_info) structure that contains the proxy and proxy bypass to be used for the request.

## Automatic Proxy Configuration Is Not Used

If the call to [**WinHttpGetIEProxyConfigForCurrentUser**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser) indicates that autoproxy is not used, the application can simply create the request with [**WinHttpOpenRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopenrequest). The proxy configuration is the same for the entire session, and per-request changes are not needed.

 

 



