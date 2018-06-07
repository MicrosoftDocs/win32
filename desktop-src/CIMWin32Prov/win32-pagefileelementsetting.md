---
Description: The Win32\_PageFileElementSetting association WMI class relates the initial settings of a page file and the state of those settings during normal use.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: efc1f20d-166e-4e27-9767-f6ec0bbd6c14
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_PageFileElementSetting class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_PageFileElementSetting class

The **Win32\_PageFileElementSetting** association [WMI class](https://msdn.microsoft.com/cfe4bcca-692e-45cd-a840-93ebfe4ae267) relates the initial settings of a page file and the state of those settings during normal use.

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

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Element"), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_PageFileUsage")
</dt> </dl>

Reference to the instance representing the properties of a page file while the Win32 system is in use.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PageFileSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Setting"), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_PageFileSetting")
</dt> </dl>

Reference to the instance representing the initial settings of a page file when the Win32 system is starting up.

</dd> </dl>

## Remarks

The **Win32\_PageFileElementSetting** class is derived from [**CIM\_ElementSetting**](cim-elementsetting.md).

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

[Operating System Classes](D0756D8C-A3D3-4C75-96A3-8C7F05300B39)
</dt> </dl>

 

 




