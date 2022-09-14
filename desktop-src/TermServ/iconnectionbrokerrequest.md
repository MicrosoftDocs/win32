---
title: IConnectionBrokerRequest interface (Cbclient.h)
description: Provides the methods needed to obtain the results of the asynchronous IConnectionBrokerClient GetTargetInfo method.
ms.assetid: 20F42FDC-7026-468E-9B8D-25DFFBE229C1
ms.tgt_platform: multiple
keywords:
- IConnectionBrokerRequest interface Remote Desktop Services
- IConnectionBrokerRequest interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IConnectionBrokerRequest
api_location:
- Cbclient.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IConnectionBrokerRequest interface

Provides the methods needed to obtain the results of the asynchronous [**IConnectionBrokerClient::GetTargetInfo**](iconnectionbrokerclient-gettargetinfo.md) method.

This interface is implemented by the system. An instance of this interface is provided to the caller with the [**IConnectionBrokerClient::GetTargetInfo**](iconnectionbrokerclient-gettargetinfo.md) method.

## Members

The **IConnectionBrokerRequest** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IConnectionBrokerRequest** also has these types of members:

-   [Methods](#methods)

### Methods

The **IConnectionBrokerRequest** interface has these methods.



| Method                                                      | Description                                                           |
|:------------------------------------------------------------|:----------------------------------------------------------------------|
| [**CheckStatus**](iconnectionbrokerrequest-checkstatus.md) | Called to determine the status of an asynchronous request.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Header<br/>                   | <dl> <dt>Cbclient.h</dt> </dl>       |
| Library<br/>                  | <dl> <dt>Cbclient.lib</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Cbclient.dll</dt> </dl>     |
| IID<br/>                      | IID\_IConnectionBrokerRequest is defined as 25114427-ED5D-46A6-AF53-C62D33A4108E<br/> |



## See also

<dl> <dt>

[**IConnectionBrokerClient::GetTargetInfo**](iconnectionbrokerclient-gettargetinfo.md)
</dt> </dl>

 

