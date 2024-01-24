---
title: SetSslBridging method of the Win32_TSGatewayServerSettings class
description: Sets the type of SSL bridging to be used by the Remote Desktop Gateway (RD Gateway) server.
ms.assetid: 11885b8b-491e-4d90-b4d4-f0a0fbe68cb1
ms.tgt_platform: multiple
keywords:
- SetSslBridging method Remote Desktop Services
- SetSslBridging method Remote Desktop Services , Win32_TSGatewayServerSettings class
- Win32_TSGatewayServerSettings class Remote Desktop Services , SetSslBridging method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServerSettings.SetSslBridging
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetSslBridging method of the Win32\_TSGatewayServerSettings class

Sets the type of SSL bridging to be used by the Remote Desktop Gateway (RD Gateway) server. This value is stored in the **SslBridging** property.

> [!IMPORTANT]
> When the SSL bridging type is changed with this method, the RD Gateway service must be restarted to make this change take effect.

 

## Syntax


```mof
uint32 SetSslBridging(
  [in] uint32 SslBridging
);
```



## Parameters

<dl> <dt>

*SslBridging* \[in\]
</dt> <dd>

Type: **uint32**

Specifies the new SSL bridging value. This can be one of the following values.

<dt>

0
</dt> <dd>

No SSL bridging.

</dd> <dt>

1
</dt> <dd>

HTTPS to HTTP bridging.

</dd> <dt>

2
</dt> <dd>

HTTPS to HTTPS bridging.

</dd> </dl> </dd> </dl>

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

 

