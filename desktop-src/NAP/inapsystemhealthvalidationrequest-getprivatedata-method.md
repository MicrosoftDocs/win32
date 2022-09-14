---
title: INapSystemHealthValidationRequest GetPrivateData method (NapSystemHealthValidator.h)
description: Allows the NapServer to retrieve state information.
ms.assetid: f85026ca-852b-4eb1-9a8c-7e03cd1765f2
keywords:
- GetPrivateData method NAP
- GetPrivateData method NAP , INapSystemHealthValidationRequest interface
- INapSystemHealthValidationRequest interface NAP , GetPrivateData method
topic_type:
- apiref
api_name:
- INapSystemHealthValidationRequest.GetPrivateData
api_location:
- qshvhost.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthValidationRequest::GetPrivateData method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthValidationRequest::GetPrivateData** method allows the NapServer to retrieve state information.

## Syntax


```C++
HRESULT GetPrivateData(
  [out] PrivateData **privateData
);
```



## Parameters

<dl> <dt>

*privateData* \[out\]
</dt> <dd>

A pointer to a pointer to [**PrivateData**](/windows/win32/api/naptypes/ns-naptypes-privatedata) opaque data blob that contains state information.

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

 

 





