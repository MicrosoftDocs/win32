---
description: Endpoint Volume Controls
ms.assetid: 667c3659-69ae-469d-9ae0-e32a189cbc71
title: Endpoint Volume Controls
ms.topic: article
ms.date: 05/31/2018
---

# Endpoint Volume Controls

The [**ISimpleAudioVolume**](/windows/desktop/api/Audioclient/nn-audioclient-isimpleaudiovolume), [**IChannelAudioVolume**](/windows/desktop/api/Audioclient/nn-audioclient-ichannelaudiovolume), and [**IAudioStreamVolume**](/windows/desktop/api/Audioclient/nn-audioclient-iaudiostreamvolume) interfaces enable clients to control the volume levels of [audio sessions](audio-sessions.md), which are collections of shared-mode audio streams. These interfaces do not work with exclusive-mode audio streams.

Applications that manage exclusive-mode streams can control the volume levels of those streams through the [**IAudioEndpointVolume**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolume) interface. This interface controls the volume level of the [audio endpoint device](audio-endpoint-devices.md). It uses the hardware volume control for the endpoint device if the audio hardware implements such a control. Otherwise, the **IAudioEndpointVolume** interface implements the volume control in software.

If a device has a hardware volume control, changes made to the control through the [**IAudioEndpointVolume**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolume) interface affect the volume level both in shared mode and in exclusive mode. If a device lacks hardware volume and mute controls, changes made to the software volume and mute controls through this interface affect the volume level in shared mode, but not in exclusive mode. In exclusive mode, the application and the audio hardware exchange audio data directly, bypassing the software controls.

As a general rule, applications should avoid using the [**IAudioEndpointVolume**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolume) interface to control the volume levels of shared-mode streams. Instead, applications should use the [**ISimpleAudioVolume**](/windows/desktop/api/Audioclient/nn-audioclient-isimpleaudiovolume), [**IChannelAudioVolume**](/windows/desktop/api/Audioclient/nn-audioclient-ichannelaudiovolume), or [**IAudioStreamVolume**](/windows/desktop/api/Audioclient/nn-audioclient-iaudiostreamvolume) interface for that purpose.

If an application displays a volume control that uses the [**IAudioEndpointVolume**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolume) interface to control the volume level of an audio endpoint device, that volume control should mirror the endpoint volume control displayed by the system volume-control program, Sndvol. As explained previously, the endpoint volume control appears on the left side of the Sndvol window, in the group box labeled **Device**. If the user changes the endpoint volume of a device through the volume control in Sndvol, the corresponding endpoint volume control in the application should move in unison with the control in Sndvol. Similarly, if the user changes the volume level through the endpoint volume control in the application window, the corresponding volume control in Sndvol should move in unison with the application's volume control.

To ensure that the endpoint volume control in an application window mirrors the endpoint volume control in Sndvol, the application should implement an [**IAudioEndpointVolumeCallback**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolumecallback) interface and register that interface to receive notifications. Thereafter, each time the user changes the endpoint volume level in Sndvol, the application receives a notification call through its [**IAudioEndpointVolumeCallback::OnNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolumecallback-onnotify) method. During this call, the **OnNotify** method can update the endpoint volume control in the application window to match the control setting shown in Sndvol. Similarly, each time the user changes the endpoint volume level through volume control in the application window, Sndvol receives a notification and immediately updates its endpoint volume control to display the new volume level.

The following code example is a header file that shows a possible implementation of the [**IAudioEndpointVolumeCallback**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolumecallback) interface:


```C++
// Epvolume.h -- Implementation of IAudioEndpointVolumeCallback interface

#include <windows.h>
#include <commctrl.h>
#include <mmdeviceapi.h>
#include <endpointvolume.h>
#include "resource.h"

// Dialog handle from dialog box procedure
extern HWND g_hDlg;

// Client's proprietary event-context GUID
extern GUID g_guidMyContext;

// Maximum volume level on trackbar
#define MAX_VOL  100

#define SAFE_RELEASE(punk)  \
              if ((punk) != NULL)  \
                { (punk)->Release(); (punk) = NULL; }

//-----------------------------------------------------------
// Client implementation of IAudioEndpointVolumeCallback
// interface. When a method in the IAudioEndpointVolume
// interface changes the volume level or muting state of the
// endpoint device, the change initiates a call to the
// client's IAudioEndpointVolumeCallback::OnNotify method.
//-----------------------------------------------------------
class CAudioEndpointVolumeCallback : public IAudioEndpointVolumeCallback
{
    LONG _cRef;

public:
    CAudioEndpointVolumeCallback() :
        _cRef(1)
    {
    }

    ~CAudioEndpointVolumeCallback()
    {
    }

    // IUnknown methods -- AddRef, Release, and QueryInterface

    ULONG STDMETHODCALLTYPE AddRef()
    {
        return InterlockedIncrement(&_cRef);
    }

    ULONG STDMETHODCALLTYPE Release()
    {
        ULONG ulRef = InterlockedDecrement(&_cRef);
        if (0 == ulRef)
        {
            delete this;
        }
        return ulRef;

    }

    HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, VOID **ppvInterface)
    {
        if (IID_IUnknown == riid)
        {
            AddRef();
            *ppvInterface = (IUnknown*)this;
        }
        else if (__uuidof(IAudioEndpointVolumeCallback) == riid)
        {
            AddRef();
            *ppvInterface = (IAudioEndpointVolumeCallback*)this;
        }
        else
        {
            *ppvInterface = NULL;
            return E_NOINTERFACE;
        }
        return S_OK;
    }

    // Callback method for endpoint-volume-change notifications.

    HRESULT STDMETHODCALLTYPE OnNotify(PAUDIO_VOLUME_NOTIFICATION_DATA pNotify)
    {
        if (pNotify == NULL)
        {
            return E_INVALIDARG;
        }
        if (g_hDlg != NULL && pNotify->guidEventContext != g_guidMyContext)
        {
            PostMessage(GetDlgItem(g_hDlg, IDC_CHECK_MUTE), BM_SETCHECK,
                        (pNotify->bMuted) ? BST_CHECKED : BST_UNCHECKED, 0);

            PostMessage(GetDlgItem(g_hDlg, IDC_SLIDER_VOLUME),
                        TBM_SETPOS, TRUE,
                        LPARAM((UINT32)(MAX_VOL*pNotify->fMasterVolume + 0.5)));
        }
        return S_OK;
    }
};
```



The CAudioEndpointVolumeCallback class in the preceding code example is an implementation of the [**IAudioEndpointVolumeCallback**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolumecallback) interface. Because **IAudioEndpointVolumeCallback** inherits from [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown), the class definition contains implementations of the **IUnknown** methods [**AddRef**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-addref), [**Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release), and [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)). The [**OnNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolumecallback-onnotify) method in the class definition is called each time one of the following methods changes the endpoint volume level:

-   [**IAudioEndpointVolume::SetChannelVolumeLevel**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-setchannelvolumelevel)
-   [**IAudioEndpointVolume::SetChannelVolumeLevelScalar**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-setchannelvolumelevelscalar)
-   [**IAudioEndpointVolume::SetMasterVolumeLevel**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-setmastervolumelevel)
-   [**IAudioEndpointVolume::SetMasterVolumeLevelScalar**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-setmastervolumelevelscalar)
-   [**IAudioEndpointVolume::SetMute**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-setmute)
-   [**IAudioEndpointVolume::VolumeStepDown**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-volumestepdown)
-   [**IAudioEndpointVolume::VolumeStepUp**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-volumestepup)

The implementation of the [**OnNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolumecallback-onnotify) method in the preceding code example sends messages to the volume control in the application window to update the displayed volume level.

An application calls the [**IAudioEndpointVolume::RegisterControlChangeNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-registercontrolchangenotify) method to register its [**IAudioEndpointVolumeCallback**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolumecallback) interface to receive notifications. When the application no longer requires notifications, it calls the [**IAudioEndpointVolume::UnregisterControlChangeNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-unregistercontrolchangenotify) method to delete the registration.

The following code example is a Windows application that calls the [**RegisterControlChangeNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-registercontrolchangenotify) and [**UnregisterControlChangeNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-unregistercontrolchangenotify) methods to register and unregister the CAudioEndpointVolumeCallback class in the preceding code example:


```C++
// Epvolume.cpp -- WinMain and dialog box functions

#include "stdafx.h"
#include "Epvolume.h"

HWND g_hDlg = NULL;
GUID g_guidMyContext = GUID_NULL;

static IAudioEndpointVolume *g_pEndptVol = NULL;
static BOOL CALLBACK DlgProc(HWND, UINT, WPARAM, LPARAM);

#define EXIT_ON_ERROR(hr)  \
              if (FAILED(hr)) { goto Exit; }
#define ERROR_CANCEL(hr)  \
              if (FAILED(hr)) {  \
                  MessageBox(hDlg, TEXT("The program will exit."),  \
                             TEXT("Fatal error"), MB_OK);  \
                  EndDialog(hDlg, TRUE); return TRUE; }

//-----------------------------------------------------------
// WinMain -- Registers an IAudioEndpointVolumeCallback
//   interface to monitor endpoint volume level, and opens
//   a dialog box that displays a volume control that will
//   mirror the endpoint volume control in SndVol.
//-----------------------------------------------------------
int APIENTRY WinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR lpCmdLine,
                     int nCmdShow)
{
    HRESULT hr = S_OK;
    IMMDeviceEnumerator *pEnumerator = NULL;
    IMMDevice *pDevice = NULL;
    CAudioEndpointVolumeCallback EPVolEvents;

    if (hPrevInstance)
    {
        return 0;
    }

    CoInitialize(NULL);

    hr = CoCreateGuid(&g_guidMyContext);
    EXIT_ON_ERROR(hr)

    // Get enumerator for audio endpoint devices.
    hr = CoCreateInstance(__uuidof(MMDeviceEnumerator),
                          NULL, CLSCTX_INPROC_SERVER,
                          __uuidof(IMMDeviceEnumerator),
                          (void**)&pEnumerator);
    EXIT_ON_ERROR(hr)

    // Get default audio-rendering device.
    hr = pEnumerator->GetDefaultAudioEndpoint(eRender, eConsole, &pDevice);
    EXIT_ON_ERROR(hr)

    hr = pDevice->Activate(__uuidof(IAudioEndpointVolume),
                           CLSCTX_ALL, NULL, (void**)&g_pEndptVol);
    EXIT_ON_ERROR(hr)

    hr = g_pEndptVol->RegisterControlChangeNotify(
                     (IAudioEndpointVolumeCallback*)&EPVolEvents);
    EXIT_ON_ERROR(hr)

    InitCommonControls();
    DialogBox(hInstance, L"VOLUMECONTROL", NULL, (DLGPROC)DlgProc);

Exit:
    if (FAILED(hr))
    {
        MessageBox(NULL, TEXT("This program requires Windows Vista."),
                   TEXT("Error termination"), MB_OK);
    }
    if (g_pEndptVol != NULL)
    {
        g_pEndptVol->UnregisterControlChangeNotify(
                    (IAudioEndpointVolumeCallback*)&EPVolEvents);
    }
    SAFE_RELEASE(pEnumerator)
    SAFE_RELEASE(pDevice)
    SAFE_RELEASE(g_pEndptVol)
    CoUninitialize();
    return 0;
}

//-----------------------------------------------------------
// DlgProc -- Dialog box procedure
//-----------------------------------------------------------

BOOL CALLBACK DlgProc(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    HRESULT hr;
    BOOL bMute;
    float fVolume;
    int nVolume;
    int nChecked;

    switch (message)
    {
    case WM_INITDIALOG:
        g_hDlg = hDlg;
        SendDlgItemMessage(hDlg, IDC_SLIDER_VOLUME, TBM_SETRANGEMIN, FALSE, 0);
        SendDlgItemMessage(hDlg, IDC_SLIDER_VOLUME, TBM_SETRANGEMAX, FALSE, MAX_VOL);
        hr = g_pEndptVol->GetMute(&bMute);
        ERROR_CANCEL(hr)
        SendDlgItemMessage(hDlg, IDC_CHECK_MUTE, BM_SETCHECK,
                           bMute ? BST_CHECKED : BST_UNCHECKED, 0);
        hr = g_pEndptVol->GetMasterVolumeLevelScalar(&fVolume);
        ERROR_CANCEL(hr)
        nVolume = (int)(MAX_VOL*fVolume + 0.5);
        SendDlgItemMessage(hDlg, IDC_SLIDER_VOLUME, TBM_SETPOS, TRUE, nVolume);
        return TRUE;

    case WM_HSCROLL:
        switch (LOWORD(wParam))
        {
        case SB_THUMBPOSITION:
        case SB_THUMBTRACK:
        case SB_LINERIGHT:
        case SB_LINELEFT:
        case SB_PAGERIGHT:
        case SB_PAGELEFT:
        case SB_RIGHT:
        case SB_LEFT:
            // The user moved the volume slider in the dialog box.
            SendDlgItemMessage(hDlg, IDC_CHECK_MUTE, BM_SETCHECK, BST_UNCHECKED, 0);
            hr = g_pEndptVol->SetMute(FALSE, &g_guidMyContext);
            ERROR_CANCEL(hr)
            nVolume = SendDlgItemMessage(hDlg, IDC_SLIDER_VOLUME, TBM_GETPOS, 0, 0);
            fVolume = (float)nVolume/MAX_VOL;
            hr = g_pEndptVol->SetMasterVolumeLevelScalar(fVolume, &g_guidMyContext);
            ERROR_CANCEL(hr)
            return TRUE;
        }
        break;

    case WM_COMMAND:
        switch ((int)LOWORD(wParam))
        {
        case IDC_CHECK_MUTE:
            // The user selected the Mute check box in the dialog box.
            nChecked = SendDlgItemMessage(hDlg, IDC_CHECK_MUTE, BM_GETCHECK, 0, 0);
            bMute = (BST_CHECKED == nChecked);
            hr = g_pEndptVol->SetMute(bMute, &g_guidMyContext);
            ERROR_CANCEL(hr)
            return TRUE;
        case IDCANCEL:
            EndDialog(hDlg, TRUE);
            return TRUE;
        }
        break;
    }
    return FALSE;
}
```



In the preceding code example, the [**WinMain**](/windows/desktop/api/winbase/nf-winbase-winmain) function calls the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) function to create an instance of the [**IMMDeviceEnumerator**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator) interface, and it calls the [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint) method to obtain the [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface of the default rendering device. **WinMain** calls the [**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate) method to obtain the device's [**IAudioEndpointVolume**](/windows/desktop/api/Endpointvolume/nn-endpointvolume-iaudioendpointvolume) interface, and it calls [**RegisterControlChangeNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-registercontrolchangenotify) to register the application to receive notifications of endpoint volume changes. Next, **WinMain** opens a dialog box to display an endpoint volume control for the device. The dialog box also displays a check box that indicates whether the device is muted. The endpoint volume control and mute check box in the dialog box mirror the settings of the endpoint volume control and mute check box displayed by Sndvol. For more information about **WinMain** and **CoCreateInstance**, see the Windows SDK documentation. For more information about **IMMDeviceEnumerator** and **IMMDevice**, see [Enumerating Audio Devices](enumerating-audio-devices.md).

The dialog box procedure, DlgProc, in the preceding code example, handles the changes that the user makes to the volume and mute settings through the controls in the dialog box. When DlgProc calls [**SetMasterVolumeLevelScalar**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-setmastervolumelevelscalar) or [**SetMute**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-setmute), Sndvol receives notification of the change and updates the corresponding control in its window to reflect the new volume or mute setting. If, instead of using the dialog box, the user updates the volume and mute settings through the controls in the Sndvol window, the [**OnNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolumecallback-onnotify) method in the CAudioEndpointVolumeCallback class updates the controls in the dialog box to display the new settings.

If the user changes the volume through the controls in the dialog box, the [**OnNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolumecallback-onnotify) method in the CAudioEndpointVolumeCallback class does not send messages to update the controls in the dialog box. To do so would be redundant. **OnNotify** updates the controls in the dialog box only if the volume change originated in Sndvol or in some other application. The second parameter in the [**SetMasterVolumeLevelScalar**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-setmastervolumelevelscalar) and [**SetMute**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-setmute) method calls in the DlgProc function is a pointer to an event-context GUID that either method passes to **OnNotify**. **OnNotify** checks the value of the event-context GUID to determine whether the dialog box is the source of the volume change. For more information about event-context GUIDs, see **IAudioEndpointVolumeCallback::OnNotify**.

When the user exits the dialog box, the [**UnregisterControlChangeNotify**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-unregistercontrolchangenotify) call in the preceding code example deletes the registration of the CAudioEndpointVolumeCallback class before the program terminates.

You can easily modify the preceding code example to display volume and mute controls for the default capture device. In the [**WinMain**](/windows/desktop/api/winbase/nf-winbase-winmain) function, change the value of the first parameter in the call to the [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint) method from eRender to eCapture.

The following code example is the resource script that defines the volume and mute controls that appear in the preceding code example:


```C++
// Epvolume.rc -- Resource script

#include "resource.h"
#include "windows.h"
#include "commctrl.h"

//
// Dialog box
//
VOLUMECONTROL DIALOGEX 0, 0, 160, 60
STYLE DS_MODALFRAME | WS_CAPTION | WS_SYSMENU | DS_SETFONT
CAPTION "Audio Endpoint Volume"
FONT 8, "Arial Rounded MT Bold", 400, 0, 0x0
BEGIN
    LTEXT      "Min",IDC_STATIC_MINVOL,10,10,20,12
    RTEXT      "Max",IDC_STATIC_MAXVOL,130,10,20,12
    CONTROL    "",IDC_SLIDER_VOLUME,"msctls_trackbar32",
               TBS_BOTH | TBS_NOTICKS | WS_TABSTOP,10,20,140,12
    CONTROL    "Mute",IDC_CHECK_MUTE,"Button",
               BS_AUTOCHECKBOX | WS_TABSTOP,20,40,70,12
END
```



The following code example is the resource header file that defines the control identifiers that appear in the preceding code examples:


```C++
// Resource.h -- Control identifiers (epvolume)

#define IDC_SLIDER_VOLUME      1001
#define IDC_CHECK_MUTE         1002
#define IDC_STATIC_MINVOL      1003
#define IDC_STATIC_MAXVOL      1004
```



The preceding code examples combine to form a simple application for controlling and monitoring the endpoint volume of the default rendering device. A more useful application might additionally notify the user when the status of the device changes. For example, the device might be disabled, unplugged, or removed. For more information about monitoring these types of events, see [Device Events](device-events.md).

## Related topics

<dl> <dt>

[Volume Controls](volume-controls.md)
</dt> </dl>

 

 
