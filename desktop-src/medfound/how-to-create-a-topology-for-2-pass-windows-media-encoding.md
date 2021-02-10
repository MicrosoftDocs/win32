---
description: Two-pass encoding modes are supported by certain Windows Media encoders and Media Foundation at the pipeline layer.
ms.assetid: 3fd5baff-142f-453e-bb97-b355ee6678fc
title: How to Create a Topology for Two-Pass Windows Media Encoding
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a Topology for Two-Pass Windows Media Encoding

Two-pass encoding modes are supported by certain Windows Media encoders and Media Foundation at the pipeline layer. The application must configure and set up the encoding topology similar to that in single-pass encoding but in the 2-pass encoding mode, the application must run the encoding session twice. On the first pass, the encoder gathers information about the content of the stream. On the second pass, by using the information gathered on the first pass, the final output file is generated. By processing the samples for the stream twice, two-pass encoding optimizes the encoding process and produces higher quality encoded files. Two-pass encoding modes cannot be used on live streams.

Media Foundation supports the following two-pass encoding modes:

-   [Unconstrained Variable Bit Rate Encoding](unconstrained-variable-bit-rate--vbr--encoding.md)
-   [Peak-Constrained Variable Bit Rate Encoding](peak-constrained-variable-bit-rate--vbr--encoding.md)

Building an encoding topology for two-pass encoding is similar to single pass modes. The following list shows the key differences.

-   Encoder configuration must include the [**MFPKEY\_PASSESUSED**](mfpkey-passesusedproperty.md) property that is set to 2 and the [**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md) property to VARIANT\_TRUE. This filters the encoder’s capabilities to two-pass modes. If you are using activation objects, pass these properties to [**MFCreateWMAEncoderActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreatewmaencoderactivate) or [**MFCreateWMVEncoderActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreatewmvencoderactivate).
-   For the first pass, use a dummy media sink in the output node because the samples that are generated in this pass are not added to the final file.
-   For the second pass, query the encoder for the required post-encoding properties and replace the dummy media sink node with the ASF media sink with these properties set.

For more information about setting up an encoding topology see, [Tutorial: Single Pass Windows Media Encoding](tutorial--1-pass-windows-media-encoding.md).

The following procedure summarizes the steps for encoding Windows Media content in an ASF container by using a two-pass encoding mode.

1.  Create a media source for the specified by using the source resolver.
2.  Enumerate the streams in the media source.
3.  Create the ASF media sink and add stream sinks depending on the streams in the media source that need to be encoded.
4.  Create the media sink.
5.  Create the Windows Media encoders for the streams in the output file.
6.  Configure the encoders with the 2-pass encoding properties.
7.  Build a partial encoding topology by connecting the source, encoders, and the media sink.
8.  Instantiate the Media Session and set the topology on the Media Session.
9.  Run the first encoding pass by controlling the Media Session and getting all the relevant events from the Media Session.
10. Close and shutdown the encoding session.
11. Query the encoder for the following properties depending on the type of encoding: 

    | Encoding type                                                                                        | Property name                                                                                                                                                                                                                                                                                                                                                     |
    |------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [Unconstrained Variable Bit Rate Encoding](unconstrained-variable-bit-rate--vbr--encoding.md)       | [**MFPKEY\_PASSESUSED**](mfpkey-passesusedproperty.md)<br/> [**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md)<br/> [**MFPKEY\_BAVG**](mfpkey-bavgproperty.md)<br/> [**MFPKEY\_RAVG**](mfpkey-ravgproperty.md)<br/>                                                                                                               |
    | [Peak-Constrained Variable Bit Rate Encoding](peak-constrained-variable-bit-rate--vbr--encoding.md) | [**MFPKEY\_PASSESUSED**](mfpkey-passesusedproperty.md)<br/> [**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md)<br/> [**MFPKEY\_BAVG**](mfpkey-bavgproperty.md)<br/> [**MFPKEY\_RAVG**](mfpkey-ravgproperty.md)<br/> [**MFPKEY\_BMAX**](mfpkey-bmaxproperty.md)<br/> [**MFPKEY\_RMAX**](mfpkey-rmaxproperty.md)<br/> |

    

     

12. Create the ASF file sink and add the required stream sinks depending on the streams you want to include in the final output file.
13. Set the encoder properties retrieved in step 11 on the file sink.
14. Replace the media sink in the output node with the newly created file sink.
15. Instantiate the Media Session and set the updated topology on the Media Session.
16. Run second encoding pass by controlling the Media Session and getting all the relevant events from the Media Session.
17. Wait for the [MEEndOfPresentation](meendofpresentation.md) event from the Media Session and in the event handler get the encoding property values from the encoder and set them on the file sink. For more information, see "Update Encoding Properties in the File Sink" in [Tutorial: Single Pass Windows Media Encoding](tutorial--1-pass-windows-media-encoding.md).
18. Close and shutdown the encoding session.

## Related topics

<dl> <dt>

[Pipeline Layer ASF Components](pipeline-layer-asf-components.md)
</dt> </dl>

 

 




