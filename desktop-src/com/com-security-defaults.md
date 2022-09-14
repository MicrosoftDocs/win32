---
title: COM Security Defaults
description: You can use the COM security defaults for your application rather than specifying your own security settings.
ms.assetid: 6f1f6925-a6ab-4cfa-b0b4-b4b4012979f2
ms.topic: article
ms.date: 05/31/2018
---

# COM Security Defaults

You can use the COM security defaults for your application rather than specifying your own security settings. In that case, COM will initialize and manage security for you. You do not need to configure the registry or call any security functions in your program.

However, if certain registry named values have been set or modified, the security defaults that COM uses will be affected. The list below describes COM security default values and explains how some values are influenced by registry settings.

Following are the default security values that COM uses:

-   The default security service provider is the one that is determined by COM to be the most compatible with the environment. COM chooses either the Kerberos v5 protocol or NTLMSSP, with the Kerberos protocol being the default choice. None of the protocols provided by Schannel are ever chosen as the default.
-   The system identifies a caller through user name and password and automatically creates an identification token used by the security system.
-   If the [LegacyAuthenticationLevel](legacyauthenticationlevel.md) named value exists and if its value has been set, that value is used. Otherwise, the authentication level is set at connect (RPC\_C\_AUTHN\_LEVEL\_CONNECT). This level means that at the first call a client makes to the server, COM does an authentication check. If the client passes the check, no further authentication is done. The AuthenticationLevel value can also be set under the [AppID](appid-key.md) key.
-   If the [LegacyImpersonationLevel](legacyimpersonationlevel.md) named value exists and if its value has been set, that value is used. Otherwise, the impersonation level is set to identify (RPC\_C\_IMP\_LEVEL\_IDENTIFY). Impersonation rights are granted by the client to the server. Identify level means that the server can obtain the client's identity. The server can impersonate the client for access control list (ACL) checking but cannot access system objects as the client. For more information, see [Impersonation Levels](impersonation-levels.md) and [Cloaking](cloaking.md).
-   If the [AccessPermission](accesspermission.md) named value under **AppID** exists and has been set, that value is used. Otherwise, COM checks for a [DefaultAccessPermission](defaultaccesspermission.md) entry. If present, that value is used. If this value is not present, COM constructs an ACL that grants permissions to the server identity and the local system.
-   If the [SRPTrustLevel](srptrustlevel.md) named value under **AppID** exists and has been set, that value is used. Otherwise, the Software Restriction Policy (SRP) trust level is set to Disallowed (SAFER\_LEVELID\_DISALLOWED), which indicates that the application is run in a constrained environment and is disallowed from accessing any security-sensitive user privileges of the user.

## Related topics

<dl> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




