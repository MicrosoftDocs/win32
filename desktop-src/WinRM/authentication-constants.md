---
title: Authentication Constants (WSManDisp.h)
description: Specify the authentication method and how to handle certificate servers for HTTPS transport of requests.
ms.assetid: adfefbc9-c386-48db-a0c2-145aa4f91bfa
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- WSManFlagCredUsernamePassword
- WSManFlagSkipCACheck
- WSManFlagSkipCNCheck
- WSManFlagUseNoAuthentication
- WSManFlagUseDigest
- WSManFlagUseNegotiate
- WSManFlagUseBasic
- WSManFlagUseKerberos
- WSManFlagNoEncryption
- WSManFlagUseClientCertificate
- WSManFlagUseCredSsp
- WSManFlagSkipRevocationCheck
- WSManFlagAllowNegotiateImplicitCredentials
- WSManFlagUseSsl
api_location:
- WSManDisp.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Authentication Constants

Authentication constants are constants in the **\_\_WSManSessionFlags** enumeration that specify the authentication method and how to handle certificate servers for HTTPS transport of requests.

One or more of the constants listed in the following list are required in the *flags* parameter in calls to [**WSMan.CreateSession**](wsman-createsession.md) or in [**IWSMan::CreateSession**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsman-createsession) calls that connect to a remote computer.

<dl> <dt>

<span id="WSManFlagCredUsernamePassword"></span><span id="wsmanflagcredusernamepassword"></span><span id="WSMANFLAGCREDUSERNAMEPASSWORD"></span>**WSManFlagCredUsernamePassword**
</dt> <dd> <dl> <dt>

4096 (0x1000)
</dt> <dt>



Use the user name and password as the credentials. Set this flag when you create a [**ConnectionOptions**](connectionoptions.md) object and supply [**Username**](connectionoptions-username.md) and [**Password**](connectionoptions-password.md). The credentials can be a domain account or an account on the local computer. By default, the account must be a member of the local Administrators group on the local or remote computer. However, the WinRM service can be configured to allow other users. For more information, see [Installation and Configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md). You can set this flag when you specify credentials for Negotiate authentication (also known as [*Windows Integrated Authentication*](windows-remote-management-glossary.md)) or for [*Basic authentication*](windows-remote-management-glossary.md).

The associated scripting method is [**WSMan.SessionFlagCredUsernamePassword**](wsman-sessionflagcredusernamepassword.md), and the C++ method is [**IWSManEx.SessionFlagCredUsernamePassword**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagcredusernamepassword).


</dt> </dl> </dd> <dt>

<span id="WSManFlagSkipCACheck"></span><span id="wsmanflagskipcacheck"></span><span id="WSMANFLAGSKIPCACHECK"></span>**WSManFlagSkipCACheck**
</dt> <dd> <dl> <dt>

8192 (0x2000)
</dt> <dt>



When connecting over HTTPS, the client does not validate that the server certificate is signed by a trusted certification authority (CA). Use this value only when the remote computer is trusted by other means, for example, if the remote computer is part of a network that is physically secure and isolated or the remote computer is listed as a trusted host in the WinRM configuration.

The associated scripting method is [**WSMan.SessionFlagSkipCACheck**](wsman-sessionflagskipcacheck.md), and the C++ method is [**IWSManEx.SessionFlagSkipCACheck**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagskipcacheck).


</dt> </dl> </dd> <dt>

<span id="WSManFlagSkipCNCheck"></span><span id="wsmanflagskipcncheck"></span><span id="WSMANFLAGSKIPCNCHECK"></span>**WSManFlagSkipCNCheck**
</dt> <dd> <dl> <dt>

16384 (0x4000)
</dt> <dt>



When connecting over HTTPS, the client will not validate that the common name (CN) in the server certificate matches the computer name in the connection string. Use only when the remote computer is trusted by other means, for example, if the remote computer is part of a network that is physically secure and isolated or the remote computer is listed as a trusted host in the WinRM configuration.

The associated scripting method is [**WSMan.SessionFlagSkipCNCheck**](wsman-sessionflagskipcncheck.md), and the C++ method is [**IWSManEx.SessionFlagSkipCNCheck**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagskipcncheck).


</dt> </dl> </dd> <dt>

<span id="WSManFlagUseNoAuthentication"></span><span id="wsmanflagusenoauthentication"></span><span id="WSMANFLAGUSENOAUTHENTICATION"></span>**WSManFlagUseNoAuthentication**
</dt> <dd> <dl> <dt>

32768 (0x8000)
</dt> <dt>



Use no authentication. Specify this constant when testing a connection to a remote computer to determine if a service that implements the WS-Management protocol is configured to listen for data requests. **WSManFlagUseNoAuthentication** cannot be combined with any other [**Session**](session.md) constant. The associated scripting method is [**WSMan.SessionFlagUseNoAuthentication**](wsman-sessionflagusenoauthentication.md), and the C++ method is [**WSManEx.SessionFlagUseNoAuthentication**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagusenoauthentication).


</dt> </dl> </dd> <dt>

<span id="WSManFlagUseDigest"></span><span id="wsmanflagusedigest"></span><span id="WSMANFLAGUSEDIGEST"></span>**WSManFlagUseDigest**
</dt> <dd> <dl> <dt>

65536 (0x10000)
</dt> <dt>



Use Digest authentication. Only the client computer can initiate a Digest authentication request. The client sends a request to the server to authenticate and receives a token string from the server. The client then sends the resource request, including the user name and a cryptographic hash of the password combined with the token string. Digest authentication is supported for HTTP and HTTPS. WinRM client scripts and applications can specify Digest authentication, but not the service.

The associated scripting method is [**WSMan.SessionFlagUseDigest**](wsman-sessionflagusedigest.md), and the C++ method is [**IWSManEx.SessionFlagUseDigest**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagusedigest).


</dt> </dl> </dd> <dt>

<span id="WSManFlagUseNegotiate"></span><span id="wsmanflagusenegotiate"></span><span id="WSMANFLAGUSENEGOTIATE"></span>**WSManFlagUseNegotiate**
</dt> <dd> <dl> <dt>

131072 (0x20000)
</dt> <dt>



Use Negotiate authentication. The client sends a request to the server to authenticate. The server determines whether to use Kerberos or NTLM. Kerberos is selected to authenticate a domain account and NTLM is selected for local computer accounts. The user name should be specified in the form domain\\username for a domain user or servername\\username for a local user on a server computer.

[User Account Control (UAC)](https://support.microsoft.com/help/922708/how-to-use-user-account-control-uac-in-windows-vista) affects access to the WinRM service. When Negotiate authentication is used in a workgroup or domain, only the built-in Administrator account can access the service. To allow all accounts in the Administrators group to access the service, set the following registry key to 1: **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\system\\LocalAccountTokenFilterPolicy**.

The associated scripting method is [**WSMan.SessionFlagUseNegotiate**](wsman-sessionflagusenegotiate.md), and the C++ method is [**IWSManEx.SessionFlagUseNegotiate**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagusenegotiate).


</dt> </dl> </dd> <dt>

<span id="WSManFlagUseBasic"></span><span id="wsmanflagusebasic"></span><span id="WSMANFLAGUSEBASIC"></span>**WSManFlagUseBasic**
</dt> <dd> <dl> <dt>

262144 (0x40000)
</dt> <dt>



Use Basic authentication. The client presents credentials in the form of a user name and password, directly transmitted in the request message. You can specify only credentials that identify a local administrator account on the remote computer.

The associated scripting method is [**WSMan.SessionFlagUseBasic**](wsman-sessionflagusebasic.md), and the C++ method is [**IWSManEx.SessionFlagUseBasic**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagusebasic).


</dt> </dl> </dd> <dt>

<span id="WSManFlagUseKerberos"></span><span id="wsmanflagusekerberos"></span><span id="WSMANFLAGUSEKERBEROS"></span>**WSManFlagUseKerberos**
</dt> <dd> <dl> <dt>

524288 (0x80000)
</dt> <dt>



Use Kerberos authentication. The client and server mutually authenticate using Kerberos tickets.

The associated scripting method is [**WSMan.SessionFlagUseKerberos**](wsman-sessionflagusekerberos.md), and the C++ method is [**IWSManEx.WSMan.SessionFlagUseKerberos**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagusekerberos).


</dt> </dl> </dd> <dt>

<span id="WSManFlagNoEncryption"></span><span id="wsmanflagnoencryption"></span><span id="WSMANFLAGNOENCRYPTION"></span>**WSManFlagNoEncryption**
</dt> <dd> <dl> <dt>

1048576 (0x100000)
</dt> <dt>



Use no encryption. Unencrypted traffic is not allowed by default and must be enabled on both the client and server.

The associated scripting method is [**WSMan.SessionFlagNoEncryption**](wsman-sessionflagnoencryption.md), and the C++ method is [**IWSManEx.SessionFlagNoEncryption**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-sessionflagnoencryption).


</dt> </dl> </dd> <dt>

<span id="WSManFlagUseClientCertificate"></span><span id="wsmanflaguseclientcertificate"></span><span id="WSMANFLAGUSECLIENTCERTIFICATE"></span>**WSManFlagUseClientCertificate**
</dt> <dd> <dl> <dt>

2097152 (0x200000)
</dt> <dt>



Use client certificate-based authentication.

The associated scripting method is [**WSMan.SessionFlagUseClientCertificate**](wsman-sessionflaguseclientcert.md), and the C++ method is [**IWSManEx2.SessionFlagUseClientCertificate**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex2-sessionflaguseclientcertificate).


</dt> </dl> </dd> <dt>

<span id="WSManFlagUseCredSsp"></span><span id="wsmanflagusecredssp"></span><span id="WSMANFLAGUSECREDSSP"></span>**WSManFlagUseCredSsp**
</dt> <dd> <dl> <dt>

16777216 (0x1000000)
</dt> <dt>



Use Credential Security Support Provider (CredSSP) authentication.

The associated scripting method is [**WSMan.SessionFlagUseCredSsp**](wsman-sessionflagusecredssp.md), and the C++ method is [**IWSManEx3.SessionFlagUseCredSsp**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex3-sessionflagusecredssp).


</dt> </dl> </dd> <dt>

<span id="WSManFlagSkipRevocationCheck"></span><span id="wsmanflagskiprevocationcheck"></span><span id="WSMANFLAGSKIPREVOCATIONCHECK"></span>**WSManFlagSkipRevocationCheck**
</dt> <dd> <dl> <dt>

0x2000000
</dt> <dt>



Do not check for certificate revocation during authentication.


</dt> </dl> </dd> <dt>

<span id="WSManFlagAllowNegotiateImplicitCredentials"></span><span id="wsmanflagallownegotiateimplicitcredentials"></span><span id="WSMANFLAGALLOWNEGOTIATEIMPLICITCREDENTIALS"></span>**WSManFlagAllowNegotiateImplicitCredentials**
</dt> <dd> <dl> <dt>

0x4000000
</dt> <dt>



Allow implicit credentials.


</dt> </dl> </dd> <dt>

<span id="WSManFlagUseSsl"></span><span id="wsmanflagusessl"></span><span id="WSMANFLAGUSESSL"></span>**WSManFlagUseSsl**
</dt> <dd> <dl> <dt>

0x8000000
</dt> <dt>



Use Secure Socket Layer, enables HTTPS.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |



## See also

<dl> <dt>

[Session Constants](session-constants.md)
</dt> </dl>

 

 





