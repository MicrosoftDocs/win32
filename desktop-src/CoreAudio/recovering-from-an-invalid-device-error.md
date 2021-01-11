---
description: Recovering from an Invalid-Device Error
ms.assetid: 1f5c3458-70ca-45ba-ac33-5c7b9f092320
title: Recovering from an Invalid-Device Error
ms.topic: article
ms.date: 05/31/2018
---

# Recovering from an Invalid-Device Error

Many of the methods in WASAPI return error code AUDCLNT\_E\_DEVICE\_INVALIDATED if the audio endpoint device that the client application is using becomes invalid. This error code indicates that the endpoint device has been unplugged, or that the audio hardware or associated hardware resources have been reconfigured, disabled, removed, or otherwise made unavailable for use. Frequently, the application can recover from this error.

>[!NOTE]
> For information on recovering from invalid device errors when using spatial audio APIs (ISAC), see [Recovering from an Invalid-Device Error (Spatial Sound)](recovering-from-an-invalid-device-error-spatial-sound.md)

The strategy that an application should use to recover from an AUDCLNT\_E\_DEVICE\_INVALIDATED error depends on which of the following techniques the application uses to select an audio endpoint device:

-   Always select the default audio rendering or capture device.
-   Select a specific audio endpoint device.

In the latter case, either the application automatically selects a specific device based on internal requirements or it allows the user to explicitly select a device from a list of available devices.

An application that uses the default device can attempt to recover from an AUDCLNT\_E\_DEVICE\_INVALIDATED error as follows:

1.  Release the [**IAudioClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclient) interface and any other WASAPI interfaces that it has acquired on the device.
2.  Call the [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint) method to get the current default audio device.
3.  Attempt to activate [**IAudioClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclient) on the default audio device.

By following the preceding steps, the application tends to respond appropriately regardless of the cause of the AUDCLNT\_E\_DEVICE\_INVALIDATED error. If reconfiguration of the default device caused the error (for example, if the user changed the stream format used by the device), then these steps, if they succeed, enable the application to continue to use the same device. If the user disabled or removed the device that the application was using and another device is available to assume the role of default device, then the application can continue by using the new default device. In either case, the application adapts automatically without requiring intervention by the user.

An application that selects a specific device can attempt to recover from the AUDCLNT\_E\_DEVICE\_INVALIDATED error as follows:

1.  Release the [**IAudioClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclient) interface and any other WASAPI interfaces that it has acquired on the device.
2.  Attempt to activate an [**IAudioClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclient) interface on the same device.
3.  If step 2 fails, then the application can, as an option, prompt the user to select another device.

Step 2 can succeed if the device being used by the application was reconfigured but not disabled or removed. If successful, step 2 enables the application to automatically continue to use the same device without requiring intervention by the user. Step 3 is appropriate if the application allows the user to explicitly select another device after the user has disabled or removed the previously used device.

An application can determine more precisely the cause of an invalid-device error by registering to receive a notification when a session loses its connection to a device. To enable this notification, the application implements an [**IAudioSessionEvents**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionevents) interface and calls the [**IAudioSessionControl::RegisterAudioSessionNotification**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessioncontrol-registeraudiosessionnotification) method to register the interface. When an invalid-device error causes the session to be disconnected, WASAPI calls the [**IAudioSessionEvents::OnSessionDisconnected**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessionevents-onsessiondisconnected) method in the registered interface. Through this method, WASAPI informs the application of the reason for the disconnection. In Windows Vista, the **OnSessionDisconnected** call identifies the following reasons:

-   The user removed the audio endpoint device.
-   The Windows audio service has shut down.
-   The preferred stream format changed for the device that the audio session is connected to.
-   The user logged off the Windows Terminal Services (WTS) session that the audio session was running in. For more information about WTS sessions, see the Windows SDK documentation.
-   The WTS session that the audio session was running in was disconnected.
-   The (shared-mode) audio session was disconnected to make the audio endpoint device available for an exclusive-mode connection.

In response to the disconnection event, WASAPI closes all of the streams that belong to the session. If an application subsequently attempts to access a closed stream through a WASAPI method such as [**IAudioClient::GetCurrentPadding**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-getcurrentpadding), then the method fails and returns error code AUDCLNT\_E\_DEVICE\_INVALIDATED.

An additional benefit to receiving notifications through the [**IAudioSessionEvents**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionevents) interface is that the notifications arrive asynchronously. Thus, even when the stream is not running, the application will still receive timely notification of invalid-device errors that can prevent the stream from running.

## Related topics

<dl> <dt>

[Stream Management](stream-management.md)
</dt> </dl>

 

 



