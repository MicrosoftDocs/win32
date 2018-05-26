---
Description: This topic describes how to register with the fax service.
ms.assetid: 797a4d48-7676-4b0d-93bf-ebe3043da4a0
title: Registration of a Fax Routing Extension
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Registration of a Fax Routing Extension

To register with the fax service, it is recommended that a fax routing extension DLL perform the following steps.

## To install an extension and register

1.  Copy the fax routing extension DLL to the location specified by the *ImageName* parameter to the [**FaxRegisterRoutingExtension**](/windows/previous-versions/Winfax/?branch=master) function.
2.  Call the [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master) function, specifying a **NULL** pointer in the *MachineName* parameter, to obtain a fax server handle to the local server.
3.  Call the [**FaxRegisterRoutingExtension**](/windows/previous-versions/Winfax/?branch=master) function to register the fax routing extension DLL with the fax service. The function calls the [**FaxRoutingInstallationCallback**](/windows/previous-versions/Winfax/nc-winfax-pfax_routing_installation_callbackw?branch=master) function once for each fax routing method in the fax routing extension DLL.

If you install a fax routing extension by using a call to [**FaxRegisterRoutingExtension**](/windows/previous-versions/Winfax/?branch=master), you must restart the fax service to use a fax routing method exported by that extension.

For information about developing a routing extension DLL, see [About the Fax Routing Extension API](-mfax-about-the-fax-routing-extension-api.md).

 

 



