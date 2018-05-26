---
title: StorPortFreeMdl routine
description: The StorPortFreeMdl routine frees a memory descriptor list (MDL) describing non-paged pool memory.
ms.assetid: 5cbdda76-c02d-4fd4-8fa9-a783375ea292
keywords:
- StorPortFreeMdl routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortFreeMdl
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

# StorPortFreeMdl routine

The **StorPortFreeMdl** routine frees a memory descriptor list (MDL) describing non-paged pool memory.

## Syntax


```C++
ULONG StorPortFreeMdl(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID Mdl
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*Mdl* \[in\]
</dt> <dd>

A pointer to the MDL to be freed.

</dd> </dl>

## Return value

StorPortFreeMdl returns one of the following status codes:



| Return code                                                                                                     | Description                                                                 |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/> |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | Indicates that the MDL was freed successfully.<br/>                   |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The pointer to the MDL is **NULL**.<br/>                              |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>      | The call was made at an invalid IRQL.<br/>                            |



 

## Remarks

A miniport driver calls the **StorPortFreeMdl** routine to free the MDL that was allocated in a previous call to [**StorPortAllocateMdl**](storportallocatemdl.md).

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>                 | &lt;=DISPATCH\_LEVEL<br/>                                                                                                         |
| DDI compliance rules<br/> | [**StorPortIrql**](https://msdn.microsoft.com/library/windows/hardware/hh454266)                                                                                       |



## See also

<dl> <dt>

[**StorPortAllocateMdl**](storportallocatemdl.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortFreeMdl%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






