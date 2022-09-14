---
title: To Use Writer Postview
description: To Use Writer Postview
ms.assetid: 9da3c749-f6bd-43b5-9eff-3a637ddef048
keywords:
- Advanced Systems Format (ASF),writer postview
- ASF (Advanced Systems Format),writer postview
- Advanced Systems Format (ASF),postviewing
- ASF (Advanced Systems Format),postviewing
- writer postview
- postviewing
ms.topic: article
ms.date: 05/31/2018
---

# To Use Writer Postview

The writer object provides postviewing capabilities so that you can verify written content without having to set up the reader object. The writer object does not support postviewing for audio content.

The writer postviewer works in much the same way as the asynchronous reader object, only with fewer features. For detailed information about reading digital media, see [Reading ASF Files](reading-asf-files.md).

To implement the postviewer, perform the following steps.

1.  Implement the [**IWMWriterPostViewCallback::OnPostViewSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterpostviewcallback-onpostviewsample) callback. This method is essentially the same as [**IWMReaderCallback::OnSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadercallback-onsample) except that it specifies stream numbers instead of outputs.
2.  Set up for writing as usual.
3.  Obtain a pointer to the [**IWMWriterPostView**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterpostview) interface of the writer object by calling **IWMWriter::QueryInterface**.
4.  Set the callback for the postviewer to use by calling [**IWMWriterPostView::SetPostViewCallback**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterpostview-setpostviewcallback).
5.  For each stream for which you want to receive postview samples, call [**IWMWriterPostView::SetReceivePostViewSamples**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterpostview-setreceivepostviewsamples). You can check to see whether a stream is set to receive postview samples by calling [**IWMWriterPostView::GetReceivePostViewSamples**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterpostview-getreceivepostviewsamples).
6.  You can manipulate the sample formats, just like you would the output formats in the reader object or synchronous reader object.
7.  When you start writing the file, you will begin to receive samples in your implementation of the **OnPostViewSample** callback method.

## Related topics

<dl> <dt>

[**IWMWriterPostViewCallback Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterpostviewcallback)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




