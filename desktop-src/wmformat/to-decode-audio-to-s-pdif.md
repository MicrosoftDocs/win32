---
title: To Decode Audio to S/PDIF
description: To Decode Audio to S/PDIF
ms.assetid: b56c2d0a-a7c6-44f8-832a-bbbe7ae053e6
keywords:
- Windows Media Format SDK,decoding audio to S/PDIF
- Windows Media Format SDK,Sony/Philips Digital Interconnect Format (S/PDIF)
- Advanced Systems Format (ASF),decoding audio to S/PDIF
- ASF (Advanced Systems Format),decoding audio to S/PDIF
- Advanced Systems Format (ASF),Sony/Philips Digital Interconnect Format (S/PDIF)
- ASF (Advanced Systems Format),Sony/Philips Digital Interconnect Format (S/PDIF)
- Sony/Philips Digital Interconnect Format (S/PDIF),decoding audio
- S/PDIF (Sony/Philips Digital Interconnect Format),decoding audio
- decoding audio
ms.topic: article
ms.date: 05/31/2018
---

# To Decode Audio to S/PDIF

Audio encoded with the Windows Media Audio 9 Professional codec can be decoded to Sony/Philips Digital Interconnect Format (S/PDIF). To generate S/PDIF output, perform the following steps:

1.  Open a file that contains a Windows Media Audio 9 Professional stream by calling the [**IWMReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-open) method.
2.  Identify the output number of the stream that you want. For more information, see [To Identify Output Numbers](to-identify-output-numbers.md).
3.  Call the [**IWMReaderAdvanced2::SetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setoutputsetting) method to configure S/PDIF output. Use g\_wszEnableWMAProSPDIFOutput for the setting name. The data type is **WMT\_TYPE\_BOOL**; set the value to **TRUE** to enable S/PDIF output.
4.  Get the output properties interface ([**IWMOutputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmoutputmediaprops)) of the desired output format by calling the [**IWMReader::GetOutputFormat**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputformat) method. For more information about enumerating output formats, see [Assigning Output Formats](assigning-output-formats.md).
5.  Set the output format by calling the [**IWMReader::SetOutputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-setoutputprops) method. Pass in a pointer to the **IWMOutputMediaProps** interface obtained in step 4.
6.  Make any other configuration changes and begin playback.

> [!Note]  
> You can perform the preceding steps on the synchronous reader by using the corresponding methods of the [**IWMSyncReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader) interface.

 

The following example code demonstrates how to set an audio stream to output audio as S/PDIF data. This function assumes that a file has already been loaded in the reader and that the output number has been identified. For more information about using this code, see [Using the Code Examples](using-the-code-examples.md).


```C++
HRESULT SetSPDIF(DWORD dwOutputNum, IWMReader* pReader)
{
    HRESULT hr = S_OK;

    IWMReaderAdvanced2*  pReaderAdv   = NULL;
    IWMOutputMediaProps* pOutputProps = NULL; 

    BOOL fValue = TRUE;

    // Get the advanced reader interface.
    hr = pReader->QueryInterface(IID_IWMReaderAdvanced2,
                                 (void**)&pReaderAdv);
    GOTO_EXIT_IF_FAILED(hr);

    // Set S/PDIF output.
    hr = pReaderAdv->SetOutputSetting(dwOutputNum, 
                                      g_wszEnableWMAProSPDIFOutput, 
                                      WMT_TYPE_BOOL, 
                                      (BYTE*)&fValue, 
                                      sizeof(BOOL));
    GOTO_EXIT_IF_FAILED(hr);

    // Get the first output format for the stream.
    // NOTE: You could also enumerate the available output formats
    // and pick one to use.

    hr = pReader->GetOutputFormat(dwOutputNum, 0, &pOutputProps);
    GOTO_EXIT_IF_FAILED(hr);

    // Set the output properties back on the reader.
    hr = pReader->SetOutputProps(dwOutputNum, pOutputProps);

Exit:
    SAFE_RELEASE(pReaderAdv);
    SAFE_RELEASE(pOutputProps);

    return hr;
}
```



## Related topics

<dl> <dt>

[**Advanced Topics**](advanced-topics.md)
</dt> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> <dt>

[**IWMReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreader)
</dt> <dt>

[**IWMReaderAdvanced2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2)
</dt> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> </dl>

 

 




