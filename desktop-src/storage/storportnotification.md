---
title: StorPortNotification routine
description: The miniport driver uses the StorPortNotification routine to notify the Storport driver of certain events and conditions.
ms.assetid: 3f361f50-3ca2-4fb6-828c-27928b50cf55
keywords:
- StorPortNotification routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortNotification
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortNotification routine

The miniport driver uses the **StorPortNotification** routine to notify the Storport driver of certain events and conditions.

The **StorPortNotification** routine takes a variable number of parameters depending on the notification type specified.

## Syntax


```C++
VOID StorPortNotification(
   IN SCSI_NOTIFICATION_TYPE NotificationType,
   IN PVOID                  HwDeviceExtension,
   ...                       arguments
);
```



## Parameters

<dl> <dt>

*NotificationType* 
</dt> <dd>

Specifies the notification type, which can be one of the following values.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Notification type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BufferOverrunDetected<br/></td>
<td>This notification type has no arguments and gives the miniport driver an opportunity to bugcheck the system if it detects a corruption.<br/></td>
</tr>
<tr class="even">
<td>BusChangeDetected<br/></td>
<td>Indicates that a target device might have been added or removed from a dynamic bus. To use this notification type, include an optional PathId parameter to indicate the SCSI port or bus where the change was detected. <br/> <span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VOID StorPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_opt_ UCHAR                  PathId
);</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="odd">
<td><p>IoTargetRequestServiceTime</p></td>
<td><p>Indicates to Storport the amount of time that was required to process a specified request.</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VOID StorPortNotification(
  _In_ SCSI_NOTIFICATION_TYPE NotificationType,
  _In_ PVOID                  HwDeviceExtension,
  _In_ ULONGLONG              Duration,
  _In_ PSCSI_REQUEST_BLOCK    Srb
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><p>LinkDown</p></td>
<td><p>Indicates that the link is down and will probably be down for some time. StorPort will pause the adapter in response to this notification.</p></td>
</tr>
<tr class="odd">
<td><p>LinkUp</p></td>
<td><p>Indicates that the link has been restored. StorPort restarts the adapter so that it can resume operation in response to this notification. Miniport drivers should not send this notification unless the link is down.</p></td>
</tr>
<tr class="even">
<td><p>QueryTickCount</p></td>
<td><p>This notification type returns a LARGE_INTEGER that holds the value from [<strong>KeQueryTickCount</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553071). The value returned in TickCount is the count of the interval timer interrupts that have occurred since the system was booted</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VOID StorPortNotification(
  _In_    SCSI_NOTIFICATION_TYPE NotificationType,
  _In_    PVOID                  HwDeviceExtension,
  _Inout_ PLARGE_INTEGER         TickCount
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><p>RequestComplete</p></td>
<td><p>Indicates that the given SRB has finished. After this notification is sent, the port driver owns the request. The Srb parameter represents a pointer to the completed SCSI request block.</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VOID StorPortNotification(
  _In_ SCSI_NOTIFICATION_TYPE NotificationType,
  _In_ PVOID                  HwDeviceExtension,
  _In_ PSCSI_REQUEST_BLOCK    Srb
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><p>RequestTimerCall</p></td>
<td><p>Indicates that the miniport driver requires the port driver to call the miniport driver's [<strong>HwStorTimer</strong>](hwstortimer.md) routine in the requested number of microseconds.</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VOID StorPortNotification(
  _In_ SCSI_NOTIFICATION_TYPE NotificationType,
  _In_ PVOID                  HwDeviceExtension,
  _In_ PHW_TIMER              HwStorTimer,
  _In_ ULONG                  MiniportTimerValue
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><p>ResetDetected</p></td>
<td><p>Indicates that the HBA has detected a reset on the bus. After this notification is sent, the miniport driver is still responsible for completing any active requests. The port driver will manage all required bus-reset delays.</p></td>
</tr>
<tr class="even">
<td><p>WMIEvent</p></td>
<td><p>Indicates that the miniport driver has detected an event for which one or more WMI data consumers are registered.</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VOID StorPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_     PWNODE_EVENT_ITEM      WMIEvent,
  _In_     UCHAR                  PathId,
  _In_opt_ UCHAR                  TargetId,
  _In_opt_ UCHAR                  Lun
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><p>WMIReregister</p></td>
<td><p>Indicates that the miniport driver has changed the data items or the number of instances of a given data block that was previously registered by calling [<strong>IoWMIRegistrationControl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550480).</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VOID StorPortNotification(
  _In_     SCSI_NOTIFICATION_TYPE NotificationType,
  _In_     PVOID                  HwDeviceExtension,
  _In_     UCHAR                  PathId,
  _In_opt_ UCHAR                  TargetId,
  _In_opt_ UCHAR                  Lun
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

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*arguments* 
</dt> <dd>

Specifies the arguments corresponding to the notification type.

</dd> </dl>

## Return value

None.

## Remarks

StorPortNotification is a polymorphic function that handles many different types of requests, making it difficult to annotate in a manner that would cover all possible uses. Because StorPortNotification returns VOID, the scanning engine should assume the LockHandle was acquired as asked.

## Requirements



|                                 |                                                                                                                                                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl>                                                       |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                                                                                    |
| Library<br/>              | <dl> <dt>Storport.lib</dt> </dl>                                                                                                       |
| DDI compliance rules<br/> | [**StorPortNotification2**](https://msdn.microsoft.com/library/windows/hardware/hh454268), [**StorPortStatusPending**](https://msdn.microsoft.com/library/windows/hardware/hh454275), [**StorPortTimer**](https://msdn.microsoft.com/library/windows/hardware/hh454276) |



## See also

<dl> <dt>

[**StorPortInitialize**](storportinitialize.md)
</dt> <dt>

[**StorPortNotification for BufferOverrunDetected**](https://msdn.microsoft.com/library/windows/hardware/ff567434)
</dt> <dt>

[**StorPortNotification for BusChangeDetected**](https://msdn.microsoft.com/library/windows/hardware/ff567437)
</dt> <dt>

[**StorPortNotification for LinkDown**](https://msdn.microsoft.com/library/windows/hardware/ff567439)
</dt> <dt>

[**StorPortNotification for LinkUp**](https://msdn.microsoft.com/library/windows/hardware/ff567441)
</dt> <dt>

[**StorPortNotification for QueryTickCount**](https://msdn.microsoft.com/library/windows/hardware/ff567445)
</dt> <dt>

[**StorPortNotification for RequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567446)
</dt> <dt>

[**StorPortNotification for RequestTimerCall**](https://msdn.microsoft.com/library/windows/hardware/ff567447)
</dt> <dt>

[**StorPortNotification for ResetDetected**](https://msdn.microsoft.com/library/windows/hardware/ff567450)
</dt> <dt>

[**StorPortNotification for WMIEvent**](https://msdn.microsoft.com/library/windows/hardware/ff567452)
</dt> <dt>

[**StorPortNotification for WMIReregister**](https://msdn.microsoft.com/library/windows/hardware/ff567456)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortNotification%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






