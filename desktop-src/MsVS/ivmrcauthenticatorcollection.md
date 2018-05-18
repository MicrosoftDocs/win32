---
title: IVMRCAuthenticatorCollection interface
description: The IVMRCAuthenticatorCollection interface defines the collection of available VMRC authenticators.
ms.assetid: '2b6a82df-c365-48e1-a585-62ca3c9f04ca'
keywords: ["IVMRCAuthenticatorCollection interface Virtual Server", "IVMRCAuthenticatorCollection interface Virtual Server , described"]
topic_type:
- apiref
api_name:
- IVMRCAuthenticatorCollection
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMRCAuthenticatorCollection interface

The **IVMRCAuthenticatorCollection** interface defines the collection of available VMRC authenticators.

## When to use

An **IVMRCAuthenticatorCollection** object is returned from the [**IVMVirtualServer::VMRCAuthenticators**](ivmvirtualserver-vmrcauthenticators.md) property.

## Members

The **IVMRCAuthenticatorCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMRCAuthenticatorCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMRCAuthenticatorCollection** interface has these properties.



| Property                                                              | Access type          | Description                                                                                                                    |
|:----------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmrcauthenticatorcollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                                                  |
| [**Count**](ivmrcauthenticatorcollection-count.md)<br/>        | Read-only<br/> | The number of authenticator objects contained in this collection.<br/>                                                   |
| [**Item**](ivmrcauthenticatorcollection-item.md)<br/>          | Read-only<br/> | The [**IVMRCAuthenticator**](ivmrcauthenticator.md) object that corresponds to the given index in this collection.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[**IVMRCAuthenticator**](ivmrcauthenticator.md)
</dt> </dl>

 

 





