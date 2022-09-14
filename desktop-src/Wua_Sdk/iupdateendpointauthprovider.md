---
description: Contains the methods used for negotiating which type of token is used for authenticating the endpoint of a service.
ms.assetid: F6177B24-C166-4BEC-83D6-3AD5B5B3CF08
title: IUpdateEndpointAuthProvider interface (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointAuthProvider
api_type: 
- COM
api_location: 
- UpdateEndpointAuth.dll
---

# IUpdateEndpointAuthProvider interface

The **IUpdateEndpointAuthProvider** interface contains the methods used for negotiating which type of token is used for authenticating the endpoint of a service.

## Members

The **IUpdateEndpointAuthProvider** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IUpdateEndpointAuthProvider** also has these types of members:

-   [Methods](#methods)

### Methods

The **IUpdateEndpointAuthProvider** interface has these methods.



| Method                                                                                             | Description                                                                                    |
|:---------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**GetEndpointToken**](iupdateendpointauthprovider-getendpointtoken.md)                           | Request a token for the endpoint of the service using the specified credentials.<br/>    |
| [**GetPreferredEndpointTokenType**](iupdateendpointauthprovider-getpreferredendpointtokentype.md) | Returns the preferred type of authentication token for the endpoint of the service.<br/> |



 

## Remarks

WUA calls the [**GetPreferredEndpointTokenType**](iupdateendpointauthprovider-getpreferredendpointtokentype.md) method of this interface to start the negotiation process. When the call is made WUA passes in the service identifier, the type of endpoint implemented by the service, and the token types that are available. The implementation of this interface then returns the token types that it preferes to use.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>                   |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>                |
| Header<br/>                   | <dl> <dt>UpdateEndpointAuth.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>UpdateEndpointAuth.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>UpdateEndpointAuth.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>UpdateEndpointAuth.dll</dt> </dl> |



 

 
