---
description: Step 9.
ms.assetid: 3e476422-ab76-4a2b-af9b-d9d065d79e5b
title: Step 9. Disconnect the Property Page
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 9. Disconnect the Property Page

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 



