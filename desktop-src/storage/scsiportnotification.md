---
title: ScsiPortNotification routine
description: The ScsiPortNotification routine informs the operating system-specific port driver of certain events, such as when a miniport driver completes a request or is ready to start another SRB, as well as when the HBA indicates certain SCSI error conditions that occurred during an operation.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: 27da3881-4c47-492c-868e-ce72210e9d6f
keywords:
- ScsiPortNotification routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortNotification
api_location:
- scsiport.lib
- scsiport.dll
- storport.lib
- storport.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScsiPortNotification routine

The **ScsiPortNotification** routine informs the operating system-specific port driver of certain events, such as when a miniport driver completes a request or is ready to start another SRB, as well as when the HBA indicates certain SCSI error conditions that occurred during an operation.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiPortNotification(
   IN SCSI_NOTIFICATION_TYPE NotificationType,
   IN PVOID                  HwDeviceExtension
);
```



## Parameters

<dl> <dt>

*NotificationType* 
</dt> <dd>

Specifies the type of notification, which can be one of the following.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Notification Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RequestComplete</strong><br/></td>
<td>Indicates that the given <em>Srb</em> has finished. If this value is set, <strong>ScsiPortNotification</strong> requires one additional parameter: the address of the SRB. After this notification, the operating system-specific port driver owns the request. The miniport driver must not access the <em>Srb</em>, and it must not pass the <em>Srb</em> to another routine (such as <strong>ScsiPortLogError</strong>).<br/> Syntax: <br/> <span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>VOID ScsiPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_ PSCSI_REQUEST_BLOCK    Srb
);</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="even">
<td><p><strong>NextRequest</strong></p></td>
<td><p>Indicates the miniport driver is ready for another request to a target that is not currently busy. This notification should be sent by the miniport driver as soon as the driver is ready for another request. Usually, this notification is sent from the [<strong>HwScsiStartIo</strong>](hwscsistartio.md) routine but, sometimes, from the [<strong>HwScsiInterrupt</strong>](hwscsiinterrupt.md) (or [<strong>HwScsiEnableInterruptsCallback</strong>](hwscsienableinterruptscallback.md)) routine.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NextLuRequest</strong></p></td>
<td><p>Indicates that the HBA is ready for another request for the specified logical unit. If this value is set, <strong>ScsiPortNotification</strong> requires three additional parameters: (1) the path ID, (2) the target ID, and (3) the logical unit number. This value should be used only if the HBA can queue multiple requests and support auto-request sense or tagged queuing.</p>
<p>Syntax:</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>VOID ScsiPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_                        PathId,
  _In_opt_                        TargetId,
  _In_opt_                        Lun
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><p><strong>ResetDetected</strong></p></td>
<td><p>Indicates that the HBA has detected a reset on the SCSI bus. After this notification, the miniport driver is still responsible for completing any active requests. The SCSI port driver will manage all required bus-reset delays.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CallEnableInterrupts</strong></p></td>
<td><p>Indicates that the miniport driver requires the operating system-specific port driver to call the miniport driver's [<strong>HwScsiEnableInterruptsCallback</strong>](hwscsienableinterruptscallback.md) routine. If this value is set, <strong>ScsiPortNotification</strong> requires an additional parameter: the entry point for the <em>HwScsiEnableInterruptsCallback</em>. The miniport driver's [<strong>HwScsiInterrupt</strong>](hwscsiinterrupt.md) routine makes this call, <em>after</em> disabling interrupts on the HBA, to defer some interrupt-driven I/O processing if the HBA requires polling or stalling in the ISR. While the callback runs, system interrupts remain enabled but the miniport driver's <em>HwScsiInterrupt</em> routine will not be called. The <em>HwScsiEnableInterruptsCallback</em> is responsible for completing the deferred I/O processing and for calling <strong>ScsiPortNotification</strong> again with <strong>CallDisableInterrupts</strong> and the miniport driver's [<strong>HwScsiDisableInterruptsCallback</strong>](hwscsidisableinterruptscallback.md) entry point.</p>
<p>Syntax:</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>VOID ScsiPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_ PHW_INTERRUPT          HwScsiXxxInterruptsCallback
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><p><strong>CallDisableInterrupts</strong></p></td>
<td><p>Indicates that the miniport driver requires the operating system-specific port driver to call the miniport driver's <em>HwScsiDisableInterruptsCallback</em> routine. If this value is set, <strong>ScsiPortNotification</strong> requires an additional parameter: the entry point for the <em>HwScsiDisableInterruptsCallback</em>. While this callback runs, it cannot be preempted by an interrupt except from a device with a higher priority interrupt than the HBA. In this callback, the miniport driver reenables interrupts on the HBA.</p>
<p>Syntax:</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>VOID ScsiPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_ PHW_INTERRUPT          HwScsiXxxInterruptsCallback
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><p><strong>RequestTimerCall</strong></p></td>
<td><p>Indicates that the miniport driver requires the operating system-specific port driver to call the miniport driver's [<em>HwScsiTimer</em>](hwscsitimer.md) routine in the requested number of microseconds. If this value is set, <strong>ScsiPortNotification</strong> requires two additional parameters: (1) the entry point for the miniport driver's <em>HwScsiTimer</em> routine, and (2) a <em>MiniportTimerValue</em> interval, in microseconds. Note that the resolution of the system timer is approximately 10 milliseconds.</p>
<p>Syntax:</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>VOID ScsiPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_ PHW_TIMER              HwScsiTimer,
  _In_opt_ ULONG                  MiniportTimerValue
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><p><strong>BusChangeDetected</strong></p></td>
<td><p>Indicates that a target device might have been added or removed from a dynamic bus. If this value is set, <strong>ScsiPortNotification</strong> requires an additional parameter: the path ID of the bus on which the change was detected. After this notification, the port driver reenumerates the bus by issuing INQUIRY commands. Bus enumeration is time-consuming and ties up the bus, so a miniport driver should not send this notification unnecessarily</p>
<p>Syntax:</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>VOID ScsiPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_ UCHAR                  PathId
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><p><strong>WMIEvent</strong></p></td>
<td><p>Indicates that the miniport driver has detected an event for which one or more WMI data consumers is registered. If this value is set, <strong>ScsiPortNotification</strong> requires at least three additional arguments: (1) a pointer to a WMI event structure, (2) the size of the event structure, and (3) the path ID of the target device if the event originated from a device, or 0Xff if the event originated from the adapter. If (3) is a path ID, <strong>ScsiPortNotification</strong> requires two additional arguments: (4) the target ID, and (5) the logical unit number (LUN) of the target device.</p>
<p>Syntax for PathId != 0xFF</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>VOID ScsiPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_ PVOID                  WMIEvent,
  _In_opt_ UCHAR                  PathId,
  _In_opt_ UCHAR                  TargetId,
  _In_opt_ UCHAR                  Lun
);</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>Syntax for PathId = 0xFF</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>VOID ScsiPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_ PVOID                  WMIEvent,
  _In_opt_ UCHAR                  PathId
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><p><strong>WMIReregister</strong></p></td>
<td><p>Indicates that the miniport driver has changed the data items or the number of instances of a given data block previously registered by calling <strong>IoWMIRegistrationControl</strong>. If <strong>WMIReregister</strong> is set, <strong>ScsiPortNotification</strong> requires at least two additional arguments: (1) the path ID of the target device to reregister that device, or 0xFF to reregister the adapter. If (1) is a path ID, <strong>ScsiPortNotification</strong> requires two additional arguments: (2) the target ID, and (3) the logical unit number (LUN) of the target device.</p>
<p>Syntax for PathId != 0xFF</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>VOID ScsiPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_ UCHAR                  PathId,
  _In_opt_ UCHAR                  TargetId,
  _In_opt_ UCHAR                  Lun
);</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>Syntax for PathId = 0xFF</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>VOID ScsiPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_ UCHAR                  PathId
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

*HwDeviceExtension* 
</dt> <dd>

Pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the HBA's mapped access ranges. This area is available to the miniport driver in the **DeviceExtension-&gt;HwDeviceExtension** member of the HBA's device object immediately after the miniport driver calls [**ScsiPortInitialize**](scsiportinitialize.md). The port driver frees this memory when it removes the device.

</dd> </dl>

## Return value

None

## Remarks

The **ScsiPortNotification** routine has a different set of optional parameters associated with each *NotificationType*. For a description of the optional parameters associated a particular *NotificationType*, see the reference page associated with that *NotificationType*. The following reference pages provide this information:

<dl>

[**ScsiPortNotification (NotificationType = RequestComplete)**](https://msdn.microsoft.com/library/windows/hardware/ff564680)  
[**ScsiPortNotification (NotificationType = NextRequest)**](https://msdn.microsoft.com/library/windows/hardware/ff564675)  
[**ScsiPortNotification (NotificationType = NextLuRequest)**](https://msdn.microsoft.com/library/windows/hardware/ff564673)  
[**ScsiPortNotification (NotificationType = ResetDetected)**](https://msdn.microsoft.com/library/windows/hardware/ff564689)  
[**ScsiPortNotification (NotificationType = CallEnableInterrupts or CallDisableInterrupts)**](https://msdn.microsoft.com/library/windows/hardware/ff564667)  
[**ScsiPortNotification (NotificationType = RequestTimerCall)**](https://msdn.microsoft.com/library/windows/hardware/ff564686)**)**  
[**ScsiPortNotification (NotificationType = BusChangeDetected)**](https://msdn.microsoft.com/library/windows/hardware/ff564662)  
[**ScsiPortNotification (NotificationType = WMIEvent, PathId != 0xFF)**](https://msdn.microsoft.com/library/windows/hardware/ff564693)  
[**ScsiPortNotification (NotificationType = WMIEvent, PathId = 0xFF)**](https://msdn.microsoft.com/library/windows/hardware/ff564690)  
[**ScsiPortNotification (NotificationType = WMIReregister, PathId != 0xFF)**](https://msdn.microsoft.com/library/windows/hardware/ff564699)  
[**ScsiPortNotification (NotificationType = WMIReregister, PathId = 0xFF)**](https://msdn.microsoft.com/library/windows/hardware/ff564695)  
</dl>

Every miniport driver must call **ScsiPortNotification** twice for each call to the miniport driver's [**HwScsiStartIo**](hwscsistartio.md) routine with an SRB that the miniport driver completes successfully. First, the miniport driver calls **ScsiPortNotification** with the *NotificationType***NextRequest** or with **NextLuRequest** if the miniport driver supports tagged queuing or multiple requests per LU. Then, the miniport driver calls **ScsiPortNotification** with the *NotificationType***RequestComplete** and the request that it has just satisfied.

A miniport driver's *HwScsiInterrupt* routine is most likely to call **ScsiPortNotification** with the *NotificationType***ResetDetected**.

If an HBA requires the miniport driver to use more than a millisecond processing interrupt-driven I/O operations, its *HwScsiInterrupt* routine should disable interrupts on the HBA and call **ScsiPortNotification** with **CallEnableInterrupts** and a driver-supplied *HwScsiEnableInterruptsCallback* routine. This routine, in turn, calls **ScsiPortNotification** with **CallDisableInterrupts** and the corresponding driver-supplied *HwScsiDisableInterruptsCallback*.

A miniport driver that is registered as a WMI data provider can call **ScsiPortNotification** with **WMIEvent** to post an event for which it has previously received an enable request. The port driver queues the event in the interrupt data area of the miniport driver's device extension for later processing at a lower IRQL. Because only a limited number of events can be queued at one time, the miniport driver should use **WMIEvent** to signal exceptional rather than routine conditions, and it should give the port driver time to get back to DISPATCH\_LEVEL between postings, to prevent events from being lost.

## Requirements



|                            |                                                                                                                                                             |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl>                                             |
| Library<br/>         | <dl> <dt>Scsiport.lib; </dt> <dt>Storport.lib</dt> </dl> |
| IRQL<br/>            | (See Remarks section)<br/>                                                                                                                            |



## See also

<dl> <dt>

[*HwScsiTimer*](hwscsitimer.md)
</dt> <dt>

[**HwScsiDisableInterruptsCallback**](hwscsidisableinterruptscallback.md)
</dt> <dt>

[**HwScsiEnableInterruptsCallback**](hwscsienableinterruptscallback.md)
</dt> <dt>

[**ScsiPortCompleteRequest**](scsiportcompleterequest.md)
</dt> <dt>

[**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortNotification%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






