---
title: Update method of the Win32_TSGatewayResourceGroup class
description: Updates the resource group.
ms.assetid: b5927046-f461-41cd-861b-0fd77f2008e5
ms.tgt_platform: multiple
keywords:
- Update method Remote Desktop Services
- Update method Remote Desktop Services , Win32_TSGatewayResourceGroup class
- Win32_TSGatewayResourceGroup class Remote Desktop Services , Update method
topic_type:
- apiref
api_name:
- Win32_TSGatewayResourceGroup.Update
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Update method of the Win32\_TSGatewayResourceGroup class

Updates the resource group.

## Syntax


```mof
uint32 Update(
  [in] string Name,
  [in] string Description,
  [in] string Resources
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the resource group.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description of the resource group.

</dd> <dt>

*Resources* \[in\]
</dt> <dd>

Semicolon-separated list of resources in this resource group. An "\*" means all resources.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

If multiple resources are in the *Resources* parameter and one of the resources cannot be processed, none of the resources will be processed.

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

[**Win32\_TSGatewayResourceGroup**](win32-tsgatewayresourcegroup.md)
</dt> </dl>

 

