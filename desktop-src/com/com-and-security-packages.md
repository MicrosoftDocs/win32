---
title: COM and Security Packages
description: Windows supports NTLMSSP (LAN Manager Security Support Provider), the Kerberos v5 authentication protocol, and the Schannel security package, which provides the PCT 1.0, SSL 2.0, SSL 3.0, and TLS 1.0 protocols.
ms.assetid: a0c095a8-93b7-4350-aac6-a9a066cccffd
ms.topic: article
ms.date: 05/31/2018
---

# COM and Security Packages

Windows supports NTLMSSP (LAN Manager Security Support Provider), the Kerberos v5 authentication protocol, and the Schannel security package, which provides the PCT 1.0, SSL 2.0, SSL 3.0, and TLS 1.0 protocols. Also supported is Snego, which checks for available security packages and selects the most appropriate one.

The following table shows the levels of authentication supported by the various security packages.



| Server/Client Authentication                                                                                           | Security Package Support                                         |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Neither can get the name of the other.<br/>                                                                      | None<br/>                                                  |
| The client can authenticate the server, but not vice versa.<br/>                                                 | Schannel<br/>                                              |
| The client cannot discover the server, but the server can get the user ID of the client.<br/>                    | NTLMSSP<br/>                                               |
| Mutual authentication: Both the client and server can know the name of the other, if permission is granted.<br/> | NTLMSSP (locally), Kerberos v5 protocol, and Schannel<br/> |



 

For more information about these security packages, see the following topics in this section:

-   [NTLMSSP](ntlmssp.md)
-   [Kerberos v5 Protocol](kerberos-v5-protocol.md)
-   [Schannel](schannel.md)
-   [Snego](snego.md)

## Related topics

<dl> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 





