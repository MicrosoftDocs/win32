---
description: The following code example demonstrates how to create a call object, discover the streams associated with the call, select and create appropriate terminals, select the terminals onto the streams, and complete the connection.
ms.assetid: 49815b18-a8ea-46e0-b2a4-3d7a82e727b0
title: Make a Call
ms.topic: article
ms.date: 05/31/2018
---

# Make a Call

The following code example demonstrates how to create a call object, discover the streams associated with the call, select and create appropriate terminals, select the terminals onto the streams, and complete the connection.

Before using this code example, you must perform the operations in [Initialize TAPI](initialize-tapi.md) and [Select an Address](select-an-address.md).

Also, you must perform the operations illustrated in [Select a Terminal](select-a-terminal.md) following the call to [**ITAddress::CreateCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddress-createcall).

> [!Note]  
> This example does not have the error checking and releases appropriate for production code.

 

``` syntax
// Specify the destination address.
//
// szAddressToCall and 
// dwAddressType have been
// retrieved from a user interface.
ITBasicCallControl * pBasicCall
bstrAddressToCall = SysAllocString( szAddressToCall );
// If ( bstrAddressToCall == NULL ) process the error here. 

HRESULT hr = pAddress->CreateCall(
    bstrAddressToCall,
    dwAddressType,
    &pBasicCall
 );
// If ( hr != S_OK ) process the error here. 

SysFreeString(bstrAddressToCall);

// Create the required terminals for this call.
{
    // See the Select a Terminal code example.
}

// Make the connection.
pBasicCall->Connect( TRUE );
```

## Related topics

<dl> <dt>

[**ITAddress::CreateCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddress-createcall)
</dt> <dt>

[**ITBasicCallControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasiccallcontrol)
</dt> <dt>

[**ITBasicCallControl::Connect**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-connect)
</dt> </dl>

 

 



