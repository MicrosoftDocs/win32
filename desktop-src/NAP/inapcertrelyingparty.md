---
title: INapCertRelyingParty interface (NapCertRelyingParty.h)
description: Certificate-relying parties must use to communicate with the NapAgent.
ms.assetid: e5ae0f4d-24fa-4049-82d9-1c9baeb34e32
keywords:
- INapCertRelyingParty interface NAP
- INapCertRelyingParty interface NAP , described
topic_type:
- apiref
api_name:
- INapCertRelyingParty
api_location:
- NapCertRelyingParty.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapCertRelyingParty interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapCertRelyingParty** interface provides methods that certificate-relying parties must use to communicate with the NapAgent.

## Members

The **INapCertRelyingParty** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapCertRelyingParty** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapCertRelyingParty** interface has these methods.



| Method                                                                                                        | Description                                                                     |
|:--------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| [**INapCertRelyingParty::GetSubscribedRelyingParties**](inapcertrelyingparty-getsubscribedrelyingparties.md) | Gets a list of relying parties that have subscribed.<br/>                 |
| [**INapCertRelyingParty::SubscribeCertByGroup**](inapcertrelyingparty-subscribecertbygroup.md)               | Subscribes to an already-registered health certificate server (HCS).<br/> |
| [**INapCertRelyingParty::UnSubscribeCertByGroup**](inapcertrelyingparty-unsubscribecertbygroup.md)           | Unsubscribes from an HCS server.<br/>                                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>NapCertRelyingParty.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCertRelyingParty.idl</dt> </dl> |



## See also

<dl> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

