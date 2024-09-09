---
title: Using Two-Pass Encoding (Windows Media Format 11 SDK)
description: Using Two-Pass Encoding
ms.assetid: 55fc768b-15f0-4236-ad0d-3792ccaa9b4f
keywords:
- Advanced Systems Format (ASF),two-pass encoding
- ASF (Advanced Systems Format),two-pass encoding
- two-pass encoding,about
- 2-pass encoding,about
- codecs,two-pass encoding
- two-pass encoding,IWMWriterPreprocess interface
- 2-pass encoding,IWMWriterPreprocess interface
- IWMWriterPreprocess
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Two-Pass Encoding (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Some codecs support two-pass encoding for certain formats. In some cases, a codec requires that a specified format be encoded using two passes. When two-pass encoding is used, you send the samples for the stream to the codec before the encoding pass. The codec analyzes the samples and configures the encoding pass based on the analysis. This results in a more efficiently encoded file.

To determine whether a codec supports one-pass encoding, or two-pass, or both, for a given format, call [**IWMCodecInfo3::SetCodecEnumerationSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmcodecinfo3-setcodecenumerationsetting) with g\_wszNumPasses and the appropriate value, and then enumerate the formats to see if the one you want is returned. For more information about the Windows Media codecs that support two-pass encoding, see [Choosing an Encoding Method](choosing-an-encoding-method.md).

You can use two-pass encoding with the Windows Media Format SDK by calling methods of the [**IWMWriterPreprocess**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterpreprocess) interface.

In cases where two-pass encoding is required for a particular format, but the application fails to perform a preprocessing pass, the first call to [**WriteSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-writesample) will fail with NS\_E\_INVALID\_NUM\_PASSES.

The following example function demonstrates how to perform two-pass encoding. This function is called after the writer has been set with a profile and started. For more information about using this code, see [Using the Code Examples](using-the-code-examples.md).


```C++
HRESULT PreProcess(IWMWriter* pWriter, DWORD dwInputNum)
{
    HRESULT hr        = S_OK;
    DWORD   dwMaxPass = 0;

    IWMWriterPreprocess* pPreProc = NULL;

    // Get the writer preprocessor interface.
    hr = pWriter->QueryInterface(IID_IWMWriterPreprocess, 
                                 (void**) &pPreProc);
    GOTO_EXIT_IF_FAILED(hr);

    // Check that the input can be preprocessed.
    hr = pPreProc->GetMaxPreprocessingPasses(dwInputNum,0, &dwMaxPass);
    GOTO_EXIT_IF_FAILED(hr);

    if(dwMaxPass == 0)
    {
        hr = NS_E_INVALID_REQUEST;
        goto Exit;
    }

    // Set the number of preprocessing passes to the maximum.
    hr = pPreProc->SetNumPreprocessingPasses(dwInputNum, 0, dwMaxPass);
    GOTO_EXIT_IF_FAILED(hr);

    // Call BeginWriting before calling BeginPreprocessingPass
    hr = pWriter->BeginWriting();

    // Start preprocessing the first pass.
    hr = pPreProc->BeginPreprocessingPass(dwInputNum, 0);
    GOTO_EXIT_IF_FAILED(hr);

    // TODO: Make repeated calls to pPreProc->PreprocessSample to
    // preprocess all the samples in the stream.

    // End preprocessing.
    hr = pPreProc->EndPreprocessingPass(dwInputNum, 0);
    GOTO_EXIT_IF_FAILED(hr);

    // TODO: If the maximum number of preprocessing passes is greater
    // than one, repeat the preprocessing steps for each pass.

Exit:
    SAFE_RELEASE(pPreProc);
    Return hr;
}

```



## Related topics

<dl> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




