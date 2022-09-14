---
title: Mutual Authentication in a Windows Sockets Service with SCP
description: The topics in this section include code examples that show how to perform mutual authentication with a service that publishes itself using a service connection point (SCP).
ms.assetid: f730464c-95ac-4285-960c-18862f6f7852
ms.tgt_platform: multiple
keywords:
- Mutual Authentication in a Windows Sockets Service with an SCP AD
- Active Directory, using, mutual authentication, Windows sockets service with an SCP
ms.topic: article
ms.date: 05/31/2018
---

# Mutual Authentication in a Windows Sockets Service with SCP

The topics in this section include code examples that show how to perform mutual authentication with a service that publishes itself using a service connection point (SCP). The examples are based on a Microsoft Windows Sockets service that uses an SSPI package to handle the mutual authentication negotiation between a client and the service. Use the following procedures to implement mutual authentication within this scenario.

**To register SPNs in a directory when a service is installed**

1.  Call the [**DsGetSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetspna) function to compose service principal names (SPNs) for the service.
2.  Call the [**DsWriteAccountSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dswriteaccountspna) function to register the SPNs on the service account or computer account in whose context the service will run. This step must be performed by a domain administrator; an exception is that a service running under the LocalSystem account can register its SPN in the form "\<service class\>/&lt;host&gt;" on the computer account of the service host.

**To verify configuration at service startup**

-   Verify that the appropriate SPNs are registered on the account under which the service is running. For more information, see [Logon Account Maintenance Tasks](logon-account-maintenance-tasks.md).

**To authenticate the service at client startup**

1.  Retrieve connection data from the service's service connection point.
2.  Establish a connection to the service.
3.  Call the [**DsMakeSpn**](/windows/desktop/api/Dsparse/nf-dsparse-dsmakespna) function to compose an SPN for the service. Compose the SPN from the known service class string, and the data retrieved from the service connection point. This data includes the host name of the server on which the service is running. Be aware that the host name must be a DNS name.
4.  Use an SSPI security package to perform the authentication:
    1.  Call the [**AcquireCredentialsHandle**](../SecAuthN/acquirecredentialshandle--general.md) function to acquire the client's credentials.
    2.  Pass the client credentials and the SPN to the [**InitializeSecurityContext**](../SecAuthN/initializesecuritycontext--general.md) function to generate a security blob to send to the service for authentication. Set the **ISC\_REQ\_MUTUAL\_AUTH** flag to request mutual authentication.
    3.  Exchange blobs with the service until the authentication is complete.
5.  Verify the returned capabilities mask for the **ISC\_REQ\_MUTUAL\_AUTH** flag to verify that mutual authentication was performed.
6.  If the authentication was successful, exchange traffic with the authenticated service. Use digital signing to ensure that messages between client and service have not been tampered with. Unless performance requirements are severe, use encryption. For more information and a code example that shows how to use the [**MakeSignature**](/windows/desktop/api/sspi/nf-sspi-makesignature), [**VerifySignature**](/windows/desktop/api/sspi/nf-sspi-verifysignature), [**EncryptMessage**](../SecAuthN/encryptmessage--general.md), and [**DecryptMessage**](../SecAuthN/decryptmessage--general.md) functions in an SSPI package, see [Ensuring Communication Integrity During Message Exchange](/windows/desktop/SecAuthN/ensuring-communication-integrity-during-message-exchange).

**To authenticate the client by the service when a client connects**

1.  Load an SSPI security package that supports mutual authentication.
2.  When a client connects, use the security package to perform the authentication:
    1.  Call the [**AcquireCredentialsHandle**](../SecAuthN/acquirecredentialshandle--general.md) function to acquire the service credentials.
    2.  Pass the service credentials and the security blob received from the client to the [**AcceptSecurityContext**](../SecAuthN/acceptsecuritycontext--general.md) function to generate a security blob to send back to the client.
    3.  Exchange blobs with the client until the authentication is complete.
3.  Check the returned capabilities mask for the **ASC\_RET\_MUTUAL\_AUTH** flag to verify that mutual authentication was performed.
4.  If the authentication was successful, exchange traffic with the authenticated client. Use digital signing and encryption unless performance is an issue.

For more information and a code example for this mutual authentication scenario, see:

-   [How a Client Authenticates an SCP-based Windows Sockets Service](how-a-client-authenticates-an-scp-based-windows-sockets-service.md)
-   [Composing and Registering SPNs for an SCP-based Windows Sockets Service](composing-and-registering-spns-for-an-scp-based-windows-sockets-service.md)
-   [How a Windows Sockets Service Authenticates a Client](how-a-windows-sockets-service-authenticates-a-client.md)

For more information, see:

-   [Publishing with service connection points](publishing-with-service-connection-points.md)
-   [SSPI documentation](/windows/desktop/SecAuthN/sspi)
-   [Windows Sockets documentation](/windows/desktop/WinSock/windows-sockets-start-page-2)

 

 
