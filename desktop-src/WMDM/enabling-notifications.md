---
title: Enabling Notifications
description: Enabling Notifications
ms.assetid: b4fc7714-a7d0-409f-a47c-4903bab883cc
keywords:
- Windows Media Device Manager,notifications
- Device Manager,notifications
- programming guide,notifications
- desktop applications,notifications
- creating Windows Media Device Manager applications,notifications
- notifications
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Notifications

Windows Media Device Manager declares four interfaces that an application can implement in a COM class to receive event notifications. These interfaces fall into two groups, as shown in the following table.



| Interfaces                                                                                                                                                | Description                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMDMNotification**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmnotification)                                                                                                            | Notifies the application when devices or storage media are connected or disconnected.                                                                                         |
| [**IWMDMProgress**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmprogress)<br/> [**IWMDMProgress2**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmprogress2)<br/> [**IWMDMProgress3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmprogress3)<br/> | A very simple notification system to alert an application about the progress of any event. The application is not required to take any actions in response to these messages. |



 

**IWMDMNotification**

**IWMDMNotification** alerts the application when Plug and Play devices are connected or disconnected from the computer, as well as when Plug and Play storage media (such as flash cards) are inserted or removed from the device. These notifications can help the application update its user interface to reflect changes.

In order to receive these notifications, your application must register to receive them using the Platform SDK **IConnectionPointContainer** and **IConnectionPoint** interfaces. Your application should register to receive events when it starts up, and unregister when it closes. Follow these steps to register to receive these notifications.

1.  Query the main **IWMDeviceManager** interface you received when you authenticated your application for **IConnectionPointContainer**.
2.  Call **IConnectionPointContainer::FindConnectionPoint** to retrieve a container connection point for **IWMDMNotification** interfaces.
3.  Register to receive events by calling **IConnectionPoint::Advise**. Pass in the class that implements **IWMDMNotification**, and retrieve a cookie, a unique ID that identifies your connection point. This must be stored, and used later to unregister for event notifications.

The following C++ code demonstrates how you can register to receive notifications from **IWMDMNotification**.


```C++
HRESULT CWMDMController::RegisterForNotifications()
{
    HRESULT hr = S_OK;
    CComPtr<IConnectionPointContainer> pConxnPointCont;
    CComPtr<IConnectionPoint> pIConnPoint;

    // Get the IConnectionPointContainer interface from IWMDeviceManager.
    if (SUCCEEDED (hr = m_IWMDMDeviceMgr->QueryInterface(IID_IConnectionPointContainer, (void**) & pConxnPointCont)))
    {
        // Get a connection point from the container.
        if (SUCCEEDED (hr = pConxnPointCont->FindConnectionPoint(IID_IWMDMNotification, &pIConnPoint)))
        {
            // Add ourselves as a callback handler for the connection point.
            // If we succeeded, indicate that by storing the connection point ID.
            DWORD dwCookie;
            if (SUCCEEDED (hr = pIConnPoint->Advise((IUnknown*)((IWMDMNotification*)this), &dwCookie)))
            {
                m_dwNotificationCookie = dwCookie;
            }
        }
    }

    return hr;
}
```



When your application closes, you must unregister with **IConnectionPoint** to indicate that it should no longer send you notifications. Follow these steps to unregister for notifications:

1.  Query the main **IWMDeviceManager** interface for **IConnectionPointContainer**.
2.  Get a connection point for **IWMDMNotification** interfaces.
3.  Unregister your application for event notifications by calling **IConnectionPoint::Unadvise**, passing in the unique ID received when you registered to receive events.

The following C++ code shows how to unregister for **IWMDMNotification** events when your application closes.


```C++
HRESULT CWMDMController::UnregisterForNotifications()
{
    HRESULT hr = S_FALSE;

    // On class initialization, we initialized the handle to -1 as a flag 
    // to indicate we had not yet registered for notifications. If registration 
    // never happened, don't bother to unregister.
    if (-1 != m_dwNotificationCookie)
    {
        CComPtr<IConnectionPointContainer> pConxnPointCont;
        CComPtr<IConnectionPoint> pIConnPoint;

        // Get the connection point container from IWMDeviceManager. 
        if (SUCCEEDED (hr = 
           m_IWMDMDeviceMgr->QueryInterface(IID_IConnectionPointContainer,
           (void**) & pConxnPointCont)))
        {
            // Get a connection point from the container.
            if (SUCCEEDED (hr = pConxnPointCont->FindConnectionPoint(IID_IWMDMNotification, &pIConnPoint)))
            {
                // Remove ourselves as a callback from the connection point.
                // If successful, reset the ID to a flag value.
                if (SUCCEEDED (hr = 
                    pIConnPoint->Unadvise(m_dwNotificationCookie)))
                {
                    m_dwNotificationCookie = -1;
                    hr = S_OK;
                }
            }
        }
    }

    return hr;
}
```



**Using IWMDMProgress**

Windows Media Device Manager can send your application status messages when specific actions, such as content transfer, secure clock acquisition, and encountering DRM file information, occur. Your application can use these messages to monitor the status of the event or cancel an event. To use this interface, implement [**IWMDMProgress**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmprogress), [**IWMDMProgress2**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmprogress2), or [**IWMDMProgress3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmprogress3), and pass it in as a parameter to a method that will accept a progress message. Note that **IWMDMProgress3** is the superior interface because it provides an identification GUID that specifies what action is being tracked. The following application methods accept a progress interface (the corresponding service provider methods should be able to send notifications to a submitted interface):

[**IWMDMStorageControl::Delete**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol-delete)

[**IWMDMStorageControl::Insert**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol-insert)

[**IWMDMStorageControl::Move**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol-move)

[**IWMDMStorageControl::Read**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol-read)

[**IWMDMStorageControl::Rename**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol-rename)

[**IWMDMStorageControl2::Insert2**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol2-insert2)

[**IWMDMStorageControl3::Insert3**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol3-insert3)

[**IWMDMStorageGlobals::Initialize**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorageglobals-initialize)

[**IWMDRMDeviceApp::AcquireDeviceData**](iwmdrmdeviceapp-acquiredevicedata.md)

Examples of passing an interface into a method are given in the documentation for these methods. For examples of implementing the callback interfaces, see the documentation for the methods of **IWMDMProgress**, **IWMDMProgress2**, or **IWMDMProgress3**.

## Related topics

<dl> <dt>

[**Creating a Windows Media Device Manager Application**](creating-a-windows-media-device-manager-application.md)
</dt> </dl>

 

 





