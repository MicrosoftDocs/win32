---
description: Handling DVD Event Notifications
ms.assetid: 7a12aa36-f709-4ee2-aac6-45ab273ad3f9
title: Handling DVD Event Notifications
ms.topic: article
ms.date: 05/31/2018
---

# Handling DVD Event Notifications

The DVD Navigator sends notifications to an application-specified window when certain events take place, such as when the DVD domain changes, when a new parental management level is encountered, and when the DVD Navigator is about to enter an angle block. The event parameters can contain additional information related to the event. Error messages and warnings are also sent in this way. The application specifies the window that will handle the event notifications by using the [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex) pointer to call [**SetNotifyWindow**](/windows/desktop/api/Control/nf-control-imediaeventex-setnotifywindow), as follows:


```C++
const DWORD WM_DVD_EVENT = WM_USER + 100;
hr = m_pIME->SetNotifyWindow(reinterpret_cast<OAHWND>(m_hWnd), WM_DVD_EVENT, 0);
```



In the preceding example, m\_hWnd is the HWND of the window to receive the messages and WM\_DVD\_EVENT is the application-defined message (greater than WM\_USER) that will signal that a DVD event has taken place. The event itself is retrieved by the application through a call to [**IMediaEvent::GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent). Because more than one event might be in the event queue at any given time, the application must call **GetEvent** within a loop that repeats until all queued events have been retrieved, as shown in the following code example.


```C++
while (SUCCEEDED(m_pIME->GetEvent(&lEvent, &lParam1, &lParam2, lTimeOut)))
{
    HRESULT hr;
    switch (lEvent)
    {

    case EC_DVD_CURRENT_HMSF_TIME:
        {
            DVD_HMSF_TIMECODE *pTC = reinterpret_cast<DVD_HMSF_TIMECODE *>(&lParam1);
            m_CurTime = *pTC;
            ...
        }
        break;
        ...
    } // switch
}
```



DVD events might contain additional information in the *lParam1* or *lParam2* parameters, as illustrated above where the current time is contained in *lParam1*. The preceding code example is from the DVD sample application in Dvdcore.cpp. For a complete list of all DVD events and their parameters, see [DVD Event Notification Codes](dvd-notification-codes.md).

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



