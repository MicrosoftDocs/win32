---
title: HW\_BUILDIO routine
description: The HwStorBuildIo routine processes the SRB with unsynchronized access to shared system data structures before passing it to HwStorStartIo.
ms.assetid: ebbb8289-5996-4d99-98b6-e95fd9dc7ec9
keywords:
- HwStorBuildIo routine Storage Devices
- HW_BUILDIO
topic_type:
- apiref
api_name:
- HwStorBuildIo
api_location:
- Storport.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HW\_BUILDIO routine

The **HwStorBuildIo** routine processes the SRB with unsynchronized access to shared system data structures before passing it to [**HwStorStartIo**](hwstorstartio.md).

## Syntax


```C++
HW_BUILDIO HwStorBuildIo;

BOOLEAN HwStorBuildIo(
   IN PVOID               DeviceExtension,
   IN PSCSI_REQUEST_BLOCK Srb 
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* 
</dt> <dd>

A pointer to the miniport driver's per HBA storage area.

</dd> <dt>

*Srb* 
</dt> <dd>

A pointer to the SCSI request block (SRB) to be processed.

</dd> </dl>

## Return value

**HwStorBuildIo** returns **TRUE** to inform the caller that StorPort should call the [**HwStorStartIo**](hwstorstartio.md) routine if StorPort considers the LUN ready to receive I/O. **HwStorBuildIo** returns **FALSE** to inform the caller that the SRB should not be passed to **HwStorStartIo**. In such cases, the miniport driver must complete the SRB by calling [**StorPortNotification**](storportnotification.md) with a notification type of **RequestComplete**. This can be done in **HwStorBuildIo** or elsewhere in the miniport driver, as long as the SRB is completed before the timeout that is specified in the **TimeOutValue** field of the SRB structure.

## Remarks

The name **HwStorBuildIo** is just a placeholder for the miniport function that is pointed to by the **HwBuildIo** member in the [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md) structure. The actual prototype of this routine is defined in Storport.h as follows:


```
typedef
BOOLEAN
HW_BUILDIO (
  _In_ PVOID DeviceExtension,
  _In_ PSCSI_REQUEST_BLOCK  Srb
  );
```



The port driver calls the **HwStorBuildIo** routine at DISPATCH IRQL without holding any spin locks. Because of this, memory allocation using [**StorPortAllocatePool**](storportallocatepool.md) and mutual exclusion via [**StorPortAcquireSpinLock**](storportacquirespinlock.md) are allowed in **HwStorBuildIo**. In a multiprocessor environment, more than one **HwStorBuildIo** can be active at a time, so the miniport driver is required to synchronize access to system resources, which may be in contention if more than one instance of **HwStorBuildIo** is active at any given time.

By completed time-consuming I/O setup activities in **HwStorBuildIo** instead of in [**HwStorStartIo**](hwstorstartio.md), the miniport driver enables greater I/O concurrency and therefore improves I/O throughput. For highest performance, miniport drivers are expected to do as much preprocessing as possible in **HwStorBuildIo** so that it can send requests to the HBA via **HwStorStartIo** in as short amount of time as possible. Preprocessed data and state can be stored in either the *DeviceExtension* or *SrbExtension* structures. Only modifications to unique portions of the *DeviceExtension* must occur since no locks are held. **HwStorBuildIo** and **HwStorStartIo** receive the following Srb function types:



| Srb function                                   | Expected action                                                                                                                                                                                                                                                                                                                                    | Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRB\_FUNCTION\_EXECUTE\_SCSI <br/>       | Sends a CDB to the specified bus/target/lun.<br/>                                                                                                                                                                                                                                                                                            | Srb-&gt;DataTransferLength is valid for all Cdbs. <br/> Srb-&gt;DataBuffer is **NULL** for read and write requests . To access the associated data, either use [**StorPortGetScatterGatherList**](storportgetscattergatherlist.md) (for Dma transfers) or [**StorPortGetSystemAddress**](storportgetsystemaddress.md) (for program controlled I/O ) to get the Scatter Gather list or the virtual address of the buffer.<br/> For other requests, Srb-&gt;Databuffer points to the data that is associated with the Srb.<br/> Srb-&gt;PathId is valid and represents the pathid given to Storport in [**StorPortNotification**](storportnotification.md) (BusChange). Writers of miniport drivers need to use pathid as an index into a table of busses within the miniport. <br/> Srb-&gt;TargetId and Srb-&gt;Lun are valid.<br/> |
| SRB\_FUNCTION\_IO\_CONTROL <br/>         | Miniport defined.<br/>                                                                                                                                                                                                                                                                                                                       | Srb-&gt;DataTransferLength and Srb-&gt;DataBuffer are valid if set by the requester.<br/> Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SRB\_FUNCTION\_RESET\_LOGICAL\_UNIT<br/> | Reset the specified logical unit (if the device is capable).<br/>                                                                                                                                                                                                                                                                            | Srb-&gt;DataTransferLength and Srb-&gt;DataBuffer are invalid.<br/> Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SRB\_FUNCTION\_RESET\_DEVICE <br/>       | Reset the specified Scsi Target.<br/>                                                                                                                                                                                                                                                                                                        | Srb-&gt;DataTransferLength and Srb-&gt;DataBuffer, Srb-&gt;Lun are invalid.<br/> Srb-&gt;PathId and Srb-&gt;TargetId are valid.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| SRB\_FUNCTION\_RESET\_BUS <br/>          | Reset all of the targets on the specified SCSI bus.<br/>                                                                                                                                                                                                                                                                                     | Only Srb-&gt;PathId is valid.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| SRB\_FUNCTION\_FLUSH <br/>               | Only performed by the miniport driver if it sets **CachesData** == **TRUE** in the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md). Instructs the miniport driver to flush all cached data.<br/>                                                                                                       | Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SRB\_FUNCTION\_SHUTDOWN<br/>             | Only performed by the miniport driver if it sets **CachesData** == **TRUE** in the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md). Instructs the miniport driver to flush all cached data preparatory to shut down.<br/>                                                                              | Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SRB\_FUNCTION\_DUMP\_POINTERS<br/>       | This request is sent to a Storport virtual miniport driver that is used to control the disk that holds the crash dump data. The request supplies information needed for the miniport driver to support crash dump and hibernation.<br/> Starting with Windows 8, non-virtual miniport drivers can optionally receive this request<br/> | Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SRB\_FUNCTION\_FREE\_DUMP\_POINTERS<br/> | Starting with Windows 8, this request is sent to the miniport to free and resources allocated during the SRB\_FUNCTION\_DUMP\_POINTERS request.<br/>                                                                                                                                                                                         | Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

Starting in Windows 8, the *Srb* parameter may point to either [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) or [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md). If the function identifier in the **Function** field of *Srb* is **SRB\_FUNCTION\_STORAGE\_REQUEST\_BLOCK**, the SRB is a **STORAGE\_REQUEST\_BLOCK** request structure.

For more information about what you can and cannot do safely in this miniport driver routine, see [Unsynchronized HwStorBuildIo Routine](https://msdn.microsoft.com/library/windows/hardware/ff567985).

## Examples

To define an **HwStorBuildIo** callback function, you must first provide a function declaration that identifies the type of callback function you re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps [Code Analysis for Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454182), [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV), and other verification tools find errors, and it s a requirement for writing drivers for the Windows operating system.

For example, to define a **HwStorBuildIo** callback routine that is named *MyHwBuildIo*, use the **HW\_BUILDIO** type as shown in this code example:


```
HW_BUILDIO MyHwBuildIo;
```



Then, implement your callback routine as follows:


```
_Use_decl_annotations_
BOOLEAN
MyHwBuildIo (
  _In_ PVOID  DeviceExtension,
  _In_ PSCSI_REQUEST_BLOCK  Srb
  );
  {
      ...
  }
```



The **HW\_BUILDIO** function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the \_Use\_decl\_annotations\_ annotation to your function definition. The \_Use\_decl\_annotations\_ annotation ensures that the annotations that are applied to the **HW\_BUILDIO** function type in the header file are used. For more information about the requirements for function declarations, see [Declaring Functions Using Function Role Types for Storport Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454209). For information about \_Use\_decl\_annotations\_, see [**Annotating Function Behavior**](https://msdn.microsoft.com/windows/desktop/c0aa268d-6fa3-4ced-a8c6-f7652b152e61).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | DISPATCH\_LEVEL (See Remarks section.)<br/>                                                                                       |



## See also

<dl> <dt>

[**HwStorStartIo**](hwstorstartio.md)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md)
</dt> <dt>

[**StorPortNotification**](storportnotification.md)
</dt> <dt>

[**StorPortAllocatePool**](storportallocatepool.md)
</dt> <dt>

[**StorPortAcquireSpinLock**](storportacquirespinlock.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_BUILDIO%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






