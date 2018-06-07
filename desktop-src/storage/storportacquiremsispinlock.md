---
title: StorPortAcquireMSISpinLock routine
description: The StorPortAcquireMSISpinLock routine acquires the message signaled interrupt (MSI) spin lock that is associated with the specified message.
ms.assetid: 8aa5a8a6-2024-4b3e-a500-5a484d937a62
keywords:
- StorPortAcquireMSISpinLock routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortAcquireMSISpinLock
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortAcquireMSISpinLock routine

The **StorPortAcquireMSISpinLock** routine acquires the message signaled interrupt (MSI) spin lock that is associated with the specified message.

## Syntax


```C++
ULONG StorPortAcquireMSISpinLock(
  _In_ PVOID  HwDeviceExtension,
  _In_ ULONG  MessageID,
  _In_ PULONG OldIrql
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*MessageID* \[in\]
</dt> <dd>

The identifier of the message whose spin lock the caller acquires.

</dd> <dt>

*OldIrql* \[in\]
</dt> <dd>

A pointer to the storage for the original IRQL value to be used in a subsequent call to [**StorPortReleaseMSISpinLock**](storportreleasemsispinlock.md).

</dd> </dl>

## Return value

**StorPortAcquireMSISpinLock** returns one of the following values:



| Return code                                                                                                     | Description                                                                 |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/> |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | Indicates that the spin lock was acquired successfully.<br/>          |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The *HwDeviceExtension* was **NULL**.<br/>                            |



 

## Remarks

A miniport driver calls the **StorPortAcquireMSISpinLock** routine to acquire the MSI spin lock for a particular message. To release the spin lock, the miniport driver calls the [**StorPortReleaseMSISpinLock**](storportreleasemsispinlock.md) routine. This routine is used by a miniport drivers to acquire a the MSI spin lock for an individual message only when the **InterruptSynchronizationMode** member of the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure is set to **InterruptSynchronizePerMessage**.

When a miniport needs to synchronize with all messages, it can use one call to [**StorPortAcquireSpinLock**](storportacquirespinlock.md) which will acquire a lock for each message in the proper order.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | This routine is available starting with Windows Vista.<br/>                                                                       |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any level<br/>                                                                                                                    |



## See also

<dl> <dt>

[**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md)
</dt> <dt>

[**StorPortAcquireSpinLock**](storportacquirespinlock.md)
</dt> <dt>

[**StorPortReleaseMSISpinLock**](storportreleasemsispinlock.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortAcquireMSISpinLock%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






