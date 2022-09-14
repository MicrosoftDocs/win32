---
title: Registry Values for System-Wide Security
description: Registry Values for System-Wide Security
ms.assetid: f1db42b8-4328-4b39-b87f-583382395235
ms.topic: article
ms.date: 05/31/2018
---

# Registry Values for System-Wide Security

It is not recommended that you change the system-wide security settings, because this will affect all COM server applications that do not set their own process-wide security, and might prevent them from working properly. If you are changing the system-wide security settings to affect the security settings for a particular COM application, then you should instead change the process-wide security settings for that particular COM application. For more information about setting process-wide security, see [Setting Process-Wide Security](setting-processwide-security.md).

Certain values in the registry are used to determine security settings for applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). You can use Dcomcnfg.exe to modify these default security settings for a computer. For step-by-step procedures that describe how to use Dcomcnfg.exe for this purpose, see [Setting System-Wide Security Using DCOMCNFG](setting-machine-wide-security-using-dcomcnfg.md).

Another way to change default system-wide settings is to manipulate registry values directly. However, only administrators and the system have full access to the portion of the registry that contains the default system-wide call-security settings. All other users have read-access only.

The named values that affect system-wide security defaults are as follows:

-   [DefaultLaunchPermission](defaultlaunchpermission.md)
-   [DefaultAccessPermission](defaultaccesspermission.md)
-   [LegacyAuthenticationLevel](legacyauthenticationlevel.md)
-   [LegacyImpersonationLevel](legacyimpersonationlevel.md)
-   [LegacySecureReferences](legacysecurereferences.md)
-   [SRPRunningObjectChecks](srprunningobjectchecks.md)
-   [SRPActivateAsActivatorChecks](srpactivateasactivatorchecks.md)

## Related topics

<dl> <dt>

[Setting Process-Wide Security](setting-processwide-security.md)
</dt> </dl>

 

 




