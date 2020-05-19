---
title: To Implement the OnSample Callback
description: To Implement the OnSample Callback
ms.assetid: 83bce8ee-6ce8-4079-9c87-2314824b1946
keywords:
- Advanced Systems Format (ASF),implementing OnStatus callback
- ASF (Advanced Systems Format),implementing OnStatus callback
- Advanced Systems Format (ASF),OnStatus callback
- ASF (Advanced Systems Format),OnStatus callback
- Advanced Systems Format (ASF),asynchronous readers
- ASF (Advanced Systems Format),asynchronous readers
- asynchronous readers,implementing OnStatus callback
- OnStatus callback method,implementing
ms.topic: article
ms.date: 05/31/2018
---

# To Implement the OnSample Callback

The asynchronous reader delivers samples to the controlling application in presentation-time order by making calls to the [**IWMReaderCallback::OnSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadercallback-onsample) callback method. When you create an application using the asynchronous reader, you must implement **OnSample** to deal with uncompressed samples. Typically, functions or methods created to render content will be called from within **OnSample**.

Typical implementation of the **OnSample** callback includes the following steps.

1.  Retrieve the location and size of the buffer containing the sample by calling [**INSSBuffer::GetBufferAndLength**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer-getbufferandlength) on the buffer passed as *pSample*.
2.  Branch your logic depending upon the output number. The output number is passed to **OnSample** as *dwOutputNumber*.
3.  Include rendering logic for each output number you want to support. If you are rendering samples from multiple outputs, you may need to synchronize your rendering.

Applications that deliver compressed samples from ASF files need to implement the [**IWMReaderCallbackAdvanced::OnStreamSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadercallbackadvanced-onstreamsample) callback method. **OnStreamSample** functions almost identically to **OnSample**, except that it receives compressed samples by stream number instead of uncompressed samples by output number.

## Related topics

<dl> <dt>

[**IWMReaderCallback Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadercallback)
</dt> <dt>

[**IWMReaderCallbackAdvanced Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadercallbackadvanced)
</dt> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> <dt>

[**Using the Callback Methods**](using-the-callback-methods.md)
</dt> </dl>

 

 




