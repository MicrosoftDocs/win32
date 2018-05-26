---
title: StorPortAllocateContiguousMemorySpecifyCacheNode routine
description: The StorPortAllocateContiguousMemorySpecifyCacheNode routine allocates a range of physically contiguous noncached, nonpaged memory.
ms.assetid: b2ed8c88-9ffd-4601-8fd0-c9390e9ba84d
keywords:
- StorPortAllocateContiguousMemorySpecifyCacheNode routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortAllocateContiguousMemorySpecifyCacheNode
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortAllocateContiguousMemorySpecifyCacheNode routine

The **StorPortAllocateContiguousMemorySpecifyCacheNode** routine allocates a range of physically contiguous noncached, nonpaged memory.

## Syntax


```C++
ULONG StorPortAllocateContiguousMemorySpecifyCacheNode(
  _In_     PVOID               HwDeviceExtension,
  _In_     SIZE_T              NumberOfBytes,
  _In_     PHYSICAL_ADDRESS    LowestAcceptableAddress,
  _In_     PHYSICAL_ADDRESS    HighestAcceptableAddress,
  _In_opt_ PHYSICAL_ADDRESS    BoundaryAddressMultiple,
  _In_     MEMORY_CACHING_TYPE CacheType,
  _In_     NODE_REQUIREMENT    PreferredNode,
  _Out_    PVOID               *BufferPointer
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*NumberOfBytes* \[in\]
</dt> <dd>

The number of bytes to allocate.

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

</dd> <dt>

*CacheType* \[in\]
</dt> <dd>

The desired cache type for the mapping.

</dd> <dt>

*PreferredNode* \[in\]
</dt> <dd>

The preferred node from which the allocation should be made if pages are available on that node.

</dd> <dt>

*BufferPointer* \[out\]
</dt> <dd>

The variable that receives the starting address of the allocated memory block. Upon return from this routine, if this variable is zero, a contiguous range could not be found to satisfy the request. If this variable is not **NULL**, it contains a pointer (for example, a virtual address in the nonpaged portion of the system) to the allocated physically contiguous memory.

</dd> </dl>

## Return value

The **StorPortAllocateContiguousMemorySpecifyCacheNode** routine returns one of the following status codes:



| Return code                                                                                                          | Description                                                                                         |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>        | This function is not implemented on the active operating system.<br/>                         |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | The operation was successful.<br/>                                                            |
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | The operation failed to allocate the requested memory because of insufficient resources.<br/> |



 

## Remarks

If the request fails, *BufferPointer* will be set to **NULL**.

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>              | Available starting with Windows 7.<br/>                                                                                           |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>                 | &lt;=DISPATCH\_LEVEL<br/>                                                                                                         |
| DDI compliance rules<br/> | [**StorPortIrql**](https://msdn.microsoft.com/library/windows/hardware/hh454266)                                                                                       |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortAllocateContiguousMemorySpecifyCacheNode%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





