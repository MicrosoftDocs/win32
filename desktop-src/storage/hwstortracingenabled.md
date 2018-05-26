---
title: HW\_TRACING\_ENABLED routine
description: The HwStorTracingEnabled callback routine enables the Storport to notify a miniport that event tracing is enabled.
ms.assetid: 2B56A2D3-1FA6-4212-A83C-3C20D826353B
keywords:
- HwStorTracingEnabled routine Storage Devices
- HW_TRACING_ENABLED
topic_type:
- apiref
api_name:
- HwStorTracingEnabled
api_location:
- Storport.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HW\_TRACING\_ENABLED routine

The **HwStorTracingEnabled** callback routine enables the Storport to notify a miniport that event tracing is enabled.

## Syntax


```C++
HW_TRACING_ENABLED HwStorTracingEnabled;

VOID HwStorTracingEnabled(
  _In_ PVOID   DeviceExtension,
  _In_ BOOLEAN Enabled
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

A pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*Enabled* \[in\]
</dt> <dd>

True to enable tracing in the miniport. Otherwise, false.

</dd> </dl>

## Return value

None.

## Remarks

The name *HwStorTracingEnabled* is placeholder text for the actual routine name. The actual prototype of this routine is defined in *Storport.h* as follows:


```
typedef
VOID
HW_TRACING_ENABLED (
    _In_ PVOID HwDeviceExtension,
    _In_ BOOLEAN Enabled
    );
```



## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                                               |



## See also

<dl> <dt>

[**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_TRACING_ENABLED%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






