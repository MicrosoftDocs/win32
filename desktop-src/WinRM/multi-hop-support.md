---
title: Multi-Hop Support in WinRM
description: Windows Remote Management (WinRM) supports the delegation of user credentials across multiple remote computers.
ms.assetid: 0e6c8966-bb05-4dfb-b154-300fa76e8d9c
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Multi-Hop Support in WinRM

Windows Remote Management (WinRM) supports the delegation of user credentials across multiple remote computers. The multi-hop support functionality can now use Credential Security Service Provider (CredSSP) for authentication. CredSSP enables an application to delegate the user's credentials from the client computer to the target server.

CredSSP authentication is intended for environments where Kerberos delegation cannot be used. Support for CredSSP was added to allow a user to connect to a remote server and have the ability to access a second-hop machine, such as a file share.

> [!Note]  
> WinRM clients and servers will support CredSSP authentication only with explicit credentials.

 

## Multi-Hop Support Configuration Setup and Details

There are multiple mechanisms for configuring WinRM settings. In the following procedure, the **winrm** utility and Group Policy editor (**GPEdit.msc**) are used. CredSSP can also be enabled for WinRM by using Windows PowerShell. See the [Enable-WSManCredSSP](/powershell/module/Microsoft.WsMan.Management/Enable-WSManCredSSP?view=powershell-5.1&preserve-view=true), [Get-WSManCredSSP](/powershell/module/Microsoft.WsMan.Management/Get-WSManCredSSP?view=powershell-5.1&preserve-view=true), and [Disable-WSManCredSSP](/powershell/module/Microsoft.WsMan.Management/Disable-WSManCredSSP?view=powershell-5.1&preserve-view=true) Windows PowerShell cmdlets for detailed configuration information and usage examples.

CredSSP delegation must be enabled in the client settings and in the service settings on the remote computer. In addition, using CredSSP requires setting up an HTTP or HTTPS [*listener*](windows-remote-management-glossary.md) on the server.

**To configure multi-hop support using CredSSP authentication for WinRM**

1.  CredSSP must be enabled in the client configuration settings. This flag can be enabled manually or through a Group Policy setting. The default setting is **False**. The **Allow CredSSP authentication** policy is located at the following path: Computer Configuration\\Administrative template\\Windows Components\\Windows Remote Management (WinRM)\\WinRM Client.

    The following command demonstrates how to use the winrm utility to enable CredSSP on the WinRM client:

    **winrm set winrm/config/client/auth @{CredSSP="true"}**

2.  CredSSP must be enabled in the WinRM service configuration settings. This flag can be enabled manually or through a Group Policy setting. The default setting is **False**. The **Allow CredSSP authentication** policy is located at the following path: Computer Configuration\\Administrative template\\Windows Components\\Windows Remote Management (WinRM)\\WinRM Service.

    The following command demonstrates how to use the winrm utility to enable CredSSP on the WinRM service:

    **winrm set winrm/config/service/auth @{CredSSP="true"}**

3.  The Allow Delegating Fresh Credentials (**AllowFreshCredentials**) policy setting must be enabled on the WinRM client, and a Service Principal Name (SPN) with the WSMAN prefix must be added to the policy. The SPN represents the target computer to which the user credentials can be delegated. The SPN can be set to one or more computers. The following table contains examples of valid formats for SPNs.

    

    | SPN                                       | Description                                                                         |
    |-------------------------------------------|-------------------------------------------------------------------------------------|
    | WSMAN/myComputer.myDomain.com<br/>  | WinRM server running on myComputer.myDomain.com.<br/>                         |
    | WSMAN/\*.myDomain.com<br/>          | All WinRM servers running in myDomain.com.<br/>                               |
    | WSMAN/\*.fabrikam.myDomain.com<br/> | All WinRM servers running in on all computers in .fabrikam.myDomain.com.<br/> |

    

     

    For more information about setting Group Policies, see [Installation and Configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md).

    For more information about the **AllowFreshCredentials** policy, see the policy description provided by the Group Policy editor. The **AllowFreshCredentials** policy is located at the following path: Computer Configuration\\Administrative Templates\\System\\Credentials Delegation.

4.  An HTTPS or HTTP [*listener*](windows-remote-management-glossary.md) must be configured on the server. The certificate thumbprint used for configuring the HTTPS *listener* is also used to configure the CertificateThumbprint setting under the WinRM service settings.

    The following command demonstrates how to use the winrm utility to configure an HTTPS [*listener*](windows-remote-management-glossary.md):

    **winrm quickconfig -transport:https**

If Kerberos authentication between the client and server is not possible, the user must configure one of the following settings for multi-hop support:

-   For better security, the user should add the **CertificateThumbprint** attribute to the WinRM service setting. If the WinRM service is configured with a **CertificateThumbprint** attribute, the service attempts to locate the corresponding certificate in the Local Machine store and uses this certificate for the CredSSP authentication. If the WinRM service uses a certificate from the Local Machine store to authenticate the server, the Network Service account must be allowed access to the private key of the certificate.

    > [!Note]  
    > If the service setting is not configured, the WinRM server uses a self-signed certificate that is created in memory to encrypt messages sent to the client. However, this certificate is not used for authentication.

     

-   If neither Kerberos authentication nor certificate thumbprints are available, the user can enable NTLM authentication. If NTLM authentication is used, the Allow Fresh Credentials with NTLM-only Server Authentication (**AllowFreshCredentialsWhenNTLMOnly**) policy must be enabled, and an SPN with the WSMAN prefix must be added to the policy. This setting is less secure than both Kerberos authentication and certificate thumbprints, because credentials are sent to an unauthenticated server.

    For more information about the **AllowFreshCredentialsWhenNTLMOnly** policy, see the policy description provided by the Group Policy editor. The **AllowFreshCredentialsWhenNTLMOnly** policy is located at the following path: Computer Configuration\\Administrative Templates\\System\\Credentials Delegation.

## Using CredSSP Authentication with Explicit Credentials

A user can specify explicit credentials over both HTTP and HTTPS. The following command demonstrates how to use the winrm utility to perform a remote operation using CredSSP authentication with explicit credentials over HTTPS:

**winrm OPERATION -remote:https://myMachine -authentication:CredSSP -username:myUsername -password:myPassword**

 

