---
title: Adding Sinks to the Writer
description: Adding Sinks to the Writer
ms.assetid: 714b84f0-5ad8-4e00-aa77-e866e65b43b0
keywords:
- Advanced Systems Format (ASF),adding sinks to the writer
- ASF (Advanced Systems Format),adding sinks to the writer
- Advanced Systems Format (ASF),sinks
- ASF (Advanced Systems Format),sinks
- Advanced Systems Format (ASF),writer sinks
- ASF (Advanced Systems Format),writer sinks
- sinks,adding to the writer
- writer sinks,adding
ms.topic: article
ms.date: 05/31/2018
---

# Adding Sinks to the Writer

Writer sinks are separate objects from the writer and must be added to the writer to be used. If you are writing to a file, you can simply call [**IWMWriter::SetOutputFilename**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setoutputfilename), which will set up the file sink automatically. Otherwise, to add a sink to the writer, call the [**IWMWriterAdvanced::AddSink**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-addsink) method. **AddSink** requires a pointer to the [**IWMWriterSink**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwritersink) interface of the sink.

When you are finished using a sink, you should close it by calling the appropriate method, depending on the type of sink, and then remove it from the writer by calling [**IWMWriterAdvanced::RemoveSink**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-removesink).

The following example code shows how to create a writer file sink and add it to the writer. For more information about using this code, see [Using the Code Examples](using-the-code-examples.md).


```C++
HRESULT AddFileSink(IWMWriterFileSink** ppFileSink, IWMWriter* pWriter)
{
    HRESULT hr = S_OK;
    IWMWriterSink*     pSinkBase       = NULL;
    IWMWriterAdvanced* pWriterAdvanced = NULL;

    hr = CreateWriterFileSink(ppFileSink);
    GOTO_EXIT_IF_FAILED(hr);

    hr = *ppFileSink->QueryInterface(IID_IWMWriterSink, 
                                     (void**) &pSinkBase);
    GOTO_EXIT_IF_FAILED(hr);

    hr = pWriter->QueryInterface(IID_IWMWriterAdvanced,
                                 (void**) &pWriterAdvanced);
    GOTO_EXIT_IF_FAILED(hr);

    hr = pWriterAdvanced->AddSink(pSinkBase);
    GOTO_EXIT_IF_FAILED(hr);

Exit:
    SAFE_RELEASE(pSinkBase);
    SAFE_RELEASE(pWriterAdvanced);
    return hr;
}

```



## Related topics

<dl> <dt>

[**Getting Error Messages from a Sink**](getting-error-messages-from-a-sink.md)
</dt> <dt>

[**IWMWriterAdvanced Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




