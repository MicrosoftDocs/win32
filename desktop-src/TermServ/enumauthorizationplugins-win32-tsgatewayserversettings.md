---
title: EnumAuthorizationPlugins method of the Win32_TSGatewayServerSettings class
description: Enumerates all registered authorization plug-ins.
ms.assetid: 525b4001-b89c-43cc-986a-00db47dd5518
ms.tgt_platform: multiple
keywords:
- EnumAuthorizationPlugins method Remote Desktop Services
- EnumAuthorizationPlugins method Remote Desktop Services , Win32_TSGatewayServerSettings class
- Win32_TSGatewayServerSettings class Remote Desktop Services , EnumAuthorizationPlugins method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServerSettings.EnumAuthorizationPlugins
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EnumAuthorizationPlugins method of the Win32\_TSGatewayServerSettings class

Enumerates all registered authorization plug-ins.

## Syntax


```mof
uint32 EnumAuthorizationPlugins(
  [out] string PluginNames[],
  [out] string CLSIDs[],
  [out] string Descriptions[]
);
```



## Parameters

<dl> <dt>

*PluginNames* \[out\]
</dt> <dd>

Type: **string\[\]**

A **string** array that receives the names of the registered authorization plug-ins.

</dd> <dt>

*CLSIDs* \[out\]
</dt> <dd>

Type: **string\[\]**

A **string** array that receives the CLSIDs of the registered authorization plug-ins.

</dd> <dt>

*Descriptions* \[out\]
</dt> <dd>

Type: **string\[\]**

A **string** array that receives the descriptions of the registered authorization plug-ins.

</dd> </dl>

## Return value

Type: **uint32**

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                        |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md)
</dt> </dl>

 

