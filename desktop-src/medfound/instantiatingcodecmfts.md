---
description: Instantiating Codec MFTs
ms.assetid: 171f9a0f-effb-4ed7-8aff-d7b1ee6e4973
title: Instantiating Codec MFTs
ms.topic: article
ms.date: 05/31/2018
---

# Instantiating Codec MFTs

[Media Foundation Transforms](media-foundation-transforms.md) (MFTs) are COM objects that implement the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface. An MFT is an object for transforming multimedia data as part of a pipeline. A pipeline is a directed acyclic graph, consisting of media sources, media transforms, and media sinks. A pipeline processes streaming multimedia data asynchronously.

Although MFTs can be instantiated and used independently of the Media Foundation pipeline infrastructure, it is preferable to use the MediaFoundation framework where possible.

You can create a codec MFT by calling the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function. You must pass the class identifier of the MFT, the interface identifier of [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform), and a pointer to an **IMFTransform** pointer.

The class identifiers of the codec MFTs are defined as constants in the wmcodecdsp.h header file.

The constant for the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface identifier is IID\_IMFTransform.

The following code example demonstrates how to create an instance of a codec MFT:


```
HRESULT CreateVideoEncoderMFT(IMFTransform** ppMFT)
{
    if (ppMFT == NULL)
        return E_POINTER;

    return CoCreateInstance(CLSID_CWMV9EncMediaObject,
                            NULL,
                            CLSCTX_INPROC_SERVER, 
                            IID_IMFTransform, 
                            (void**)ppMFT);
}
```



## Related topics

<dl> <dt>

[Working with Codec MFTs](workingwithcodecmfts.md)
</dt> </dl>

 

 
