---
title: HW\_STARTIO routine
description: The Storport driver calls the HwStorStartIo routine one time for each incoming I/O request.
ms.assetid: 73085ca7-a442-4c16-b1e3-6de048e7f1f7
keywords:
- HwStorStartIo routine Storage Devices
- HW_STARTIO
topic_type:
- apiref
api_name:
- HwStorStartIo
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

# HW\_STARTIO routine

The Storport driver calls the **HwStorStartIo** routine one time for each incoming I/O request.

## Syntax


```C++
HW_STARTIO HwStorStartIo;

BOOLEAN HwStorStartIo(
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

A pointer to the SCSI request block to be started.

</dd> </dl>

## Return value

**HwStorStartIo** returns **TRUE** if the request was successfully initiated. Otherwise, it returns **FALSE**.

## Remarks

**HwStorStartIo** initiates an I/O operation. StorPort is designed to use miniport private data that is prepared in [**HwStorBuildIo**](hwstorbuildio.md) and stored in either the *DeviceExtension* or *Srb-&gt;SrbExtension*. Because **HwStorBuildIo** is called without spin locks, the best driver performance is achieved by preparing as much data as possible in **HwStorBuildIo**.

Storport calls **HwStorStartIo** in the following ways:

-   For [storage non-virtual miniport drivers](https://msdn.microsoft.com/library/windows/hardware/ff566993), depending on the value of **SynchronizationModel** set in [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md), Storport always calls **HwStorStartIo** the same IRQL and uses an internal spin lock to ensure that I/O requests are initiated sequentially. The IRQL is either DISPATCH\_LEVEL (full-duplex mode) or DIRQL (half-duplex mode).

    When handling I/O in half-duplex mode, the **HwStorStartIo** routine does not have to acquire its own spin lock. Also, memory allocation using [**StorPortAllocatePool**](storportallocatepool.md) and mutual exclusion via [**StorPortAcquireSpinLock**](storportacquirespinlock.md) are not allowed in the **HwStorStartIo** routine. In full-duplex mode, **StorPortAllocatePool** and **StorPortAcquireSpinLock** may be used in the **HwStorStartIo** routine.

    If a non-virtual miniport supports the concurrent channels optimization (STOR\_PERF\_CONCURRENT\_CHANNELS set by [**StorPortInitializePerfOpts**](storportinitializeperfopts.md)), multiple calls to **HwStorStartIo** concurrently are possible. In this case, the miniport will need to ensure that any shared resources are protected by a lock. With this performance optimization, Storport will not acquire the StartIo lock prior to calling **HwStorStartIo** and the miniport must provide its own lock if required.

-   For [storage virtual miniport drivers](https://msdn.microsoft.com/library/windows/hardware/ff567012), Storport calls **HwStorStartIo** at any IRQL &lt;= DISPATCH\_LEVEL and does not use an internal spin lock. The **HwStorStartIo** routine may acquire its own spin lock by calling [**StorPortAcquireSpinLock**](storportacquirespinlock.md). Also, calls to [**StorPortAllocatePool**](storportallocatepool.md) are allowed in the **HwStorStartIo** routine of a storage virtual miniport driver.

The SRB is expected to be completed when SCSI status is received. When the Storport driver completes the SRB by calling [**StorPortNotification**](storportnotification.md) with a *NotificationType* of [**RequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567446), an SRB is expected to return one of the following values in the **SrbStatus** field of the Srb:



| Status                          | Indicates                                                                                                          | StorPort Action                                                                                                                                                   | Miniport action                                                                                                                                                                                                                                                                                         |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRB\_STATUS\_SUCCESS<br/> | The Srb was sent and SCSI status (possibly with data) was returned.<br/>                                     | Returns the data and status to the caller.<br/>                                                                                                             | None, except to complete the request by using [**StorPortNotification for RequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567446), probably from the [**HwStorDpcRoutine**](hwstordpcroutine.md).<br/>                                                             |
| SRB\_STATUS\_BUSY<br/>    | There is a temporary problem with sending the Srb (for example, adapter registers or buffers are busy).<br/> | Discards the original Srb and issues a new Srb, including calls to **HwStorBuildIo** and **HwStorStartIo**. All data in the SrbExtension will be lost.<br/> | Because a new SRB is issued, the miniport must make sure that it never issues SRB\_STATUS\_BUSY in the middle of a SCSI transaction. After the transaction is started, it must be completed or canceled. Hardware busy states during the transaction must be handled by the miniport driver.<br/> |



 

The name **HwStorStartIo** is a placeholder to describe the miniport routine set in the **HwStartIo** member of [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md) structure. This structure is passed in the *HwInitializationData* parameter of [**StorPortInitialize**](storportinitialize.md). The actual prototype of this routine is defined in Storport.h as follows:


```
typedef
BOOLEAN
(*PHW_STARTIO) (
  _In_ PVOID  DeviceExtension,
  _In_ PSCSI_REQUEST_BLOCK  Srb
  );
```



Starting in Windows 8, the *Srb* parameter may point to either [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) or [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md). If the function identifier in the **Function** field of *Srb* is **SRB\_FUNCTION\_STORAGE\_REQUEST\_BLOCK**, the SRB is a **STORAGE\_REQUEST\_BLOCK** request structure.

## Examples

To define a **HwStorStartIo** callback routine, you must first provide a function declaration that [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV) and other verification tools require, as shown in the following code example:

To define an **HwStorStartIo** callback function, you must first provide a function declaration that identifies the type of callback function you re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps [Code Analysis for Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454182), [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV), and other verification tools find errors, and it s a requirement for writing drivers for the Windows operating system.

For example, to define a **HwStorStartIo** callback routine that is named *MyHwStartIo*, use the **HW\_STARTIO** type as shown in this code example:


```
HW_STARTIO MyHwStartIo;
```



Then, implement your callback routine as follows:


```
BOOLEAN
MyHwStartIo (
  _In_ PVOID  DeviceExtension,
  _In_ PSCSI_REQUEST_BLOCK  Srb
  );
  {
      ...
  }
```



The **HW\_STARTIO** function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the \_Use\_decl\_annotations\_ annotation to your function definition. The \_Use\_decl\_annotations\_ annotation ensures that the annotations that are applied to the **HW\_STARTIO** function type in the header file are used. For more information about the requirements for function declarations, see [Declaring Functions Using Function Role Types for Storport Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454209). For information about \_Use\_decl\_annotations\_, see [**Annotating Function Behavior**](https://msdn.microsoft.com/windows/desktop/c0aa268d-6fa3-4ced-a8c6-f7652b152e61).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | DISPATCH\_LEVEL (See Remarks section.)<br/>                                                                                       |



## See also

<dl> <dt>

[**HwStorBuildIo**](hwstorbuildio.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md)
</dt> <dt>

[**StorPortInitialize**](storportinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_STARTIO%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






