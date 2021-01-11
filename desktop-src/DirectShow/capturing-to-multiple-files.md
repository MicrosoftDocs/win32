---
description: Capturing to Multiple Files
ms.assetid: 6073a891-e9f5-442d-a2d9-3a7b97f7f735
title: Capturing to Multiple Files
ms.topic: article
ms.date: 05/31/2018
---

# Capturing to Multiple Files

After you have captured some video to a file, you can switch to a new file by stopping the graph and setting the file name on the [File Writer](file-writer-filter.md) filter. Call the [**IFileSinkFilter::SetFileName**](/windows/desktop/api/Strmif/nf-strmif-ifilesinkfilter-setfilename) method on the File Writer. You can get a pointer to the [**IFileSinkFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter) interface when you build the graph, through the *pSink* parameter of the SetOutputFileName method. The following code shows how to do this:


```C++
IBaseFilter *pMux;
IFileSinkFilter *pSink
hr = pBuild->SetOutputFileName(&MEDIASUBTYPE_Avi, L"C:\\YourFileName.avi", 
    &pMux, &pSink);
if (SUCCEEDED(hr))
{
    hr = pBuild->RenderStream(&PIN_CATEGORY_CAPTURE, &MEDIATYPE_Video, 
        pCap, NULL, pMux);

    if (SUCCEEDED(hr))
    {
        pControl->Run();
        /* Wait awhile, then stop the graph. */
        pControl->Stop();
        // Change the file name and run the graph again.
        pSink->SetFileName(L"YourFileName02.avi", 0);
        pControl->Run();
    }
    pMux->Release();
    pSink->Release();
}
```



## Related topics

<dl> <dt>

[Capturing Video to a File](capturing-video-to-a-file.md)
</dt> </dl>

 

 



