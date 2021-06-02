---
description: Encoding Properties
ms.assetid: 6845c3fb-38a8-4b0d-aea2-e10f7e518653
title: Encoding Properties
ms.topic: article
ms.date: 05/31/2018
---

# Encoding Properties

The Windows Media Audio and Windows Media Video encoders support a variety of encoding modes. These modes are generally configured by setting properties on the encoder [Media Foundation transform](media-foundation-transforms.md) (MFT). To perform file encoding, whether using WMContainer-level components or by building a partial topology, you must configure the encoder appropriately by setting properties depending on the mode of encoding and the media type of the stream. The same set of properties must be set both on the encoder and the object (ASF file sink or ASF multiplexer) you are using to write the ASF file.

The encoder properties are defined in wmcodecdsp.h. The specific properties that are used to configure the encoder are set by using the methods of the [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) interface.

-   [Audio Stream Properties](#audio-stream-properties)
-   [Video Stream Properties](#video-stream-properties)
-   [Configuring the Encoder's Property Store](#configuring-the-encoders-property-store)

### Audio Stream Properties

The following table shows the encoder configurations for an audio stream.



| Encoding type                                                                                        | Property name - Value                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Constant Bit Rate Encoding](constant-bit-rate-encoding.md)                                         | MFPKEY\_VBRENABLED - **FALSE** (Optional)By default, MFPKEY\_VBRENABLED is set to **FALSE**.<br/>                                                                                             |
| [Quality-Based Variable Bit Rate Encoding](quality-based-variable-bit-rate--vbr--encoding.md)       | MFPKEY\_VBRENABLED - **TRUE**<br/> MFPKEY\_PASSESUSED - 1 (Optional)<br/> By default, MFPKEY\_PASSESUSED is set to 1.<br/> MFPKEY\_DESIRED\_VBRQUALITY - From 0 to 100<br/> |
| [Unconstrained Variable Bit Rate Encoding](unconstrained-variable-bit-rate--vbr--encoding.md)       | MFPKEY\_VBRENABLED - **TRUE**<br/> MFPKEY\_PASSESUSED - 2<br/>                                                                                                                          |
| [Peak-Constrained Variable Bit Rate Encoding](peak-constrained-variable-bit-rate--vbr--encoding.md) | MFPKEY\_VBRENABLED - **TRUE**<br/> MFPKEY\_PASSESUSED - 2<br/> MFPKEY\_RMAX - Maximum bit rate<br/> MFPKEY\_BMAX - Maximum buffer window<br/>                               |



 

### Video Stream Properties

The following table shows the encoder configurations for a video stream.



| Encoding type                                                                                        | Property name                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Constant Bit Rate Encoding](constant-bit-rate-encoding.md)                                         | MFPKEY\_VBRENABLED - **FALSE** (Optional)<br/> By default, MFPKEY\_VBRENABLED is set to **FALSE**.<br/> MFPKEY\_VIDEOWINDOW - Buffer window<br/>                                  |
| [Quality-Based Variable Bit Rate Encoding](quality-based-variable-bit-rate--vbr--encoding.md)       | MFPKEY\_VBRENABLED - **TRUE**<br/> MFPKEY\_PASSESUSED - 1 (Optional)<br/> By default, MFPKEY\_PASSESUSED is set to 1.<br/> MFPKEY\_DESIRED\_VBRQUALITY - From 0 to 100<br/> |
| [Unconstrained Variable Bit Rate Encoding](unconstrained-variable-bit-rate--vbr--encoding.md)       | MFPKEY\_VBRENABLED - **TRUE**<br/> MFPKEY\_PASSESUSED - 2<br/>                                                                                                                          |
| [Peak-Constrained Variable Bit Rate Encoding](peak-constrained-variable-bit-rate--vbr--encoding.md) | MFPKEY\_VBRENABLED - **TRUE**<br/> MFPKEY\_PASSESUSED - 2<br/> MFPKEY\_RMAX - Maximum bit rate<br/> MFPKEY\_BMAX - Maximum buffer window<br/>                               |



 

### Configuring the Encoder's Property Store

You must configure an encoder by specifying the type of encoding and the various stream-specific settings before the encoding session. You must also set the encoder properties in the property store of an [ASF ContentInfo Object](asf-contentinfo-object.md) that represents the ASF Header Object of the output file.

If you are using an encoder MFT:

1.  Get a reference to the encoder MFT's [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface as described in [Using an Encoder's IMFTransform Interface](using-an-encoder-s-imftransform--interface.md).
2.  Querying the encoder MFT for the **IPropertyStore** interface.
3.  Setting the required properties by calling **IPropertyStore::SetValue**.

If you are using the built-in encoder activation objects and have already created an configured the ASF file sink, you can pass the ASF media sink's property store to [**MFCreateWMAEncoderActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreatewmaencoderactivate) or [**MFCreateWMVEncoderActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreatewmvencoderactivate). The encoder is configured automatically based on the settings specified by the application. For more information, see the procedure described in [Using an Encoder's Activation Objects](using-an-encoder-s-activation-objects.md).

For more information about creating Media Foundation objects by using activation objects, see [Activation Objects](activation-objects.md).

## Related topics

<dl> <dt>

[Instantiating an Encoder MFT](instantiating-the-encoder-mft.md)
</dt> <dt>

[Windows Media Encoders](windows-media-encoders.md)
</dt> </dl>

 

 
