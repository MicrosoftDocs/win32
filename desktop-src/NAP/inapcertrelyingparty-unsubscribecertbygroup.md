---
title: INapCertRelyingParty UnSubscribeCertByGroup method (NapCertRelyingParty.h)
description: Unsubscribes from a health certificate server (HCS).
ms.assetid: 2b26b110-8aba-487e-bd49-c6afc6af11f8
keywords:
- UnSubscribeCertByGroup method NAP
- UnSubscribeCertByGroup method NAP , INapCertRelyingParty interface
- INapCertRelyingParty interface NAP , UnSubscribeCertByGroup method
topic_type:
- apiref
api_name:
- INapCertRelyingParty.UnSubscribeCertByGroup
api_location:
- NapCertRelyingParty.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapCertRelyingParty::UnSubscribeCertByGroup method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **UnSubscribeCertByGroup** method unsubscribes from a health certificate server (HCS).

## Syntax


```C++
HRESULT UnSubscribeCertByGroup(
  [in]        EnforcementEntityId   id,
  [in] const  VARIANT             * reserved
);
```



## Parameters

<dl> <dt>

 *id* \[in\]
</dt> <dd>

An [**EnforcementEntityId**](nap-datatypes.md) that contains the ID of the enforcement client that is unsubscribing.

</dd> <dt>

 *reserved* \[in\]
</dt> <dd>

Must be **NULL**.

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

If there are no other subscribers to the HCS, the NapAgent will delete the corresponding health certificates from the local machine store.

Before calling this method, call [**SubscribeCertByGroup**](inapcertrelyingparty-subscribecertbygroup.md).

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

 

 





