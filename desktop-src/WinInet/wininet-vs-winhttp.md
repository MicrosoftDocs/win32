---
title: WinINet vs. WinHTTP
description: With a few exceptions, WinINet is a superset of WinHTTP. When selecting between the two, you should use WinINet, unless you plan to run within a service or service-like process that requires impersonation and session isolation.
ms.assetid: 77386b54-2c86-4a30-8c4c-88d5f15313d7
keywords:
- WinINet vs. WinHTTP
ms.topic: article
ms.date: 05/31/2018
---

# WinINet vs. WinHTTP

With a few exceptions, [WinINet](portal.md) is a superset of [WinHTTP](https://msdn.microsoft.com/library/windows/desktop/aa384273). When selecting between the two, you should use WinINet, unless you plan to run within a service or service-like process that requires impersonation and session isolation.

## Comparison of features



| Feature                                                                                                                                                                                                                                                                                                            | WinINet        | WinHTTP        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|----------------|
| **Credential Cache**<br/> Allows all built-in applications in Windows Internet Explorer to get credentials automatically. It also allows an application running outside of Internet Explorer to prompt/specify the credentials for the server only once. From then on the requests are automatic.<br/> | yes<br/> | no<br/>  |
| **Credential Prompting**<br/> Provides an API that allows the calling code to prompt the user for credentials.<br/>                                                                                                                                                                                    | yes<br/> | no<br/>  |
| **FTP**<br/>                                                                                                                                                                                                                                                                                                 | yes<br/> | no<br/>  |
| **Autodial/RAS Support**<br/> This is legacy functionality. Use [Remote Access](https://msdn.microsoft.com/library/windows/desktop/bb545679) instead.<br/>                                                                                                                                                                                             | yes<br/> | no<br/>  |
| **Zones**<br/> Automatic integration with Internet Explorer security zones.<br/>                                                                                                                                                                                                                       | yes<br/> | no<br/>  |
| **IDNA Support**<br/> Integrated support for the IDNA RFC/Punycode.<br/>                                                                                                                                                                                                                               | yes<br/> | no<br/>  |
| **Cookie Jar APIs**<br/> Persistent and non-persistent cookies are supported. Any application or script can use this to see the same cookies as the browser.<br/>                                                                                                                                      | yes<br/> | no<br/>  |
| **Protected Mode IE Support**<br/>                                                                                                                                                                                                                                                                           | yes<br/> | no<br/>  |
| **Decompression Support**<br/> Support for gzip and deflate compression scheme.<br/>                                                                                                                                                                                                                   | yes<br/> | no<br/>  |
| **Chunked Upload Support**<br/> Client code must perform the chunking.<br/>                                                                                                                                                                                                                            | no<br/>  | yes<br/> |
| **SOCKS v4 Support**<br/> Does not include v4a or v5.<br/>                                                                                                                                                                                                                                             | yes<br/> | no<br/>  |
| **Bidirectional Send and Receive**<br/>                                                                                                                                                                                                                                                                      | no<br/>  | no<br/>  |
| **Overlapped I/O**<br/>                                                                                                                                                                                                                                                                                      | no<br/>  | no<br/>  |
| **File scheme support**<br/> Useful for proxy scripts with a file scheme.<br/>                                                                                                                                                                                                                         | yes<br/> | no<br/>  |
| **InternetOpenUrl**<br/> Simplified code to open a URL.<br/>                                                                                                                                                                                                                                           | yes<br/> | no<br/>  |
| **Services Support**<br/> Can be run from a service or a service account.<br/>                                                                                                                                                                                                                         | no<br/>  | yes<br/> |
| **Session Isolation**<br/> Separate sessions do not impact each other.<br/>                                                                                                                                                                                                                            | no<br/>  | yes<br/> |
| **Impersonation**<br/> Supports being called while the thread is impersonating a different user.<br/>                                                                                                                                                                                                  | no<br/>  | yes<br/> |



 

## Related topics

<dl> <dt>

[WinINet](portal.md)
</dt> <dt>

[WinHTTP](https://msdn.microsoft.com/library/windows/desktop/aa384273)
</dt> </dl>

 

 





