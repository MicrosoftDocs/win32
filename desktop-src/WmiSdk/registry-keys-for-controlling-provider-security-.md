---
description: To enhance the security of the Windows Management Instrumentation (WMI) shared provider host process (wmiprvse.exe), changes were made to Windows platforms that secure the provider host process with a service security identifier (SID).
ms.assetid: f93ac155-512c-4efa-8168-ca2d56fe6f01
ms.tgt_platform: multiple
title: Registry Keys and Values for Controlling Provider Security
ms.topic: article
ms.date: 05/31/2018
---

# Registry Keys and Values for Controlling Provider Security

To enhance the security of the Windows Management Instrumentation (WMI) shared provider host process (wmiprvse.exe), changes were made to Windows platforms that secure the provider host process with a [*service security identifier (SID)*](gloss-s.md). These changes introduce the following running modes for the WMI shared host: secure and compatible.

The following sections are covered in this topic:

-   [Secure and Compatible Modes](#secure-and-compatible-modes)
-   [Registry Keys and Values](#registry-keys-and-values)
-   [Configuring a Provider to Run in Secure or Compatible Mode](#configuring-a-provider-to-run-in-secure-or-compatible-mode)

## Secure and Compatible Modes

Starting in Windows 7, the following two running modes for the WMI shared host process were added:

<dl> <dt>

<span id="Secure_mode"></span><span id="secure_mode"></span><span id="SECURE_MODE"></span>Secure mode
</dt> <dd>

WMI provider host process resources are secured with a [*service SID*](gloss-s.md). Only the *service SID* has permissions for these resources.

</dd> <dt>

<span id="Compatible_mode"></span><span id="compatible_mode"></span><span id="COMPATIBLE_MODE"></span>Compatible mode
</dt> <dd>

The WMI shared provider host process is not secured with a [*service SID*](gloss-s.md). The provider host process allows access to the NetworkService or LocalService accounts depending on the hosting model. For more information about hosting models, see [Provider Hosting and Security](provider-hosting-and-security.md).

</dd> </dl>

**Windows Vista and Windows Server 2008:** To access the registry keys and values for controlling secure and compatible modes for the provider host process, you must install the security update in [KB 959454](https://support.microsoft.com/kb/959454). For more information, see the [Microsoft Security Bulletin MS09-012](https://www.microsoft.com/technet/security/bulletin/ms09-012.mspx).

## Registry Keys and Values

The secure and compatible mode settings are specified through registry keys. The registry keys for WMI are located in the registry at **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**CIMOM**\\.

The following registry keys and **DWORD** value described in the following list were added to control the behavior of WMI providers.

<dl> <dt>

<span id="SecuredHostProviders"></span><span id="securedhostproviders"></span><span id="SECUREDHOSTPROVIDERS"></span>**SecuredHostProviders**
</dt> <dd>

This key controls the behavior of individual providers. All of the providers that are listed in this key always run in secure mode. All inbox providers that are shipped with Windows are listed under this key, and are run in secure mode by default.

This key takes precedence over providers listed in the **CompatibleHostProviders** key.

</dd> <dt>

<span id="CompatibleHostProviders"></span><span id="compatiblehostproviders"></span><span id="COMPATIBLEHOSTPROVIDERS"></span>**CompatibleHostProviders**
</dt> <dd>

This key controls the behavior of individual providers. All providers that are listed in this key always run in compatible mode. This key is empty by default.

If a provider is listed both in the **SecuredHostProviders** key and in the **CompatibleHostProviders** key, the provider is run in secure mode.

> [!Note]  
> The **CompatibleHostProviders** key provides application compatibility for third-party applications if the **DefaultSecuredHost** key is set to 1 and the provider is known to not function in secure mode.

 

</dd> <dt>

<span id="DefaultSecuredHost"></span><span id="defaultsecuredhost"></span><span id="DEFAULTSECUREDHOST"></span>**DefaultSecuredHost**
</dt> <dd>

A global registry **DWORD** value that determines whether all of the providers, which are not listed in the **SecuredHostProviders** or **CompatibleHostProviders** keys, are run in the secure or compatible mode. This **DWORD** value lets the administrator decide under which mode a third-party provider must run. By default, this value is set to zero and all third-party providers are run in compatible mode. Administrators can make their computer more secure by default by setting the **DefaultSecuredHost** value to 1.

> [!Note]  
> The **DefaultSecuredHost** value does not affect the other registry keys. The providers that are listed in the **SecuredHostProviders** key remain in secure mode, and the ones that are listed in the **CompatibleHostProviders** key remain in compatible mode.

 

The following settings are possible:

<dl> <dt>

<span id="0"></span>0
</dt> <dd>

Specifies that providers run in compatible mode.

</dd> <dt>

<span id="1"></span>1
</dt> <dd>

Specifies that providers run in secure mode.

</dd> </dl> </dd> </dl>

The following list lists the possible registry settings and the associated running modes for a provider.



| Listed under SecuredHostProviders | Listed under CompatibleHostProviders | DefaultSecuredHost Setting | Mode       |
|-----------------------------------|--------------------------------------|----------------------------|------------|
| No                                | No                                   | 0                          | Compatible |
| No                                | Yes                                  | 0                          | Compatible |
| Yes                               | No                                   | 0                          | Secure     |
| Yes                               | Yes                                  | 0                          | Secure     |
| No                                | No                                   | 1                          | Secure     |
| No                                | Yes                                  | 1                          | Compatible |
| Yes                               | No                                   | 1                          | Secure     |
| Yes                               | Yes                                  | 1                          | Secure     |



 

## Configuring a Provider to Run in Secure or Compatible Mode

The registry keys can be modified using the Group Policy Management Console (GPMC). For more information, see [Group Policy Management Console](/previous-versions/windows/desktop/gpmc/group-policy-management-console-portal).

The following procedures illustrate how to manage secure and compatible mode settings by using group policy preferences. For more information about group policy preferences, see the [Group Policy Preferences Overview](/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn581922(v=ws.11)).

**To add a provider to either the secure or compatible mode by using Group Policy**

1.  Open the GPMC.
2.  Create a Group Policy Object (GPO).
3.  Edit the GPO.
4.  Browse to Preferences/Windows Settings/Registry.
5.  Right-click and select **New... Registry**. This action presents a user interface where you can enter registry information.
6.  Select the **Create** command.
7.  Select the following registry key path:

    **Secure Mode:  HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**CIMOM**\\**SecuredHostProviders**

    **Compatible Mode:  HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**CIMOM**\\**CompatibleHostProviders**

8.  In the **name** field, enter the name of the provider you want to add to this key. The provider name must be in the following format: <namespace>:<\_\_RELPATH>. For example, root\\cimv2:\_\_win32provider.name="MyProvider".
9.  In the **data** field, enter 0.
10. Click OK.

**To remove a provider from either the secure or compatible mode by using Group Policy**

1.  Open the GPMC.
2.  Create a GPO.
3.  Edit the GPO.
4.  Browse to Preferences/Windows Settings/Registry.
5.  Right-click and select **New... Registry**. This action presents a user interface where you can enter registry information.
6.  Select the **Remove** command.
7.  Select the following registry key path:

    **Secure Mode:  HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**CIMOM**\\**SecuredHostProviders**

    **Compatible Mode:  HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**CIMOM**\\**CompatibleHostProviders**

8.  In the **name** field, enter the name of the provider you want to remove from this key.
9.  In the **data** field, enter 0.
10. Click OK.

The following procedure provides details about how to modify the behavior of providers that are not listed in either the **SecuredHostProviders** or **CompatibleHostProviders** keys.

**To change the default value of the DefaultSecuredHost key by using Group Policy**

1.  Open the GPMC.
2.  Create a GPO.
3.  Edit the GPO.
4.  Browse to Preferences/Windows Settings/Registry.
5.  Right-click and select **New... Registry**. This action presents a user interface where you can enter registry information.
6.  Select the **Update** command.
7.  Select the following registry key path: **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**CIMOM**.
8.  In the **name** field, enter **DefaultSecuredHost**.
9.  In the **data** field, enter 0 for compatible mode or 1 for secure mode.
10. Click OK.

 

 
