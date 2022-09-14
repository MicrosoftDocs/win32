---
title: IConnectionBrokerClient interface (Cbclient.h)
description: Provides the methods needed to use the Remote Desktop Connection Broker client.
ms.assetid: AFFE0157-DEF5-480D-8CE0-D89E9EF70EAF
ms.tgt_platform: multiple
keywords:
- IConnectionBrokerClient interface Remote Desktop Services
- IConnectionBrokerClient interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IConnectionBrokerClient
api_location:
- Cbclient.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IConnectionBrokerClient interface

Provides the methods needed to use the Remote Desktop Connection Broker client.

This interface is implemented by the system. To obtain an instance of this interface, use the [**CBCreateClientInstance**](cbcreateclientinstance.md) function.

## Members

The **IConnectionBrokerClient** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IConnectionBrokerClient** also has these types of members:

-   [Methods](#methods)

### Methods

The **IConnectionBrokerClient** interface has these methods.



| Method                                                         | Description                                                                                          |
|:---------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**GetTargetInfo**](iconnectionbrokerclient-gettargetinfo.md) | Requests information about the target computer where the connection should be redirected.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Header<br/>                   | <dl> <dt>Cbclient.h</dt> </dl>      |
| Library<br/>                  | <dl> <dt>Cbclient.lib</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Cbclient.dll</dt> </dl>    |
| IID<br/>                      | IID\_IConnectionBrokerClient is defined as D6818DF2-8338-4EB7-AD77-DE210817987C<br/> |



## See also

<dl> <dt>

[**CBCreateClientInstance**](cbcreateclientinstance.md)
</dt> </dl>

 

