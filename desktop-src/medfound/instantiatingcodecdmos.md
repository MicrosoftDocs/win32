---
description: Instantiating Codec DMOs
ms.assetid: e031d0d4-dd70-409e-8a2e-5a1433fe909e
title: Instantiating Codec DMOs
ms.topic: article
ms.date: 05/31/2018
---

# Instantiating Codec DMOs

You can create a codec DMO by calling the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) COM function. You must pass the class identifier of the DMO, the interface identifier of **IMediaObject**, and a pointer to an **IMediaObject** pointer.

The class identifiers of the codec DMOs are defined as constants in the wmcodecdsp.h header file.

The constant for the **IMediaObject** interface identifier is IID\_IMediaObject.

The following code example demonstrates how to create an instance of a codec DMO:


```
HRESULT CreateVideoEncoderDMO(IMediaObject** ppDMO)
{
    if(ppDMO == NULL)
        return E_POINTER;

    return CoCreateInstance(CLSID_CWMV9EncMediaObject,
                            NULL,
                            CLSCTX_INPROC_SERVER, 
                            IID_IMediaObject, 
                            (void**)ppDMO);
}
```



## Related topics

<dl> <dt>

[Working with Codec DMOs](workingwithcodecdmos.md)
</dt> </dl>

 

 
