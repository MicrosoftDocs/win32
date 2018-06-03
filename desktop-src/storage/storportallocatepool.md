---
title: StorPortAllocatePool routine
description: The StorPortAllocatePool routine allocates a block of non-contiguous, non-paged pool memory.
ms.assetid: e6823b9c-9717-49ab-8e67-c1d522774826
keywords:
- StorPortAllocatePool routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortAllocatePool
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

# StorPortAllocatePool routine

The **StorPortAllocatePool** routine allocates a block of non-contiguous, non-paged pool memory.

## Syntax


```C++
ULONG StorPortAllocatePool(
  _In_  PVOID HwDeviceExtension,
  _In_  ULONG NumberOfBytes,
  _In_  ULONG Tag,
  _Out_ PVOID *BufferPointer
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

The size, in bytes, of the block of memory being allocated.

</dd> <dt>

*Tag* \[in\]
</dt> <dd>

The pool tag for the allocated memory. Drivers specify the pool tag as a string of four characters, delimited by single quotation marks. The string is usually specified in reverse order. The ASCII value of each character in the tag must be between zero and 127.

</dd> <dt>

*BufferPointer* \[out\]
</dt> <dd>

A pointer to the address of the allocated memory block or **NULL** if not successful.

</dd> </dl>

## Return value

StorPortAllocatePool returns one of the following status codes:



| Return code                                                                                                          | Description                                                                                        |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>        | This function is not implemented on the active operating system.<br/>                        |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | Indicates that the routine successfully allocated a memory block of the requested size.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>      | The pointer to receive the buffer address is **NULL**.<br/>                                  |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>           | The call was made at an invalid IRQL.<br/>                                                   |
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | Unable to allocate memory of the requested size.<br/>                                        |



 

## Remarks

A miniport driver calls the **StorPortAllocatePool** routine to allocate a block of non-contiguous memory from the non-paged pool. To free the block of memory, the miniport driver calls the [**StorPortFreePool**](storportfreepool.md) routine. If the request fails, BufferPointer will be set to **NULL**.

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>                 | &lt;=DISPATCH\_LEVEL<br/>                                                                                                         |
| DDI compliance rules<br/> | [**StorPortAllocatePool2**](https://msdn.microsoft.com/library/windows/hardware/hh454259), [**StorPortIrql**](https://msdn.microsoft.com/library/windows/hardware/hh454266)                  |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortAllocatePool%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





