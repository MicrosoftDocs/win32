---
title: Streaming Capture from an MCI Device
description: Streaming Capture from an MCI Device
ms.assetid: 44cbf375-f97e-426a-a703-dfb1b1933138
keywords:
- MCI (Media Control Interface),streaming capture
- WM_CAP_SET_MCI_DEVICE message
- capSetMCIDeviceName macro
- WM_CAP_GET_MCI_DEVICE message
- capGetMCIDeviceName macro
ms.topic: article
ms.date: 05/31/2018
---

# Streaming Capture from an MCI Device

MCI devices augment the capture operation in real-time capture and step-frame capture. You can specify the MCI device, such as a videodisc or video-cassette recorder (VCR), acting as the video source for your capture operation by using the [**WM\_CAP\_SET\_MCI\_DEVICE**](wm-cap-set-mci-device.md) message (or the [**capSetMCIDeviceName**](/windows/desktop/api/Vfw/nf-vfw-capsetmcidevicename) macro) and specifying the name of the device. You can also retrieve the device name currently set by using the [**WM\_CAP\_GET\_MCI\_DEVICE**](wm-cap-get-mci-device.md) message (or the [**capGetMCIDeviceName**](/windows/desktop/api/Vfw/nf-vfw-capgetmcidevicename) macro).

In real-time capture, the capture window synchronizes the capture operation and compensates for delays associated with positioning the MCI video source and initializing the resources (such as capture buffers) required for capturing data. The capture window expects a valid MCI video device to be installed in the system for capturing data this way.

Specifications for controlling an MCI device are stored in the members of the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure. MCI-compatible video sources include VCRs and laserdiscs. If the **fMCIControl** member of this structure is set to **TRUE**, the capture window coordinates MCI operation. The capture window uses the parameters specified in the **dwMCIStartTime** and **dwMCIStopTime** members to obtain the starting and stopping positions, in milliseconds, of the sequence. If the value of **fMCIControl** is **FALSE**, the video source is not treated as an MCI device and the contents of **dwMCIStartTime** and **dwMCIStopTime** are ignored.

You can use Media Player to quickly verify that an MCI video device is properly connected to the system. Playing a device with Media Player verifies that the MCI configuration for the device is correct. If an image appears on the video display, the video source is connected properly to the capture hardware.

In step-frame capture, the capture window synchronizes the capture operation and compensates for the delays associated with positioning the MCI video source and initializing the resources required for capturing data. In addition, the capture window ensures that no frames are dropped; it steps through the video frames individually, ensuring that the frame is captured and stored before capturing the next frame in the video stream.

Specifications for controlling step-frame capture are stored in the members of the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure. Step-frame capture uses the following members in addition to the members used for real-time capture: **fStepMCIDevice**, **fStepCaptureAt2x**, and **wStepCaptureAverageFrames**. If the **fStepMCIDevice** member is set to **TRUE**, the capture window coordinates step-frame capture. The capture window uses the parameters specified in the **dwMCIStartTime** and **dwMCIStopTime** members for the starting and stopping positions, in milliseconds, of the sequence. The capture window uses **fStepCaptureAt2x** to determine if the capture hardware should capture video frames at twice the normal resolution and uses **wStepCaptureAverageFrames** to specify the number of times each frame in the capture operation is sampled.

If **fStepMCIDevice** is **FALSE**, real-time capture is used instead of step-frame capture and the contents of **fStepCaptureAt2x**, and **wStepCaptureAverageFrames** are ignored.

If a step-frame capture is specified and **fStepCaptureAt2x** is set to **TRUE**, the capture hardware captures at twice the specified resolution. (The resolutions of both the height and width are doubled.) The software interpolates the pixels in the higher resolution image to produce the image at the specified resolution. This form of averaging can improve the edge definition of images in a frame. You can enable this option if the hardware does not support hardware-based decimation and you are capturing in the RGB format.

> [!Note]  
> If your hardware supports hardware-based decimation, it can capture samples at a higher rate than specified and use these additional samples to obtain color definitions that are more consistent with the original image. The additional samples are discarded after they are used, and the hardware passes samples to the capture driver at the specified rate.

 

If a step-frame capture is specified, the **wStepCaptureAverageFrames** member specifies the number of times a frame is sampled when creating a frame based on the average sample. This averaging technique reduces the random digitization noise appearing in a frame. A typical value for the number of averages is 5.

For more information about MCI, see [MCI](mci.md).

## Related topics

<dl> <dt>

[Capture Variations](capture-variations.md)
</dt> </dl>

 

 




