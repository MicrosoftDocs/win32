---
description: The information in this topic applies to Windows Server 2003 and Windows XP.
ms.assetid: 45536902-af80-4dca-b3ce-207086844763
title: Secure Sockets Layer Protocol
ms.topic: article
ms.date: 05/31/2018
---

# Secure Sockets Layer Protocol

The information in this topic applies to Windows Server 2003 and Windows XP. For cipher suites for Windows Server 2008 and Windows Vista, see [Cipher Suites in Schannel](cipher-suites-in-schannel.md).

Schannel supports versions 2.0 and 3.0 of the [*Secure Sockets Layer (SSL) protocol*](../secgloss/s-gly.md).

> [!Note]  
> Beginning with Windows 10, version 1607 and Windows Server 2016, SSL 2.0 has been removed and is no longer supported.

 

## SSL 3.0

SSL 3.0 is the predecessor of the [Transport Layer Security Protocol](transport-layer-security-protocol.md).

Schannel supports the cipher suites listed under [TLS Cipher Suites](/windows/win32/secauthn/cipher-suites-in-schannel) for SSL 3.0. SSL 3.0 supports all of the cipher suites listed under TLS Cipher Suites as well as SSL\_FORTEZZA\_KEA\_WITH\_FORTEZZA\_CBC\_SHA.

## SSL 2.0

SSL 2.0 has been superseded by TLS and should not be used for new development.

Schannel supports the following cipher suites for SSL 2.0. The suites are listed in order from most secure to least secure.

-   SSL\_RC4\_128\_WITH\_MD5
-   SSL\_DES\_192\_EDE3\_CBC\_WITH\_MD5
-   SSL\_RC2\_CBC\_128\_CBC\_WITH\_MD5
-   SSL\_DES\_64\_CBC\_WITH\_MD5
-   SSL\_RC4\_128\_EXPORT40\_WITH\_MD5

 

 