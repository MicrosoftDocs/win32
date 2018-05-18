---
Description: 'The Security provider allows you to retrieve or change security settings that control ownership, auditing, and access rights to NTFS files, directories, and shares.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'e2c6c640-9ae0-43c4-8269-22a578bb99a1'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Security Provider
---

# Security Provider

The Security provider allows you to retrieve or change security settings that control ownership, auditing, and access rights to NTFS files, directories, and shares. The [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instance name is "SECRCW32".

As an instance and method provider, the Security provider supports the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**DeleteInstanceAsync**](https://msdn.microsoft.com/library/aa392102)
-   [**ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

The Security provider uses the following CIM classes.

-   [**Win32\_AccountSID**](win32-accountsid.md)
-   [**Win32\_ACE**](win32-ace.md)
-   [**Win32\_DCOMApplicationAccessAllowedSetting**](win32-dcomapplicationaccessallowedsetting.md)
-   [**Win32\_DCOMApplicationLaunchAllowedSetting**](win32-dcomapplicationlaunchallowedsetting.md)
-   [**Win32\_LogicalFileAccess**](win32-logicalfileaccess.md)
-   [**Win32\_LogicalFileAuditing**](win32-logicalfileauditing.md)
-   [**Win32\_LogicalFileGroup**](win32-logicalfilegroup.md)
-   [**Win32\_LogicalFileOwner**](win32-logicalfileowner.md)
-   [**Win32\_LogicalFileSecuritySetting**](win32-logicalfilesecuritysetting.md)
-   [**Win32\_LogicalShareAccess**](win32-logicalshareaccess.md)
-   [**Win32\_LogicalShareAuditing**](win32-logicalshareauditing.md)
-   [**Win32\_LogicalShareSecuritySetting**](win32-logicalsharesecuritysetting.md)
-   [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md)
-   [**Win32\_SecurityDescriptorHelper**](win32-securitydescriptorhelper.md)
-   [**Win32\_SecuritySetting**](win32-securitysetting.md)
-   [**Win32\_SecuritySettingAccess**](win32-securitysettingaccess.md)
-   [**Win32\_SecuritySettingAuditing**](win32-securitysettingauditing.md)
-   [**Win32\_SecuritySettingGroup**](win32-securitysettinggroup.md)
-   [**Win32\_SecuritySettingOfLogicalFile**](win32-securitysettingoflogicalfile.md)
-   [**Win32\_SecuritySettingOfLogicalShare**](win32-securitysettingoflogicalshare.md)
-   [**Win32\_SecuritySettingOfObject**](win32-securitysettingofobject.md)
-   [**Win32\_SecuritySettingOwner**](win32-securitysettingowner.md)
-   [**Win32\_SID**](win32-sid.md)
-   [**Win32\_Trustee**](win32-trustee.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 



