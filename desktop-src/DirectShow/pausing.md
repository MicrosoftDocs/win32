---
description: Pausing
ms.assetid: 945e1b1a-2557-4be2-bfdb-bb11ac7c3fe8
title: Pausing
ms.topic: article
ms.date: 05/31/2018
---

# Pausing

All filter state changes must hold the filter lock. In the **Pause** method, create any resources the filter needs:


```C++
HRESULT CMyFilter::Pause()
{
    CAutoLock lock_it(m_pLock);

    /* Create filter resources. */

    return CBaseFilter::Pause();
}
```



The [**CBaseFilter::Pause**](cbasefilter-pause.md) method sets the correct state on the filter (State\_Paused) and calls the [**CBasePin::Active**](cbasepin-active.md) method on every connected pin in the filter. The **Active** method informs the pin that the filter has become active. If the pin creates resources, override the **Active** method, as follows:


```C++
HRESULT CMyInputPin::Active()
{
    // You do not need to hold the filter lock here. It is already held in Pause.

    /* Create pin resources. */

    return CBaseInputPin::Active()
}
```



 

 



