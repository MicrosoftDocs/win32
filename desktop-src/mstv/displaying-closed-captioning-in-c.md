---
title: Displaying Closed Captioning in C
description: Displaying Closed Captioning in C
ms.assetid: 699f4021-1c9c-4855-8295-5b84bc512252
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Displaying Closed Captioning in C

This topic applies to Windows XP or later.

To display closed captioning (CC), the application must activate the closed captioning feature. For analog television, the application must also active the data services feature. You can find the features by enumerating the Video Control's available features collection. To activate a feature, add it to the active features collection.

To activate the closed captioning feature, perform the following steps:

Using **CoCreateInstance**, create an empty features collection as an [MSVidFeatures](msvidfeatures.md) object.

Retrieve the available features from the Video Control, by calling the [**IMSVidCtl::get\_FeaturesAvailable**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-get_featuresavailable?branch=master) method.

Loop through the returned collection, comparing each feature's CLSID against the CLSID of the CC feature. With analog TV, do the same for the data services feature. Call the [**IMSVidDevice::get\_\_ClassID**](/windows/win32/segment/nf-segment-imsviddevice-get__classid?branch=master) method to obtain the CLSID of each feature.

When you find a matching feature, add it to the features collection created in Step 1. Also, query the CC feature for the [**IMSVidClosedCaptioning**](/windows/win32/segment/nn-segment-imsvidclosedcaptioning?branch=master) interface and store this for later use.

Set the new features collection as the Video Control's active features collection, by calling the [**IMSVidCtl::put\_FeaturesActive**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-put_featuresactive?branch=master) method.

Perform these steps before building the graph; that is, before calling [**IMSVidCtl::Build**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-build?branch=master) or [**IMSVidCtl::Run**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-run?branch=master). If the graph is already built, call [**IMSVidCtl::Decompose**](/windows/previous-versions/msvidctl/nf-msvidctl-imsvidctl-decompose?branch=master) to tear it down, and build it again afterward.

Once the CC feature is in the active features collection, you can build the graph. Enable or disable closed captioning at any time by calling the [**IMSVidClosedCaptioning::put\_Enable**](/windows/win32/segment/nf-segment-imsvidclosedcaptioning-put_enable?branch=master) method. By default, the feature is disabled.

> [!Note]  
> *Activating* the CC feature causes the Video Control to build a filter graph that is capable of receiving and displaying closed captions. *Enabling* the CC feature causes the captions to be displayed.

 

The following code example activates and enables CC. It assumes that **m\_pVidControl** is a member variable in the control container, which holds a pointer to the Video Control's [**IMSVidCtl**](/windows/previous-versions/msvidctl/nn-msvidctl-imsvidctl?branch=master) interface. The *bWantDataSvc* parameter specifies whether to include data services. For brevity, the example performs only minimal error checking.


```C++
HRESULT CMyContainer::ActivateCC(bool bWantDataSvc)
{
    HRESULT hr = S_OK;
    _ASSERT(m_pVidControl != NULL);  
    
    // Get the available features.
    CComPtr<IMSVidFeatures> pFeatures;
    hr = m_pVidControl->get_FeaturesAvailable(&amp;pFeatures);
    if (SUCCEEDED(hr))
    {
        // Create an empty features collection.
        CComPtr<IMSVidFeatures> pActiveFeatures;
        hr = pActiveFeatures.CoCreateInstance(__uuidof(MSVidFeatures), 
            NULL, CLSCTX_INPROC_SERVER);
        
        // Enumerate the features and look for CC.
        long lCount = 0;
        pFeatures->get_Count(&amp;lCount);
        for (long ix = 0; ix < lCount; ix++)
        {
            CComVariant var(ix);
            CComPtr<IMSVidFeature> pFeature;
            GUID clsid;
            hr =  pFeatures->get_Item(var, &amp;pFeature);
            hr = pFeature->get__ClassID(&amp;clsid);
            if (clsid == __uuidof(MSVidClosedCaptioning))
            {
                // Found CC, add it to the collection.
                hr = pActiveFeatures->Add(pFeature);
                CComQIPtr<IMSVidClosedCaptioning> pCC(pFeature);
                if (pCC) {
                    hr = pCC->put_Enable(VARIANT_TRUE);
                }
            }
            else if (bWantDataSvc &amp;&amp; clsid == __uuidof(MSVidDataServices))
            {
                hr = pActiveFeatures->Add(pFeature);
            }
        }
        // Set this collection as the active features collection.
        hr = m_pVidControl->put_FeaturesActive(pActiveFeatures);
    }
    return hr;
}
```



 

 




