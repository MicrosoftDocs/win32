---
title: INapEnforcementClientCallback interface (NapEnforcementClient.h)
description: Enforcement clients must implement to enable the NapAgent to communicate with them.
ms.assetid: d7d63c5b-7952-4f04-9d3d-3f13b0b52d97
keywords:
- INapEnforcementClientCallback interface NAP
- INapEnforcementClientCallback interface NAP , described
topic_type:
- apiref
api_name:
- INapEnforcementClientCallback
api_location:
- NapEnforcementClient.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientCallback interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientCallback** interface provides callback methods that enforcement clients must implement to enable the NapAgent to communicate with them.

## Members

The **INapEnforcementClientCallback** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapEnforcementClientCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapEnforcementClientCallback** interface has these methods.



| Method                                                                                                         | Description                                                                      |
|:---------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**INapEnforcementClientCallback::GetConnections**](inapenforcementclientcallback-getconnections-method.md)   | Used by the NapAgent to retrieve connections.<br/>                         |
| [**INapEnforcementClientCallback::NotifySoHChange**](inapenforcementclientcallback-notifysohchange-method.md) | Used by the NapAgent to inform the enforcement client of SoH changes.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapEnforcementClient.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapEnforcementClient.idl</dt> </dl> |



 

