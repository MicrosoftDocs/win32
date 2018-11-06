---
title: Fixed Buffer Serialization
description: Fixed buffer serialization.
ms.assetid: 3432f468-89f2-48e2-8d86-15ba549f0fc7
ms.topic: article
ms.date: 05/31/2018
---

# Fixed Buffer Serialization

When using the fixed buffer style, specify a buffer that is large enough to accommodate the encoding (marshalling) operations performed with the handle. When unmarshaling, you provide the buffer that contains all of the data to decode.

The fixed buffer style of serialization uses the following routines:

-   [**MesEncodeFixedBufferHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesencodefixedbufferhandlecreate)
-   [**MesDecodeBufferHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesdecodebufferhandlecreate)
-   [**MesBufferHandleReset**](/windows/desktop/api/Midles/nf-midles-mesbufferhandlereset)
-   [**MesHandleFree**](/windows/desktop/api/Midles/nf-midles-meshandlefree)

The **MesEncodeFixedBufferHandleCreate** function allocates the memory needed for the encoding handle, and then initializes it. The application can call [**MesBufferHandleReset**](/windows/desktop/api/Midles/nf-midles-mesbufferhandlereset) to reinitialize the handle, or it can call [**MesHandleFree**](/windows/desktop/api/Midles/nf-midles-meshandlefree) to free the handle's memory. To create a decoding handle corresponding to the fixed style–encoding handle, you must use [**MesDecodeBufferHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesdecodebufferhandlecreate).

The application calls [**MesHandleFree**](/windows/desktop/api/Midles/nf-midles-meshandlefree) to free the encoding or decoding buffer handle.

## Examples of Fixed Buffer Encoding

The following section provides an example of how to use a fixed buffer style–serializing handle for procedure encoding.

``` syntax
/*This is a fragment of the IDL file defining MooProc */

...
void __RPC_USER
MyProc( [in] handle_t Handle, [in,out] MyType * pMyObject,
        [in, out] ThisType * pThisObject);
...

/*This is an ACF file. MyProc is defined in the IDL file */

[
    explicit_handle
]
interface regress
{
    [ encode,decode ] MyProc();
}
```

The following excerpt represents a part of an application.

``` syntax
if (MesEncodeFixedBufferHandleCreate (
        Buffer, BufferSize, 
        pEncodedSize, &Handle) == RPC_S_OK)
{
    ...
    /* Manufacture a MyObject and a ThisObject */
    ...
    /* The serialization works from the beginning of the buffer because 
   the handle is in the initial state. The function MyProc does the    
   following when called with an encoding handle:
     - sizes all the parameters for marshalling,
     - marshalls into the buffer (and sets the internal state 
    appropriately) 
    */

    MyProc ( Handle, pMyObject, pThisObject );
    ...
    MesHandleFree ();
}
if (MesDecodeBufferHandleCreate (Buffer, BufferSize, &Handle) ==
    RPC_S_OK)
{

    /* The MooProc does the following for you when called with a decoding 
    handle:
     - unmarshalls the objects from the buffer into *pMooObject and 
       *pBarObject
*/

MyProc ( Handle, pMyObject, pThisObject);
...
MesHandleFree ( Handle );
}
```

The following section provides an example of how to use a fixed buffer style–serializing handle for type encoding.

``` syntax
/* This is an ACF file. MyType is defined in the IDL file */

[    
    explicit_handle
]
interface regress
{
    typedef [ encode,decode ] MyType;
}
```

The following excerpt represents the relevant application fragments.


```C++
if (MesEncodeFixedBufferHandleCreate (Buffer, BufferSize, 
    pEncodedSize, &Handle) == RPC_S_OK)
{
    //...
    /* Manufacture a MyObject and a pMyObject */
    //...
    MyType_Encode ( Handle, pMyObject );
    //...
    MesHandleFree ();
}
if (MesDecodeBufferHandleCreate (Buffer, BufferSize, &Handle) ==
    RPC_S_OK )
{
    MooType_Decode (Handle, pMooObject);
    //...
    MesHandleFree ( Handle );
}
```



 

 




