---
Description: The Win32\_SystemTimeZone association WMI class relates a computer system and a time zone.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 53c74a61-c91d-4daa-933e-4cc7b9583d98
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SystemTimeZone class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_SystemTimeZone class

The **Win32\_SystemTimeZone** association [WMI class](https://msdn.microsoft.com/cfe4bcca-692e-45cd-a840-93ebfe4ae267) relates a computer system and a time zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C504-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemTimeZone : Win32_SystemSetting
{
  Win32_ComputerSystem REF Element;
  Win32_TimeZone       REF Setting;
};
```

## Members

The **Win32\_SystemTimeZone** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemTimeZone** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Element"), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_ComputerSystem")
</dt> </dl>

Reference to the instance representing the computer system keeping track of the system time zone.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_TimeZone**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Setting"), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_TimeZone")
</dt> </dl>

Reference to the instance representing the time zone properties tracked by the computer system.

</dd> </dl>

## Remarks

The **Win32\_SystemTimeZone** class is derived from [**Win32\_SystemSetting**](win32-systemsetting.md).

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

[**Win32\_SystemSetting**](win32-systemsetting.md)
</dt> <dt>

[Operating System Classes](https://www.bing.com/search?q=Operating+System+Classes)
</dt> </dl>

 

 




