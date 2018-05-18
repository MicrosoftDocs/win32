---
title: StorPortPutScatterGatherList routine
description: The StorPortPutScatterGatherList routine releases any resources associated with a scatter/gather list that was previously created by a call to the StorPortBuildScatterGatherList routine.
ms.assetid: '0b380597-09dc-414f-b2c6-f541d35540da'
keywords: ["StorPortPutScatterGatherList routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortPutScatterGatherList
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortPutScatterGatherList routine

The **StorPortPutScatterGatherList** routine releases any resources associated with a scatter/gather list that was previously created by a call to the [**StorPortBuildScatterGatherList**](storportbuildscattergatherlist.md) routine.

## Syntax


```C++
ULONG StorPortPutScatterGatherList(
  _In_ PVOID                     HwDeviceExtension,
  _In_ PSTOR_SCATTER_GATHER_LIST ScatterGatherList,
  _In_ BOOLEAN                   WriteToDevice
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*ScatterGatherList* \[in\]
</dt> <dd>

A pointer to a buffer that contains a scatter/gather list that was previously created by a call to the [**StorPortBuildScatterGatherList**](storportbuildscattergatherlist.md) routine.

</dd> <dt>

*WriteToDevice* \[in\]
</dt> <dd>

A value that indicates the direction of the DMA transfer that has completed. A value of **TRUE** indicates a transfer from the data buffer to the device, and **FALSE** indicates a transfer from the device to the data buffer.

</dd> </dl>

## Return value

**StorPortPutScatterGatherList** returns one of the following status codes:



| Return code                                                                                                     | Description                                                                          |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/>          |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | Indicates that the routine released the scatter/gather list successfully.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The *HwDeviceExtension* that was passed was **NULL**.<br/>                     |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>      | The call was made at an invalid IRQL.<br/>                                     |



 

## Remarks

The **StorPortPutScatterGatherList** routine does not free the buffer memory for the scatter/gather list, because the miniport driver allocated this memory.

After the **StorPortPutScatterGatherList** routine returns, the miniport driver can reuse the buffer to create a new scatter/gather list by calling the [**StorPortBuildScatterGatherList**](storportbuildscattergatherlist.md) again. If a miniport driver has finished using the buffer for the scatter/gather list, it should free the memory for the buffer after the **StorPortPutScatterGatherList** routine returns. If the miniport driver allocates the buffer memory with the [**StorPortAllocatePool**](storportallocatepool.md) routine, it should free the memory by calling the [**StorPortFreePool**](storportfreepool.md) routine.

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>                 | DISPATCH\_LEVEL<br/>                                                                                                              |
| DDI compliance rules<br/> | [**StorPortIrql**](https://msdn.microsoft.com/library/windows/hardware/hh454266)                                                                                       |



## See also

<dl> <dt>

[**StorPortBuildScatterGatherList**](storportbuildscattergatherlist.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortPutScatterGatherList%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






