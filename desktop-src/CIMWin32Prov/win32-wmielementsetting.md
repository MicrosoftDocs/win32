---
Description: The Win32\_WMIElementSetting association WMI class relates a service running in the Windows system and the WMI settings it can use.
ms.assetid: 00e9f882-5f54-4042-a916-2f90ed9a37c0
ms.tgt_platform: multiple
title: Win32_WMIElementSetting class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_WMIElementSetting
- Win32_WMIElementSetting.Element
- Win32_WMIElementSetting.Setting
api_type: 
- DllExport
api_location: 
- Wbemcore.dll
---

# Win32\_WMIElementSetting class

The **Win32\_WMIElementSetting** association [WMI class](https://msdn.microsoft.com/en-us/library/Aa393244(v=VS.85).aspx) relates a service running in the Windows system and the WMI settings it can use.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("WBEMCORE"), UUID("{A83EF167-CA8D-11d2-B33D-00104BCC4B4A}"), AMENDMENT]
class Win32_WMIElementSetting : CIM_ElementSetting
{
  Win32_Service    REF Element;
  Win32_WMISetting REF Setting;
};
```

## Members

The **Win32\_WMIElementSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_WMIElementSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/en-us/library/Aa392157(v=VS.85).aspx), [**Override**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("Element"), [**MappingStrings**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("WMI\|Win32\_Service")
</dt> </dl>

Reference to the instance representing the Windows service using or surfacing WMI properties.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_WMISetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/en-us/library/Aa392157(v=VS.85).aspx), [**Override**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("Setting"), [**MappingStrings**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("WMI\|Win32\_WMISetting")
</dt> </dl>

Reference to the instance representing the WMI settings available to the Windows service.

</dd> </dl>

## Remarks

The **Win32\_WMIElementSetting** class is derived from [**CIM\_ElementSetting**](cim-elementsetting.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemcore.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementSetting**](cim-elementsetting.md)
</dt> <dt>

[WMI Service Management Classes](https://msdn.microsoft.com/en-us/library/Dn792273(v=VS.85).aspx)
</dt> </dl>

 

 




