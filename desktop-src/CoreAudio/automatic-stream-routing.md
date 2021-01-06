---
description: This article describes how to update a WASAPI implementation to take advantage of automatic stream routing.
ms.assetid: 718CBEB9-A7A0-4898-81B7-CBD76AFA3A06
title: Automatic Stream Routing
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Stream Routing

This article describes how to update a WASAPI implementation to take advantage of automatic stream routing.

Starting with Windows 7, whenever the default audio device changes, an app's audio playback stream is seamlessly transferred from the previous default audio device to the new default audio device . This transfer occurs automatically without any additional application code. However, prior to Windows 10, version 1607, apps that used the low-level Windows Audio Session API (WASAPI) could not participate in this automated stream routing functionality. Apps using WASAPI were required to implement their own form of stream routing by adding additional code to detect the arrival and removal of audio devices and switch the stream to those devices as appropriate. Applications using WASAPI that did not implement their own stream routing mechanism on device arrival or removal risked providing a less than ideal user experience.

Starting with the Windows 10, version 1607, apps that use WASAPI can take advantage of automatic stream routing. If your application uses WASAPI it is highly recommended that you update your application to take advantage of this new capability using the following steps:

1.  Windows 10, version 1607, defines two new GUIDs that can be used to activate an audio render or capture interface with automatic stream routing, [DEVINTERFACE\_AUDIO\_RENDER](/windows/desktop/CoreAudio/devinterface-xxx-guids) and [DEVINTERFACE\_AUDIO\_CAPTURE](/windows/desktop/CoreAudio/devinterface-xxx-guids). Get a string representation of these GUIDs by calling [**StringFromIID**](/windows/desktop/api/combaseapi/nf-combaseapi-stringfromiid). The following example shows this call for the audio render GUID.

    ```C++
    PWSTR audioRenderGuidString;
    StringFromIID(DEVINTERFACE_AUDIO_RENDER, &audioRenderGuidString);
    ```

    

2.  Activate the audio endpoint by passing the identifier string to the WASAPI [**ActivateAudioInterfaceAsync**](/windows/desktop/api/mmdeviceapi/nf-mmdeviceapi-activateaudiointerfaceasync) function. The following example passes in the audio render identifier obtained in step 1:

    ```C++
    //Activate the default audio interface
    ActivateAudioInterfaceAsync(audioRenderGuidString
                                __uuidof(IAudioClient),
                                NULL,
                                completionHandler.Get(),
                                operation.GetAddressOf()));
    ```

    

3.  Free the memory allocated for holding the endpoint identifier:

    ```C++
    CoTaskMemFree(audioRenderGuidString);  //free the string memory
    ```

    

After you have modified your app to activate the audio interface in the manner described above, it will participate in the automatic stream routing feature.

To demonstrate automatic stream routing, use a laptop or tablet equipped with internal speakers to play back audio. You should hear the audio playing through the device's internal speakers. While audio is playing, connect a pair of headphones. You should now hear audio playing through the headphones. Then, unplug the headphones and audio should automatically route back to the internal speakers.

## Related topics

<dl> <dt>

[Stream Routing](stream-routing.md)
</dt> <dt>

[**MediaDevice.GetDefaultAudioRenderId**](/uwp/api/windows.media.devices.mediadevice.getdefaultaudiorenderid)
</dt> <dt>

[**MediaDevice.GetDefaultAudioCaptureId**](/uwp/api/windows.media.devices.mediadevice.getdefaultaudiocaptureid)
</dt> <dt>

[**ActivateAudioInterfaceAsync**](/windows/desktop/api/mmdeviceapi/nf-mmdeviceapi-activateaudiointerfaceasync)
</dt> </dl>

 

 
