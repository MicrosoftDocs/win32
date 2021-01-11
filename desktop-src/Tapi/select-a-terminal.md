---
description: The following code example demonstrates how to select terminals onto streams associated with a call.
ms.assetid: ff43e81c-ff39-466d-870a-54b75c2938a4
title: Select a Terminal
ms.topic: article
ms.date: 05/31/2018
---

# Select a Terminal

The following code example demonstrates how to select terminals onto streams associated with a call.

Before using this code example, you must perform the operations in [Initialize TAPI](initialize-tapi.md) and [Select an Address](select-an-address.md).

Also, this example requires that the application already have a pointer to the [**ITBasicCallControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasiccallcontrol) interface of either an incoming or outgoing call. See [Make a Call](make-a-call.md) or [Receive a Call](receive-a-call.md) for code examples on how to obtain this pointer.

> [!Note]  
> This example does not have the error checking and releases appropriate for production code.

 

``` syntax
// pAddress is an ITAddress interface pointer.
// pBasicCall is an ITBasicCallControl interface pointer.

// Get the ITStreamControl interface.
ITStreamControl * pStreamControl;
HRESULT hr = pBasicCall->QueryInterface(
        IID_ITStreamControl,
        (void **) &pStreamControl
        );
// If ( hr != S_OK ) process the error here. 

// Enumerate the streams and select 
// terminals onto them.
IEnumStream * pEnumStreams;
ITStream    * pStream;
hr = pStreamControl->EnumerateStreams(&pEnumStreams);
// If ( hr != S_OK ) process the error here. 

while ( S_OK == pEnumStreams->Next(1, &pStream, NULL) )
{
    // Get the media type and direction of this stream.
    long                lMediaType;
    TERMINAL_DIRECTION  dir;
    hr = pStream->get_MediaType( &lMediaType );
    // If ( hr != S_OK ) process the error here. 
    hr = pStream->get_Direction( &dir );
    // If ( hr != S_OK ) process the error here. 

    // Create the default terminal for this media type and direction.
    //   If lMediaType == TAPIMEDIATYPE_VIDEO and
    //   dir == TD_RENDER, a dynamic video render terminal
    //   is required. Please see Incoming.cpp in 
    //   the samples section of the SDK. 
    // For all other terminals, get the default static terminal.
    ITTerminal * pTerminal;
    ITTerminalSupport * pTerminalSupport;
    hr = pAddress->QueryInterface( 
            IID_ITTerminalSupport, 
            (void **)&pTerminalSupport
         );
    // If ( hr != S_OK ) process the error here. 
    hr = pTerminalSupport->GetDefaultStaticTerminal(
            lMediaType,
            dir,
            pTerminal
         );
    // If ( hr != S_OK ) process the error here. 
    // Select the terminal on the stream.
    hr = pStream->SelectTerminal(pTerminal);
    // If ( hr != S_OK ) process the error here. 
}
```

## Related topics

<dl> <dt>

[**ITAddress**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddress)
</dt> <dt>

[**ITBasicCallControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasiccallcontrol)
</dt> <dt>

[**ITStreamControl**](/windows/win32/api/tapi3if/nn-tapi3if-itstreamcontrol)
</dt> <dt>

[**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream)
</dt> <dt>

[**IEnumStream**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumstream)
</dt> <dt>

[**ITTerminal**](/windows/win32/api/tapi3if/nn-tapi3if-itterminal)
</dt> <dt>

[**ITTerminalSupport**](/windows/win32/api/tapi3if/nn-tapi3if-itterminalsupport)
</dt> </dl>

 

 
