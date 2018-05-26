---
Description: Custom exit modules must implement the ICertExit interface, which is called by the server engine.
ms.assetid: 509e7945-b656-4c4c-b5eb-45fbe80377c7
title: Writing Custom Exit Modules
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Writing Custom Exit Modules

Custom exit modules must implement the [**ICertExit**](/windows/win32/Certexit/nn-certexit-icertexit?branch=master) interface, which is called by the server engine. The [**ICertExit::Initialize**](/windows/win32/Certexit/nf-certexit-icertexit-initialize?branch=master) method is called by the server engine when the exit module is loaded. It allows the exit module to perform initialization and returns a value that informs the server engine of the kinds of events for which it wants notification. The [**ICertExit::GetDescription**](/windows/win32/Certexit/nf-certexit-icertexit-getdescription?branch=master) method must return a description string when the server engine requests it. The [**ICertExit::Notify**](/windows/win32/Certexit/nf-certexit-icertexit-notify?branch=master) method is called by the server engine to notify the exit module that an event has occurred.

Exit modules can call the [**ICertServerExit**](/windows/win32/Certif/nn-certif-icertserverexit?branch=master) interface, which supports many of the same methods as the [**ICertServerPolicy**](/windows/win32/Certif/nn-certif-icertserverpolicy?branch=master) interface, with the exception of the [**SetCertificateExtension**](/windows/win32/Certif/nf-certif-icertserverpolicy-setcertificateextension?branch=master) and [**SetCertificateProperty**](/windows/win32/Certif/nf-certif-icertserverpolicy-setcertificateproperty?branch=master) methods.

For information about removing the existing exit module and installing a new one, see the Exit Module Customization topic in Help.

 

 



