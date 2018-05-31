---
Description: This topic describes how to register with the fax service.
ms.assetid: 797a4d48-7676-4b0d-93bf-ebe3043da4a0
title: Registration of a Fax Routing Extension
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registration of a Fax Routing Extension

To register with the fax service, it is recommended that a fax routing extension DLL perform the following steps.

## To install an extension and register

1.  Copy the fax routing extension DLL to the location specified by the *ImageName* parameter to the [**FaxRegisterRoutingExtension**](/previous-versions/windows/desktop/api/Winfax/) function.
2.  Call the [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera) function, specifying a **NULL** pointer in the *MachineName* parameter, to obtain a fax server handle to the local server.
3.  Call the [**FaxRegisterRoutingExtension**](/previous-versions/windows/desktop/api/Winfax/) function to register the fax routing extension DLL with the fax service. The function calls the [**FaxRoutingInstallationCallback**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfax_routing_installation_callbackw) function once for each fax routing method in the fax routing extension DLL.

If you install a fax routing extension by using a call to [**FaxRegisterRoutingExtension**](/previous-versions/windows/desktop/api/Winfax/), you must restart the fax service to use a fax routing method exported by that extension.

For information about developing a routing extension DLL, see [About the Fax Routing Extension API](-mfax-about-the-fax-routing-extension-api.md).

 

 



