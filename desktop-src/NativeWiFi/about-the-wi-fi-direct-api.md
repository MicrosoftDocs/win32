---
description: The Native Wifi API contains a set of functions that support the use of Wi-Fi Direct for desktop apps.
ms.assetid: A649EBBA-1076-4426-9C4D-85AB8C415C66
title: About the Wi-Fi Direct feature
ms.topic: article
ms.date: 05/31/2018
---

# About the Wi-Fi Direct feature

The Native Wifi API contains a set of functions that support the use of Wi-Fi Direct for desktop apps. Starting on Windows 8 and Windows Server 2012, Wi-Fi Direct functions were added to the Native Wifi API.

The Wi-Fi Direct feature is based on the development of the Wi-Fi Peer-to-Peer Technical Specification v1.1 by the Wi-Fi Alliance (see [Wi-Fi Alliance Published Specifications](https://www.wi-fi.org/)). The goal of the Wi-Fi Peer-to-Peer Technical Specification is to provide a solution for Wi-Fi device-to-device connectivity without the need for either a Wireless Access Point (wireless AP) to setup the connection or the use of the existing Wi-Fi ad hoc (IBSS) mechanism.

> [!Note]  
> Ad hoc mode might not be available in future versions of Windows. Starting with Windows 8.1 and Windows Server 2012 R2, use Wi-Fi Direct instead.

 

For a desktop app, the Wi-Fi Direct feature requires that Wi-FI Direct devices be previously paired by the user with the Windows Pairing experience user interface. Once this pairing is completed, a profile is stored that allows the Wi-Fi Direct functions to be used to start a Wi-Fi Direct session to establish a connection between the Wi-Fi Direct devices.

The following functions support the Wi-Fi Direct feature.

-   [**WFDCancelOpenSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdcancelopensession) - Indicates that the app wants to cancel a pending [**WFDStartOpenSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdstartopensession) function that has not completed.
-   [**WFDCloseHandle**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdclosehandle) - Closes a handle to the Wi-Fi Direct service.
-   [**WFDCloseSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdclosesession) - Closes a session after a previously successful call to the [**WFDStartOpenSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdstartopensession) function.
-   [**WFDOpenHandle**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdopenhandle) - Opens a handle to the Wi-Fi Direct service and negotiates a version of the Wi-FI Direct API to use.
-   [**WFDOpenLegacySession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdopenlegacysession) - Retrieves and applies a stored profile for a Wi-Fi Direct legacy device.
-   [**WFDStartOpenSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdstartopensession) - Starts an on-demand connection to a specific Wi-Fi Direct device, which has been previously paired through the Windows Pairing experience.
-   [**WFDUpdateDeviceVisibility**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdupdatedevicevisibility) - Updates device visibility for the Wi-Fi Direct device address for a given installed Wi-Fi Direct device node.
-   [**WFD\_OPEN\_SESSION\_COMPLETE\_CALLBACK**](/windows/desktop/api/wlanapi/nc-wlanapi-wfd_open_session_complete_callback) - Defines the callback function that is called by the [**WFDStartOpenSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdstartopensession) function when the **WFDStartOpenSession** operation completes

For more information on using Wi-Fi Direct in a desktop app, see [Using the Wi-Fi Direct functions](using-the-wi-fi-direct-api.md).

For more information on Wi-Fi Direct for use in Windows Store apps, see [**PeerFinder**](/uwp/api/Windows.Networking.Proximity.PeerFinder) and related classes in the [**Windows.Networking.Proximity**](/uwp/api/Windows.Networking.Proximity) namespace.

## Related topics

<dl> <dt>

**Other resources**
</dt> <dt>

[About Native Wifi](about-native-wifi.md)
</dt> <dt>

[About the Native Wifi API](about-the-native-wifi-api.md)
</dt> <dt>

[About the Wireless Ad Hoc API](about-the-wireless-ad-hoc-api.md)
</dt> <dt>

[Using the Wi-Fi Direct functions](using-the-wi-fi-direct-api.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**PeerFinder**](/uwp/api/Windows.Networking.Proximity.PeerFinder)
</dt> <dt>

[**WFD\_OPEN\_SESSION\_COMPLETE\_CALLBACK**](/windows/desktop/api/wlanapi/nc-wlanapi-wfd_open_session_complete_callback)
</dt> <dt>

[**WFDCancelOpenSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdcancelopensession)
</dt> <dt>

[**WFDCloseHandle**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdclosehandle)
</dt> <dt>

[**WFDCloseSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdclosesession)
</dt> <dt>

[**WFDOpenHandle**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdopenhandle)
</dt> <dt>

[**WFDOpenLegacySession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdopenlegacysession)
</dt> <dt>

[**WFDStartOpenSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdstartopensession)
</dt> <dt>

[**WFDUpdateDeviceVisibility**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdupdatedevicevisibility)
</dt> <dt>

[**Windows.Networking.Proximity**](/uwp/api/Windows.Networking.Proximity)
</dt> </dl>

 

 
