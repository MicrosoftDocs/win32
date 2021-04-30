---
description: The following attributes can be used to configure the Capture Engine.
ms.assetid: C153F0AD-4E8B-41DA-B7FB-8D10AC20D22E
title: Capture Engine Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Capture Engine Attributes

The following attributes can be used to configure the Capture Engine.

The following attributes are related to capture devices:



| Attribute                                                                                                                              | Description                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [MF\_CAPTURE\_ENGINE\_CAMERA\_STREAM\_BLOCKED](mf-capture-engine-camera-stream-blocked.md)                                            | Signals that video capture is being blocked by the driver.                                                         |
| [MF\_CAPTURE\_ENGINE\_CAMERA\_STREAM\_UNBLOCKED](mf-capture-engine-camera-stream-unblocked.md)                                        | Signals that video capture is restored after being blocked.                                                        |
| [MF\_CAPTURE\_ENGINE\_D3D\_MANAGER](mf-capture-engine-d3d-manager.md)                                                                 | Sets a pointer to the DXGI Device Manager on the capture engine.                                                   |
| [MF\_CAPTURE\_ENGINE\_DECODER\_MFT\_FIELDOFUSE\_UNLOCK\_ATTRIBUTE](mf-capture-engine-decoder-mft-fieldofuse-unlock-attribute.md)      | Enables the capture engine to use a decoder that has field-of-use restrictions.                                    |
| [MF\_CAPTURE\_ENGINE\_DISABLE\_DXVA](mf-capture-engine-disable-dxva.md)                                                               | Specifies whether the capture engine uses DirectX Video Acceleration (DXVA) for video decoding.                    |
| [MF\_CAPTURE\_DISABLE\_HARDWARE\_TRANSFORMS](mf-capture-engine-disable-hardware-transforms.md)                                        | Disables the use of hardware-based Media Foundation transforms (MFTs) in the capture engine.                       |
| [MF\_CAPTURE\_ENGINE\_ENABLE\_CAMERA\_STREAMSTATE\_NOTIFICATION](mf-capture-engine-enable-camera-streamstate-notification.md)         | Indicates whether stream state notifications should be enabled.                                                    |
| [MF\_CAPTURE\_ENGINE\_ENCODER\_MFT\_FIELDOFUSE\_UNLOCK\_ATTRIBUTE](mf-capture-engine-encoder-mft-fieldofuse-unlock-attribute.md)      | Enables the capture engine to use an encoder that has field-of-use restrictions.                                   |
| [MF\_CAPTURE\_ENGINE\_EVENT\_GENERATOR\_GUID](mf-capture-engine-event-generator-guid.md)                                              | Identifies the component that generated a capture event.                                                           |
| [MF\_CAPTURE\_ENGINE\_EVENT\_STREAM\_INDEX](mf-capture-engine-event-stream-index.md)                                                  | Identifies which stream generated a capture event.                                                                 |
| [MF\_CAPTURE\_ENGINE\_MEDIASOURCE\_CONFIG](mf-capture-engine-mediasource-config.md)                                                   | Contains configuration properties for the capture source.                                                          |
| [MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_AUDIO\_MAX\_PROCESSED\_SAMPLES](mf-capture-engine-record-sink-audio-max-processed-samples.md)     | Sets the maximum number of processed samples that can be buffered in the record sink audio path.                   |
| [MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_AUDIO\_MAX\_UNPROCESSED\_SAMPLES](mf-capture-engine-record-sink-audio-max-unprocessed-samples.md) | Sets the maximum number of unprocessed samples that can be buffered for processing in the record sink audio path.. |
| [MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_VIDEO\_MAX\_PROCESSED\_SAMPLES](mf-capture-engine-record-sink-video-max-processed-samples.md)     | Sets the maximum number of processed samples that can be buffered in the record sink video path.                   |
| [MF\_CAPTURE\_ENGINE\_RECORD\_SINK\_VIDEO\_MAX\_UNPROCESSED\_SAMPLES](mf-capture-engine-record-sink-video-max-unprocessed-samples.md) | Sets the maximum number of unprocessed samples that can be buffered for processing in the record sink video path.  |
| [MF\_CAPTURE\_ENGINE\_SINK\_TYPE](/windows/desktop/api/mfcaptureengine/ne-mfcaptureengine-mf_capture_engine_sink_type)                                                                     | Specifies a type of capture sink.                                                                                  |
| [MF\_CAPTURE\_ENGINE\_USE\_AUDIO\_DEVICE\_ONLY](mf-capture-engine-use-audio-device-only.md)                                           | Specifies whether the capture engine captures audio but not video.                                                 |
| [MF\_CAPTURE\_ENGINE\_USE\_VIDEO\_DEVICE\_ONLY](mf-capture-engine-use-video-device-only.md)                                           | Specifies whether the capture engine captures video but not audio.                                                 |



 

## Related topics

<dl> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[**IMFCaptureEngine::Initialize**](/windows/desktop/api/mfcaptureengine/nf-mfcaptureengine-imfcaptureengine-initialize)
</dt> </dl>

 

 



