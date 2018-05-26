---
Description: A media application that wants to provide a customised ducking experience must listen for the event notifications when a communication stream is opened or closed in the system.
ms.assetid: 709ad912-6b03-4ad3-bc47-ad8b6bd6de45
title: Getting Ducking Events
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting Ducking Events

A media application that wants to provide a customised ducking experience must listen for the event notifications when a communication stream is opened or closed in the system. The custom implementation can be provided by using MediaFoundation, DirectShow, or DirectSound, which use the Core Audio APIs. A direct WASAPI client can also override the default handling if it knows when the communication session starts and ends.

To provide a custom implementation, a media application needs to get notifications from the system when a communication application starts or ends a communication stream. The media application must implement the [**IAudioVolumeDuckNotification**](/windows/win32/AudioPolicy/nn-audiopolicy-iaudiovolumeducknotification?branch=master) interface and register the implementation with the audio system. Upon successful registration, the media application receives event notifications in the form of callbacks through the methods in the interface. For more information, see [Implementation Considerations for Ducking Notifications](handling-audio-ducking-events-from-communication-devices.md).

To send ducking notifications, the audio system must know which audio session is listening for the ducking events. Each audio session is uniquely identified with a GUID—session instance identifier. The session manager allows an application to get information about the session such as title of audio session, the rendering state, and the session instance identifier. The identifier can be retrieved by using the policy control interface, [**IAudioSessionControl2**](/windows/win32/audiopolicy/nn-audiopolicy-iaudiosessioncontrol2?branch=master).

The following steps summarize the process of getting the session instance identifier of the media application:

1.  Instantiate the device enumerator and use it to get a reference to the endpoint of the device that the media application is using to render the non-communication stream.
2.  Activate the session manager from the device endpoint and get a reference to the [**IAudioSessionManager2**](/windows/win32/audiopolicy/nn-audiopolicy-iaudiosessionmanager2?branch=master) interface of the session manager.
3.  By using the [**IAudioSessionManager2**](/windows/win32/audiopolicy/nn-audiopolicy-iaudiosessionmanager2?branch=master) pointer, get a reference to the [**IAudioSessionControl**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessioncontrol?branch=master) interface of the session manager.
4.  Query for the [**IAudioSessionControl2**](/windows/win32/audiopolicy/nn-audiopolicy-iaudiosessioncontrol2?branch=master) from the [**IAudioSessionControl**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessioncontrol?branch=master) interface.
5.  Call [**IAudioSessionControl2::GetSessionInstanceIdentifier**](/windows/win32/audiopolicy/nf-audiopolicy-iaudiosessioncontrol2-getsessioninstanceidentifier?branch=master) and retrieve a string that contains the session identifier for the current audio session.

To get ducking notifications about communication streams, the media application calls [**IAudioSessionManager2::RegisterDuckNotification**](/windows/win32/audiopolicy/nf-audiopolicy-iaudiosessionmanager2-registerducknotification?branch=master). The media application supplies its session instance identifier to the audio system and a pointer to the [**IAudioVolumeDuckNotification**](/windows/win32/AudioPolicy/nn-audiopolicy-iaudiovolumeducknotification?branch=master) implementation. The application can now receive event notification when a stream opened on the communication device. To stop getting notification, the media application must call [**IAudioSessionManager2::UnregisterDuckNotification**](/windows/win32/audiopolicy/nf-audiopolicy-iaudiosessionmanager2-unregisterducknotification?branch=master).

The following code shows how an application can register to get ducking notifications. The CMediaPlayer class is defined in [Implementation Considerations for Ducking Notifications](handling-audio-ducking-events-from-communication-devices.md). The [DuckingMediaPlayer](duckingmediaplayer.md) sample implements this functionality.


```C++
////////////////////////////////////////////////////////////////////
//Description: Registers for duck notifications depending on the 
//             the ducking options specified by the caller.
//Parameters: 
//    If DuckingOptOutChecked is TRUE, the client is registered for
//    to receive ducking notifications; 
//    FALSE, the client's registration is deleted.
////////////////////////////////////////////////////////////////////

HRESULT CMediaPlayer::DuckingOptOut(bool DuckingOptOutChecked)
{
    HRESULT hr = S_OK;

    IMMDeviceEnumerator* pDeviceEnumerator NULL;
    IMMDevice* pEndpoint = NULL;
    IAudioSessionManager2* pSessionManager2 = NULL;
    IAudioSessionControl* pSessionControl = NULL;
    IAudioSessionControl2* pSessionControl2 = NULL;

    LPWSTR sessionId = NULL;

    //  Start with the default endpoint.

    hr = CoCreateInstance(__uuidof(MMDeviceEnumerator), 
                          NULL, 
                          CLSCTX_INPROC_SERVER, 
                          IID_PPV_ARGS(&amp;pDeviceEnumerator));
    
    if (SUCCEEDED(hr))
    {
        hr = pDeviceEnumerator>GetDefaultAudioEndpoint(
              eRender, eConsole, &amp;pEndpoint);

        pDeviceEnumerator>Release();
        pDeviceEnumerator = NULL;
    }

    // Activate the session manager.
    if (SUCCEEDED(hr))
    {
        hr = pEndpoint->Activate(__uuidof(IAudioSessionManager2), 
                                 CLSCTX_INPROC_SERVER,
                                 NULL, 
                                 reinterpret_cast<void **>
                                 (&amp;pSessionManager2));
        pEndpoint->Release();
        pEndpoint = NULL;
    }
    if (SUCCEEDED(hr))
    {
        hr = pSessionManager2->GetAudioSessionControl(
                                  NULL, 0, &amp;pSessionControl);
        
    }

    if (SUCCEEDED(hr))
    {
        hr = pSessionControl->QueryInterface(
                               IID_PPV_ARGS(&amp;pSessionControl2));
                
        pSessionControl->Release();
        pSessionControl = NULL;
    }

    // Get the session instance identifier.
    
    if (SUCCEEDED(hr))
    {
        hr = pSessionControl2->GetSessionInstanceIdentifier(
                                 sessionId);
                
        pSessionControl2->Release();
        pSessionControl2 = NULL;
    }

    //  Register for ducking events depending on 
    //  the specified preference.

    if (SUCCEEDED(hr))
    {
        if (DuckingOptOutChecked)
        {
            hr = pSessionManager2->RegisterDuckNotification(
                                    sessionId, this);
        }
        else
        {
            hr = pSessionManager2->UnregisterDuckNotification
                                      (FALSE);
        }
        pSessionManager2->Release();
        pSessionManager2 = NULL;
    }
    return hr;
}
```



## Related topics

<dl> <dt>

[Using a Communication Device](using-the-communication-device.md)
</dt> <dt>

[Default Ducking Experience](stream-attenuation.md)
</dt> <dt>

[Disabling the Default Ducking Experience](disabling-the-ducking-experience.md)
</dt> <dt>

[Providing a Custom Ducking Behavior](providing-a-custom-ducking-experience.md)
</dt> <dt>

[Implementation Considerations for Ducking Notifications](handling-audio-ducking-events-from-communication-devices.md)
</dt> </dl>

 

 



