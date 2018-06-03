---
Description: The Win32\_SecuritySettingOfObject abstract association WMI class relates an object to its security settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 09f125a4-14ac-478c-9360-4ef9b6975724
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SecuritySettingOfObject class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_SecuritySettingOfObject class

The **Win32\_SecuritySettingOfObject** abstract association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an object to its security settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{8502C584-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SecuritySettingOfObject : CIM_ElementSetting
{
  CIM_LogicalElement    REF Element;
  Win32_SecuritySetting REF Setting;
};
```

## Members

The **Win32\_SecuritySettingOfObject** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SecuritySettingOfObject** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Element")
</dt> </dl>

Reference to the instance representing the object.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SecuritySetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Setting")
</dt> </dl>

Reference to the instance representing the security settings of the object.

</dd> </dl>

## Remarks

The **Win32\_SecuritySettingOfObject** class is derived from [**CIM\_ElementSetting**](https://msdn.microsoft.com/library/aa387263).

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

[**CIM\_ElementSetting**](https://msdn.microsoft.com/library/aa387263)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




