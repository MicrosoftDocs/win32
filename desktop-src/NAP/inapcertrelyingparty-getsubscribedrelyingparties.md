---
title: INapCertRelyingParty GetSubscribedRelyingParties method (NapCertRelyingParty.h)
description: Gets a list of relying parties that have subscribed.
ms.assetid: 7eef28fd-71cd-4765-89a5-2c9ce29fdc00
keywords:
- GetSubscribedRelyingParties method NAP
- GetSubscribedRelyingParties method NAP , INapCertRelyingParty interface
- INapCertRelyingParty interface NAP , GetSubscribedRelyingParties method
topic_type:
- apiref
api_name:
- INapCertRelyingParty.GetSubscribedRelyingParties
api_location:
- NapCertRelyingParty.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapCertRelyingParty::GetSubscribedRelyingParties method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **GetSubscribedRelyingParties** method gets a list of relying parties that have subscribed.

## Syntax


```C++
HRESULT GetSubscribedRelyingParties(
  [out] EnforcementEntityCount *count,
  [out]  EnforcementEntityId   **relyingParties
);
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

A pointer to a [**EnforcementEntityCount**](nap-datatypes.md) that contains the number of subscribed relying parties.

</dd> <dt>

*relyingParties* \[out\]
</dt> <dd>

A pointer to a pointer to an [**EnforcementEntityId**](nap-datatypes.md) that contains the list of subscribed relying parties.

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

The caller must free the *relyingParties* parameter using **CoTaskMemFree**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>NapCertRelyingParty.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCertRelyingParty.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapCertRelyingParty**](inapcertrelyingparty.md)
</dt> </dl>

 

 





