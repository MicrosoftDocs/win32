---
title: SetAuthenticationPluginAndRecycleRpcApplicationPools method of the Win32_TSGatewayServerSettings class
description: Sets the current authentication plug-in for the Remote Desktop Gateway (RD Gateway) server and recycles the RPC application pools in IIS.
ms.assetid: cdceaf50-3d0a-4af0-9ad5-fb43760fcf7b
ms.tgt_platform: multiple
keywords:
- SetAuthenticationPluginAndRecycleRpcApplicationPools method Remote Desktop Services
- SetAuthenticationPluginAndRecycleRpcApplicationPools method Remote Desktop Services , Win32_TSGatewayServerSettings class
- Win32_TSGatewayServerSettings class Remote Desktop Services , SetAuthenticationPluginAndRecycleRpcApplicationPools method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServerSettings.SetAuthenticationPluginAndRecycleRpcApplicationPools
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetAuthenticationPluginAndRecycleRpcApplicationPools method of the Win32\_TSGatewayServerSettings class

Sets the current authentication plug-in for the Remote Desktop Gateway (RD Gateway) server and recycles the RPC application pools in IIS.

This method is equivalent to calling the [**SetAuthenticationPlugin**](setauthenticationplugin-win32-tsgatewayserversettings.md) and [**RecycleRpcApplicationPools**](recyclerpcapplicationpools-win32-tsgatewayserversettings.md) methods in sequence.

## Syntax


```mof
uint32 SetAuthenticationPluginAndRecycleRpcApplicationPools(
  [in] string PluginName
);
```



## Parameters

<dl> <dt>

*PluginName* \[in\]
</dt> <dd>

Type: **string**

Name of the authentication plug-in

</dd> </dl>

## Return value

Type: **uint32**

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

Calling this method results in all existing connections being disconnected.

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
</dt> <dt>

[**SetAuthenticationPlugin**](setauthenticationplugin-win32-tsgatewayserversettings.md)
</dt> <dt>

[**RecycleRpcApplicationPools**](recyclerpcapplicationpools-win32-tsgatewayserversettings.md)
</dt> </dl>

 

