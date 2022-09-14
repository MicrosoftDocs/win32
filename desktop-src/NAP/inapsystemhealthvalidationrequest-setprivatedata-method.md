---
title: INapSystemHealthValidationRequest SetPrivateData method (NapSystemHealthValidator.h)
description: Allows the NapServer to store state information.
ms.assetid: 128f9beb-e5da-4b20-bf5e-fcf064209da3
keywords:
- SetPrivateData method NAP
- SetPrivateData method NAP , INapSystemHealthValidationRequest interface
- INapSystemHealthValidationRequest interface NAP , SetPrivateData method
topic_type:
- apiref
api_name:
- INapSystemHealthValidationRequest.SetPrivateData
api_location:
- qshvhost.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthValidationRequest::SetPrivateData method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthValidationRequest::SetPrivateData** method allows the NapServer to store state information.

## Syntax


```C++
HRESULT SetPrivateData(
  [in] const PrivateData *privateData
);
```



## Parameters

<dl> <dt>

*privateData* \[in\]
</dt> <dd>

A pointer to a [**PrivateData**](/windows/win32/api/naptypes/ns-naptypes-privatedata) data blob that contains the opaque state information.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

Only the NapServer can interpret the data blob.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                    |
| Header<br/>                   | <dl> <dt>NapSystemHealthValidator.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthValidator.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qshvhost.dll</dt> </dl>                 |



## See also

<dl> <dt>

[**INapSystemHealthValidationRequest**](inapsystemhealthvalidationrequest.md)
</dt> </dl>

 

 





