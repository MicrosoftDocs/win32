---
Description: The Win32\_WMIElementSetting association WMI class relates a service running in the Windows system and the WMI settings it can use.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 00e9f882-5f54-4042-a916-2f90ed9a37c0
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_WMIElementSetting class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_WMIElementSetting class

The **Win32\_WMIElementSetting** association [WMI class](https://msdn.microsoft.com/cfe4bcca-692e-45cd-a840-93ebfe4ae267) relates a service running in the Windows system and the WMI settings it can use.

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

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Element"), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_Service")
</dt> </dl>

Reference to the instance representing the Windows service using or surfacing WMI properties.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_WMISetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Setting"), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_WMISetting")
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

[WMI Service Management Classes](EF58AC04-FE04-4D0C-A5F7-3491C885A0E4)
</dt> </dl>

 

 




