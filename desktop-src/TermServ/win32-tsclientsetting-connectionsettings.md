---
title: ConnectionSettings method of the Win32_TSClientSetting class
description: The ConnectionSettings method sets the session settings that apply to the connection and logon process.
ms.assetid: 603807fe-f341-4358-a3b0-0300785cbdb1
ms.tgt_platform: multiple
keywords:
- ConnectionSettings method Remote Desktop Services
- ConnectionSettings method Remote Desktop Services , Win32_TSClientSetting class
- Win32_TSClientSetting class Remote Desktop Services , ConnectionSettings method
topic_type:
- apiref
api_name:
- Win32_TSClientSetting.ConnectionSettings
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ConnectionSettings method of the Win32\_TSClientSetting class

The **ConnectionSettings** method sets the session settings that apply to the connection and logon process.

## Syntax


```mof
uint32 ConnectionSettings(
  [in] uint32 ConnectClientDrivesAtLogon,
  [in] uint32 ConnectPrinterAtLogon,
  [in] uint32 DefaultToClientPrinter
);
```



## Parameters

<dl> <dt>

*ConnectClientDrivesAtLogon* \[in\]
</dt> <dd>

Flag enabling or disabling the **ConnectClientDrivesAtLogon** property which specifies whether the client's drives are automatically connected during the logon procedure.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

The client's drives are not automatically connected.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

The client's drives are automatically connected.

</dd> </dl> </dd> <dt>

*ConnectPrinterAtLogon* \[in\]
</dt> <dd>

Flag enabling or disabling the **ConnectPrinterAtLogon** property, which specifies whether all mapped local client printers are automatically connected during the logon procedure.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

All mapped local printers are not automatically connected.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

All mapped local printers are automatically connected.

</dd> </dl> </dd> <dt>

*DefaultToClientPrinter* \[in\]
</dt> <dd>

Flag enabling or disabling the **DefaultToClientPrinter** property which specifies whether print jobs are automatically sent to the client's local printer.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Print jobs are not automatically sent.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Print jobs are automatically sent.

</dd> </dl> </dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the user's connection settings are overridden by the server.

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSClientSetting**](win32-tsclientsetting.md)
</dt> </dl>

 

