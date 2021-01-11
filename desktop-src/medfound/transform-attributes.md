---
description: Transform Attributes
ms.assetid: 9beb1306-1378-499c-b9e1-c768a7b4c8bc
title: Transform Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Transform Attributes

The following attributes apply either to [Media Foundation Transforms](media-foundation-transforms.md) (MFTs), or to [Activation Objects](activation-objects.md) for MFTs, or both.



| Attribute                                                                                                     | Description                                                                                                                                                                                   | Applies To                  |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| [**MF\_ACTIVATE\_MFT\_LOCKED**](mf-activate-mft-locked-attribute.md)                                         | Specifies whether the Topology Loader will change the media types on an MFT.                                                                                                                  | MFTs                        |
| [**MF\_SA\_D3D\_AWARE**](mf-sa-d3d-aware-attribute.md)                                                       | Specifies whether a Media Foundation transform (MFT) supports DirectX Video Acceleration.                                                                                                     | MFTs                        |
| [MF\_TRANSFORM\_ASYNC](mf-transform-async.md)                                                                | Specifies whether an MFT performs asynchronous processing.                                                                                                                                    | MFTs                        |
| [MF\_TRANSFORM\_ASYNC\_UNLOCK](mf-transform-async-unlock.md)                                                 | Enables the use of an asynchronous MFT.                                                                                                                                                       | MFTs                        |
| [MF\_TRANSFORM\_CATEGORY\_Attribute](mf-transform-category-attribute.md)                                     | Specifies the category for an MFT.                                                                                                                                                            | MFT activation objects      |
| [MF\_TRANSFORM\_FLAGS\_Attribute](mf-transform-flags-attribute.md)                                           | Contains flags for an MFT activation object.                                                                                                                                                  | MFT activation objects      |
| [MFT\_CODEC\_MERIT\_Attribute](mft-codec-merit-attribute.md)                                                 | Contains the merit value of a hardware codec.                                                                                                                                                 | MFT activation objects      |
| [MFT\_CONNECTED\_STREAM\_ATTRIBUTE](mft-connected-stream-attribute.md)                                       | Contains a pointer to the stream attributes of the connected stream on a hardware-based MFT.                                                                                                  | MFTs                        |
| [MFT\_CONNECTED\_TO\_HW\_STREAM](mft-connected-to-hw-stream.md)                                              | Specifies whether a hardware-based MFT is connected to another hardware-based MFT.                                                                                                            | MFTs                        |
| [MFT\_DECODER\_EXPOSE\_OUTPUT\_TYPES\_IN\_NATIVE\_ORDER](mft-decoder-expose-output-types-in-native-order.md) | Specifies whether a decoder exposes IYUV/I420 output types (suitable for transcoding) before other formats.                                                                                   | MFTs                        |
| [MFT\_DECODER\_FINAL\_VIDEO\_RESOLUTION\_HINT](mft-decoder-final-video-resolution-hint.md)                   | Specifies the final output resolution of the decoded image, after video processing.                                                                                                           | MFTs                        |
| [MFT\_ENCODER\_SUPPORTS\_CONFIG\_EVENT](mft-encoder-supports-config-event.md)                                | Specifies that the MFT encoder supports receiving [MEEncodingParameter](meencodingparameters.md) events while streaming.                                                                     | MFTs                        |
| [MFT\_ENUM\_ADAPTER\_LUID](mft-enum-adapter-luid.md)                                                         | Specifies a unique identifier for a video adapter. Use this attribute when calling MFTEnum2 to enumerate MFTs associated with a specific adapter.                                             | MFTs                        |
| [MFT\_ENUM\_HARDWARE\_URL\_Attribute](mft-enum-hardware-url-attribute.md)                                    | Contains the symbolic link for a hardware-based MFT.                                                                                                                                          | MFTs/MFT activation objects |
| [MFT\_ENUM\_HARDWARE\_VENDOR\_ID\_Attribute](mft-enum-hardware-vendor-id-attribute.md)                       | Specifies the vendor ID for a hardware-based Media Foundation Transform                                                                                                                       | MFTs                        |
| [MFT\_ENUM\_TRANSCODE\_ONLY\_ATTRIBUTE](mft-enum-transcode-only-attribute.md)                                | Specifies whether a decoder is optimized for transcoding rather than for playback.                                                                                                            | MFTs                        |
| [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md)                                     | Contains an [**IMFFieldOfUseMFTUnlock**](/windows/desktop/api/mfidl/nn-mfidl-imffieldofusemftunlock) pointer, which can be used to unlock the MFT.                                                                            | MFT activation objects      |
| [MFT\_FRIENDLY\_NAME\_Attribute](mft-friendly-name-attribute.md)                                             | Contains the display name for a hardware-based MFT.                                                                                                                                           | MFT activation objects      |
| [MFT\_INPUT\_TYPES\_Attributes](mft-input-types-attributes.md)                                               | Contains the registered input types for an MFT.                                                                                                                                               | MFT activation objects      |
| [MFT\_OUTPUT\_TYPES\_Attributes](mft-output-types-attributes.md)                                             | Contains the registered output types for an MFT.                                                                                                                                              | MFT activation objects      |
| [MFT\_PREFERRED\_ENCODER\_PROFILE](mft-preferred-encoder-profile.md)                                         | Contains configuration properties for an encoder.                                                                                                                                             | MFT activation objects      |
| [MFT\_PREFERRED\_OUTPUTTYPE\_Attribute](mft-preferred-outputtype-attribute.md)                               | Specifies the preferred output format for an encoder.                                                                                                                                         | MFT activation objects      |
| [MFT\_PREFERRED\_OUTPUTTYPE\_Attribute](mft-preferred-outputtype-attribute.md)                               | Specifies the preferred output format for an encoder.                                                                                                                                         | MFT activation objects      |
| [MFT\_PROCESS\_LOCAL\_Attribute](mft-process-local-attribute.md)                                             | Specifies whether an MFT is registered only in the application's process.                                                                                                                     | MFT activation objects      |
| [MFT\_REMUX\_MARK\_I\_PICTURE\_AS\_CLEAN\_POINT](mft-remux-mark-i-picture-as-clean-point.md)                 | Specifies whether the H.264 video remux MFT should mark I pictures as clean point for better seek-ability. This has the potential for corruptions on seeks in non-conforming final MP4 files. | MFT activation objects      |
| [MFT\_SUPPORT\_3DVIDEO](mft-support-3dvideo.md)                                                              | Specifies whether a Media Foundation transform (MFT) supports 3D stereoscopic video.                                                                                                          | MFT activation objects      |
| [**MFT\_SUPPORT\_DYNAMIC\_FORMAT\_CHANGE**](mft-support-dynamic-format-change-attribute.md)                  | Specifies whether a Media Foundation transform (MFT) supports dynamic format changes.                                                                                                         | MFTs                        |
| [MFT\_TRANSFORM\_CLSID\_Attribute](mft-transform-clsid-attribute.md)                                         | Contains the class identifier (CLSID) of an MFT.                                                                                                                                              | MFT activation objects      |



 

## Related topics

<dl> <dt>

[**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> </dl>

 

 



