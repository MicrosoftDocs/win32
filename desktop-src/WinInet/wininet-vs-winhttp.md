---
title: WinINet vs. WinHTTP
description: Learn how to choose between WinInet and WinHTTP. Read a comparison of features, and review related topics.
ms.assetid: 77386b54-2c86-4a30-8c4c-88d5f15313d7
keywords: WinINet vs. WinHTTP, SOCKS5, SOCKS4
ms.topic: concept-article
ms.date: 12/06/2023
---

# WinINet vs. WinHTTP

With a few exceptions, [WinINet](portal.md) is a superset of [WinHTTP](/windows/desktop/WinHttp/winhttp-start-page). When you're choosing between the two, you should use WinINet *unless you plan to run within a service or service-like process that requires impersonation and session isolation*.

## Comparison of features

| Feature | WinINet | WinHTTP |
|-|-|-|
| **Credential cache**. Allows all built-in applications in Windows Internet Explorer to get credentials automatically. It also allows an application running outside of Internet Explorer to prompt/specify the credentials for the server only once. From then on the requests are automatic. | yes | no |
| **Credential prompting**. Provides an API that allows the calling code to prompt the user for credentials. | yes | no |
| **FTP** | yes | no |
| **Autodial/RAS support**. This is legacy functionality. Use [Remote Access](/windows/desktop/RRAS/portal) instead. | yes | no |
| **Zones**. Automatic integration with Internet Explorer security zones. | yes | no |
| **IDNA support**. Integrated support for the IDNA RFC/Punycode. | yes | yes |
| **Cookie Jar APIs**. Persistent and non-persistent cookies are supported. Any application or script can use this to see the same cookies as the browser. | yes | no |
| **Protected mode IE support** | yes | no |
| **Decompression support**. Support for gzip and deflate compression scheme. | yes | yes |
| **Chunked upload support**. Client code must perform the chunking. | no | yes |
| **SOCKS4 (SOCKS version 4) support**. Doesn't include v4a. | yes | no |
| **SOCKS5 (SOCKS version 5) support** | no | no |
| **Bidirectional send and receive** | no | no |
| **Overlapped I/O** | no | no |
| **File scheme support**. Useful for proxy scripts with a file scheme. | yes | no |
| **InternetOpenUrl**. Simplified code to open a URL. | yes | no |
| **Services support**. Can be run from a service or a service account. | no | yes |
| **Session isolation**. Separate sessions do not impact each other. | no | yes |
| **Impersonation**. Supports being called while the thread is impersonating a different user. | no | yes |

## Related topics

* [WinINet](/windows/desktop/WinInet/about-wininet)
* [WinHTTP](/windows/desktop/WinHttp/winhttp-start-page)
