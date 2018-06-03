---
title: StorPortAllocateHostMemoryBuffer routine
description: This function allocates one or more ranges of physically contiguous memory to be used as a Host Memory Buffer (HMB).
ms.assetid: B8413B02-32A6-40AE-9DD2-C25AD2D2D45C
keywords:
- StorPortAllocateHostMemoryBuffer routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortAllocateHostMemoryBuffer
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

# StorPortAllocateHostMemoryBuffer routine

This function allocates one or more ranges of physically contiguous memory to be used as a Host Memory Buffer (HMB). This is memory that the device may use directly and exclusively. The device may use this memory however it sees fit, but it must ensure that there is no data loss or data corruption in the event of a surprise removal or unexpected power loss.

Depending on the allocation policy, this function may allocate as much as the device's preferred size, as little as the device's minimum size, or no memory at all. This function will attempt to allocate as few physically contiguous address ranges as possible, but it may have to use multiple physical address ranges to satisfy the desired HMB size.

## Syntax


```C++
ULONG StorPortAllocateHostMemoryBuffer(
  _In_     PVOID                                                                                 HwDeviceExtension,
  _In_     SIZE_T                                                                                MinimumBytes,
  _In_     SIZE_T                                                                                PreferredBytes,
  _In_     ULONGLONG                                                                             UtilizationBytes,
  _In_     ULONG                                                                                 AlignmentBytes,
  _In_     PHYSICAL_ADDRESS                                                                      LowestAcceptableAddress,
  _In_     PHYSICAL_ADDRESS                                                                      HighestAcceptableAddress,
  _In_opt_ PHYSICAL_ADDRESS                                                                      BoundaryAddressMultiple,
           _Out_writes_to_(*PhysicalAddressRangeCount, *PhysicalAddressRangeCount) PACCESS_RANGE PhysicalAddressRanges,
  _Inout_  PULONG                                                                                PhysicalAddressRangeCount
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*MinimumBytes* \[in\]
</dt> <dd>

The minimum amount of memory that will be useful to the device, in bytes. A value of 0 indicates that any size of memory up to the preferred size is acceptable.

</dd> <dt>

*PreferredBytes* \[in\]
</dt> <dd>

The amount of memory the device prefers, in bytes. This must be a multiple of the page size.

</dd> <dt>

*UtilizationBytes* \[in\]
</dt> <dd>

The total number of blocks allocated on the device, in bytes.

</dd> <dt>

*AlignmentBytes* \[in\]
</dt> <dd>

The Host Memory Buffer alignment requirement from the device.

</dd> <dt>

*LowestAcceptableAddress* \[in\]
</dt> <dd>

The lowest physical address that is valid for the allocation. For example, if the device can only reference physical memory in the 8 MB to 16 MB range, this value would be set to 0x800000 (8 MB).

</dd> <dt>

*HighestAcceptableAddress* \[in\]
</dt> <dd>

The highest physical address that is valid for the allocation. For example, if the device can only reference physical memory below 16 MB, this value would be set to 0xFFFFFF (16 MB - 1).

</dd> <dt>

*BoundaryAddressMultiple* \[in, optional\]
</dt> <dd>

The physical address multiple that this allocation must not cross.

> [!Note]  
> This parameter is currently not used and must be set to 0.

 

</dd> <dt>

*PhysicalAddressRanges* 
</dt> <dd>

An array of physical address ranges that make up the Host Memory Buffer. The caller should provide a pre-allocated array. **StorPortAllocateHostMemoryBuffer** will fill in the array with one or more physical address ranges.

</dd> <dt>

*PhysicalAddressRangeCount* \[in, out\]
</dt> <dd>

The number of entries in **PhysicalAddressRanges**. This function will update this parameter to indicate how many physical address ranges it filled in.

</dd> </dl>

## Return value

**StorPortAllocateHostMemoryBuffer** returns one of the following status codes:



| Return code                                                                                                          | Description                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | The **PhysicalAddressRanges** array contains one or more valid physical address ranges that represent the host memory buffer.<br/>                  |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>      | This could indicate a minimum value that is greater than a maximum value, a non-page-aligned size, or that **PhysicalAddressRanges** is empty.<br/> |
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | The host memory buffer could not be allocated.<br/>                                                                                                 |



 

## Remarks

The caller should subsequently call [**StorPortFreeHostMemoryBuffer**](https://msdn.microsoft.com/library/windows/hardware/mt795368) when it is done with the host memory buffer.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            |                                                                                                                                         |



## See also

<dl> <dt>

[**StorPortFreeHostMemoryBuffer**](https://msdn.microsoft.com/library/windows/hardware/mt795368)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortAllocateHostMemoryBuffer%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






