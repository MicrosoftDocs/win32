---
description: Configuring Codec MFTs
ms.assetid: 0de0cb2e-67bc-4db5-879a-95879f16b98d
title: Configuring Codec MFTs
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Codec MFTs

This topic describes the process of configuring the codec MFTs. Each codec has specific procedures, but the information common to all is described here.

## Configuring MFT Inputs and Outputs

Every MFT supports specific input and output types. You can retrieve supported input types by repeatedly calling [**IMFTransform::GetInputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputavailabletype), incrementing the type index with each call. When you find an appropriate type, set the input type by calling [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype). You can then repeat the process for the output type using the calls [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) and [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype). You must query or set the available output types only after setting the input type.

## Configuring the Codec MFTs for Encoding

All of the Windows Media Audio and Video codecs support a variety of encoding features. These features are generally configured by setting properties on the MFT by using the methods of the **IPropertyStore** interface. Some properties are configured using specialized codec interfaces. These interfaces are listed for each codec in the section [Codec Objects](codecobjects.md).

The general order of operations for configuring an encoding MFT is as follows:

1.  Configure codec features as desired by using the methods of **IPropertyStore**.
2.  Use the codec MFT interfaces to configure additional features, if needed.
3.  Configure the input and output types. The order in which the types should be configured varies for individual codecs. For more information, see [Working with Audio](workingwithaudio.md) and [Working with Video](workingwithvideo.md).

## Configuring the Codec MFTs for Decoding

Decoding is simpler than encoding, as fewer decoder features are supported.

The general order of operations for configuring a decoding MFT is as follows:

1.  Configure decoder features as desired by using the methods of **IPropertyStore**.
2.  Set the input type to the type used for the encoder output.
3.  Configure the output type. The supported output types are different for different inputs.

> [!Note]  
> It is important to use the same media type for the decoder input as was used for the encoder output. This is because the Windows Media Audio and Video codecs use media formats with extra data. Without the extended format data, you cannot decode the compressed content.

 

## Related topics

<dl> <dt>

[Working with Codec MFTs](workingwithcodecmfts.md)
</dt> </dl>

 

 



