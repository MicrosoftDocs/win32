---
description: Step 2.
ms.assetid: 8be83564-07ad-47cf-9538-73136f42ba79
title: Step 2. Implement ISpecifyPropertyPages
ms.topic: article
ms.date: 05/31/2018
---

# Step 2. Implement ISpecifyPropertyPages

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

 

 



