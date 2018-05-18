---
Description: 'The Win32\_SystemSetting abstract association WMI class relates a computer system and a general setting on that system.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '796ee263-2526-43f8-bd3d-23442b6bd4ca'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_SystemSetting class'
---

# Win32\_SystemSetting class

The **Win32\_SystemSetting** abstract association [WMI class](wmi.retrieving_a_class) relates a computer system and a general setting on that system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{8502C501-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemSetting : CIM_ElementSetting
{
  Win32_ComputerSystem REF Element;
  CIM_Setting          REF Setting;
};
```

## Members

The **Win32\_SystemSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](wmi.key_qualifier), [**Override**](wmi.standard_qualifiers) ("Element"), [**MappingStrings**](wmi.standard_qualifiers) ("WMI\|Win32\_ComputerSystem")
</dt> </dl>

Reference to the instance representing the properties of a computer system where this setting can be applied.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Setting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](wmi.key_qualifier), [**Override**](wmi.standard_qualifiers) ("Setting"), [**MappingStrings**](wmi.standard_qualifiers) ("CIM\|CIM\_Setting")
</dt> </dl>

Reference to the instance representing the properties of the setting that can be applied to the computer system.

</dd> </dl>

## Remarks

The **Win32\_SystemSetting** class is derived from [**CIM\_ElementSetting**](cim-elementsetting.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementSetting**](cim-elementsetting.md)
</dt> <dt>

[Operating System Classes](wmi.operating_system_classes)
</dt> </dl>

 

 




