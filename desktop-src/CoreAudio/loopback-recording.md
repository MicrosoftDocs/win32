---
description: Loopback Recording
ms.assetid: 71c567f7-fffa-4b75-897a-63ed30c4c9b0
title: Loopback Recording
ms.topic: article
ms.date: 05/31/2018
---

# Loopback Recording

In loopback mode, a client of WASAPI can capture the audio stream that is being played by a rendering endpoint device. To open a stream in loopback mode, the client must:

-   Obtain an [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface for the rendering endpoint device.
-   Initialize a capture stream in loopback mode on the rendering endpoint device.

After following these steps, the client can call the [**IAudioClient::GetService**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-getservice) method to obtain an [**IAudioCaptureClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudiocaptureclient) interface on the rendering endpoint device.

WASAPI provides loopback mode primarily to support acoustic echo cancellation (AEC). However, other types of audio applications might find loopback mode useful for capturing the system mix that is being played by the audio engine.

In the code example in [Capturing a Stream](capturing-a-stream.md), the RecordAudioStream function can be easily modified to configure a loopback-mode capture stream. The required modifications are:

-   In the call to the [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint) method, change the first parameter (*dataFlow*) from eCapture to eRender.
-   In the call to the [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize) method, change the value of the second parameter (*StreamFlags*) from 0 to AUDCLNT\_STREAMFLAGS\_LOOPBACK.

In versions of Windows prior to Windows 10 1703, pull-mode capture client does not receive any events when a stream is initialized with event-driven buffering and is loopback-enabled. To work around this, initialize a render stream in event-driven mode. Each time the client receives an event for the render stream, it must signal the capture client to run the capture thread that reads the next set of samples from the capture endpoint buffer. In Windows 10 versions 1703 and higher, event-driven loopback clients are supported, and no longer need the workaround involving the render stream.  

A client can enable loopback mode only for a shared-mode stream (AUDCLNT\_SHAREMODE\_SHARED). Exclusive-mode streams cannot operate in loopback mode.

The implementation of loopback by WASAPI depend on the capabilities of the hardware. If the hardware supports a loopback pin on the render endpoint, WASAPI uses the audio provided on this pin for the loopback stream. When the hardware does not support a loopback pin, WASAPI copies the output stream from the audio engine into the loopback application's capture buffer, in addition to copying the audio data to the hardware's render pin.

Some hardware vendors implement loopback devices (as opposed to pin instances on render devices) in their audio adapters. Although hardware loopback devices are similar in operation to the WASAPI loopback mode, they can be more difficult to use.

Hardware loopback devices have the following disadvantages for audio applications:

-   Not all audio adapters have loopback devices. Thus, applications that depend on them will not work on all systems.
-   Before an application can record from a loopback device, the user must identify the loopback device and enable it for use.

Different vendors assign different names to their hardware loopback devices. The following names are examples:

-   Stereo Mix
-   Waveout Mix
-   Mixed Output
-   What You Hear

The lack of standardized names might cause users to have difficulty identifying a loopback device in a list of device names.

A hardware loopback device is a capture device. Thus, if an adapter supports a loopback device, an audio application can record from the device in the same way that it records from any other capture device.

For example, if you select a hardware loopback device to be the default capture device, you can use the RecordAudioStream function (without modification) in the code example in [Capturing a Stream](capturing-a-stream.md) to capture the stream from the device. (You can also use a legacy audio API, such as the Windows multimedia **waveInXxx** functions, to capture the stream from the device.)

If your audio adapter contains a hardware loopback device, you can use the Windows multimedia control panel, Mmsys.cpl, to designate the device as the default capture device. The steps are as follows:

1.  To run Mmsys.cpl, open a Command Prompt window and enter the following command:

    ```C++
    control mmsys.cpl
    ```

    

    Alternatively, you can run Mmsys.cpl by right-clicking the speaker icon in the notification area, which is located on the right side of the taskbar, and selecting **Recording Devices**.

2.  After the Mmsys.cpl window opens, right-click anywhere in the list of recording devices and verify that the **Show Disabled Devices** option is checked. (Otherwise, if the loopback device is disabled, it will not appear in the list.)
3.  Browse the list of recording devices to locate the loopback device (if it exists). If the loopback device is disabled, enable it by right-clicking the device and clicking **Enable**.
4.  Finally, to select the loopback device to be the default capture device, right-click the device and click **Set as Default Device**.

WASAPI supports loopback recording regardless of whether the audio hardware contains a loopback device, or whether the user has enabled the device.

Windows Vista provides digital rights management (DRM). Content providers rely on DRM to protect their proprietary music or other content from unauthorized copying and other illegal uses. Similarly, a trusted audio driver does not permit a loopback device to capture digital streams that contain protected content. Windows Vista allows only trusted drivers to play protected content. For more information about trusted drivers and DRM, see the Windows DDK documentation.

WASAPI loopback contains the mix of all audio being played, regardless of the Terminal Services session the audio originated from. For example, you can run a loopback client in a service running in session 0 and capture audio from all user sessions, as well as audio being played from session 0.

Remote Desktop allows redirecting audio to the client. This is implemented by creating new audio devices that only appear for that session.

## Related topics

<dl> <dt>

[Stream Management](stream-management.md)
</dt> </dl>

 

 



