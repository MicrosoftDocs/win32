---
description: Custom File Formats
ms.assetid: 4dc77cfa-0cab-4055-9e11-f036e2d1dcca
title: Custom File Formats
ms.topic: article
ms.date: 05/31/2018
---

# Custom File Formats

If you have a custom mux or file-writer filter that supports your own file format, you can specify the CLSID as the first parameter of the [**ICaptureGraphBuilder2::SetOutputFileName**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-setoutputfilename) method:


```C++
IBaseFilter *pMux = 0;
IFileSinkFilter *pSink = 0;
hr = pBuild->SetOutputFileName(&CLSID_MyCustomMuxFilter, 
    L"C:\\VidCap.avi", &pMux, &pSink);
```



For more information about this usage, see [**ICaptureGraphBuilder2::SetOutputFileName**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-setoutputfilename).

## Related topics

<dl> <dt>

[Capturing Video to a File](capturing-video-to-a-file.md)
</dt> </dl>

 

 



