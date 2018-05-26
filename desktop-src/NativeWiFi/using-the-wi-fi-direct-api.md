---
Description: Shows how to use Wi-Fi Direct functions in desktop apps.
ms.assetid: 50B95B7D-B860-44DF-8E78-1E7D2DC5A9B6
title: Using the Wi-Fi Direct functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Wi-Fi Direct functions

This topics shows how to use Wi-Fi Direct functions in desktop apps. Starting on Windows 8 and Windows Server 2012, Wi-Fi Direct functions were added to the Native Wifi API.

The Wi-Fi Direct feature is based on the development of the Wi-Fi Peer-to-Peer Technical Specification v1.1 by the Wi-Fi Alliance (see [Wi-Fi Alliance Published Specifications](http://go.microsoft.com/fwlink/p/?linkid=253656)). The goal of the Wi-Fi Peer-to-Peer Technical Specification is to provide a solution for Wi-Fi device-to-device connectivity without the need for either a Wireless Access Point (wireless AP) to setup the connection or the use of the existing Wi-Fi ad hoc (IBSS) mechanism.

> [!Note]  
> Ad hoc mode might not be available in future versions of Windows. Starting with Windows 8.1 and Windows Server 2012 R2, use Wi-Fi Direct instead.

 

The following functions support the Wi-Fi Direct feature.

-   [**WFDCancelOpenSession**](/windows/win32/wlanapi/nf-wlanapi-wfdcancelopensession?branch=master) - Indicates that the app wants to cancel a pending [**WFDStartOpenSession**](/windows/win32/wlanapi/nf-wlanapi-wfdstartopensession?branch=master) function that has not completed.
-   [**WFDCloseHandle**](/windows/win32/wlanapi/nf-wlanapi-wfdclosehandle?branch=master) - Closes a handle to the Wi-Fi Direct service.
-   [**WFDCloseSession**](/windows/win32/wlanapi/nf-wlanapi-wfdclosesession?branch=master) - Closes a session after a previously successful call to the [**WFDStartOpenSession**](/windows/win32/wlanapi/nf-wlanapi-wfdstartopensession?branch=master) function.
-   [**WFDOpenHandle**](/windows/win32/wlanapi/nf-wlanapi-wfdopenhandle?branch=master) - Opens a handle to the Wi-Fi Direct service and negotiates a version of the Wi-FI Direct API to use.
-   [**WFDOpenLegacySession**](/windows/win32/wlanapi/nf-wlanapi-wfdopenlegacysession?branch=master) - Retrieves and applies a stored profile for a Wi-Fi Direct legacy device.
-   [**WFDStartOpenSession**](/windows/win32/wlanapi/nf-wlanapi-wfdstartopensession?branch=master) - Starts an on-demand connection to a specific Wi-Fi Direct device, which has been previously paired through the Windows Pairing experience.
-   [**WFDUpdateDeviceVisibility**](/windows/win32/wlanapi/nf-wlanapi-wfdupdatedevicevisibility?branch=master) - Updates device visibility for the Wi-Fi Direct device address for a given installed Wi-Fi Direct device node.
-   [**WFD\_OPEN\_SESSION\_COMPLETE\_CALLBACK**](/windows/win32/wlanapi/nc-wlanapi-wfd_open_session_complete_callback?branch=master) - Defines the callback function that is called by the [**WFDStartOpenSession**](/windows/win32/wlanapi/nf-wlanapi-wfdstartopensession?branch=master) function when the **WFDStartOpenSession** operation completes

For a desktop app, the Wi-Fi Direct feature requires that Wi-FI Direct devices be previously paired by the user with the Windows Pairing experience user interface. Once this pairing is completed, a profile is stored that allows the Wi-Fi Direct functions to be used to start a Wi-Fi Direct session to establish a connection between the Wi-Fi Direct devices.

In order to use Wi-Fi Direct, an app must first obtain a handle to the Wi-Fi Direct service by calling the [**WFDOpenHandle**](/windows/win32/wlanapi/nf-wlanapi-wfdopenhandle?branch=master) function. The Wi-Fi Direct (WFD) handle returned by the **WFDOpenHandle** function is used for subsequent Wi-Fi Direct function calls made to the Wi-Fi Direct service.

The [**WFDStartOpenSession**](/windows/win32/wlanapi/nf-wlanapi-wfdstartopensession?branch=master) function starts an asynchronous operation to start an on-demand connection to a specific Wi-Fi Direct device. The target Wi-Fi device must previously have been paired through the Windows Pairing experience. When the asynchronous operation completes, the callback function specified in the *pfnCallback* parameter is called.

Once an application is done using the Wi-Fi Direct service, the application should call the [**WFDCloseHandle**](/windows/win32/wlanapi/nf-wlanapi-wfdclosehandle?branch=master) function to signal to the Wi-Fi Direct service that the application is done using the service. This allows the Wi-Fi Direct service to release resources used by the application.

For more information on Wi-Fi Direct for use in Windows Store apps, see [**PeerFinder**](w_net_prox.peerfinder) and related classes in the [**Windows.Networking.Proximity**](w_net_prox.windows_networking_proximity) namespace.

## Related topics

<dl> <dt>

**Other resources**
</dt> <dt>

[About Native Wifi](about-native-wifi.md)
</dt> <dt>

[About the Native Wifi API](about-the-native-wifi-api.md)
</dt> <dt>

[About the Wi-Fi Direct feature](about-the-wi-fi-direct-api.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**PeerFinder**](w_net_prox.peerfinder)
</dt> <dt>

[**WFD\_OPEN\_SESSION\_COMPLETE\_CALLBACK**](/windows/win32/wlanapi/nc-wlanapi-wfd_open_session_complete_callback?branch=master)
</dt> <dt>

[**WFDCancelOpenSession**](/windows/win32/wlanapi/nf-wlanapi-wfdcancelopensession?branch=master)
</dt> <dt>

[**WFDCloseHandle**](/windows/win32/wlanapi/nf-wlanapi-wfdclosehandle?branch=master)
</dt> <dt>

[**WFDCloseSession**](/windows/win32/wlanapi/nf-wlanapi-wfdclosesession?branch=master)
</dt> <dt>

[**WFDOpenHandle**](/windows/win32/wlanapi/nf-wlanapi-wfdopenhandle?branch=master)
</dt> <dt>

[**WFDOpenLegacySession**](/windows/win32/wlanapi/nf-wlanapi-wfdopenlegacysession?branch=master)
</dt> <dt>

[**WFDStartOpenSession**](/windows/win32/wlanapi/nf-wlanapi-wfdstartopensession?branch=master)
</dt> <dt>

[**WFDUpdateDeviceVisibility**](/windows/win32/wlanapi/nf-wlanapi-wfdupdatedevicevisibility?branch=master)
</dt> <dt>

[**Windows.Networking.Proximity**](w_net_prox.windows_networking_proximity)
</dt> </dl>

 

 



