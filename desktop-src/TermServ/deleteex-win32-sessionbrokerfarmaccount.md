---
title: DeleteEx method of the Win32_SessionBrokerFarmAccount class
description: The Win32\_SessionBrokerFarmAccount class is no longer available for use as of Windows Server 2012. | DeleteEx method of the Win32_SessionBrokerFarmAccount class
ms.assetid: d30c5d3e-f63c-4b21-85ae-a0b8d5868d64
ms.tgt_platform: multiple
keywords:
- DeleteEx method Remote Desktop Services
- DeleteEx method Remote Desktop Services , Win32_SessionBrokerFarmAccount class
- Win32_SessionBrokerFarmAccount class Remote Desktop Services , DeleteEx method
topic_type:
- apiref
api_name:
- Win32_SessionBrokerFarmAccount.DeleteEx
api_location:
- TssdWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DeleteEx method of the Win32\_SessionBrokerFarmAccount class

\[The [**Win32\_SessionBrokerFarmAccount**](win32-sessionbrokerfarmaccount.md) class is no longer available for use as of Windows Server 2012.\]

Deletes the farm account.

## Syntax


```mof
uint32 DeleteEx(
  [in] boolean DeleteComputerObject
);
```



## Parameters

<dl> <dt>

*DeleteComputerObject* \[in\]
</dt> <dd>

Indicates whether the computer object associated with the farm is to be removed from Active Directory.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| End of client support<br/>    | None supported<br/>                                                              |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                               |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TssdWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SessionBrokerFarmAccount**](win32-sessionbrokerfarmaccount.md)
</dt> </dl>

 

 





