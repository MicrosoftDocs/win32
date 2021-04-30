---
title: SetResourceGroup method of the Win32_TSGatewayResourceAuthorizationPolicy class
description: Sets the resource group type and name.
ms.assetid: a3dd0ffa-a39b-46f9-8317-fcc90a8afcd1
ms.tgt_platform: multiple
keywords:
- SetResourceGroup method Remote Desktop Services
- SetResourceGroup method Remote Desktop Services , Win32_TSGatewayResourceAuthorizationPolicy class
- Win32_TSGatewayResourceAuthorizationPolicy class Remote Desktop Services , SetResourceGroup method
topic_type:
- apiref
api_name:
- Win32_TSGatewayResourceAuthorizationPolicy.SetResourceGroup
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetResourceGroup method of the Win32\_TSGatewayResourceAuthorizationPolicy class

Sets the resource group type and name.

## Syntax


```mof
uint32 SetResourceGroup(
  [in] string ResourceGroupName,
  [in] string ResourceGroupType
);
```



## Parameters

<dl> <dt>

*ResourceGroupName* \[in\]
</dt> <dd>

Resource group name. This value replaces the existing **ResourceGroupName** property.

</dd> <dt>

*ResourceGroupType* \[in\]
</dt> <dd>

Identifies the type of the resource group. This value replaces the existing **ResourceGroupType** property.

<dt>

"RG"
</dt> <dd>

Resource group.

</dd> <dt>

"CG"
</dt> <dd>

Computer group, as stored in Active Directory Domain Services.

</dd> <dt>

"ALL"
</dt> <dd>

All resources.

</dd> </dl> </dd> </dl>

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

[**Win32\_TSGatewayResourceAuthorizationPolicy**](win32-tsgatewayresourceauthorizationpolicy.md)
</dt> </dl>

 

