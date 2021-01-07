---
description: Step 5.
ms.assetid: 7c715129-5bdf-468f-96cd-a46ab9c97f4c
title: Step 5. Store a Pointer to the Filter
ms.topic: article
ms.date: 05/31/2018
---

# Step 5. Store a Pointer to the Filter

Override the [**CBasePropertyPage::OnConnect**](cbasepropertypage-onconnect.md) method to store a pointer to the filter. The following example queries the *pUnk* parameter for the filter's custom ISaturation interface:


```C++
HRESULT CGrayProp::OnConnect(IUnknown *pUnk)
{
    if (pUnk == NULL)
    {
        return E_POINTER;
    }
    ASSERT(m_pGray == NULL);
    return pUnk->QueryInterface(IID_ISaturation, 
        reinterpret_cast<void**>(&m_pGray));
}
```



Next: [Step 6. Initialize the Dialog](step-6--initialize-the-dialog.md).

## Related topics

<dl> <dt>

[Creating a Filter Property Page](creating-a-filter-property-page.md)
</dt> </dl>

 

 



