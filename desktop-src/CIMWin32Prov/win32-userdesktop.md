---
Description: The Win32\_UserDesktop association WMI class relates a user account and desktop settings that are specific to it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5ea83ad6-bd0a-4c16-85b2-e3e61ef05903
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_UserDesktop class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_UserDesktop class

The **Win32\_UserDesktop** association [WMI class](https://msdn.microsoft.com/cfe4bcca-692e-45cd-a840-93ebfe4ae267) relates a user account and desktop settings that are specific to it.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4FF-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_UserDesktop : CIM_ElementSetting
{
  Win32_UserAccount REF Element;
  Win32_Desktop     REF Setting;
};
```

## Members

The **Win32\_UserDesktop** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_UserDesktop** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_UserAccount**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Element"), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_UserAccount")
</dt> </dl>

Reference to the instance representing the user account whose desktop can be customized by the **Settings** property of this class.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Desktop**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Setting"), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_Desktop")
</dt> </dl>

Reference to the instance representing the desktop settings that serve to customize a specific user account desktop.

</dd> </dl>

## Remarks

The **Win32\_UserDesktop** class is derived from [**CIM\_ElementSetting**](cim-elementsetting.md).

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

[Operating System Classes](https://msdn.microsoft.com/windows/desktop/D0756D8C-A3D3-4C75-96A3-8C7F05300B39)
</dt> </dl>

 

 




