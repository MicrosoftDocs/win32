---
title: StorPortFreeTimer routine
description: Frees a Storport timer context object previously created by the StorPortInitializeTimer routine.
ms.assetid: 'AF6B1693-6242-4F09-8226-472E75B809F3'
keywords: ["StorPortFreeTimer routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortFreeTimer
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortFreeTimer routine

Frees a Storport timer context object previously created by the [**StorPortInitializeTimer**](storportinitializetimer.md) routine.

## Syntax


```C++
ULONG StorPortFreeTimer(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID TimerHandle
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*TimerHandle* \[in\]
</dt> <dd>

A pointer to an opaque buffer for the timer context returned by [**StorPortInitializeTimer**](storportinitializetimer.md).

</dd> </dl>

## Return value

The **StorPortFreeTimer** routine returns one of these status codes:



| Return code                                                                                                          | Description                                                        |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>           | Current IRQL &gt; DISPATCH\_LEVEL.<br/>                      |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>      | Either *HwDeviceExtension* or *TimerHandle* is NULL.<br/>    |
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | Insufficient resources are available to free the timer.<br/> |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | The timer was successfully freed.<br/>                       |
| <dl> <dt>**STOR\_STATUS\_UNSUCCESSFUL**</dt> </dl>            | The timer is already free.<br/>                              |



 

## Remarks

Miniports should call **StorPortFreeTimer** whenever a work item is no longer needed or when the miniport receives a PnP SRB notification that the adapter is removed.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | &lt;= DISPATCH\_LEVEL<br/>                                                                                                        |



## See also

<dl> <dt>

[**HwStorAdapterControl**](hwstoradaptercontrol.md)
</dt> <dt>

[**StorPortInitializeTimer**](storportinitializetimer.md)
</dt> <dt>

[**StorPortRequestTimer**](storportrequesttimer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortFreeTimer%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






