---
Description: The Win32\_SecuritySettingOfLogicalFile association WMI class represents security settings of a file or directory object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eeff98cd-8560-447f-bbae-be1c4edc9433
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SecuritySettingOfLogicalFile class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_SecuritySettingOfLogicalFile class

The **Win32\_SecuritySettingOfLogicalFile** association [WMI class](https://msdn.microsoft.com/library/aa393244) represents security settings of a file or directory object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("SECRCW32"), UUID("{8502C58D-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SecuritySettingOfLogicalFile : Win32_SecuritySettingOfObject
{
  CIM_LogicalFile                  REF Element;
  Win32_LogicalFileSecuritySetting REF Setting;
};
```

## Members

The **Win32\_SecuritySettingOfLogicalFile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SecuritySettingOfLogicalFile** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalFile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Element"), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the file or directory.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalFileSecuritySetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Setting"), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the security settings of the file or directory.

</dd> </dl>

## Remarks

The **Win32\_SecuritySettingOfLogicalFile** class is derived from [**Win32\_SecuritySettingOfObject**](win32-securitysettingofobject.md).

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

[**Win32\_SecuritySettingOfObject**](win32-securitysettingofobject.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




