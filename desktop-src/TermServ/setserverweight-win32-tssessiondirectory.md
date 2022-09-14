---
title: SetServerWeight method of the Win32_TSSessionDirectory class
description: Sets the server weight value for Remote Desktop Connection Broker (RD Connection Broker) load balancing.
ms.assetid: 9c7563e5-bb45-495d-90b0-43170b58581e
ms.tgt_platform: multiple
keywords:
- SetServerWeight method Remote Desktop Services
- SetServerWeight method Remote Desktop Services , Win32_TSSessionDirectory class
- Win32_TSSessionDirectory class Remote Desktop Services , SetServerWeight method
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory.SetServerWeight
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetServerWeight method of the Win32\_TSSessionDirectory class

Sets the server weight value for Remote Desktop Connection Broker (RD Connection Broker) load balancing.

## Syntax


```mof
uint32 SetServerWeight(
  [in] uint32 ServerWeightValue
);
```



## Parameters

<dl> <dt>

*ServerWeightValue* \[in\]
</dt> <dd>

Type: **uint32**

The server weight value. The valid range is 1 to 10000.

</dd> </dl>

## Remarks

By default in the user interface of Remote Desktop Services Configuration, the server weight value is 100. The server weight is relative. Therefore, if you assign one server a value of 100, and one a value of 200, the server with a relative weight of 200 will receive twice the number of sessions.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSSessionDirectory**](win32-tssessiondirectory.md)
</dt> </dl>

 

