---
description: The Win32\_PageFileElementSetting association WMI class relates the initial settings of a page file and the state of those settings during normal use.
ms.assetid: efc1f20d-166e-4e27-9767-f6ec0bbd6c14
ms.tgt_platform: multiple
title: Win32_PageFileElementSetting class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PageFileElementSetting
- Win32_PageFileElementSetting.Element
- Win32_PageFileElementSetting.Setting
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_PageFileElementSetting class

The **Win32\_PageFileElementSetting** association [WMI class](../wmisdk/retrieving-a-class.md) relates the initial settings of a page file and the state of those settings during normal use.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8E7F70E8-C856-11D2-B364-00105A1F77A1}"), AMENDMENT]
class Win32_PageFileElementSetting : CIM_ElementSetting
{
  Win32_PageFileUsage   REF Element;
  Win32_PageFileSetting REF Setting;
};
```

## Members

The **Win32\_PageFileElementSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PageFileElementSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PageFileUsage**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("Element"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_PageFileUsage")
</dt> </dl>

Reference to the instance representing the properties of a page file while the Win32 system is in use.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PageFileSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("Setting"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_PageFileSetting")
</dt> </dl>

Reference to the instance representing the initial settings of a page file when the Win32 system is starting up.

</dd> </dl>

## Remarks

The **Win32\_PageFileElementSetting** class is derived from [**CIM\_ElementSetting**](cim-elementsetting.md).

## Requirements



| Requirement | Value |
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

[Operating System Classes](./operating-system-classes.md)
</dt> </dl>

 

 
