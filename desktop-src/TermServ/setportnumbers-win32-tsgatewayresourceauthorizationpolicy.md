---
title: SetPortNumbers method of the Win32_TSGatewayResourceAuthorizationPolicy class
description: Sets the port numbers that are allowed to connect to the resource through Remote Desktop Gateway (RD Gateway).
ms.assetid: f8237ec3-84dc-44f8-ad86-54c46be1fd03
ms.tgt_platform: multiple
keywords:
- SetPortNumbers method Remote Desktop Services
- SetPortNumbers method Remote Desktop Services , Win32_TSGatewayResourceAuthorizationPolicy class
- Win32_TSGatewayResourceAuthorizationPolicy class Remote Desktop Services , SetPortNumbers method
topic_type:
- apiref
api_name:
- Win32_TSGatewayResourceAuthorizationPolicy.SetPortNumbers
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetPortNumbers method of the Win32\_TSGatewayResourceAuthorizationPolicy class

Sets the port numbers that are allowed to connect to the resource through Remote Desktop Gateway (RD Gateway).

## Syntax


```mof
uint32 SetPortNumbers(
  [in] string PortNumbers
);
```



## Parameters

<dl> <dt>

*PortNumbers* \[in\]
</dt> <dd>

List of semicolon-separated port numbers that are allowed for this Remote Desktop resource authorization policy (RD RAP). To allow any port number, set "\*".

</dd> </dl>

## Remarks

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

[**Win32\_TSGatewayResourceAuthorizationPolicy**](win32-tsgatewayresourceauthorizationpolicy.md)
</dt> </dl>

 

