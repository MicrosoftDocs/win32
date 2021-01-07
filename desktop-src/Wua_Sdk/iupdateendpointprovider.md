---
description: Contains the method used to get an endpoint that is used to connect to a service.
ms.assetid: 4380776A-3B89-444B-B1E9-DCF640D0AEB4
title: IUpdateEndpointProvider interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointProvider
api_type: 
- COM
---

# IUpdateEndpointProvider interface

Contains the method used to get an endpoint that is used to connect to a service. This interface is implemented when writing an endpoint provider.

## Members

The **IUpdateEndpointProvider** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IUpdateEndpointProvider** also has these types of members:

-   [Methods](#methods)

### Methods

The **IUpdateEndpointProvider** interface has these methods.



| Method                                                                       | Description                                                           |
|:-----------------------------------------------------------------------------|:----------------------------------------------------------------------|
| [**GetServiceEndpoint**](iupdateendpointauthprovider-getserviceendpoint.md) | Requests an endpoint that is used to connect to a service.<br/> |



 

## Remarks

WUA calls the [**GetServiceEndpoint**](iupdateendpointauthprovider-getserviceendpoint.md) method to start the negotiation process. When the call is made, WUA passes in the registered token types, and the implementation of this interface returns the token types that it prefers to use.

 

 
