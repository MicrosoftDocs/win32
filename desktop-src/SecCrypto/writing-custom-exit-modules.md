---
description: Custom exit modules must implement the ICertExit interface, which is called by the server engine.
ms.assetid: 509e7945-b656-4c4c-b5eb-45fbe80377c7
title: Writing Custom Exit Modules
ms.topic: article
ms.date: 05/31/2018
---

# Writing Custom Exit Modules

Custom exit modules must implement the [**ICertExit**](/windows/desktop/api/Certexit/nn-certexit-icertexit) interface, which is called by the server engine. The [**ICertExit::Initialize**](/windows/desktop/api/Certexit/nf-certexit-icertexit-initialize) method is called by the server engine when the exit module is loaded. It allows the exit module to perform initialization and returns a value that informs the server engine of the kinds of events for which it wants notification. The [**ICertExit::GetDescription**](/windows/desktop/api/Certexit/nf-certexit-icertexit-getdescription) method must return a description string when the server engine requests it. The [**ICertExit::Notify**](/windows/desktop/api/Certexit/nf-certexit-icertexit-notify) method is called by the server engine to notify the exit module that an event has occurred.

Exit modules can call the [**ICertServerExit**](/windows/desktop/api/Certif/nn-certif-icertserverexit) interface, which supports many of the same methods as the [**ICertServerPolicy**](/windows/desktop/api/Certif/nn-certif-icertserverpolicy) interface, with the exception of the [**SetCertificateExtension**](/windows/desktop/api/Certif/nf-certif-icertserverpolicy-setcertificateextension) and [**SetCertificateProperty**](/windows/desktop/api/Certif/nf-certif-icertserverpolicy-setcertificateproperty) methods.

For information about removing the existing exit module and installing a new one, see the Exit Module Customization topic in Help.

 

 



