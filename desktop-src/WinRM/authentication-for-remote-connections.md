---
title: Authentication for Remote Connections
description: Windows Remote Management maintains security for communication between computers by supporting several standard methods of authentication and message encryption.
ms.assetid: 97a13b07-ae7a-4d2f-8841-77a22c91b204
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Authentication for Remote Connections

Windows Remote Management maintains security for communication between computers by supporting several standard methods of authentication and message encryption.

## Default Group Access

During setup, WinRM creates the local group **WinRMRemoteWMIUsers\_\_**. WinRM then restricts remote access to any user that is not a member of either the local administration group or the **WinRMRemoteWMIUsers\_\_** group. You can add a local user, domain user, or domain group to **WinRMRemoteWMIUsers\_\_** by typing **net localgroup WinRMRemoteWMIUsers\_\_ /add &lt;domain&gt;\\&lt;username&gt;** at the command prompt. Optionally, you can use the Group Policy to add a user to the group.

## Default Authentication Settings

The default credentials, user name, and password, are the credentials for the logged-on user account that runs the script.

**To change to another account on a remote computer**

1.  Specify the credentials in a [**ConnectionOptions**](connectionoptions.md) or [**IWSManConnectionOptions**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanconnectionoptions) object and supply that to the [**CreateSession**](wsman-createsession.md) call.
2.  Set the **WSManFlagCredUserNamePassword** in the *flags* parameter in the [**CreateSession**](wsman-createsession.md) call.

The following list contains a list of what occurs when a script or application runs under the default credentials:

-   [*Kerberos*](windows-remote-management-glossary.md) is the default method of authentication when the client is in a domain and the remote destination string is not one of the following: localhost, 127.0.0.1, or \[::1\].
-   [*Negotiate*](windows-remote-management-glossary.md) is the default method when the client is not in a domain, but the remote destination string is one of the following: localhost, 127.0.0.1, or \[::1\].

If you supply explicit credentials with a [**ConnectionOptions**](connectionoptions.md) object, Negotiate is the default method. Negotiate authentication determines whether the ongoing authentication method is Kerberos or NTLM, depending on whether the computers are in a domain or workgroup. If connecting to a remote target computer using a local account, then the account should be prefixed with the computer name. For example, myComputer\\myUsername.

If you specify Negotiate, Digest, or Basic authentication and fail to supply a [**ConnectionOptions**](connectionoptions.md) object, then you will receive an error indicating that explicit credentials are required. If HTTPS is not the transport, then the target remote computer must be configured in the list of trusted host computers.

For more information about the authentication types that are enabled in the default configuration settings, see [Installation and Configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md).

## Basic Authentication

To explicitly establish [*Basic*](windows-remote-management-glossary.md) authentication in the call to [**WSMan.CreateSession**](wsman-createsession.md), set the **WSManFlagUseBasic** and **WSManFlagCredUserNamePassword** flags in the *flags* parameter. Basic authentication is disabled in the default configuration settings for both the WinRM client and the WinRM server.

## Digest Authentication

To explicitly establish [*Digest*](windows-remote-management-glossary.md) authentication in the call to [**WSMan.CreateSession**](wsman-createsession.md), set the **WSManFlagUseDigest** flag in the *flags* parameter. Digest is not supported. It cannot be configured, for the WinRM server component.

## Negotiate Authentication

To explicitly establish [*Negotiate*](windows-remote-management-glossary.md) authentication, also known as Windows Integrated Authentication, in the call to [**WSMan.CreateSession**](wsman-createsession.md), set the **WSManFlagUseNegotiate** flag in the *flags* parameter.

[User Account Control (UAC)](https://support.microsoft.com/help/922708/how-to-use-user-account-control-uac-in-windows-vista) affects access to the WinRM service. When Negotiate authentication is used in a workgroup, only the built-in Administrator account can access the service. To allow all accounts in the Administrators group to access the service, set the following registry value:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Policies**\\**System**\\**LocalAccountTokenFilterPolicy** = 1

## Kerberos Authentication

To explicitly establish [*Kerberos*](windows-remote-management-glossary.md) authentication in the call to [**WSMan.CreateSession**](wsman-createsession.md), set the **WSManFlagUseKerberos** flag in the *flags* parameter. Both the client and the server computers must be joined to a domain. If you use Kerberos as the authentication method, you cannot use an IP address in the call to [**WSMan.CreateSession**](wsman-createsession.md) or [**IWSMan::CreateSession**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsman-createsession).

## Client Certificate-based Authentication

To establish client certificate-based authentication in the call to [**WSMan.CreateSession**](wsman-createsession.md), set the **WSManFlagUseClientCertificate** flag in the *flags* parameter.

You must first enable certificate authentication on both the client and service by using the Winrm command line tool. For more information, see [Enabling Authentication Options](#enabling-or-disabling-authentication-options). You must also create an entry in the CertMapping table on the WinRM server computer. This establishes a mapping between one or more certificates and a local account. After the certificate has been used for authentication and authorization, the corresponding local account is used for operations performed by the WinRM service.

The mapping can be created for a specific resource URI. To learn more, including how to create a CertMapping table entry, type **winrm help certmapping** at the command prompt.

> [!Note]  
> The maximum size certificate usable by WinRM in this context is 16KB.

 

## Enabling or Disabling Authentication Options

The default authentication option at system installation is Kerberos. For more information, see [Installation and Configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md).

If your script or application requires a specific authentication method that is not enabled, you must change the configuration to enable this type of authentication. This change can be made using the **Winrm** command-line tool or through Group Policy for the **Windows Remote Management Group Policy Object**. You may also choose to disable certain methods of authentication.

**To enable or disable authentication with the Winrm tool**

1.  To set the configuration for the WinRM client, use the **Winrm Set** command and specify the client. For example, the following command disables digest authentication for the client.

    **winrm set winrm/config/client/auth @{Digest="false"}**

2.  To set the configuration for the WinRM server, use the **Winrm Set** command and specify the service. For example, the following command enables Kerberos authentication for the service.

    **winrm set winrm/config/service/auth @{Kerberos="true"}**

## Related topics

<dl> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[**WSMan.CreateSession**](wsman-createsession.md)
</dt> <dt>

[Using Windows Remote Management](using-windows-remote-management.md)
</dt> </dl>

 

 




