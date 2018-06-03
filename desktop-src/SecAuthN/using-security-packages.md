---
Description: Lists the security packages that can be used with SSPI.
ms.assetid: f5999d41-b334-49be-8883-d9b9042d20dc
title: Using Security Packages
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Security Packages

The [*Security Support Provider Interface*](https://www.bing.com/search?q=*Security Support Provider Interface*) (SSPI) can be used with the following [*security packages*](https://www.bing.com/search?q=*security packages*):

-   [Kerberos Security Package](#kerberos-security-package)
-   [NTLM Security Package](#ntlm-security-package)

The [*Kerberos*](https://www.bing.com/search?q=*Kerberos*) and NTLM protocols are implemented as security packages from the Secur32.dll [*security support provider*](https://www.bing.com/search?q=*security support provider*) (SSP) supplied with the operating system. By default, support for both Kerberos and NTLM authentication are loaded by the [*local security authority*](https://www.bing.com/search?q=*local security authority*) (LSA) on a computer when the system starts. In Windows Server or Windows domains, either package can be used to authenticate network logons and client/server connections. Which one is used depends on the capabilities of the computer on the other side of the connection. The Kerberos protocol is always preferred, if available.

After a security context for an interactive user has been established, another instance of the Kerberos or NTLM package can be loaded by a process running in the security context of the user to support the exchanging, signing, verifying, encrypting, and decrypting of messages. However, no process other than the LSA is ever permitted access to [*session keys*](https://www.bing.com/search?q=*session keys*) or tickets in the credentials cache.

System services and transport-level applications access an SSP through SSPI, which provides functions for enumerating the security packages available on a system, selecting a package, and using that package to obtain an authenticated connection.

The methods in SSPI are generic routines that developers can use without knowing the details of a particular [*security protocol*](https://www.bing.com/search?q=*security protocol*). For example, when a client/server connection is authenticated:

1.  The application on the client side of the connection sends [*credentials*](https://www.bing.com/search?q=*credentials*) to the server using the SSPI function [**InitializeSecurityContext (General)**](/windows/desktop/api/Sspi/).
2.  The application on the server side of the connection responds with the SSPI function [**AcceptSecurityContext (General)**](/windows/desktop/api/Sspi/).
3.  After the connection has been authenticated, the LSA on the server uses information from the client to build an [*access token*](https://www.bing.com/search?q=*access token*).
4.  The server can then call the SSPI function [**ImpersonateSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-impersonatesecuritycontext) to attach the access token to an impersonation thread for the service.

## Kerberos Security Package

The Kerberos [*security package*](https://www.bing.com/search?q=*security package*) is based on the [*Kerberos authentication protocol*](https://www.bing.com/search?q=*Kerberos authentication protocol*).

If the Kerberos protocol is being used to authenticate a client/server connection, [**InitializeSecurityContext (Kerberos)**](/windows/desktop/api/Sspi/) generates a GSSAPI message that includes a KRB\_AP\_REQ message from the client. [**AcceptSecurityContext (Kerberos)**](/windows/desktop/api/Sspi/) then generates a GSSAPI message that includes a KRB\_AP\_REP message from the server.

For background information on the steps that take place behind the scenes in the implementation of a Kerberos protocol, see [Microsoft Kerberos](microsoft-kerberos.md).

All distributed services use SSPI to access the Kerberos protocol. A partial list of the ways in which the Kerberos protocol is used for authentication includes:

-   Print spooler services
-   CIFS/SMB remote file access
-   [*LDAP*](https://www.bing.com/search?q=*LDAP*) queries to the Active Directory
-   Distributed file system management and referrals
-   IPsec host-to-host security authority authentication
-   Reservation requests for network Quality of Service
-   Intranet authentication to Internet Information Services
-   Remote server or workstation management using authenticated RPC
-   [*Certificate requests*](https://www.bing.com/search?q=*Certificate requests*) to Certificate Services for domain users and computers

## NTLM Security Package

The NTLM security package is based on the NTLM authentication protocol.

 

 



