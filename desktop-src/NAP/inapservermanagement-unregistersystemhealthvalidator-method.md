---
title: INapServerManagement UnregisterSystemHealthValidator method (NapServerManagement.h)
description: Is used to unregister an SHV with the NAP server.
ms.assetid: f4148df1-a230-4845-ac8b-9e04be9e0d6c
keywords:
- UnregisterSystemHealthValidator method NAP
- UnregisterSystemHealthValidator method NAP , INapServerManagement interface
- INapServerManagement interface NAP , UnregisterSystemHealthValidator method
topic_type:
- apiref
api_name:
- INapServerManagement.UnregisterSystemHealthValidator
api_location:
- qsvrmgmt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapServerManagement::UnregisterSystemHealthValidator method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapServerManagement::UnregisterSystemHealthValidator** method is used to unregister an SHV with the NAP server.

## Syntax


```C++
HRESULT UnregisterSystemHealthValidator(
  [in] SystemHealthEntityId id
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

A [**SystemHealthEntityId**](nap-type-constants.md) that contains the unique identifier of the SHV to unregister.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

If there are any asynchronous calls pending on the SHV, they will complete at a later time and will be discarded.

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

 

 





