---
description: The IWiaDevMgr2::RegisterEventCallbackProgram method registers an application to receive device events. It is primarily provided for backward compatibility with applications that were not written for Windows Image Acquisition (WIA) 2.0.
ms.assetid: 6b427f19-719b-44ce-8e2c-3c44672345c8
title: IWiaDevMgr2::RegisterEventCallbackProgram method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaDevMgr2.RegisterEventCallbackProgram
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaDevMgr2::RegisterEventCallbackProgram method

The **IWiaDevMgr2::RegisterEventCallbackProgram** method registers an application to receive device events. It is primarily provided for backward compatibility with applications that were not written for Windows Image Acquisition (WIA) 2.0.

## Syntax


```C++
HRESULT RegisterEventCallbackProgram(
  [in]       LONG lFlags,
  [in]       BSTR bstrDeviceID,
  [in] const GUID *pEventGUID,
  [in]       BSTR bstrFullAppName,
  [in]       BSTR bstrCommandlineArg,
  [in]       BSTR bstrName,
  [in]       BSTR bstrDescription,
  [in]       BSTR bstrIcon
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

The registration flags. Can be set to the following values.



| Value                                                                                                                                                                                                           | Meaning                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <span id="WIA_REGISTER_EVENT_CALLBACK"></span><span id="wia_register_event_callback"></span><dl> <dt>**WIA\_REGISTER\_EVENT\_CALLBACK**</dt> </dl>       | Register for the event.<br/>                           |
| <span id="WIA_UNREGISTER_EVENT_CALLBACK"></span><span id="wia_unregister_event_callback"></span><dl> <dt>**WIA\_UNREGISTER\_EVENT\_CALLBACK**</dt> </dl> | Delete the registration for the event.<br/>            |
| <span id="WIA_SET_DEFAULT_HANDLER"></span><span id="wia_set_default_handler"></span><dl> <dt>**WIA\_SET\_DEFAULT\_HANDLER**</dt> </dl>                   | Set the application as the default event handler.<br/> |



 

</dd> <dt>

*bstrDeviceID* \[in\]
</dt> <dd>

Type: **BSTR**

A device identifier. Pass **NULL** to register for the event on all WIA 2.0 devices.

</dd> <dt>

*pEventGUID* \[in\]
</dt> <dd>

Type: **const GUID\***

The event that the application is registering for. For a list of valid event GUIDs, see [WIA Event Identifiers](-wia-wia-event-identifiers.md).

</dd> <dt>

*bstrFullAppName* \[in\]
</dt> <dd>

Type: **BSTR**

The full path name of the application.

</dd> <dt>

*bstrCommandlineArg* \[in\]
</dt> <dd>

Type: **BSTR**

The appropriate command-line arguments for the application.

</dd> <dt>

*bstrName* \[in\]
</dt> <dd>

Type: **BSTR**

The name of the application. The name is displayed to the user when multiple applications register for the same event.

</dd> <dt>

*bstrDescription* \[in\]
</dt> <dd>

Type: **BSTR**

The description of the application. The description is displayed to the user when multiple applications register for the same event.

</dd> <dt>

*bstrIcon* \[in\]
</dt> <dd>

Type: **BSTR**

The icon that represents the application. The icon is displayed to the user when multiple applications register for the same event. The string contains the name of the application and the zero-based index of the icon separated by a comma, for example, "MyApp, 0". There might be more than one icon that represents an application.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Use **IWiaDevMgr2::RegisterEventCallbackProgram** to register for hardware device events. When an event occurs that an application is registered for, the application is launched, and the event information is transmitted to the application.

Use the [**EnumRegisterEventInfo**](-wia-iwiaitem2-enumregistereventinfo.md) method to retrieve a pointer to an enumerator object for event registration properties.

Only use the **IWiaDevMgr2::RegisterEventCallbackProgram** method for backward compatibility with applications not written for the WIA 2.0 architecture. Use the Component Object Model (COM) interfaces provided by the WIA 2.0 architecture for new applications. Specifically, call [**IWiaDevMgr2::RegisterEventCallbackInterface**](-wia-iwiadevmgr2-registereventcallbackinterface.md) or [**IWiaDevMgr2::RegisterEventCallbackCLSID**](-wia-iwiadevmgr2-registereventcallbackclsid.md) to register a new application for device events.

Typically, this method is called by an install program or a script. The install program or script registers the application to receive WIA 2.0 device events. When the event occurs, the application is started by the WIA 2.0 run-time system.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl> |



 

 




