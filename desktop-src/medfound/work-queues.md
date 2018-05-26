---
Description: In Microsoft Media Foundation, a work queue is an efficient way to perform asynchronous operations on another thread.
ms.assetid: 6be05df7-e8ff-4110-8f73-a62eb31fd414
title: Work Queues
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Work Queues

In Microsoft Media Foundation, a work queue is an efficient way to perform asynchronous operations on another thread.

This section contains the following topics.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Using Work Queues](using-work-queues.md)</td>
<td>Describes how an application or component can use work queues to perform asynchronous operations.</td>
</tr>
<tr class="even">
<td>[Writing an Asynchronous Method](writing-an-asynchronous-method.md)</td>
<td>Describes how to write an asynchronous method that follows the Begin/End pattern described in [Asynchronous Callback Methods](asynchronous-callback-methods.md).</td>
</tr>
<tr class="odd">
<td>[Custom Asynchronous Result Objects](custom-asynchronous-result-objects.md)</td>
<td>Describes how to create a custom implementation of the [<strong>IMFAsyncResult</strong>](/windows/win32/mfobjects/nn-mfobjects-imfasyncresult?branch=master) interface.<br/>
<blockquote>
[!Note]<br />
Most applications should use the stock implementation provided by [<strong>MFCreateAsyncResult</strong>](/windows/win32/mfapi/nf-mfapi-mfcreateasyncresult?branch=master). This topic is for applications with advanced requirements.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[Work Queue and Threading Improvements](media-foundation-work-queue-and-threading-improvements.md)</td>
<td>Describes improvements in Windows 8 for work queues and threading in the Media Foundation platform.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> </dl>

 

 




