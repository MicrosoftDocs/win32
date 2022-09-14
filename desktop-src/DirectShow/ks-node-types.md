---
description: The following globally unique identifiers (GUIDs) define node types for kernel-mode filters. To find the node type, query the filter for the IKsTopologyInfo interface.
ms.assetid: 0e133ce3-8815-47d1-a5c3-577a98963912
title: KS Node Types (Ksmedia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- KSNODETYPE_DEV_SPECIFIC
- KSNODETYPE_VIDEO_CAMERA_TERMINAL
- KSNODETYPE_VIDEO_INPUT_MTT
- KSNODETYPE_VIDEO_INPUT_TERMINAL
- KSNODETYPE_VIDEO_OUTPUT_MTT
- KSNODETYPE_VIDEO_OUTPUT_TERMINAL
- KSNODETYPE_VIDEO_PROCESSING
- KSNODETYPE_VIDEO_SELECTOR
- KSNODETYPE_VIDEO_STREAMING
api_type: 
- HeaderDef
api_location: 
- Ksmedia.h
---

# KS Node Types

The following globally unique identifiers (GUIDs) define node types for kernel-mode filters. To find the node type, query the filter for the [**IKsTopologyInfo**](/previous-versions/windows/desktop/api/Vidcap/nn-vidcap-ikstopologyinfo) interface.



| GUID                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                              |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="KSNODETYPE_DEV_SPECIFIC"></span><span id="ksnodetype_dev_specific"></span><dl> <dt>**KSNODETYPE\_DEV\_SPECIFIC**</dt> </dl>                             | Represents one or more device-specific processing functions. The node has one input connection and one output connection.<br/> The node may expose a custom COM interface through a KsProxy plug-in, if provided by the device manufacturer.<br/>                                            |
| <span id="KSNODETYPE_VIDEO_CAMERA_TERMINAL"></span><span id="ksnodetype_video_camera_terminal"></span><dl> <dt>**KSNODETYPE\_VIDEO\_CAMERA\_TERMINAL**</dt> </dl> | Represents data moving into the device from a camera sensor, independent of the USB bus. The node has one output connection.<br/> The node exposes the [**IAMCameraControl**](/windows/desktop/api/Strmif/nn-strmif-iamcameracontrol) and [**ICameraControl**](/previous-versions/windows/desktop/api/Vidcap/nn-vidcap-icameracontrol) interfaces for controlling the camera.<br/> |
| <span id="KSNODETYPE_VIDEO_INPUT_MTT"></span><span id="ksnodetype_video_input_mtt"></span><dl> <dt>**KSNODETYPE\_VIDEO\_INPUT\_MTT**</dt> </dl>                   | Represents data moving into the device from a sequential media transport, such as a VTR tape, independent of the USB bus. The node has one output connection.<br/> The node exposes the [**IAMExtTransport**](/windows/desktop/api/Strmif/nn-strmif-iamexttransport) interface for controlling the transport mechanism.<br/>   |
| <span id="KSNODETYPE_VIDEO_INPUT_TERMINAL"></span><span id="ksnodetype_video_input_terminal"></span><dl> <dt>**KSNODETYPE\_VIDEO\_INPUT\_TERMINAL**</dt> </dl>    | Represents data moving into the device, independent of the USB bus. For example, this node may represent an analog audio jack or S/PDIF jack. The node has one output connection.<br/>                                                                                                             |
| <span id="KSNODETYPE_VIDEO_OUTPUT_MTT"></span><span id="ksnodetype_video_output_mtt"></span><dl> <dt>**KSNODETYPE\_VIDEO\_OUTPUT\_MTT**</dt> </dl>                | Represents data moving from the device to a sequential media transport, such as a VTR tape, independent of the USB bus. The node has one input connection.<br/> The node exposes the [**IAMExtTransport**](/windows/desktop/api/Strmif/nn-strmif-iamexttransport) interface for controlling the transport mechanism.<br/>      |
| <span id="KSNODETYPE_VIDEO_OUTPUT_TERMINAL"></span><span id="ksnodetype_video_output_terminal"></span><dl> <dt>**KSNODETYPE\_VIDEO\_OUTPUT\_TERMINAL**</dt> </dl> | Represents data moving from the device, independent of the USB bus. For example, this node may represent an analog audio jack or S/PDIF jack. The node has one input connection.<br/>                                                                                                              |
| <span id="KSNODETYPE_VIDEO_PROCESSING"></span><span id="ksnodetype_video_processing"></span><dl> <dt>**KSNODETYPE\_VIDEO\_PROCESSING**</dt> </dl>                 | Represents one or more video processing functions. The node has one input connection and one output connection.<br/> The node exposes the [**IAMVideoProcAmp**](/windows/desktop/api/Strmif/nn-strmif-iamvideoprocamp) and [**IVideoProcAmp**](/previous-versions/windows/desktop/api/Vidcap/nn-vidcap-ivideoprocamp) interfaces to adjust the qualities of the video signal.<br/> |
| <span id="KSNODETYPE_VIDEO_SELECTOR"></span><span id="ksnodetype_video_selector"></span><dl> <dt>**KSNODETYPE\_VIDEO\_SELECTOR**</dt> </dl>                       | Represents a mechanism to select the input path from two or more possible sources. The node has two or more input connections and one output connection.<br/> The node exposes the [**ISelector**](/previous-versions/windows/desktop/api/Vidcap/nn-vidcap-iselector) interface for selecting between inputs.<br/>                               |
| <span id="KSNODETYPE_VIDEO_STREAMING"></span><span id="ksnodetype_video_streaming"></span><dl> <dt>**KSNODETYPE\_VIDEO\_STREAMING**</dt> </dl>                    | Represents data moving between the host and the device. For UVC devices, this node represents a USB endpoint. Input endpoints have one input connection; output endpoints have one output connection.<br/>                                                                                         |



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ksmedia.h</dt> </dl> |



## See also

<dl> <dt>

[Constants and GUIDs](constants-and-guids.md)
</dt> </dl>

 

 




