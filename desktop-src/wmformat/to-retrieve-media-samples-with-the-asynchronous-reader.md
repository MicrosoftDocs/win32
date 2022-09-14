---
title: To Retrieve Media Samples with the Asynchronous Reader
description: To Retrieve Media Samples with the Asynchronous Reader
ms.assetid: 0d8c3099-f068-4074-b717-2f5b9ed9eeb8
keywords:
- Advanced Systems Format (ASF),retrieving media samples
- ASF (Advanced Systems Format),retrieving media samples
- Advanced Systems Format (ASF),asynchronous readers
- ASF (Advanced Systems Format),asynchronous readers
- asynchronous readers,retrieving media samples
ms.topic: article
ms.date: 05/31/2018
---

# To Retrieve Media Samples with the Asynchronous Reader

After you have received the WMT\_OPENED status message in your implementation of [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus), you can begin receiving samples by calling [**IWMReader::Start**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-start). The asynchronous reader delivers samples to your implementation of [**IWMReaderCallback::OnSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadercallback-onsample). Samples are delivered in presentation-time order.

**Start** is an asynchronous call. It will return almost immediately and continue to run on separate threads. The asynchronous reader uses multiple threads when decoding content and delivering samples. When the end of the file is reached, the reader sends a WMT\_EOF status message to your implementation of the **OnStatus** callback. When WMT\_EOF is sent, the reader stops its own processing; you do not need to respond to WMT\_EOF with a call to [**IWMReader::Stop**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-stop).

## Related topics

<dl> <dt>

[**IWMReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreader)
</dt> <dt>

[**To Implement Reader Messages in the OnStatus Callback**](to-implement-reader-messages-in-the-onstatus-callback.md)
</dt> <dt>

[**To Implement the OnSample Callback**](to-implement-the-onsample-callback.md)
</dt> </dl>

 

 




