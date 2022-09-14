---
title: Building Filter Graphs in DRM-Enabled Applications
description: Building Filter Graphs in DRM-Enabled Applications
ms.assetid: 447bec2a-0982-4a05-87bb-aed6db684b36
keywords:
- Windows Media Format SDK,building filter graphs
- Windows Media Format SDK,DirectShow
- Windows Media Format SDK,DRM-enabled applications
- Advanced Systems Format (ASF),building filter graphs
- ASF (Advanced Systems Format),building filter graphs
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- Advanced Systems Format (ASF),DRM-enabled applications
- ASF (Advanced Systems Format),DRM-enabled applications
- DirectShow,building filter graphs
- DirectShow,DRM-enabled applications
- digital rights management (DRM),DirectShow
- DRM (digital rights management),DirectShow
- digital rights management (DRM),building filter graphs
- DRM (digital rights management),building filter graphs
ms.topic: article
ms.date: 05/31/2018
---

# Building Filter Graphs in DRM-Enabled Applications

If your DirectShow application supports playback of DRM-protected files, then you generally should not use **RenderFile** to create the filter graph because there is no way to specify which DRM rights you are requesting before the file is opened. The WM ASF Reader by default asks for only playback rights. The filter is not added to the graph, and is therefore not discoverable by applications, until a file is successfully opened.

To build a DRM-enabled playback graph using the [WM ASF Reader](wm-asf-reader-filter.md), you must instantiate the filter using **CoCreateInstance**, add it to the filter graph using **IGraphBuilder::AddFilter**, configure it, and then render its output pins. This technique is demonstrated in the PlayWndASF sample. When you build the graph in this way, you already have the **IBaseFilter** pointer that can be used to call **QueryService** to obtain **IWMDRMWriter**. However, this interface is not available until the Windows Media Format SDK reader object is created internally by the WM ASF Reader. The first opportunity the application has to set DRM rights is in its WMT\_NO\_RIGHTS\_EX event handler, as shown in this code snippet:


```C++
case WMT_NO_RIGHTS_EX:

    IServiceProvider *pServiceProvider;
    IWMDRMReader pWMDRMReader;
    JIF(g_pReader->QueryInterface(IID_IServiceProvider, (void **) &pServiceProvider));
    JIF(pServiceProvider->QueryService(IID_IWMDRMReader, IID_IWMDRMReader, (void **) &pWMDRMReader)); 
    SAFE_RELEASE(pServiceProvider);

    // Set the rights we want for this file. These are the actions we 
    // might want to perform on the file. Here we ask for two rights only.
    // In a real application you should enable users to select which 
    // rights they want.
    hr = pWMDRMReader->SetDRMProperty(g_wszWMDRM_Rights, WMT_TYPE_STRING,
        BYTE*) wszRights, (sizeof(wszRights) / sizeof(wszRights[0])) * 2);
    SAFE_RELEASE(pWMDRMReader);
    if (FAILED(hr))
    {
       Msg(TEXT("SetDRMProperty Failed!  hr=0x%x\n"), hr);
       return hr;
    }
    // Now proceed with license acqusition.
    if( pEventData->pData )
    {
        hr = HandleNoRightsEx(pEventData->hrStatus, 
        (WM_GET_LICENSE_DATA *)pEventData->pData);
    }
    else
    {
         hr = E_FAIL;
    }
    break;

```



## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**DRM Attribute List**](drm-attribute-list.md)
</dt> <dt>

[**DRM Properties**](drm-properties.md)
</dt> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> <dt>

[**IWMDRMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader)
</dt> <dt>

[**IWMDRMWriter**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmwriter)
</dt> </dl>

 

 




