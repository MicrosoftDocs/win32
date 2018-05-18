---
Description: 'Custom exit modules must implement the ICertExit interface, which is called by the server engine.'
ms.assetid: '509e7945-b656-4c4c-b5eb-45fbe80377c7'
title: Writing Custom Exit Modules
---

# Writing Custom Exit Modules

Custom exit modules must implement the [**ICertExit**](icertexit.md) interface, which is called by the server engine. The [**ICertExit::Initialize**](icertexit2-initialize.md) method is called by the server engine when the exit module is loaded. It allows the exit module to perform initialization and returns a value that informs the server engine of the kinds of events for which it wants notification. The [**ICertExit::GetDescription**](icertexit2-getdescription.md) method must return a description string when the server engine requests it. The [**ICertExit::Notify**](icertexit2-notify.md) method is called by the server engine to notify the exit module that an event has occurred.

Exit modules can call the [**ICertServerExit**](icertserverexit.md) interface, which supports many of the same methods as the [**ICertServerPolicy**](icertserverpolicy.md) interface, with the exception of the [**SetCertificateExtension**](icertserverpolicy-setcertificateextension.md) and [**SetCertificateProperty**](icertserverpolicy-setcertificateproperty.md) methods.

For information about removing the existing exit module and installing a new one, see the Exit Module Customization topic in Help.

 

 



