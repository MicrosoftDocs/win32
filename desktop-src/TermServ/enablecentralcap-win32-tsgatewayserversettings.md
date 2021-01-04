---
title: EnableCentralCAP method of the Win32_TSGatewayServerSettings class
description: Controls the CentralCAPEnabled property, which controls the Remote Desktop Services connection authorization policies (RD \ 160;CAPs) for the Remote Desktop Gateway (RD Gateway) server.
ms.assetid: 43e476df-714d-43bd-b40f-33511b7757a4
ms.tgt_platform: multiple
keywords:
- EnableCentralCAP method Remote Desktop Services
- EnableCentralCAP method Remote Desktop Services , Win32_TSGatewayServerSettings class
- Win32_TSGatewayServerSettings class Remote Desktop Services , EnableCentralCAP method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServerSettings.EnableCentralCAP
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EnableCentralCAP method of the Win32\_TSGatewayServerSettings class

Controls the **CentralCAPEnabled** property, which controls the Remote Desktop Services connection authorization policies (RD CAPs) for the Remote Desktop Gateway (RD Gateway) server.

## Syntax


```mof
uint32 EnableCentralCAP(
  [in] boolean CentralCAPEnabled
);
```



## Parameters

<dl> <dt>

*CentralCAPEnabled* \[in\]
</dt> <dd>

If set to **True**, RD CAPs from central RD CAP servers will be used. If set to **False**, only policies from the local server will be used.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md)
</dt> </dl>

 

