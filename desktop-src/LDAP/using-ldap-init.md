---
title: Using ldap\_init
description: Security can be addressed in different ways by using the ldap\_init function to initialize the LDAP Server session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c85b0d17-f554-4e39-a122-cd3d6c59f87f
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Using ldap_init LDAP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using ldap\_init

Security can be addressed in different ways by using the [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master) function to initialize the LDAP Server session.

Consider the following primary security concepts when establishing an LDAP connection.



| Security concept  | Consideration                                                   |
|-------------------|-----------------------------------------------------------------|
| Authentication    | Verify the identity of the client and server.                   |
| Message Integrity | Verify that the sent message cannot be intercepted and altered. |
| Privacy           | Verify that the sent message cannot be intercepted and read.    |



 

Authentication, message integrity and privacy can be addressed through the use of the [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master) function. The **ldap\_init** function can set the proper conditions for the secure connection.

> [!Note]  
> No action is performed, until the connection is established. To set a level of security, after making the call to the [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master) function, one or more calls to the [**ldap\_set\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_set_option?branch=master) function must be made.

 

## Simple Authentication and Security Layer Protocol

The Simple Authentication and Security Layer (SASL) protocol is a method for adding authentication support to connection-based protocols. One of the advantages of using SASL security context options is that no certificates are required.

To use SASL security contexts, call the [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master) function with the port number set to **LDAP\_PORT** (389).

You can authenticate the client, sign the message, and encrypt the message by using one of the SASL methods available as [**Session Options**](session-options.md). These options include:

-   **LDAP\_OPT\_SIGN**
-   **LDAP\_OPT\_ENCRYPT**

To authenticate the client securely, call the [**ldap\_bind\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_bind_s?branch=master) function and pass it the **LDAP\_AUTH\_NEGOTIATE** option. In this case the security context is negotiated between Kerberos and NTLM, and the client can be authenticated securely, but the remaining message is unencrypted and is transmitted in plaintext.

To ensure that a message is not tampered with enroute to its destination, secure the data by setting the **LDAP\_OPT\_SIGN** session option by using the [**ldap\_set\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_set_option?branch=master) function. If the message is tampered, it can be detected on the other end. Again, the message itself is sent in plaintext.

To protect the privacy of the message, an encrypted session can be established by turning on the **LDAP\_OPT\_ENCRYPT** session option with a call to the [**ldap\_set\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_set_option?branch=master) function.

Some SASL security features are not supported on all operating systems. The following table lists which security contexts are supported on which operating systems.



| Operating system    | Kerberos | NTLM | Digest | Simple |
|---------------------|----------|------|--------|--------|
| Windows Server 2003 | Yes      | Yes  | Yes    | No     |



 

## Transport Layer Security Protocol

The Transport Layer Security (TLS) protocol is an authentication and encryption security context that uses certificates to confirm the identity of the client and server involved in establishing a connection. TLS is a technology formerly known as SSL.

There are two ways to establish a TLS (SSL) connection using the [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master) function.

-   To have the entire session encrypted, including the authentication step, call the [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master) function with its *PortNumber* parameter set to either **LDAP\_SSL\_PORT** (636) or to **LDAP\_SSL\_GC\_PORT** (3269).
-   To start the encryption after authentication, call the [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master) function with its *PortNumber* parameter set to **LDAP\_PORT** (389), and then call the [**ldap\_set\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_set_option?branch=master) function, passing in **LDAP\_OPT\_SSL**.

## An Unencrypted Session

An unencrypted session can be created using the [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master) function. To do this, call the **ldap\_init** function with its *PortNumber* parameter set to **LDAP\_PORT** (389).

If the session is unencrypted, then a network monitor connected to the network can read the messages transmitted between the server and client.

> \[!Caution\]  
> Consider what content is transmitted over an unencrypted connection. For example, if the session is unencrypted and the client authenticates itself by sending a name and password to the server, as might be done with a call to [**ldap\_simple\_bind\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_simple_bind_s?branch=master), that name and password could be compromised.

 

For an example of using [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master), see [Example Code for Establishing a Session Without Encryption](example-code-for-establishing-a-session-without-encryption.md).

 

 




