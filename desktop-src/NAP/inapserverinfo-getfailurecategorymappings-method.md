---
title: INapServerInfo GetFailureCategoryMappings method (NapServerManagement.h)
description: Retrieves the failure category mappings for a specified SHA or SHV.
ms.assetid: 89b89003-40b3-4763-aec8-01cd0c307649
keywords:
- GetFailureCategoryMappings method NAP
- GetFailureCategoryMappings method NAP , INapServerInfo interface
- INapServerInfo interface NAP , GetFailureCategoryMappings method
topic_type:
- apiref
api_name:
- INapServerInfo.GetFailureCategoryMappings
api_location:
- qsvrmgmt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapServerInfo::GetFailureCategoryMappings method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapServerInfo::GetFailureCategoryMappings** method retrieves the failure category mappings for a specified SHA or SHV.

## Syntax


```C++
HRESULT GetFailureCategoryMappings(
  [in]  SystemHealthEntityId   id,
  [out] FailureCategoryMapping *mapping
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

A [**SystemHealthEntityId**](nap-type-constants.md) that contains the unique identifier of the SHA or the SHV.

</dd> <dt>

*mapping* \[out\]
</dt> <dd>

A pointer to a [**FailureCategoryMapping**](/windows/win32/api/naptypes/ns-naptypes-failurecategorymapping) that contains the mapping data.

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

[**INapServerInfo**](inapserverinfo.md)
</dt> </dl>

 

 





