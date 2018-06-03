---
Description: The Win32\_VideoSettings association WMI class relates a video controller and video settings that can be applied to it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0cc42352-0a89-434d-a8b6-230c677de49c
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_VideoSettings class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_VideoSettings class

The **Win32\_VideoSettings** association [WMI class](https://msdn.microsoft.com/windows/desktop/cfe4bcca-692e-45cd-a840-93ebfe4ae267) relates a video controller and video settings that can be applied to it.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{1008CCEE-7BFF-11D2-AAD2-006008C78BC7}"), AMENDMENT]
class Win32_VideoSettings : CIM_VideoSetting
{
  CIM_VideoControllerResolution REF Setting;
  Win32_VideoController         REF Element;
};
```

## Members

The **Win32\_VideoSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_VideoSettings** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_VideoController**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/windows/desktop/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**Override**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Element"), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_VideoController")
</dt> </dl>

A [**Win32\_VideoController**](win32-videocontroller.md) containing the properties of the video controller that a video setting can be used on.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VideoControllerResolution**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/windows/desktop/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**Override**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Setting"), [**MappingStrings**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("CIM\|CIM\_VideoControllerResolution")
</dt> </dl>

A [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md) containing settings that can be applied to the video controller.

</dd> </dl>

## Remarks

The **Win32\_VideoSettings** class is derived from [**CIM\_VideoSetting**](cim-videosetting.md).

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

[**CIM\_VideoSetting**](cim-videosetting.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 




