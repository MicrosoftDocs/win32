---
description: 'Applications can register to be notified of Windows Image Acquisition (WIA) hardware device events by calling one of the following IWiaDevMgr or IWiaDevMgr2 interface methods: IWiaDevMgr::RegisterEventCallbackCLSID or IWiaDevMgr2::RegisterEventCallbackCLSIDIWiaDevMgr::RegisterEventCallbackInterface or IWiaDevMgr2::RegisterEventCallbackInterfaceIWiaDevMgr::RegisterEventCallbackProgram or IWiaDevMgr2::RegisterEventCallbackProgram'
ms.assetid: 0c142083-835f-4bbd-ab32-eb6130f99c59
title: Registering WIA Events
ms.topic: article
ms.date: 05/31/2018
---

# Registering WIA Events

Applications can register to be notified of Windows Image Acquisition (WIA) hardware device events by calling one of the following [**IWiaDevMgr**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadevmgr) or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interface methods:

-   [**IWiaDevMgr::RegisterEventCallbackCLSID**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-registereventcallbackclsid) or [**IWiaDevMgr2::RegisterEventCallbackCLSID**](-wia-iwiadevmgr2-registereventcallbackclsid.md)
-   [**IWiaDevMgr::RegisterEventCallbackInterface**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-registereventcallbackinterface) or [**IWiaDevMgr2::RegisterEventCallbackInterface**](-wia-iwiadevmgr2-registereventcallbackinterface.md)
-   [**IWiaDevMgr::RegisterEventCallbackProgram**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-registereventcallbackprogram) or [**IWiaDevMgr2::RegisterEventCallbackProgram**](-wia-iwiadevmgr2-registereventcallbackprogram.md)

All of these methods take parameters that specify the event and the hardware device for which the application is to be notified. Applications register to receive an event for all WIA devices by passing a **NULL** value for the parameter that specifies the hardware device.

The **RegisterEventCallbackInterface** method registers an application to receive a WIA hardware device event if the application is running at the time the event occurs. When the event for which the application is registered occurs, WIA calls the [**IWiaEventCallback::ImageEventCallback**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaeventcallback-imageeventcallback) method of the application-provided object to transmit the event information.

The **RegisterEventCallbackCLSID** method registers an application that is a registered Component Object Model (COM) component to receive a WIA hardware device event even if the application is not running. In addition to the parameters mentioned previously, this method takes a parameter, *pClsID*, that specifies the class ID of the application. When the specified event occurs, the WIA system uses the [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function and the class ID specified by *pClsID* to create a new instance of the application, and calls the [**IWiaEventCallback::ImageEventCallback**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaeventcallback-imageeventcallback) method of that application to transmit the event information.

The **RegisterEventCallbackProgram** method registers an application to receive a WIA hardware device event even if the application is not running when the event occurs. The application need not be a registered COM component. WIA launches the application with a command line statement. **RegisterEventCallbackProgram** takes a parameter, *bstrCommandline*, that specifies the full path and filename of the executable application. **RegisterEventCallbackProgram** exists for backward compatibility with applications that were not written for WIA, and should be avoided. Use **RegisterEventCallbackInterface** or **RegisterEventCallbackCLSID** instead.

To determine which handlers are registered for events on a specific WIA device, an application calls a [**IWiaItem::EnumRegisterEventInfo**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaitem-enumregistereventinfo) or [**IWiaItem2::EnumRegisterEventInfo**](-wia-iwiaitem2-enumregistereventinfo.md) method of a root item. This method creates an enumeration object for the registration information. The application can then use the [**IEnumWIA\_DEV\_CAPS**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_caps) interface of that object to enumerate information about the handlers registered to receive events for that device.

If an event occurs for which a running application is registered through **RegisterEventCallbackInterface** and either **RegisterEventCallbackCLSID** or **RegisterEventCallbackProgram**, WIA notifies the running application and does not attempt to launch a new instance of the application because event registration through **RegisterEventCallbackInterface** takes precedence over both **RegisterEventCallbackCLSID** and **RegisterEventCallbackProgram**.

> [!Note]  
> In a multi-threaded application, there is no guarantee that the thread that the event notification callback will return on is the same thread that registered the callback.

 

 

 
