---
description: Operational Correspondence with Motion Compensation Device Driver
ms.assetid: bd92a0f4-98d9-497a-99b9-0cf432347daf
title: Operational Correspondence with Motion Compensation Device Driver
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Operational Correspondence with Motion Compensation Device Driver

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section contains a description of the Motion Compensation device driver side of the DirectX VA interface. (Reference:Windows 2000 DDK - Graphics Drivers - Design Guide - 3.0 DirectDraw DDI - 3.12 Motion Compensation. See the Windows DDK for documentation on the structures in boldface.)

The following items refer to entries accessed through the **DD\_MOTIONCOMPCALLBACKS** structure:

1.  At the start of the relevant processing, the device driver's **DdMoCompCreate** is used to notify the driver that the software decoder will start using a video acceleration object.
2.  GUIDs received from [**IAMVideoAccelerator::GetVideoAcceleratorGUIDs**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-getvideoacceleratorguids) originate from the device driver's **DdMoCompGetGUIDs**.
3.  A call to the downstream input pin's [**IAMVideoAccelerator::GetUncompFormatsSupported**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-getuncompformatssupported) returns data from the device driver's **DdMoCompGetFormats**.
4.  The DXVA\_ConnectMode data structure from the decoder's [**IAMVideoAcceleratorNotify::GetCreateVideoAcceleratorData**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoacceleratornotify-getcreatevideoacceleratordata) is passed to the device driver's **DdMoCompCreate**.
5.  Data returned from [**IAMVideoAccelerator::GetCompBufferInfo**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-getcompbufferinfo) originates from the device driver's **DdMoCompGetBuffInfo**.
6.  Buffers sent using [**IAMVideoAccelerator::Execute**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-execute) are received by the device driver's **DdMoCompRender**.
7.  Use of [**IAMVideoAccelerator::QueryRenderStatus**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-queryrenderstatus) invokes the device driver's **DdMoCompQueryStatus**. A return code of DDERR\_WASSTILLDRAWING from DdMoCompQueryStatus will be seen by the host decoder as a return code of E\_PENDING from **IAMVideoAccelerator::QueryRenderStatus**.
8.  Data sent to [**IAMVideoAccelerator::BeginFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-beginframe) are received by the device driver's **DdMoCompBeginFrame**. A return code of E\_PENDING is needed from DdMoCompBeginFrame in order for E\_PENDING to be seen by the host decoder in response to **IAMVideoAccelerator::BeginFrame**.
9.  Data sent to [**IAMVideoAccelerator::EndFrame**](/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-endframe) are received by the device driver's **DdMoCompEndFrame**.
10. At the end of the relevant processing, the device driver's **DdMoCompDestroy** is used to notify the driver that the current video acceleration object will no longer be used, so that the driver can perform any necessary cleanup.

 

 



