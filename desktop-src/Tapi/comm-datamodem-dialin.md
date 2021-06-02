---
description: comm/datamodem/dialin
ms.assetid: 7330db08-5064-47c9-9d28-c5b2b15c3ac6
title: comm/datamodem/dialin
ms.topic: article
ms.date: 05/31/2018
---

# comm/datamodem/dialin

The **comm/datamodem/dialin** device class consists of datamodem devices used only for incoming calls. This class replaces the [**comm/datamodem**](comm-datamodem.md) class on Windows 2000 and later operating systems.

Before Windows 2000, the Unimodem TSP only supported the [**comm/datamodem**](comm-datamodem.md) device class. Unexpected behavior may occur when an application dialing an outbound call changes the configuration set by a service waiting for an incoming call. Applications using Windows 2000 and later operating systems should specify either **comm/datamodem/dialin** or [**comm/datamodem/dialout**](comm-datamodem-dialout.md) in calls to [**lineConfigDialog**](/windows/desktop/api/Tapi/nf-tapi-lineconfigdialog) or [**lineSetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig). This enables Unimodem to maintain a dial-in configuration independent of the dial-out configuration.

While **comm/datamodem/dialin** is used by Unimodem on Windows 2000 and later, it may also be used by other TSPs on any platform. Applications that must run on all platforms should first use **comm/datamodem/dialin** in calls to APIs that require a device class and only use [**comm/datamodem**](comm-datamodem.md) if the API returns **LINEERR\_INVALCALLSTATE**.

The Unimodem Service Provider translates the [**comm/datamodem**](comm-datamodem.md) device class in calls to [**lineConfigDialog**](/windows/desktop/api/Tapi/nf-tapi-lineconfigdialog) and [**lineSetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig) to either **comm/datamodem/dialin** or [**comm/datamodem/dialout**](comm-datamodem-dialout.md) as follows:

-   Windows 2000 and later:
    -   If **NULL** is specified in the *lpszDeviceClass* parameter in the call to [**lineConfigDialog**](/windows/desktop/api/Tapi/nf-tapi-lineconfigdialog), Unimodem assumes **comm/datamodem/dialin**. If [**comm/datamodem**](comm-datamodem.md) or [**tapi/line**](tapi-line.md) is specified in the call to **lineConfigDialog**, Unimodem translates this to [**comm/datamodem/dialout**](comm-datamodem-dialout.md).
    -   In the call to [**lineSetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig) or [**lineGetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linegetdevconfig), [**comm/datamodem**](comm-datamodem.md) is handled as [**comm/datamodem/dialout**](comm-datamodem-dialout.md). **NULL** indicates an invalid device class.
-   Before Windows 2000:
    -   If either **NULL** or [**tapi/line**](tapi-line.md) is specified in [**lineConfigDialog**](/windows/desktop/api/Tapi/nf-tapi-lineconfigdialog), Unimodem assumes [**comm/datamodem**](comm-datamodem.md).

The **comm/datamodem/dialin** class uses the structures and configurations described in the [**comm/datamodem**](comm-datamodem.md) device class.

 

 



