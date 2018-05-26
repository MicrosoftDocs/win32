---
Description: Capturing to Multiple Files
ms.assetid: 6073a891-e9f5-442d-a2d9-3a7b97f7f735
title: Capturing to Multiple Files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Capturing to Multiple Files

After you have captured some video to a file, you can switch to a new file by stopping the graph and setting the file name on the [File Writer](file-writer-filter.md) filter. Call the [**IFileSinkFilter::SetFileName**](/windows/win32/Strmif/nf-strmif-ifilesinkfilter-setfilename?branch=master) method on the File Writer. You can get a pointer to the [**IFileSinkFilter**](/windows/win32/Strmif/nn-strmif-ifilesinkfilter?branch=master) interface when you build the graph, through the *pSink* parameter of the SetOutputFileName method. The following code shows how to do this:


```C++
IBaseFilter *pMux;
IFileSinkFilter *pSink
hr = pBuild->SetOutputFileName(&amp;MEDIASUBTYPE_Avi, L"C:\\YourFileName.avi", 
    &amp;pMux, &amp;pSink);
if (SUCCEEDED(hr))
{
    hr = pBuild->RenderStream(&amp;PIN_CATEGORY_CAPTURE, &amp;MEDIATYPE_Video, 
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

 

 



