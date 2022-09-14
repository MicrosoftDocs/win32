---
description: Audio Events for Legacy Audio Applications
ms.assetid: 91a93b79-2563-4b25-af5d-ca5f7d35d77b
title: Audio Events for Legacy Audio Applications
ms.topic: article
ms.date: 05/31/2018
---

# Audio Events for Legacy Audio Applications

Legacy audio APIs such as DirectSound, DirectShow, and the **waveOutXxx** functions enable applications to get and set the volume levels of audio streams. Applications can use the volume-control capabilities in these APIs to display volume sliders in their application windows.

In Windows Vista, the system volume-control program, Sndvol, allows users to control the audio volume levels for individual applications. The volume sliders that are displayed by applications should be linked to the corresponding volume sliders in Sndvol. If a user adjusts the application volume through a volume slider in an application window, then the corresponding volume slider in Sndvol immediately moves to indicate the new volume level. Conversely, if the user adjusts the application volume through Sndvol, then the volume sliders in the application window should move to indicate the new volume level.

In Windows Vista, Sndvol immediately reflects volume changes that an application makes through calls to the **IDirectSoundBuffer::SetVolume** method or **waveOutSetVolume** function. However, a legacy audio API such as DirectSound or the **waveOutXxx** functions provides no means to notify an application when the user changes the application volume through Sndvol. If an application displays a volume slider but does not receive notifications of volume changes, then the slider will fail to reflect changes made by the user in Sndvol. To implement the appropriate behavior, the application designer must somehow compensate for the lack of notifications by the legacy audio API.

One solution might be for the application to set a timer to periodically remind it to check the volume level to see if it has changed.

A more elegant solution is for the application to use the event notification capabilities of the core audio APIs. In particular, the application can register an [**IAudioSessionEvents**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionevents) interface to receive callbacks when volume changes or other types of audio events occur. When the volume changes, the volume-change callback routine can immediately update the application's volume slider to reflect the change.

The following code example shows how an application can register to receive notifications of volume changes and other audio events:


```C++
//-----------------------------------------------------------
// Register the application to receive notifications when the
// volume level changes on the default process-specific audio
// session (with session GUID value GUID_NULL) on the audio
// endpoint device with the specified data-flow direction
// (eRender or eCapture) and device role.
//-----------------------------------------------------------
#define EXIT_ON_ERROR(hr)  \
              if (FAILED(hr)) { goto Exit; }
#define SAFE_RELEASE(punk)  \
              if ((punk) != NULL)  \
                { (punk)->Release(); (punk) = NULL; }

class AudioVolumeEvents
{
    HRESULT _hrStatus;
    IAudioSessionManager *_pManager;
    IAudioSessionControl *_pControl;
    IAudioSessionEvents *_pAudioEvents;
public:
    AudioVolumeEvents(EDataFlow, ERole, IAudioSessionEvents*);
    ~AudioVolumeEvents();
    HRESULT GetStatus() { return _hrStatus; };
};

// Constructor
AudioVolumeEvents::AudioVolumeEvents(EDataFlow flow, ERole role,
                                     IAudioSessionEvents *pAudioEvents)
{
    IMMDeviceEnumerator *pEnumerator = NULL;
    IMMDevice *pDevice = NULL;

    _hrStatus = S_OK;
    _pManager = NULL;
    _pControl = NULL;
    _pAudioEvents = pAudioEvents;

    if (_pAudioEvents == NULL)
    {
        _hrStatus = E_POINTER;
        return;
    }

    _pAudioEvents->AddRef();

    // Get the enumerator for the audio endpoint devices
    // on this system.
    _hrStatus = CoCreateInstance(__uuidof(MMDeviceEnumerator),
                                 NULL, CLSCTX_INPROC_SERVER,
                                 __uuidof(IMMDeviceEnumerator),
                                 (void**)&pEnumerator);
    EXIT_ON_ERROR(_hrStatus)

    // Get the audio endpoint device with the specified data-flow
    // direction (eRender or eCapture) and device role.
    _hrStatus = pEnumerator->GetDefaultAudioEndpoint(flow, role,
                                                     &pDevice);
    EXIT_ON_ERROR(_hrStatus)

    // Get the session manager for the endpoint device.
    _hrStatus = pDevice->Activate(__uuidof(IAudioSessionManager),
                                  CLSCTX_INPROC_SERVER, NULL,
                                  (void**)&_pManager);
    EXIT_ON_ERROR(_hrStatus)

    // Get the control interface for the process-specific audio
    // session with session GUID = GUID_NULL. This is the session
    // that an audio stream for a DirectSound, DirectShow, waveOut,
    // or PlaySound application stream belongs to by default.
    _hrStatus = _pManager->GetAudioSessionControl(NULL, 0, &_pControl);
    EXIT_ON_ERROR(_hrStatus)

    _hrStatus = _pControl->RegisterAudioSessionNotification(_pAudioEvents);
    EXIT_ON_ERROR(_hrStatus)

Exit:
    SAFE_RELEASE(pEnumerator)
    SAFE_RELEASE(pDevice)
}

// Destructor
AudioVolumeEvents::~AudioVolumeEvents()
{
    if (_pControl != NULL)
    {
        _pControl->UnregisterAudioSessionNotification(_pAudioEvents);
    }
    SAFE_RELEASE(_pManager)
    SAFE_RELEASE(_pControl)
    SAFE_RELEASE(_pAudioEvents)
};
```



The preceding code example implements a class named AudioVolumeEvents. During program initialization, the audio application enables audio-event notifications by creating an AudioVolumeEvents object. The constructor for this class takes three input parameters:

-   *flow*—the data-flow direction of the [audio endpoint device](audio-endpoint-devices.md) (an [**EDataFlow**](/windows/win32/api/mmdeviceapi/ne-mmdeviceapi-edataflow) enumeration value).
-   *role*—the current [device role](device-roles.md) of the endpoint device (an [**ERole**](/windows/win32/api/mmdeviceapi/ne-mmdeviceapi-erole) enumeration value).
-   *pAudioEvents*—pointer to an object (an [**IAudioSessionEvents**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionevents) interface instance) that contains a set of callback routines that are implemented by the application.

The constructor supplies the flow and role values as input parameters to the [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint) method. The method creates an [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) object that encapsulates the audio endpoint device with the specified data-flow direction and device role.

The application implements the object pointed to by *pAudioEvents*. (The implementation is not shown in the preceding code example. For a code example that implements an **IAudioSessionEvents** interface, see [Audio Session Events](audio-session-events.md).) Each method in this interface receives notifications of a particular type of audio event. If the application is not interested in a particular event type, then the method for that event type should do nothing but return S\_OK.

The [**IAudioSessionEvents::OnSimpleVolumeChanged**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessionevents-onsimplevolumechanged) method receives notifications of volume changes. Typically, this method updates the application's volume slider.

In the preceding code example, the constructor for the AudioVolumeEvents class registers for notifications on the process-specific [audio session](audio-sessions.md) that is identified by session GUID value GUID\_NULL. By default, legacy audio APIs such as DirectSound, DirectShow, and the **waveOutXxx** functions assign their streams to this session. However, a DirectSound or DirectShow application can, as an option, override the default behavior and assign its streams to a cross-process session or to a session that is identified by a GUID value other than GUID\_NULL. (No mechanism is currently provided for a **waveOutXxx** application to override the default behavior in a similar manner.) For a code example of a DirectShow application with this behavior, see [Device Roles for DirectShow Applications](device-roles-for-directshow-applications.md). To accommodate such an application, you can modify the constructor in the preceding code example to accept two additional input parameters—a session GUID and a flag to indicate whether the session that is to be monitored is a cross-process or process-specific session. Pass these parameters to the call to the [**IAudioSessionManager::GetAudioSessionControl**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessionmanager-getaudiosessioncontrol) method in the constructor.

After the constructor calls the [**IAudioSessionControl::RegisterAudioSessionNotification**](/windows/desktop/api/Audiopolicy/nf-audiopolicy-iaudiosessioncontrol-registeraudiosessionnotification) method to register for notifications, the application continues to receive notifications for only as long as either the [**IAudioSessionControl**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessioncontrol) or [**IAudioSessionManager**](/windows/desktop/api/Audiopolicy/nn-audiopolicy-iaudiosessionmanager) interface exists. The AudioVolumeEvents object in the preceding code example holds references to these interfaces until its destructor is called. This behavior ensures that the application will continue to receive notifications for the lifetime of the AudioVolumeEvents object.

Instead of implicitly selecting an audio device based on its device role, a DirectSound or legacy Windows multimedia application might allow the user to explicitly select a device from a list of available devices that are identified by their friendly names. To support this behavior, the preceding code example must be modified to generate audio-event notifications for the selected device. Two modifications are required. First, change the constructor definition to accept an [endpoint ID string](endpoint-id-strings.md) as an input parameter (in place of the flow and role parameters in the code example). This string identifies the audio endpoint device that corresponds to the selected DirectSound or legacy waveform device. Second, replace the call to the [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint) method with a call to the [**IMMDeviceEnumerator::GetDevice**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdevice) method. The **GetDevice** call takes the endpoint ID string as an input parameter and creates an instance of the endpoint device that is identified by the string.

The technique for obtaining the endpoint ID string for a DirectSound device or legacy waveform device is as follows.

First, during device enumeration, DirectSound supplies the endpoint ID string for each enumerated device. To begin device enumeration, the application passes a callback function pointer as an input parameter to the **DirectSoundCreate** or **DirectSoundCaptureCreate** function. The definition of the callback function is:


```C++
BOOL DSEnumCallback(
  LPGUID  lpGuid,
  LPCSTR  lpcstrDescription,
  LPCSTR  lpcstrModule,
  LPVOID  lpContext
);
```



In Windows Vista, the *lpcstrModule* parameter points to the endpoint ID string. (In earlier versions of Windows, including Windows Server 2003, Windows XP, and Windows 2000, the *lpcstrModule* parameter points to the name of the driver module for the device.) The *lpcstrDescription* parameter points to a string that contains the friendly name of the device. For more information about DirectSound device enumeration, see the Windows SDK documentation.

Second, to obtain the endpoint ID string for a legacy waveform device, use the **waveOutMessage** or **waveInMessage** function to send a DRV\_QUERYFUNCTIONINSTANCEID message to the waveform device driver. For a code example that shows the use of this message, see [Device Roles for Legacy Windows Multimedia Applications](device-roles-for-legacy-windows-multimedia-applications.md).

## Related topics

<dl> <dt>

[Interoperability with Legacy Audio APIs](interoperability-with-legacy-audio-apis.md)
</dt> </dl>

 

 



