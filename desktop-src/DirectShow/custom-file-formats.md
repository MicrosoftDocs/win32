---
Description: Custom File Formats
ms.assetid: 4dc77cfa-0cab-4055-9e11-f036e2d1dcca
title: Custom File Formats
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Custom File Formats

If you have a custom mux or file-writer filter that supports your own file format, you can specify the CLSID as the first parameter of the [**ICaptureGraphBuilder2::SetOutputFileName**](/windows/win32/Strmif/nf-strmif-icapturegraphbuilder2-setoutputfilename?branch=master) method:


```C++
IBaseFilter *pMux = 0;
IFileSinkFilter *pSink = 0;
hr = pBuild->SetOutputFileName(&amp;CLSID_MyCustomMuxFilter, 
    L"C:\\VidCap.avi", &amp;pMux, &amp;pSink);
```



For more information about this usage, see [**ICaptureGraphBuilder2::SetOutputFileName**](/windows/win32/Strmif/nf-strmif-icapturegraphbuilder2-setoutputfilename?branch=master).

## Related topics

<dl> <dt>

[Capturing Video to a File](capturing-video-to-a-file.md)
</dt> </dl>

 

 



