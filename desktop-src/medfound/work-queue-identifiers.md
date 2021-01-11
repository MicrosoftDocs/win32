---
description: The following constants identify the standard Media Foundation work queues.
ms.assetid: c769f876-83ca-4b04-a054-22fa7146310e
title: Work Queue Identifiers (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Work Queue Identifiers

The following constants identify the standard Media Foundation work queues.

Applications should use MFASYNC\_CALLBACK\_QUEUE\_MULTITHREADED or use a work queue obtained from [**MFLockSharedWorkQueue**](/windows/desktop/api/mfapi/nf-mfapi-mflocksharedworkqueue) if they want to control the execution priority. Note that the default platform work queue priorities can dynamically change when an application calls [**RegisterPlatformWithMMCSS**](/windows/desktop/api/mfapi/nf-mfapi-mfregisterplatformwithmmcss). For more information about work queues, see [Work Queues](work-queues.md).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant/value</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="MFASYNC_CALLBACK_QUEUE_STANDARD"></span><span id="mfasync_callback_queue_standard"></span><dl> <dt><strong>MFASYNC_CALLBACK_QUEUE_STANDARD</strong></dt> <dt>0x00000001</dt> </dl></td>
<td style="text-align: left;">In most cases, applications should use <strong>MFASYNC_CALLBACK_QUEUE_MULTITHREADED</strong>.<br/> This work queue is used for synchronous operations. Using the standard work queue may run the risk of deadlocking. Applications can create a private synchronous queue on top of the multithreaded queue by using <a href="/windows/desktop/api/mfapi/nf-mfapi-mfallocateserialworkqueue"><strong>MFAllocateSerialWorkQueue</strong></a>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="MFASYNC_CALLBACK_QUEUE_RT"></span><span id="mfasync_callback_queue_rt"></span><dl> <dt><strong>MFASYNC_CALLBACK_QUEUE_RT</strong></dt> <dt>0x00000002</dt> </dl></td>
<td style="text-align: left;">Not for general application use.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="MFASYNC_CALLBACK_QUEUE_IO"></span><span id="mfasync_callback_queue_io"></span><dl> <dt><strong>MFASYNC_CALLBACK_QUEUE_IO</strong></dt> <dt>0x00000003</dt> </dl></td>
<td style="text-align: left;">Not for general application use.<br/> This work queue is used internally for I/O operations such as reading files and reading from the network.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="MFASYNC_CALLBACK_QUEUE_TIMER"></span><span id="mfasync_callback_queue_timer"></span><dl> <dt><strong>MFASYNC_CALLBACK_QUEUE_TIMER</strong></dt> <dt>0x00000004</dt> </dl></td>
<td style="text-align: left;">Not for general application use.<br/> This work queue is used for periodic callbacks and scheduled work items. The following functions put work items in this queue:<br/>
<ul>
<li><a href="/windows/desktop/api/mfapi/nf-mfapi-mfaddperiodiccallback"><strong>MFAddPeriodicCallback</strong></a></li>
<li><a href="/windows/desktop/api/mfapi/nf-mfapi-mfscheduleworkitem"><strong>MFScheduleWorkItem</strong></a></li>
<li><a href="/windows/desktop/api/mfapi/nf-mfapi-mfscheduleworkitemex"><strong>MFScheduleWorkItemEx</strong></a></li>
</ul></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="MFASYNC_CALLBACK_QUEUE_MULTITHREADED"></span><span id="mfasync_callback_queue_multithreaded"></span><dl> <dt><strong>MFASYNC_CALLBACK_QUEUE_MULTITHREADED</strong></dt> <dt>0x00000005</dt> </dl></td>
<td style="text-align: left;">This multithreaded work queue should be used in most cases. <br/> This work queue is used for asynchronous operations throughout Media Foundation.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="MFASYNC_CALLBACK_QUEUE_LONG_FUNCTION"></span><span id="mfasync_callback_queue_long_function"></span><dl> <dt><strong>MFASYNC_CALLBACK_QUEUE_LONG_FUNCTION</strong></dt> <dt>0x00000007</dt> </dl></td>
<td style="text-align: left;">Not for general application use. Applications should instead use <strong>MFASYNC_CALLBACK_QUEUE_MULTITHREADED</strong>.<br/></td>
</tr>
</tbody>
</table>



In addition, the following constants are used in connection with work queues.



| Constant/value                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                          |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MFASYNC_CALLBACK_QUEUE_UNDEFINED"></span><span id="mfasync_callback_queue_undefined"></span><dl> <dt>**MFASYNC\_CALLBACK\_QUEUE\_UNDEFINED**</dt> <dt>0x00000000</dt> </dl>           | Undefined work queue.<br/>                                                                                                                                                                                                                                                                                                     |
| <span id="MFASYNC_CALLBACK_QUEUE_PRIVATE_MASK"></span><span id="mfasync_callback_queue_private_mask"></span><dl> <dt>**MFASYNC\_CALLBACK\_QUEUE\_PRIVATE\_MASK**</dt> <dt>0xFFFF0000</dt> </dl> | Bit mask to distinguish platform work queues from those created by calling [**MFAllocateWorkQueue**](/windows/desktop/api/mfapi/nf-mfapi-mfallocateworkqueue).<br/> For a work queue created by [**MFAllocateWorkQueue**](/windows/desktop/api/mfapi/nf-mfapi-mfallocateworkqueue), the following value is nonzero:<br/> `(identifier & MFASYNC_CALLBACK_QUEUE_PRIVATE_MASK)`<br/> |
| <span id="MFASYNC_CALLBACK_QUEUE_ALL"></span><span id="mfasync_callback_queue_all"></span><dl> <dt>**MFASYNC\_CALLBACK\_QUEUE\_ALL**</dt> <dt>0xFFFFFFFF</dt> </dl>                             | All platform work queues.<br/>                                                                                                                                                                                                                                                                                                 |



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Constants](media-foundation-constants.md)
</dt> <dt>

[Work Queues](work-queues.md)
</dt> <dt>

[Work Queue and Threading Improvements](media-foundation-work-queue-and-threading-improvements.md)
</dt> </dl>

 

 




