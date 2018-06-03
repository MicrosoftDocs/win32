---
title: HBA\_RegisterForLinkEvents routine
description: The HBA\_RegisterForLinkEvents routine registers with a specified adapter for asynchronous fabric link-level events.
ms.assetid: f0e6834c-b827-4342-83f1-5980f8edce24
keywords:
- HBA_RegisterForLinkEvents routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_RegisterForLinkEvents
api_location:
- Hbaapi.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HBA\_RegisterForLinkEvents routine

The **HBA\_RegisterForLinkEvents** routine registers with a specified adapter for asynchronous fabric link-level events.

## Syntax


```C++
HBA_STATUS HBA_API HBA_RegisterForLinkEvents(
   HBA_LINK_CALLBACK  callback,
   void               *userData,
   void               *pRLIRBuffer,
   HBA_UINT32         RLIRBufferSize,
   HBA_HANDLE         handle,
   HBA_CALLBACKHANDLE *callbackHandle
);
```



## Parameters

<dl> <dt>

*callback* 
</dt> <dd>

Pointer to a callback routine of type [**HBA\_LINK\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff556121) to call when the event occurs.

</dd> <dt>

*userData* 
</dt> <dd>

Pointer to user input data that is passed to the callback routine when it is called with each occurrence of the event. This data can synchronize the event handling with event registration.

</dd> <dt>

*pRLIRBuffer* 
</dt> <dd>

Pointer to registered link incident report (RLIR) data that is passed to the callback routine with each occurrence of the event. This data is overwritten by the callback routine each time it is called.

</dd> <dt>

*RLIRBufferSize* 
</dt> <dd>

Contains the size, in bytes, of the buffer at *pRLIRBuffer*.

</dd> <dt>

*handle* 
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA for which event callbacks are requested.

</dd> <dt>

*callbackHandle* 
</dt> <dd>

Pointer to an opaque identifier that may be used to deregister the caller and suspend calls to the callback routine when events occur.

</dd> </dl>

## Return value

The **HBA\_RegisterForLinkEvents** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_RegisterForLinkEvents** returns one of the following values.



| Return code                                                                                                       | Description                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                    | Returned if the callback registration was successful. <br/>                                              |
| <dl> <dt>**HBA\_STATUS\_ERROR\_NOT\_SUPPORTED**</dt> </dl> | Returned if either the library or the system does not support events. <br/>                              |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>                 | Returned if an unspecified error occurred that prevented the registration of the callback routine. <br/> |



 

## Remarks

Only RLIR events are reported. To stop event delivery, call [**HBA\_RemoveCallback**](hba-removecallback.md).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_LINK\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff556121)
</dt> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[**HBA\_RemoveCallback**](hba-removecallback.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_RegisterForLinkEvents%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






