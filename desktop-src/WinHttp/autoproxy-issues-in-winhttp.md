---
description: Consider the following important issues when using the WinHTTP autoproxy feature.
ms.assetid: 9bae89b7-8f54-42ec-a240-998c97e26d25
title: AutoProxy Issues in WinHTTP
ms.topic: article
ms.date: 05/31/2018
---

# AutoProxy Issues in WinHTTP

Consider the following important issues when using the WinHTTP autoproxy feature.

## Only One Proxy Server is Currently Supported

WinHTTP does not currently support proxy configurations that specify more than one proxy server. If [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) returns a [**WINHTTP\_PROXY\_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_proxy_info) structure that contains a list of proxy servers, which the application then sets on the request handle using the **WINHTTP\_OPTION\_PROXY** option, WinHTTP uses only the first proxy server in the list. If that proxy server is not accessible, WinHTTP does not failover to any of the other proxy servers in the list. It is up to the application to handle this case by setting the **WINHTTP\_OPTION\_PROXY** option again with the next proxy server in the list, and resending the request.

## Security Risk Mitigation

Processing the proxy auto-configuration file requires executing downloaded script code. Some security concerns to consider: If the server on which the PAC file resides has been compromised, it is possible the PAC script code is malicious. Therefore, WinHTTP uses the following precautions to protect the client:

1.  The script code is prevented from instantiating any ActiveX objects. This blocks a lot of potentially dangerous functionality, such as the ability to access files and to perform network I/O.
2.  **Windows Server 2003:  **[**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) delegates the entire WPAD processing to an external out-of-process service, the WinHTTP Web Proxy Auto-Discovery service, which runs under the low-privileged Local Service built-in user account.

3.  **Windows XP with SP2 and Windows Server 2003:** A PAC script is not permitted to execute for longer than 60 seconds, after which script execution is terminated.

4.  **Windows XP with SP2 and Windows Server 2003:** WinHTTP rejects PAC files larger than 1MB. A typical PAC file is usually no more than a few kilobytes in size.

Be aware that processing the PAC script code requires the use of COM, because WinHTTP uses Microsoft JScript component to execute the script. If WinHTTP cannot delegate WPAD protocol processing to an external, out-of-process Web Proxy Auto-Discovery service, [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) loads the COM runtime within the application process for the duration of the call. If the application itself is already using COM, this should not be a concern.

## Performance Considerations

The auto-detection process can be slow, possibly as long as several seconds. The [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) and [WinHttpDetectAutoProxyConfigUrl](/windows/desktop/api/Winhttp/nf-winhttp-winhttpdetectautoproxyconfigurl) functions are blocking, synchronous functions. It could be that one particular auto-detection mechanism (such as DHCP) is much slower than the other (such as DNS). If both the **WINHTTP\_AUTO\_DETECT\_TYPE\_DHCP** and **WINHTTP\_AUTO\_DETECT\_TYPE\_DNS\_A** auto-detection flags are specified, WinHTTP uses DHCP first, in accordance with the WPAD specification. If no PAC URL is discovered by issuing a DHCP request, then WinHTTP tries to locate the PAC file at a well-known DNS address.

[**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) uses the WinHTTP Session handle parameter for caching the PAC file and the results of auto-detection. It is best to use the same session handle for multiple **WinHttpGetProxyForUrl** calls if possible to avoid repeated PAC URL detection and file downloading. The PAC file is cached in-memory only, and is discarded when the application closes the session handle.

Because of the performance impact of autoproxy, it is recommended that only desktop client applications or services use the feature; server-based applications should rely on the server administrator using the "ProxyCfg.exe" utility.

 

 



