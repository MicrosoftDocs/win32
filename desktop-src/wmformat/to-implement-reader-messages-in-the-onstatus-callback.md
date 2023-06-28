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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Implement Reader Messages in the OnStatus Callback

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




