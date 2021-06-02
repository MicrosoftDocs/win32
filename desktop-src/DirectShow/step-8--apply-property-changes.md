---
description: Step 8.
ms.assetid: c54745ef-beeb-40b6-9db6-6e3b5da860f8
title: Step 8. Apply Property Changes
ms.topic: article
ms.date: 05/31/2018
---

# Step 8. Apply Property Changes

Override the [**CBasePropertyPage::OnApplyChanges**](cbasepropertypage-onapplychanges.md) method to commit any property changes. In this example, the m\_lNewVal variable is updated whenever the user scrolls the slider bar. The **OnApplyChanges** method copies this value into the m\_lVal variable, overwriting the original value:


```C++
HRESULT CGrayProp::OnApplyChanges(void)
{
    m_lVal = m_lNewVal;
    return S_OK;
} 
```



Next: [Step 9. Disconnect the Property Page](step-9--disconnect-the-property-page.md).

## Related topics

<dl> <dt>

[Creating a Filter Property Page](creating-a-filter-property-page.md)
</dt> </dl>

 

 



