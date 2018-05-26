---
title: RegistryKeyChangeEvent class
description: The RegistryKeyChangeEvent class represents changes to a specific key.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2de566a8-6195-4325-b1d3-4ef37031cbda
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RegistryKeyChangeEvent class
- RegistryKeyChangeEvent class, described
topic_type:
- apiref
api_name:
- RegistryKeyChangeEvent
- RegistryKeyChangeEvent.Hive
- RegistryKeyChangeEvent.KeyPath
api_location:
- StdProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RegistryKeyChangeEvent class

The **RegistryKeyChangeEvent** class represents changes to a specific key. The changes apply only to the key, not its subkeys. For more information about using the WMI registry event classes, see the [Modifying the System Registry](https://msdn.microsoft.com/library/aa392388) section. For code examples, see [WMI Tasks: Registry](https://msdn.microsoft.com/library/aa394600).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class RegistryKeyChangeEvent : RegistryEvent
{
  string Hive;
  string KeyPath;
};
```

## Members

The **RegistryKeyChangeEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **RegistryKeyChangeEvent** class has these properties.

<dl> <dt>

**Hive**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the hive (subtree) that contains the key (or keys) that is changed. For example, **HKEY\_LOCAL\_MACHINE**. Changes to the **HKEY\_CLASSES\_ROOT** and **HKEY\_CURRENT\_USER** hives are not supported by [**RegistryEvent**](registryevent.md) or classes derived from it, such as **RegistryKeyChangeEvent**.

</dd> <dt>

**KeyPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Path to the registry key. For example, "**SOFTWARE\\Microsoft\\WBEM\\Scripting**".

</dd> </dl>

## Remarks

Queries that provide a **KeyPath** must have backslashes escaped. For example,


```VB
wmiServices.ExecNotificationQuery("SELECT * FROM RegistryKeyChangeEvent "_
    & "WHERE Hive='HKEY_LOCAL_MACHINE' AND KeyPath='SOFTWARE\\Microsoft'")
```



Registry provider classes, unlike most of the [Win32 classes](https://msdn.microsoft.com/library/aa394388) are located in the WMI "Root\\Default" namespace.

## Examples

The following VBScript code example calls the asynchronous method [**SWbemServices.ExecNotificationQueryAsync**](https://msdn.microsoft.com/library/aa393865) to monitor changes in any values under the registry key **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**Scripting**. Note that the backslashes in the registry key are escaped by a backslash ("\\"). For more information about asynchronous calls and security, see [Making an Asynchronous Call with VBScript](https://msdn.microsoft.com/library/aa392295).

To see the operation of this script, execute the script and use a registry editor such as Regedit to change the **Default Namespace** value under this key. Be sure to change it back to the original value.

The following script runs until the computer is restarted, WMI is stopped, or the script is stopped. To stop the script manually, use Task Manager to stop the process. To stop it programmatically, use the [**Terminate**](https://msdn.microsoft.com/library/aa393907) method in the Win32\_Process class.


```VB
Set wmiServices = GetObject("winmgmts:root/default") 
Set wmiSink = WScript.CreateObject("WbemScripting.SWbemSink", "SINK_") 
wmiServices.ExecNotificationQueryAsync wmiSink, "SELECT * FROM RegistryKeyChangeEvent " _
    & "WHERE Hive='HKEY_LOCAL_MACHINE' AND KeyPath='SOFTWARE\\Microsoft\\WBEM\\Scripting'" 
WScript.Echo "Listening for Registry Key Change Events..." & vbCrLf 
While(True) 
    WScript.Sleep 1000 
Wend 
Sub SINK_OnObjectReady(wmiObject, wmiAsyncContext) 
    WScript.Echo "Received Registry Change Event" & vbCrLf & wmiObject.GetObjectText_() 
End Sub
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\default<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RegEvent.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StdProv.dll</dt> </dl>  |



## See also

<dl> <dt>

[**RegistryEvent**](registryevent.md)
</dt> <dt>

[Registering for System Registry Events](https://msdn.microsoft.com/library/aa393035)
</dt> </dl>

 

 





