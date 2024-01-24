---
description: Video Color Source
ms.assetid: e6addd55-06ca-4d4b-b2b0-fde281fab244
title: Video Color Source
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Color Source

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Video Color Source creates a continuous video image of a solid color.

Class ID (CLSID): **{0CFDD070-581A-11D2-9EE6-006008039E37}**

CLSID Variable Name: **CLSID\_ColorSource**

Properties



| Property | Type      | Default | Description                                   |
|----------|-----------|---------|-----------------------------------------------|
| "Color"  | **DWORD** | 0       | Specifies the color to generate. See Remarks. |



 

## Remarks

The Video Color Source is used with source objects. First, create a new source object. Then set the source object's subobject GUID to CLSID\_ColorSource, by calling the [**IAMTimelineObj::SetSubObjectGUID**](iamtimelineobj-setsubobjectguid.md) method.

To set the color, create a [Property Setter](property-setter.md) object and apply the "Color" property at time zero. The value of this property is a hexadecimal number with the format *0xAARRGGBB*, where *AA* is the alpha value, *RR* is the red value, *GG* is the green value, and *BB* is the blue value. Alpha values range from 0x00 (transparent) to 0xFF (opaque). The property is static and must be applied at time zero.

If you do not specify the alpha value, it defaults to zero (transparent). In a 32-bit-color video project, this will cause transitions or effects that use alpha to render the Video Color Source as completely transparent. To be safe, always specify the alpha. For example, opaque black is **0xFF000000**.

The following code example shows how to use this object. For more information about using [**IPropertySetter**](ipropertysetter.md), see [Setting Properties on Effects and Transitions](setting-properties-on-effects-and-transitions.md):


```C++
DWORD           dwYellow = 0xFFFF00;
IAMTimelineObj  *pSource = NULL;

// Create the source.
HRESULT hr = pTimeline->CreateEmptyNode(&pSource, TIMELINE_MAJOR_TYPE_SOURCE);
if (SUCCEEDED(hr))
{
    hr = pSource->SetStartStop(0, 50000000);
}

if (SUCCEEDED(hr))
{
    hr = pSource->SetSubObjectGUID(CLSID_ColorSource);
}

// Create a property setter.
if (SUCCEEDED(hr))
{
    IPropertySetter *pProp = NULL;
    
    hr = CoCreateInstance(CLSID_PropertySetter, NULL, CLSCTX_INPROC_SERVER, 
        IID_PPV_ARGS(&pProp));

    if SUCCEEDED(hr))
    {
        // Set the color.    
        DEXTER_PARAM param;
        DEXTER_VALUE val;

        param.Name = SysAllocString(OLESTR("Color"));
        param.dispID = 0;
        param.nValues = 1;

        if (param.Name == NULL)
        {
            hr = E_OUTOFMEMORY;
        }
        else
        {
            val.v.vt = VT_I4;
            val.v.lVal = dwYellow;
            val.rt = 0;  // Time must be zero.
            val.dwInterp = DEXTERF_JUMP;

            hr = pProp->AddProp(param, &val);
            
            SysFreeString(param.Name);
        }

        if (SUCCEEDED(hr))
        {
            hr = pSource->SetPropertySetter(pProp); 
        }
        pProp->Release();
    }
}
```



The following example shows the XML representation of the object created in the previous example. In this case the [**param**](param-element.md) element does not support [**at**](at-element.md) or [**linear**](linear-element.md) elements, because the object does not support dynamic properties:


```C++
<clip start="0" stop="5" clsid="{0CFDD070-581A-11D2-9EE6-006008039E37}">
    <param name="Color" value="16776960"/>
</clip>
```



 

 



