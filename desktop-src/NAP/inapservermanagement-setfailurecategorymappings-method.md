---
title: INapServerManagement SetFailureCategoryMappings method (NapServerManagement.h)
description: Is used to set the SHV's failure category mappings.
ms.assetid: be482f82-c79c-405c-b619-9bcb9b4dc349
keywords:
- SetFailureCategoryMappings method NAP
- SetFailureCategoryMappings method NAP , INapServerManagement interface
- INapServerManagement interface NAP , SetFailureCategoryMappings method
topic_type:
- apiref
api_name:
- INapServerManagement.SetFailureCategoryMappings
api_location:
- qsvrmgmt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapServerManagement::SetFailureCategoryMappings method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapServerManagement::SetFailureCategoryMappings** method is used to set the SHV's failure category mappings.

## Syntax


```C++
HRESULT SetFailureCategoryMappings(
  [in]       SystemHealthEntityId   id,
  [in] const FailureCategoryMapping mapping
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

A [**SystemHealthEntityId**](nap-type-constants.md) that contains the unique identifier of the SHV.

</dd> <dt>

*mapping* \[in\]
</dt> <dd>

A [**FailureCategoryMapping**](/windows/win32/api/naptypes/ns-naptypes-failurecategorymapping) structure that contains the failure category mapping data.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>NapServerManagement.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapServerManagement.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qsvrmgmt.dll</dt> </dl>            |



## See also

<dl> <dt>

[**INapServerManagement**](inapservermanagement.md)
</dt> </dl>

 

 





