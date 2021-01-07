---
description: Step 9.
ms.assetid: 3e476422-ab76-4a2b-af9b-d9d065d79e5b
title: Step 9. Disconnect the Property Page
ms.topic: article
ms.date: 05/31/2018
---

# Step 9. Disconnect the Property Page

Override the [**CBasePropertyPage::OnDisconnect**](cbasepropertypage-ondisconnect.md) method to release any interfaces that you obtained in the **OnConnect** method. Also, if the user dismisses the property sheet without committing the changes, you should restore the original values if they have changed. There is no "OnCancel" method that gets called when the user cancels, so you need to keep track of whether the user has called **OnApplyChanges**. This example uses the m\_lVal variable, described earlier:


```C++
HRESULT CGrayProp::OnDisconnect(void)
{
    if (m_pGray)
    {
        // If the user clicked OK, m_lVal holds the new value.
        // Otherwise, if the user clicked Cancel, m_lVal is the old value.
        m_pGray->SetSaturation(m_lVal);  
        m_pGray->Release();
        m_pGray = NULL;
    }
    return S_OK;
}
```



Next: [Step 10. Support COM Registration](step-10--support-com-registration.md)

## Related topics

<dl> <dt>

[Creating a Filter Property Page](creating-a-filter-property-page.md)
</dt> </dl>

 

 



