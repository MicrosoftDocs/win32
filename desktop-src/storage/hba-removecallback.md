---
title: HBA\_RemoveCallback routine
description: The HBA\_RemoveCallback routine de-registers a callback routine.
ms.assetid: 9b97e93c-a375-4df7-9d2d-86f1ad72b62d
keywords:
- HBA_RemoveCallback routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_RemoveCallback
api_location:
- Hbaapi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HBA\_RemoveCallback routine

The **HBA\_RemoveCallback** routine de-registers a callback routine.

## Syntax


```C++
HBA_STATUS HBA_API HBA_RemoveCallback(
  _In_ HBA_CALLBACKHANDLE callbackHandle
);
```



## Parameters

<dl> <dt>

*callbackHandle* \[in\]
</dt> <dd>

Contains an opaque handle specified with the call to [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the callback routine to de-register.

</dd> </dl>

## Return value

The **HBA\_RemoveCallback** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_RemoveCallback** returns one of the following values.



| Return code                                                                                       | Description                                                                                                       |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>    | Returned if the callback routine was successfully de-registered. <br/>                                      |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl> | Returned if an unspecified error occurred that prevented the de-registration of the callback routine. <br/> |



 

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_RemoveCallback%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






