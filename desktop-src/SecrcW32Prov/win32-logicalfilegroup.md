---
Description: The Win32\_LogicalFileGroup association WMI class relates the security settings of a file or directory and its group. You cannot enumerate this class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dfc0c3b3-2421-44fa-8463-b1a2a43bba4c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_LogicalFileGroup class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_LogicalFileGroup class

The **Win32\_LogicalFileGroup** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates the security settings of a file or directory and its group. You cannot enumerate this class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("SECRCW32"), UUID("{8502C58F-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_LogicalFileGroup : Win32_SecuritySettingGroup
{
  Win32_SID                        REF Group;
  Win32_LogicalFileSecuritySetting REF SecuritySetting;
};
```

## Members

The **Win32\_LogicalFileGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_LogicalFileGroup** class has these properties.

<dl> <dt>

**Group**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SID**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Group")
</dt> </dl>

Reference to the instance representing the security settings of the file or directory object group.

</dd> <dt>

**SecuritySetting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalFileSecuritySetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SecuritySetting")
</dt> </dl>

Reference to the instance representing the security settings of the file or directory object. This property cannot be enumerated.

</dd> </dl>

## Remarks

The **Win32\_LogicalFileGroup** class is derived from [**Win32\_SecuritySettingGroup**](win32-securitysettinggroup.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SecuritySettingGroup**](win32-securitysettinggroup.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




