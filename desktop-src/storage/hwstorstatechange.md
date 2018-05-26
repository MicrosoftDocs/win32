---
title: HW\_STATE\_CHANGE routine
description: A miniport-provided callback that is called after a notification from StorPortStateChangeDetected is processed.
ms.assetid: E7E5E26A-B477-453C-AAFC-9B3572F4FC72
keywords:
- HwStorStateChange routine Storage Devices
- HW_STATE_CHANGE
topic_type:
- apiref
api_name:
- HwStorStateChange
api_location:
- storport.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HW\_STATE\_CHANGE routine

A miniport-provided callback that is called after a notification from [**StorPortStateChangeDetected**](storportstatechangedetected.md) is processed.

## Syntax


```C++
HW_STATE_CHANGE HwStorStateChange;

VOID HwStorStateChange(
  _In_     IN PVOID DeviceExtension,
  _In_opt_ PVOID    Context,
  _In_     SHORT    AddressType,
  _In_     PVOID    Address,
  _In_     ULONG    Status
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

A pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*Context* \[in, optional\]
</dt> <dd>

The context supplied as *HwStateChangeContext* by the miniport in the call to [**StorPortStateChangeDetected**](storportstatechangedetected.md).

</dd> <dt>

*AddressType* \[in\]
</dt> <dd>

The type of the address in *Address*.

</dd> <dt>

*Address* \[in\]
</dt> <dd>

A pointer to a [**STOR\_ADDRESS**](stor-address.md) structure for the entity whose state change was processed.

</dd> <dt>

*Status* \[in\]
</dt> <dd>

The processing status for the state change notification.

</dd> </dl>

## Return value

None.

## Remarks

The *HwStorStateChange* is called with the StartIo lock acquired by Storport.

This callback enables miniports to do any additional processing that is needed after hardware addition or removal. If a hardware change occurs on the HBA port or bus, the miniport can call [**StorPortStateChangeDetected**](storportstatechangedetected.md) to alert the system of the event.

If the value for *Status* is &lt; 0x80000000, then the notification processing was successful. Otherwise, the notification process failed.

The name *HwStorStateChange* is just a placeholder for the miniport function that is pointed to by the *HwStateChange* parameter of [**StorPortStateChangeDetected**](storportstatechangedetected.md). The actual prototype of this routine is defined in *Storport.h* as follows:


```
typedef
VOID
HW_STATE_CHANGE (
    _In_ PVOID HwDeviceExtension,
    _In_opt_ PVOID Context,
    _In_ SHORT AddressType,
    _In_ PVOID Address,
    _In_ ULONG Status
    );
```



## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | DISPATCH<br/>                                                                                                                     |



## See also

<dl> <dt>

[**STOR\_ADDRESS**](stor-address.md)
</dt> <dt>

[**StorPortStateChangeDetected**](storportstatechangedetected.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_STATE_CHANGE%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






