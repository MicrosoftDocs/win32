---
title: Getting Error Messages from a Sink
description: Getting Error Messages from a Sink
ms.assetid: c948d06f-7728-4d89-8dc4-40d192c94099
keywords:
- Advanced Systems Format (ASF),error messages from sinks
- ASF (Advanced Systems Format),error messages from sinks
- Advanced Systems Format (ASF),sinks
- ASF (Advanced Systems Format),sinks
- sinks,error messages
- error messages
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting Error Messages from a Sink

The writer object does not send messages to the [**IWMStatusCallback::OnStatus**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus?branch=master) callback method. However, you can set writer sinks to send messages to OnStatus. Each sink must be set to deliver status separately, but all sinks can report to the same callback.

To set a sink to deliver status messages to **OnStatus**, call the [**IWMRegisterCallback::Advise**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmregistercallback-advise?branch=master) method.

The following example code demonstrates how to set all of the sinks to deliver status messages to an **OnStatus** callback. In this example, the index of each sink will be used as the context parameter so that the **OnStatus** method can differentiate between messages from the different sinks. For more information about using this code, see [Using the Code Examples](using-the-code-examples.md).


```C++
HRESULT SetSinksForStatus (IWMWriter* pWriter, IWMStatusCallback* pStatus)
{
    HRESULT hr          = S_OK;
    DWORD   cSinks      = 0;
    DWORD   dwSinkIndex = 0;

    IWMWriterAdvanced*   pWriterAdvanced = NULL;
    IWMWriterSink*       pSink           = NULL;
    IWMRegisterCallback* pRegisterCallbk = NULL;

    // Get the advanced writer interface.
    hr = pWriter->QueryInterface(IID_IWMWriterAdvanced, 
                                 (void**)&amp;pWriterAdvanced);
    GOTO_EXIT_IF_FAILED(hr);

    // Get the number of sinks that are added to the writer object.
    hr = pWriterAdvanced->GetSinkCount(&amp;cSinks);
    GOTO_EXIT_IF_FAILED(hr);

    // Loop through all of the sinks.
    for(dwSinkIndex = 0; dwSinkIndex < cSinks; dwSinkIndex++)
    {
        // Get the base interface for the next sink.
        hr = pWriterAdvanced->GetSink(dwSinkIndex, &amp;pSink);
        GOTO_EXIT_IF_FAILED(hr);

        // Get the callback registration interface for the sink.
        hr = pSink->QueryInterface(IID_IWMRegisterCallback,
                                   (void**)&amp;pRegisterCallbk);
        GOTO_EXIT_IF_FAILED(hr);

        // Register the OnStatus callback.
        hr = pRegisterCallbk->Advise(pStatus, (void*) &amp;dwSinkIndex);
        GOTO_EXIT_IF_FAILED(hr);

        // Release for the next iteration.
        SAFE_RELEASE(pSink);
        SAFE_RELEASE(pRegisterCallbk);
    } // end for dwSinkIndex

Exit:
    SAFE_RELEASE(pSink);
    SAFE_RELEASE(pRegisterCallbk);
    SAFE_RELEASE(pWriterAdvanced);
    return hr;
}

```



## Related topics

<dl> <dt>

[**IWMRegisterCallback Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmregistercallback?branch=master)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




