---
description: Provides the methods that WUA can use to gather information about the endpoint token.
ms.assetid: 52D22909-B926-426F-98C7-643C4469D021
title: IUpdateEndpointAuthToken interface (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointAuthToken
api_type: 
- COM
api_location: 
- UpdateEndpointAuth.dll
---

# IUpdateEndpointAuthToken interface

Provides the methods that WUA can use to gather information about the endpoint token.

## Members

The **IUpdateEndpointAuthToken** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IUpdateEndpointAuthToken** also has these types of members:

-   [Methods](#methods)

### Methods

The **IUpdateEndpointAuthToken** interface has these methods.



| Method                                                                                | Description                                                                                                                 |
|:--------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**ServiceID**](iupdateendpointauthtoken-serviceid.md)                               | Gets the identifier of the service to be authenticated.<br/>                                                          |
| [**SigningKey**](iupdateendpointauthtoken-signingkey.md)                             | Gets the key used to sign outgoing messages between the client computer and the sercvice.<br/>                        |
| [**TokenData**](iupdateendpointauthtoken-tokendata.md)                               | Gets the XML data (sent over the wire) that represents the token. <br/>                                               |
| [**TokenReferenceAttached**](iupdateendpointauthtoken-tokenreferenceattached.md)     | Gets the XML format of an attached reference to the token.<br/>                                                       |
| [**TokenReferenceUnattached**](iupdateendpointauthtoken-tokenreferenceunattached.md) | Gets the XML format of an unattached reference to the token.<br/>                                                     |
| [**TokenType**](iupdateendpointauthtoken-tokentype.md)                               | Gets the type of the endpoint token, such as a WS-Security SAML (Security Assertion Markup Language) 1.1 token. <br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>                   |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>                |
| Header<br/>                   | <dl> <dt>UpdateEndpointAuth.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>UpdateEndpointAuth.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>UpdateEndpointAuth.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>UpdateEndpointAuth.dll</dt> </dl> |



 

 
