---
title: StorPortInitializeSpinlock routine
description: The StorPortInitializeSpinLock routine initializes a variable of type STOR\_KSPIN\_LOCK.
ms.assetid: 150B1ED3-572A-4986-BED6-628ED6C54CCF
keywords:
- StorPortInitializeSpinlock routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortInitializeSpinlock
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

# StorPortInitializeSpinlock routine

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **StorPortInitializeSpinLock** routine initializes a variable of type **STOR\_KSPIN\_LOCK**.

## Syntax


```C++
ULONG StorPortInitializeSpinlock(
  _In_  PVOID            HwDeviceExtension,
  _Out_ PSTOR_KSPIN_LOCK Lock
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*Lock* \[out\]
</dt> <dd>

Pointer to a spin lock of type **STOR\_KSPIN\_LOCK**, for which the caller must provide the storage

</dd> </dl>

## Return value

**StorPortInitializeSpinlock** returns one of the following status codes:



| Return code                                                                                                     | Description                                                                       |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/>       |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The list items were removed successfully or the list is already empty.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | A pointer in *ListHead* or *Result* is **NULL**.<br/>                       |



 

## Remarks

This routine must be called before an initial call to [**StorPortAcquireSpinLock**](storportacquirespinlock.md), to any other support routine that requires a spin lock as an argument.

For more information about spin locks, see [Spin Locks](https://msdn.microsoft.com/library/windows/hardware/ff563830).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



## See also

<dl> <dt>

[**StorPortAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff567025)
</dt> <dt>

[**StorPortAcquireMSISpinLock**](storportacquiremsispinlock.md)
</dt> <dt>

[**StorPortReleaseSpinLock**](storportreleasespinlock.md)
</dt> <dt>

[**StorPortReleaseMSISpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff567494)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInitializeSpinlock%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






