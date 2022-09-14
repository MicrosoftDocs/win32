---
title: To Implement Reader Messages in the OnStatus Callback
description: To Implement Reader Messages in the OnStatus Callback
ms.assetid: f0535e02-a283-48bf-9242-ebcc17a6fb66
keywords:
- Advanced Systems Format (ASF),implementing reader messages
- ASF (Advanced Systems Format),implementing reader messages
- Advanced Systems Format (ASF),OnStatus callback
- ASF (Advanced Systems Format),OnStatus callback
- Advanced Systems Format (ASF),asynchronous readers
- ASF (Advanced Systems Format),asynchronous readers
- asynchronous readers,implementing reader messages
- OnStatus callback method,implementing reader messages
ms.topic: article
ms.date: 05/31/2018
---

# To Implement Reader Messages in the OnStatus Callback

To use the asynchronous reader to deliver content from an ASF file, you must implement a minimum of two callback methods, [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) and [**IWMReaderCallback::OnSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadercallback-onsample). This section describes how to implement **IWMStatusCallback::OnStatus** to receive and respond to status messages sent by the reader. **OnStatus** is used by other objects in the Windows Media Format SDK. For general information about **OnStatus**, see [Using the OnStatus Callback](using-the-onstatus-callback.md).

When using the asynchronous reader, you must trap the following messages in **IWMStatusCallback::OnStatus**.



| Status message | Description                                     |
|----------------|-------------------------------------------------|
| WMT\_OPENED    | Sent when file opening operations are complete. |
| WMT\_CLOSED    | Sent when file closing operations are complete. |



 

You should use the status messages listed above to control execution of your reading application. For example, you must wait until receiving the **WMT\_OPENED** message to start the reader or call other methods that require the reader to have a file ready. Frequently, applications built with the asynchronous reader use an event to signal the completion of asynchronous calls and proceed with processing. For more information about using events for signaling completion of operations, see [Using Events with Asynchronous Calls](using-events-with-asynchronous-calls.md).

Many other messages are sent to **OnStatus** by the reader object to enable the application to respond to the status of reading operations. The possible status message values are defined in the [**WMT\_STATUS**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_status) enumeration type.

## Related topics

<dl> <dt>

[**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus)
</dt> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> <dt>

[**Using the OnStatus Callback**](using-the-onstatus-callback.md)
</dt> </dl>

 

 




