---
Description: The Win32\_SecuritySettingOfLogicalShare association WMI class relates the security settings of a share object with the object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c3880889-c1b8-4d50-887f-0e7f7c71bf08
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SecuritySettingOfLogicalShare class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_SecuritySettingOfLogicalShare class

The **Win32\_SecuritySettingOfLogicalShare** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates the security settings of a share object with the object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("SECRCW32"), UUID("{8502C592-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SecuritySettingOfLogicalShare : Win32_SecuritySettingOfObject
{
  Win32_Share                       REF Element;
  Win32_LogicalShareSecuritySetting REF Setting;
};
```

## Members

The **Win32\_SecuritySettingOfLogicalShare** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SecuritySettingOfLogicalShare** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Share**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Element"), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the share.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalShareSecuritySetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Setting"), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the security settings of the share.

</dd> </dl>

## Remarks

The **Win32\_SecuritySettingOfLogicalShare** class is derived from [**Win32\_SecuritySettingOfObject**](win32-securitysettingofobject.md).

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

 

 




