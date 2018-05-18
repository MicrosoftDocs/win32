---
title: StorPortReleaseMSISpinLock routine
description: The StorPortReleaseMSISpinLock routine releases a previously acquired message signaled interrupt (MSI) spin lock for the specified message.
ms.assetid: '5a2cf757-9dca-4717-a775-834a22c02a12'
keywords: ["StorPortReleaseMSISpinLock routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortReleaseMSISpinLock
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortReleaseMSISpinLock routine

The **StorPortReleaseMSISpinLock** routine releases a previously acquired message signaled interrupt (MSI) spin lock for the specified message.

## Syntax


```C++
ULONG StorPortReleaseMSISpinLock(
  _In_ PVOID HwDeviceExtension,
  _In_ ULONG MessageID,
  _In_ ULONG OldIrql
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

The identifier of the message.

</dd> <dt>

*OldIrql* \[in\]
</dt> <dd>

The IRQL that the [**StorPortAcquireMSISpinLock**](storportacquiremsispinlock.md) routine returned when the miniport driver acquired the spin lock.

</dd> </dl>

## Return value

StorPortReleaseMSISpinLock returns one of the following status codes:



| Return code                                                                                                     | Description                                                                 |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/> |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | Indicates that the spin lock was released successfully.<br/>          |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | HwDeviceExtension was **NULL**.<br/>                                  |



 

## Remarks

Miniport drivers are not required to acquire MSI spin locks for messages unless the **InterruptSynchronizePerMessage** member of the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure indicates a synchronization mode of **InterruptSynchronizationMode**.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | This routine is available starting with Windows Vista.<br/>                                                                       |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any level<br/>                                                                                                                    |



## See also

<dl> <dt>

[**StorPortAcquireMSISpinLock**](storportacquiremsispinlock.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortReleaseMSISpinLock%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






