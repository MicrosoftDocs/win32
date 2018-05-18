---
Description: 'The Win32\_SecuritySettingGroup abstract, association WMI class relates the security of an object and its group.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'df817d00-ed4c-4de2-9774-a3db6e3e99c0'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_SecuritySettingGroup class'
---

# Win32\_SecuritySettingGroup class

The **Win32\_SecuritySettingGroup** abstract, association [WMI class](https://msdn.microsoft.com/library/aa393244) relates the security of an object and its group.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract, Association, UUID("{8502C586-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SecuritySettingGroup
{
  Win32_SID             REF Group;
  Win32_SecuritySetting REF SecuritySetting;
};
```

## Members

The **Win32\_SecuritySettingGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SecuritySettingGroup** class has these properties.

<dl> <dt>

**Group**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SID**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the object's group.

</dd> <dt>

**SecuritySetting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SecuritySetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the security settings of an object.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




