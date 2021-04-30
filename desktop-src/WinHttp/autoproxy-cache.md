---
description: AutoProxy Cache
ms.assetid: 087104e8-ab38-4ba4-be70-23a5ea2bb130
title: AutoProxy Cache
ms.topic: article
ms.date: 05/31/2018
---

# AutoProxy Cache

The [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) function performs autoproxy lookup on a per-request basis for the specified URL. If multiple proxies are returned, client applications should test each proxy before sending the request (for more information, see the [Only One Proxy Server is Currently Supported](autoproxy-issues-in-winhttp.md) section in AutoProxy Issues in WinHTTP). The information in this topic applies to calls to **WinHttpGetProxyForUrl** when the client specifies automatic proxy discovery.

[**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) optionally locates the autoproxy URL and downloads the autoproxy script from that site. WinHttp uses the autoproxy script to locate the proxy servers. Both the autoproxy URL and the autoproxy script are cached for the specified session. Only one autoproxy URL and script are cached for each session. Typically, the autoproxy script and URL are cached until the IP address associated with the computer changes. If a new IP address is detected during a call to **WinHttpGetProxyForUrl**, the call will attempt to locate a new autoproxy URL and script and cache the results. Only one user should be allowed per session, so that the cached data is not shared with other users on the computer. For more information, see [WinHTTP Sessions Overview](winhttp-sessions-overview.md).

If the out-of-process service is active when [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) is called, the cached autoproxy URL and script are available to the whole computer. However, if the out-of-process service is used, and the **fAutoLogonIfChallenged** flag in the *pAutoProxyOptions* structure is true, then the autoproxy URL and script are not cached. Therefore, calling **WinHttpGetProxyForUrl** with the **fAutoLogonIfChallenged** member set to **TRUE** results in additional overhead operations that may affect performance. The following steps can be used to improve performance.

**To improve performance**

1.  Call [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) with the fAutoLogonIfChallenged parameter set to **false**. The autoproxy URL and script are cached for future calls to **WinHttpGetProxyForUrl**.
2.  If Step 1 fails, with **ERROR\_WINHTTP\_LOGIN\_FAILURE**, then call [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) with the **fAutoLogonIfChallenged** member set to **TRUE**.

 

 



