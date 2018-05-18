---
Description: 'The following example uses the Windows Image Acquisition (WIA) 1.0 IWiaDevMgr::RegisterEventCallbackCLSID method to register for notification when any Windows Image Acquisition (WIA) device is connected to the system.'
ms.assetid: '1f2c7bc9-876a-4693-9439-52735e4b9d5f'
title: Registering for Events
---

# Registering for Events

The following example uses the Windows Image Acquisition (WIA) 1.0 [**IWiaDevMgr::RegisterEventCallbackCLSID**](-wia-iwiadevmgr-registereventcallbackclsid.md) method to register for notification when any Windows Image Acquisition (WIA) device is connected to the system. Applications can also use WIA 1.0 [**IWiaDevMgr::RegisterEventCallbackInterface**](-wia-iwiadevmgr-registereventcallbackinterface.md) and WIA 1.0 [**IWiaDevMgr::RegisterEventCallbackProgram**](-wia-iwiadevmgr-registereventcallbackprogram.md) to register for events. With Windows Vista and later, you can use the Windows Image Acquisition (WIA) 2.0 [**IWiaDevMgr2::RegisterEventCallbackCLSID**](-wia-iwiadevmgr2-registereventcallbackclsid.md), [**IWiaDevMgr2::RegisterEventCallbackInterface**](-wia-iwiadevmgr2-registereventcallbackinterface.md), or [**IWiaDevMgr2::RegisterEventCallbackProgram**](-wia-iwiadevmgr2-registereventcallbackprogram.md) methods to register for events.

It is assumed that the example is taken from an application that is registered as a Component Object Model (COM) out-of-process server object.

The call to [**IWiaDevMgr::RegisterEventCallbackCLSID**](-wia-iwiadevmgr-registereventcallbackclsid.md) (or [**IWiaDevMgr2::RegisterEventCallbackCLSID**](-wia-iwiadevmgr2-registereventcallbackclsid.md)) is as follows:


```
    pWiaDevMgr->RegisterEventCallbackCLSID( WIA_REGISTER_EVENT_CALLBACK,
                                            NULL,
                                            WIA_EVENT_DEVICE_CONNECTED,
                                            pCLSID,
                                            bstrName,
                                            bstrDescription,
                                            bstrIcon
                                            );
```



In the previous code, **pWiaDevMgr** is a valid pointer to the [**IWiaDevMgr**](-wia-iwiadevmgr.md) (or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md)) interface, WIA\_REGISTER\_EVENT\_CALLBACK is a constant that specifies that this call is to register for the event as opposed to unregistering for the event, WIA\_EVENT\_DEVICE\_CONNECTED is a constant that specifies that the application is registering to be notified whenever a device is connected to the user's computer, **pCLSID** is a pointer to the registered CLSID of the application, **bstrName** is the name of the application, **bstrDescription** is a text description of the application, and **bstrIcon** is the name of an image file to be used for the icon for the application registering for the event.

The application must then implement the [**IWiaEventCallback::ImageEventCallback**](-wia-iwiaeventcallback-imageeventcallback.md) method, which is called whenever an event occurs for which the application is registered.

An application can use the [**IWiaItem::EnumRegisterEventInfo**](-wia-iwiaitem-enumregistereventinfo.md) (or [**IWiaItem2::EnumRegisterEventInfo**](-wia-iwiaitem2-enumregistereventinfo.md)) method to enumerate the information about events for which it is registered.

 

 



