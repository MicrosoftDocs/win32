---
title: BrokenConnection method of the Win32_TSSessionSetting class (Wtsprotocol.h)
description: Sets the BrokenConnectionAction property, which is the action the server takes if the session time-limit is reached or if the connection is broken.
ms.assetid: 2422e314-9e1c-4bed-a958-eedd2daeca66
ms.tgt_platform: multiple
keywords:
- BrokenConnection method Remote Desktop Services
- BrokenConnection method Remote Desktop Services , Win32_TSSessionSetting class
- Win32_TSSessionSetting class Remote Desktop Services , BrokenConnection method
topic_type:
- apiref
api_name:
- Win32_TSSessionSetting.BrokenConnection
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# BrokenConnection method of the Win32\_TSSessionSetting class

Sets the **BrokenConnectionAction** property, which is the action the server takes if the session time-limit is reached or if the connection is broken.

## Syntax


```mof
uint32 BrokenConnection(
  [in] uint32 BrokenConnectionAction
);
```



## Parameters

<dl> <dt>

*BrokenConnectionAction* \[in\]
</dt> <dd>

The action to take.

<dt>

<span id="Disconnect"></span><span id="disconnect"></span><span id="DISCONNECT"></span>

<span id="Disconnect"></span><span id="disconnect"></span><span id="DISCONNECT"></span>**Disconnect** (0)


</dt> <dd>

The user is disconnected from the session.

</dd> <dt>

<span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span>

<span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span>**Terminate** (1)


</dt> <dd>

The session is permanently deleted from the server.

</dd> </dl> </dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under Group Policy control.

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| Header<br/>                   | <dl> <dt>Wtsprotocol.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Win32\_TSSessionSetting**](win32-tssessionsetting.md)
</dt> </dl>

 

