---
description: Windows Challenge/Response (NTLM) is the authentication protocol used on networks that include systems running the Windows operating system and on stand-alone systems.
ms.assetid: 35a38858-d36f-45c9-95f4-2541a182f5ac
title: Microsoft NTLM
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft NTLM

Windows Challenge/Response (NTLM) is the authentication protocol used on networks that include systems running the Windows operating system and on stand-alone systems.

The Microsoft [*Kerberos*](../secgloss/k-gly.md) [*security package*](../secgloss/s-gly.md) adds greater security than NTLM to systems on a network. Although Microsoft *Kerberos* is the protocol of choice, NTLM is still supported. NTLM must also be used for logon authentication on stand-alone systems. For more information about Kerberos, see [Microsoft Kerberos](microsoft-kerberos.md).

NTLM credentials are based on data obtained during the interactive logon process and consist of a domain name, a user name, and a one-way [*hash*](../secgloss/h-gly.md) of the user's password. NTLM uses an encrypted challenge/response protocol to authenticate a user without sending the user's password over the wire. Instead, the system requesting authentication must perform a calculation that proves it has access to the secured NTLM credentials.

Interactive NTLM authentication over a network typically involves two systems: a client system, where the user is requesting authentication, and a domain controller, where information related to the user's password is kept. Noninteractive authentication, which may be required to permit an already logged-on user to access a resource such as a server application, typically involves three systems: a client, a server, and a domain controller that does the authentication calculations on behalf of the server.

The following steps present an outline of NTLM noninteractive authentication. The first step provides the user's NTLM credentials and occurs only as part of the interactive authentication (logon) process.

1.  (Interactive authentication only) A user accesses a client computer and provides a domain name, user name, and password. The client computes a cryptographic [*hash*](../secgloss/h-gly.md) of the password and discards the actual password.
2.  The client sends the user name to the server (in [*plaintext*](../secgloss/p-gly.md)).
3.  The server generates a 16-byte random number, called a *challenge* or [*nonce*](../secgloss/n-gly.md), and sends it to the client.
4.  The client encrypts this challenge with the hash of the user's password and returns the result to the server. This is called the *response*.
5.  The server sends the following three items to the domain controller:

    -   User name
    -   Challenge sent to the client
    -   Response received from the client

6.  The domain controller uses the user name to retrieve the hash of the user's password from the Security Account Manager database. It uses this password hash to encrypt the challenge.
7.  The domain controller compares the encrypted challenge it computed (in step 6) to the response computed by the client (in step 4). If they are identical, authentication is successful.

Your application should not access the NTLM [*security package*](../secgloss/s-gly.md) directly; instead, it should use the [*Negotiate*](../secgloss/n-gly.md) security package. Negotiate allows your application to take advantage of more advanced [*security protocols*](../secgloss/s-gly.md) if they are supported by the systems involved in the authentication. Currently, the Negotiate security package selects between [*Kerberos*](../secgloss/k-gly.md) and NTLM. Negotiate selects Kerberos unless it cannot be used by one of the systems involved in the authentication.

 

 
