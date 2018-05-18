---
Description: 'This topic explains how to set up the Windows Installer, formerly the Microsoft Software Installer (MSI), keys for your MAPI dynamic link-library (DLL).'
ms.assetid: '5888EF22-C056-4e3a-8313-8B5821074DEB'
title: Setting Up the MSI Keys for Your MAPI DLL
---

# Setting Up the MSI Keys for Your MAPI DLL

This topic explains how to set up the Windows Installer, formerly the Microsoft Software Installer (MSI), keys for your MAPI dynamic link-library (DLL).

## Setting Up the MSI Keys for Your MAPI DLL

If your mail client supports on-demand installation using the Windows Installer, create **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail**\\***MyMailClient***\\**MSIComponentID** and set its value to an MSI PublishComponent category ID (GUID), which identifies a DLL that exports Simple MAPI and/or MAPI calls.

> [!Note]  
> It is recommended that you install the MSI DLL (along with the mail client files) in a private installation location on the file system and provide full paths to the various DLLs.

 

If **MSIComponentID** is set, it has precedence over the **DLLPath** and **DLLPathEx** values, and the application installs the component on demand using the Windows Installer, loads the DLL and calls the specific function.

Your application can also set additional values in *MyMailClient* if your mail client supports different languages. The subkeys are listed in the following table.



| Subkey                            | Type                      | Description                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MSIApplicationLCID**<br/> | REG\_MULTI\_SZ<br/> | Locale identifier for your application. The first string value identifies a subkey from **HKEY\_LOCAL\_MACHINE**\\**Software** and subsequent string values identify registry values below this key that contain locale information. For example, Microsoft Office 2007 sets the key to **Microsoft**\\**Office**\\**12.0**\\**Outlook\[~\]LastUILanguage** in MSI notation.<br/> |
| **MSIOfficeLCID**<br/>      | REG\_MULTI\_SZ<br/> | LCIDs for Microsoft Office. The first string value identifies a subkey from **HKEY\_LOCAL\_MACHINE**\\**Software** and subsequent string values identify registry values below this key. For example, Microsoft Office 2007 sets the key to **Microsoft**\\**Office**\\**12.0**\\**Common**\\**LanguageResources\[~\]UILanguage\[~\]InstallLanguage\[~\]** in MSI notation.<br/>  |
| **MSIInstallOnWTS**<br/>    | REG\_DWORD<br/>     | Value specifying whether to install on demand Windows Terminal Server (WTS). Set this to 0 (zero) to prevent installation on demand of WTS; set it to 1 to allow installation on demand of WTS.<br/>                                                                                                                                                                              |



 

The order of precedence for the subkeys is **MSIApplicationLCID**, **MSIOfficeLCID**, the default user or system LCIDs, and then finally English. When using **MSIApplicationLCID** or **MSIOfficeLCID**, the stub library first checks **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies** and then **HKEY\_LOCAL\_MACHINE**\\**Software**.

## Related topics

<dl> <dt>

[Mapi32 Stub Library](mapi32-stub-library.md)
</dt> </dl>

 

 




