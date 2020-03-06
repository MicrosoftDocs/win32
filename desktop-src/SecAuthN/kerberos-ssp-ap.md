---
Description: The Kerberos authentication package is used when logging on to a network; local logons are handled by MSV1\_0.
ms.assetid: 43970c99-53f1-43c1-9d9f-65573572f731
title: Kerberos SSP/AP
ms.topic: article
ms.date: 05/31/2018
---

# Kerberos SSP/AP

The [*Kerberos*](https://msdn.microsoft.com/library/ms721590(v=VS.85).aspx) authentication package is used when logging on to a network; local logons are handled by MSV1\_0.

When a user logs on using a network account, by default, Kerberos attempts to connect to the Kerberos [*Key Distribution Center*](https://msdn.microsoft.com/library/ms721590(v=VS.85).aspx) (KDC) on the domain controller and obtain a ticket granting ticket (TGT) by using the logon data supplied by the user.

If a Kerberos KDC is not available, Windows uses MSV1\_0 and pass-through authentication as described in [MSV1\_0 Authentication Package](msv1-0-authentication-package.md).

The Kerberos authentication package supports version 5, revision 6 of the Kerberos protocol. This protocol is based on Internet [RFC 4120](https://www.ietf.org/rfc/rfc4120.txt). For more information, see the IETF website:

[https://www.ietf.org](https://www.ietf.org/)

For more information about Kerberos, see [Microsoft Kerberos](microsoft-kerberos.md).

## Kerberos Credential Formats

The user [*credentials*](https://msdn.microsoft.com/library/ms721572(v=VS.85).aspx) assigned by the Kerberos authentication package after a successful logon attempt are a ticket and a temporary encryption key, often called a [*session key*](https://msdn.microsoft.com/library/ms721625(v=VS.85).aspx). The ticket contains both an encrypted copy of the client's credentials and the session key.

 

 



