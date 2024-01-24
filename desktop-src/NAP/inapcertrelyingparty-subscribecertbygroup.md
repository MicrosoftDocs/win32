---
title: INapCertRelyingParty SubscribeCertByGroup method (NapCertRelyingParty.h)
description: Subscribes to a health certificate server (HCS).
ms.assetid: 6fce113d-e183-45d7-8fb5-e04b6f4afcca
keywords:
- SubscribeCertByGroup method NAP
- SubscribeCertByGroup method NAP , INapCertRelyingParty interface
- INapCertRelyingParty interface NAP , SubscribeCertByGroup method
topic_type:
- apiref
api_name:
- INapCertRelyingParty.SubscribeCertByGroup
api_location:
- NapCertRelyingParty.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapCertRelyingParty::SubscribeCertByGroup method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **SubscribeCertByGroup** method subscribes to a health certificate server (HCS). The HCS must already be registered before subscribing.

## Syntax


```C++
HRESULT SubscribeCertByGroup(
  [in]        EnforcementEntityId  id,
  [in]  const BSTR                subscriberName,
  [in]  const  VARIANT            *reserved,
  [out]       BOOL                *certExists
);
```



## Parameters

<dl> <dt>

 *id* \[in\]
</dt> <dd>

An [**EnforcementEntityId**](nap-datatypes.md) that contains the ID of the enforcement client that is subscribing.

</dd> <dt>

*subscriberName* \[in\]
</dt> <dd>

The name of the subscriber.

> [!Note]  
> This is currently only used for logging purposes.

 

</dd> <dt>

*reserved* \[in\]
</dt> <dd>

Must be **NULL**.

</dd> <dt>

*certExists* \[out\]
</dt> <dd>

Indicates whether a health certificate from this HCS is already being maintained by the NapAgent and is present in the machine store. If **TRUE**, a health certificate is already being maintained and is present. If **FALSE**, a health certificate is not currently being maintained and present.

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

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

 

 





