---
title: RegistryTreeChangeEvent class
description: WMI registry event class. Includes example showing use of registry event classes, semisynchronous access, and date conversion using SWbemDateTime.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'eb0d328e-60bd-4ecb-8e26-0d14c1eddc46'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RegistryTreeChangeEvent class", "RegistryTreeChangeEvent class, described"]
topic_type:
- apiref
api_name:
- RegistryTreeChangeEvent
- RegistryTreeChangeEvent.Hive
- RegistryTreeChangeEvent.RootPath
api_location:
- StdProv.dll
api_type:
- DllExport
---

# RegistryTreeChangeEvent class

The **RegistryTreeChangeEvent** class represents changes to a key and its subkeys. For more information about using the WMI registry event classes, see the [Modifying the System Registry](https://msdn.microsoft.com/library/aa392388) section. For code examples, see the [WMI Tasks: Registry](https://msdn.microsoft.com/library/aa394600) topic.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class RegistryTreeChangeEvent : RegistryEvent
{
  string Hive;
  string RootPath;
};
```

## Members

The **RegistryTreeChangeEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **RegistryTreeChangeEvent** class has these properties.

<dl> <dt>

**Hive**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the hive that contains the key (or keys) that is changed. For example, **HKEY\_LOCAL\_MACHINE**. Changes to the **HKEY\_CLASSES\_ROOT** and **HKEY\_CURRENT\_USER** hives are not supported by [**RegistryEvent**](registryevent.md) or classes derived from it, such as **RegistryTreeChangeEvent**.

</dd> <dt>

**RootPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Path to the registry key that contains the subkeys. For example, "SOFTWARE\\Microsoft".

</dd> </dl>

## Remarks

Queries that provide a **RootPath** must have backslashes escaped. For example,


```VB
wmiServices.ExecNotificationQuery("SELECT * FROM RegistryTreeChangeEvent " _
    & "WHERE Hive='HKEY_LOCAL_MACHINE' AND RootPath='SOFTWARE\\Microsoft'")
```



Registry provider classes, unlike most of the [Win32 classes](https://msdn.microsoft.com/library/aa394388) are located in the WMI root\\default namespace.

## Examples

The following example waits for changes in the **HKEY\_LOCAL\_MACHINE** hive using [*semisynchronous*](https://msdn.microsoft.com/library/aa390836#wmi-gloss-semisynchronous) access. It runs until the Wscript.exe process is stopped in Task Manager. The 64-bit **TIME\_CREATED** property is converted to a printable date by [**SWbemDateTime**](https://msdn.microsoft.com/library/aa393687) methods. For more information, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

The following script runs until the computer is restarted, WMI is stopped, or the script is stopped. To stop the script manually, use Task Manager to stop the process. To stop it programmatically, use the [**Terminate**](https://msdn.microsoft.com/library/aa393907) method in the [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) class.


```VB
wbemFlagReturnImmediately = 16
wbemFlagForwardOnly = 32
IFlags = wbemFlagReturnImmediately + wbemFlagForwardOnly

Set wmiServices = GetObject("winmgmts:root/default") 
Set dtmCreateTime = CreateObject("WbemScripting.SWbemDateTime")

Set colRegChanges = wmiServices.ExecNotificationQuery _
    ("SELECT * FROM RegistryTreeChangeEvent " _
    & "WHERE Hive='HKEY_LOCAL_MACHINE' AND RootPath='",, IFlags)

Do While (True)
   Set TreeChange = colRegChanges.NextEvent

'Time_Created property is 64-bit and
' must be converted into CIM_DateTime format
   dtmCreateTime.SetFileTime TreeChange.Time_Created, false

'Convert to VT_DATE format using GetVarDate
' for printing to screen
   Wscript.Echo "Time = " & dtmCreateTime.GetVarDate() _
              & VBNewLine _
              & "Hive = " & TreeChange.Hive & VBNewLine _
              & "RootPath = "&amp; TreeChange.RootPath    
Loop
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\default<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RegEvent.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StdProv.dll</dt> </dl>  |



## See also

<dl> <dt>

[**RegistryEvent**](registryevent.md)
</dt> <dt>

[Registering for System Registry Events](https://msdn.microsoft.com/library/aa393035)
</dt> </dl>

 

 





