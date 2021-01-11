---
description: Registers a running application for Windows Image Acquisition (WIA) 2.0 event notification.
ms.assetid: 978dcd41-d63b-421d-b7e1-8e9368b36180
title: IWiaDevMgr2::RegisterEventCallbackInterface method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaDevMgr2.RegisterEventCallbackInterface
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaDevMgr2::RegisterEventCallbackInterface method

Registers a running application for Windows Image Acquisition (WIA) 2.0 event notification.

## Syntax


```C++
HRESULT RegisterEventCallbackInterface(
  [in]        LONG              lFlags,
  [in]        BSTR              bstrDeviceID,
  [in]  const GUID              *pEventGUID,
  [in]        IWiaEventCallback *pIWiaEventCallback,
  [out]       IUnknown          **pEventObject
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Currently unused. Should be set to zero.

</dd> <dt>

*bstrDeviceID* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the unique identifier of a WIA 2.0 device. Set this parameter to **NULL** to register for the event on all WIA 2.0 devices.

</dd> <dt>

*pEventGUID* \[in\]
</dt> <dd>

Type: **const GUID\***

Specifies a pointer to the event identifier that the application is registering for. See [WIA Event Identifiers](-wia-wia-event-identifiers.md) for standard event identifiers.

</dd> <dt>

*pIWiaEventCallback* \[in\]
</dt> <dd>

Type: **[**IWiaEventCallback**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaeventcallback)\***

Specifies a pointer to the [**IWiaEventCallback**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaeventcallback) interface that the WIA 2.0 uses to send event notification.

</dd> <dt>

*pEventObject* \[out\]
</dt> <dd>

Type: **[IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown)\*\***

Receives the address of a pointer to the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns the standard COM error codes or the following.



| Return code                                                                               | Description                                                            |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface cannot be returned. <br/> |



 

## Remarks

> [!WARNING]
> Using the [**IWiaDevMgr::RegisterEventCallbackInterface**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-registereventcallbackinterface), **IWiaDevMgr2::RegisterEventCallbackInterface**, and [**DeviceManager.RegisterEvent**](/previous-versions/windows/desktop/wiaaut/-wiaaut-idevicemanager-registerevent) methods from the same process after the Still Image Service is restarted may cause an access violation, if the functions were used before the service was stopped.

 

When WIA 2.0 applications begin executing, they use this method to register to receive hardware device events. This prevents the application from being restarted when another event for which it is registered occurs. Once an application calls **IWiaDevMgr2::RegisterEventCallbackInterface** to register itself to receive WIA 2.0 events from a device, the registered events are routed to the program by WIA 2.0.

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers they receive through the *pEventObject* parameter.

> [!Note]  
> In a multithreaded application, the event notification callback may come in on a different thread from the one that registered the callback.

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
