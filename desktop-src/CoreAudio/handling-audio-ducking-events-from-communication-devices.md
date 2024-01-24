---
description: The Default Ducking Experience provided by the system ducks all non-communication streams available in the system when a communication stream opens.
ms.assetid: 1b92574e-7cde-49c0-a68e-223492412361
title: Implementation Considerations for Ducking Notifications
ms.topic: article
ms.date: 05/31/2018
---

# Implementation Considerations for Ducking Notifications

The [Default Ducking Experience](stream-attenuation.md) provided by the system ducks all non-communication streams available in the system when a communication stream opens. A media application can override the default handling if it knows when the communication session starts and ends.

Consider the scenario implemented by the media application in the [DuckingMediaPlayer](duckingmediaplayer.md) sample. The application pauses the audio stream that it is playing when it receives a duck notification and continues playback when it receives an unduck notification. The pause and continue events are reflected in the media application's user interface. This is supported through two application-defined window messages, WM\_APP\_SESSION\_DUCKED and WM\_APP\_SESSION\_UNDUCKED. The ducking notifications are received asynchronously in the background and the media application must not block the notification thread to process the window messages. The window messages must be processed on the user interface thread.

The ducking behavior works through a notification mechanism. To provide a customized experience, the media application must implement the [**IAudioVolumeDuckNotification**](/windows/desktop/api/AudioPolicy/nn-audiopolicy-iaudiovolumeducknotification) interface and register the implementation with the audio system. Upon successful registration, the media application receives event notifications in the form of callbacks through the methods in the interface. The session manager handling the communication session calls [**IAudioVolumeDuckNotification::OnVolumeDuckNotification**](/windows/desktop/api/AudioPolicy/nf-audiopolicy-iaudiovolumeducknotification-onvolumeducknotification) when the communication stream opens and then calls [**IAudioVolumeDuckNotification::OnVolumeUnduckNotification**](/windows/desktop/api/AudioPolicy/nf-audiopolicy-iaudiovolumeducknotification-onvolumeunducknotification) when the stream is closed on the communication device.

The following code shows a sample implementation of the [**IAudioVolumeDuckNotification**](/windows/desktop/api/AudioPolicy/nn-audiopolicy-iaudiovolumeducknotification) interface. For the definition of CMediaPlayer::DuckingOptOut, see Getting Ducking Events from a Communication Device.


```C++
class CMediaPlayer : public IAudioVolumeDuckNotification
{
    LONG _refCount;

    HWND _AppWindow;

    ~CMediaPlayer();

    STDMETHOD(OnVolumeDuckNotification) (LPCWSTR sessionID, 
                  UINT32 countCommunicationSessions);
    STDMETHOD(OnVolumeUnduckNotification) (LPCWSTR sessionID);

public:
    CDuckingImpl(HWND hWnd);
    HRESULT DuckingOptOut(bool GetDuckEvents);

    // IUnknown
    IFACEMETHODIMP QueryInterface(__in REFIID riid, __deref_out void **ppv);
    IFACEMETHODIMP_(ULONG) AddRef();
    IFACEMETHODIMP_(ULONG) Release();
};

CMediaPlayer::CMediaPlayer(HWND AppWindow) :
        _AppWindow(AppWindow),
        _refCount(1)
{
}
CMediaPlayer::~CMediaPlayer()
{
}

// When we receive a duck notification, 
// post a "Session Ducked" message to the application window.

STDMETHODIMP CMediaPlayer::OnVolumeDuckNotification(LPCWSTR SessionID, 
                                                    UINT32 CountCommunicationsSessions)
{
    PostMessage(_AppWindow, WM_APP_SESSION_DUCKED, 0, 0);
    return 0;
}


// When we receive an unduck notification, 
// post a "Session Unducked" message to the application window.

STDMETHODIMP CMediaPlayer::OnVolumeUnduckNotification(LPCWSTR SessionID)
{
    PostMessage(_AppWindow, WM_APP_SESSION_UNDUCKED, 0, 0);
    return 0;
}

IFACEMETHODIMP CMediaPlayer::QueryInterface(REFIID iid, void **pvObject)
{
    if (pvObject == NULL)
    {
        return E_POINTER;
    }
    *pvObject = NULL;
    if (iid == IID_IUnknown)
    {
        *pvObject = static_cast<IUnknown *>(static_cast<IAudioVolumeDuckNotification *>
                                                                              (this));
        AddRef();
    }
    else if (iid == __uuidof(IAudioVolumeDuckNotification))
    {
        *pvObject = static_cast<IAudioVolumeDuckNotification *>(this);
        AddRef();
    }
    else
    {
        return E_NOINTERFACE;
    }
    return S_OK;
}

IFACEMETHODIMP_(ULONG) CMediaPlayer::AddRef()
{
    return InterlockedIncrement(&_refCount);
}

IFACEMETHODIMP_(ULONG) CMediaPlayer::Release()
{
    LONG refs = InterlockedDecrement(&_refCount);

    if (refs == 0)
    {
        delete this; 
    }

    return refs;   
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

[Getting Ducking Events](getting-ducking-events-from-a-communication-device.md)
</dt> </dl>

 

 



