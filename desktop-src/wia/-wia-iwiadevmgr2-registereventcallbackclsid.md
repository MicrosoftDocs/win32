---
description: The IWiaDevMgr2::RegisterEventCallbackCLSID method registers an application to receive events even if the application is not running.
ms.assetid: e0d421a7-ef49-4e27-9661-c358ac819712
title: IWiaDevMgr2::RegisterEventCallbackCLSID method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaDevMgr2.RegisterEventCallbackCLSID
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaDevMgr2::RegisterEventCallbackCLSID method

The **IWiaDevMgr2::RegisterEventCallbackCLSID** method registers an application to receive events even if the application is not running.

## Syntax


```C++
HRESULT RegisterEventCallbackCLSID(
  [in]               LONG lFlags,
  [in]               BSTR bstrDeviceID,
  [in]         const GUID *pEventGUID,
  [in, unique] const GUID *pClsID,
  [in]               BSTR bstrName,
  [in]               BSTR bstrDescription,
  [in]               BSTR bstrIcon
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Specifies registration flags. Can be set to the following values:



| Registration Flag                | Meaning                                           |
|----------------------------------|---------------------------------------------------|
| WIA\_REGISTER\_EVENT\_CALLBACK   | Register for the event.                           |
| WIA\_UNREGISTER\_EVENT\_CALLBACK | Delete the registration for the event.            |
| WIA\_SET\_DEFAULT\_HANDLER       | Set the application as the default event handler. |



 

</dd> <dt>

*bstrDeviceID* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies a device identifier. Pass **NULL** to register for the event on all WIA 2.0 devices.

</dd> <dt>

*pEventGUID* \[in\]
</dt> <dd>

Type: **const GUID\***

Specifies the event that the application is registering for. For a list of standard events, see [WIA Event Identifiers](-wia-wia-event-identifiers.md).

</dd> <dt>

*pClsID* \[in\]
</dt> <dd>

Type: **const GUID\***

Pointer to the application class ID (**CLSID**). The WIA 2.0 run-time system uses the application **CLSID** to start the application when an event occurs that it is registered for.

</dd> <dt>

*bstrName* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the name of the application that registers for the event.

</dd> <dt>

*bstrDescription* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies a text description of the application that registers for the event.

</dd> <dt>

*bstrIcon* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the name of an image file to use for the icon for the application that registers for the event.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

WIA 2.0 applications use this method to register to receive hardware device events. After **IWiaDevMgr2::RegisterEventCallbackCLSID** is called, the application is registered to receive WIA 2.0 device events even if it is not running.

When the event occurs, the WIA 2.0 system determines which application is registered to receive the event. It uses the [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function and the CLSID specified in the *pClsID* parameter to create an instance of the application, and then calls the [**ImageEventCallback**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaeventcallback-imageeventcallback) method to transmit the event information to the application.

An application can invoke the [**EnumRegisterEventInfo**](-wia-iwiaitem2-enumregistereventinfo.md) method to enumerate event registration information.

If the application is not a registered Component Object Model (COM) component and is not compatible with the WIA 2.0 architecture, use the [**IWiaDevMgr2::RegisterEventCallbackProgram**](-wia-iwiadevmgr2-registereventcallbackprogram.md) method to register an application for device events.

> [!Note]  
> In a multi-threaded application, there is no guarantee that the event notification callback is returned on the same thread that registered the callback.

 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl> |



 

 
