---
description: Implement the ISpecifyPropertyPages interface in your filter as part of creating a filter property page for a custom DirectShow filter.
ms.assetid: 8be83564-07ad-47cf-9538-73136f42ba79
title: Step 2. Implement ISpecifyPropertyPages
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 2. Implement ISpecifyPropertyPages

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Next, implement the **ISpecifyPropertyPages** interface in your filter. This interface has a single method, **GetPages**, which returns an array of CLSIDs for the property pages that the filter supports. In this example, the filter has a single property page. Start by generating the CLSID and declaring it in your header file:


```C++
// Always create new GUIDs! Never copy a GUID from an example.
DEFINE_GUID(CLSID_SaturationProp, 0xa9bd4eb, 0xded5, 
0x4df0, 0xba, 0xf6, 0x2c, 0xea, 0x23, 0xf5, 0x72, 0x61);
```



Now implement the **GetPages** method:


```C++
class CGrayFilter : public ISaturation,
                    public ISpecifyPropertyPages, 
                    /* Other inherited classes. */
{
public:
    STDMETHODIMP GetPages(CAUUID *pPages)
    {
        if (pPages == NULL) return E_POINTER;
        pPages->cElems = 1;
        pPages->pElems = (GUID*)CoTaskMemAlloc(sizeof(GUID));
        if (pPages->pElems == NULL) 
        {
            return E_OUTOFMEMORY;
        }
        pPages->pElems[0] = CLSID_SaturationProp;
        return S_OK;
    }
};

/* ... */

}
```



Allocate memory for the array using **CoTaskMemAlloc**. The caller will release the memory.

Next: [Step 3. Support QueryInterface](step-3--support-queryinterface.md).

## Related topics

<dl> <dt>

[Creating a Filter Property Page](creating-a-filter-property-page.md)
</dt> </dl>

 

 



