---
title: IVMRCAuthenticator interface
description: The IVMRCAuthenticator interface defines an interface to a VMRC authentication method.
ms.assetid: a36cd63e-695b-42ec-8287-2efd4af10822
keywords:
- IVMRCAuthenticator interface Virtual Server
- IVMRCAuthenticator interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMRCAuthenticator
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMRCAuthenticator interface

The **IVMRCAuthenticator** interface defines an interface to a VMRC authentication method.

## When to use

It is used to retrieve basic information about the authentication methods supported by Virtual Server. You can retrieve an **IVMRCAuthenticator** object from the [**IVMRCAuthenticatorCollection**](ivmrcauthenticatorcollection.md) object returned from the [**IVMVirtualServer::VMRCAuthenticators**](ivmvirtualserver-vmrcauthenticators.md) property.

## Members

The **IVMRCAuthenticator** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMRCAuthenticator** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMRCAuthenticator** interface has these properties.



| Property                                                         | Access type          | Description                                                        |
|:-----------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------|
| [**Description**](ivmrcauthenticator-description.md)<br/> | Read-only<br/> | The authenticator's description.<br/>                        |
| [**Name**](ivmrcauthenticator-name.md)<br/>               | Read-only<br/> | The authenticator's name.<br/>                               |
| [**Type**](ivmrcauthenticator-type.md)<br/>               | Read-only<br/> | An internal value representing the authentication type.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





