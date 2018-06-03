---
title: StorPortBuildScatterGatherList routine
description: The StorPortBuildScatterGatherList routine creates a scatter/gather list for the specified data buffer.
ms.assetid: cdea67aa-14fa-45c1-8af0-8db48042b1b2
keywords:
- StorPortBuildScatterGatherList routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortBuildScatterGatherList
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

# StorPortBuildScatterGatherList routine

The **StorPortBuildScatterGatherList** routine creates a scatter/gather list for the specified data buffer.

## Syntax


```C++
ULONG StorPortBuildScatterGatherList(
  _In_    PVOID                        HwDeviceExtension,
  _In_    PVOID                        Mdl,
  _In_    PVOID                        CurrentVa,
  _In_    ULONG                        Length,
  _In_    PPOST_SCATTER_GATHER_EXECUTE ExecutionRoutine,
  _In_    PVOID                        Context,
  _In_    BOOLEAN                      WriteToDevice,
  _Inout_ PVOID                        ScatterGatherBuffer,
  _In_    ULONG                        ScatterGatherBufferLength
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

A pointer to a memory descriptor list (MDL) that describes the memory pages associated with the data buffer.

</dd> <dt>

*CurrentVa* \[in\]
</dt> <dd>

The virtual address of the data buffer.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

The length, in bytes, of the data buffer.

</dd> <dt>

*ExecutionRoutine* \[in\]
</dt> <dd>

A pointer to a miniport driver-supplied *ExecutionRoutine*. The Storport driver calls this routine after creating the scatter/gather list. The miniport driver should perform all operations that make use of the scatter/gather list inside the execution routine, not in the code that follows the call to the **StorPortBuildScatterGatherList** routine.

An *ExecutionRoutine* is declared as follows:


```
VOID
ExecutionRoutine (
    IN PVOID  *DeviceObject,
    IN PVOID  *Irp,
    IN PSTOR_SCATTER_GATHER_LIST  ScatterGather,
    IN PVOID  Context
    );
```



<dl> <dt>

<span id="DeviceObject"></span><span id="deviceobject"></span><span id="DEVICEOBJECT"></span>*DeviceObject*
</dt> <dd>

Miniport drivers should ignore this parameter.

</dd> <dt>

<span id="Irp"></span><span id="irp"></span><span id="IRP"></span>*Irp*
</dt> <dd>

Miniport drivers should ignore this parameter.

</dd> <dt>

<span id="ScatterGather"></span><span id="scattergather"></span><span id="SCATTERGATHER"></span>*ScatterGather*
</dt> <dd>

A pointer to a [**STOR\_SCATTER\_GATHER\_LIST**](stor-scatter-gather-list.md) structure that contains the scatter/gather list for the specified data buffer.

</dd> <dt>

<span id="Context"></span><span id="context"></span><span id="CONTEXT"></span>*Context*
</dt> <dd>

The context value specified in the **StorPortBuildScatterGatherList** function's *Context* parameter.

</dd> </dl>

The Storport driver calls a miniport driver's *ExecutionRoutine* at IRQL = DISPATCH\_LEVEL.

</dd> <dt>

*Context* \[in\]
</dt> <dd>

A context value that the port driver passes to the execution routine specified in the *ExecutionRoutine* parameter. The execution routine uses this value to uniquely identify the request.

</dd> <dt>

*WriteToDevice* \[in\]
</dt> <dd>

A value that indicates the direction of the DMA transfer. A value of **TRUE** indicates a transfer that is from the data buffer to the device, and a value of **FALSE** indicates a transfer that is from the device to the data buffer.

</dd> <dt>

*ScatterGatherBuffer* \[in, out\]
</dt> <dd>

A pointer to a miniport-supplied buffer that receives the scatter/gather list. A miniport driver can allocate memory for this buffer by calling the [**StorPortAllocatePool**](storportallocatepool.md) routine.

</dd> <dt>

*ScatterGatherBufferLength* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by the *ScatterGatherBuffer* parameter.

</dd> </dl>

## Return value

**StorPortBuildScatterGatherList** returns one of the following values:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>STOR_STATUS_NOT_IMPLEMENTED</strong></dt> </dl></td>
<td>This function is not implemented on the active operating system.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>STOR_STATUS_SUCCESS</strong></dt> </dl></td>
<td>Indicates that the routine created the scatter/gather list successfully.<br/>
<blockquote>
[!Important]<br />
See 'Remarks'.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>STOR_STATUS_INVALID_PARAMETER</strong></dt> </dl></td>
<td>The <em>HwDeviceExtension</em> passed was <strong>NULL</strong>.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>STOR_STATUS_INVALID_IRQL</strong></dt> </dl></td>
<td>The call was made at an invalid IRQL.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>STOR_STATUS_INSUFFICIENT_RESOURCES</strong></dt> </dl></td>
<td>The system has insufficient map registers available for the transfer.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>STOR_STATUS_BUFFER_TOO_SMALL</strong> </dt> </dl></td>
<td>The Length parameter is too big to fit within the buffer.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

The miniport driver calls [**StorPortPutScatterGatherList**](storportputscattergatherlist.md) to release the resources that **StorPortBuildScatterGatherList** allocated while constructing the scatter/gather list.

The miniport driver must call [**StorPortPutScatterGatherList**](storportputscattergatherlist.md) before freeing or reusing the memory it allocated for the scatter/gather list.

> [!Note]  
> If **StorPortBuildScatterGatherList** returns STOR\_STATUS\_SUCCESS, then the callback in *ExecutionRoutine* was successfully queued to execute after the scatter/gather list is created. The miniport must not assume that *ExecutionRoutine* was called or that the scatter/gather list is ready when **StorPortBuildScatterGatherList** returns. If necessary, the miniport can synchronize the execution of code following **StorPortBuildScatterGatherList** with the callback in *ExecutionRoutine* to ensure that the scatter/gather list is available.

 

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | DISPATCH\_LEVEL<br/>                                                                                                              |



## See also

<dl> <dt>

[**StorPortAllocatePool**](storportallocatepool.md)
</dt> <dt>

[**StorPortPutScatterGatherList**](storportputscattergatherlist.md)
</dt> <dt>

[**STOR\_SCATTER\_GATHER\_LIST**](stor-scatter-gather-list.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortBuildScatterGatherList%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






