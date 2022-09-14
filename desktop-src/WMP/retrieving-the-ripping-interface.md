---
title: Retrieving the Ripping Interface
description: Retrieving the Ripping Interface
ms.assetid: 760610eb-e356-4b50-b865-53557ba9b815
keywords:
- Windows Media Player,CD ripping
- Windows Media Player object model,CD ripping
- object model,CD ripping
- Windows Media Player ActiveX control,CD ripping
- ActiveX control,CD ripping
- Windows Media Player Mobile ActiveX control,CD ripping
- Windows Media Player Mobile,CD ripping
- CD ripping,IWMPCdromRip interface
- ripping CDs,IWMPCdromRip interface
- IWMPCdromRip interface
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving the Ripping Interface

To enumerate the CD drives on the user's computer, use the **IWMPCdromCollection** interface. Retrieve a pointer to this interface by calling [IWMPCore::get\_cdromCollection](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcore-get_cdromcollection).

By using the [get\_count](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromcollection-get_count) and [item](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromcollection-item) methods, you can iterate the collection to retrieve an [IWMPCdrom](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdrom) interface for each CD drive on the user's computer.

The **IWMPCdrom** interface represents an individual CD drive. Before you begin ripping a CD, you must first call **QueryInterface** through an **IWMPCdrom** pointer to retrieve the [IWMPCdromRip](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromrip) interface.

The following code example demonstrates how to retrieve an interface for ripping a CD from a specific drive:


```C++
HRESULT CMainDlg::GetCdromDriveCount (long &lDriveCount)
{
    HRESULT hr = m_spPlayer->get_cdromCollection(&m_spCdromCollection);

    // Get the number of CDROM drives.
    if (SUCCEEDED(hr))
    {
        hr = m_spCdromCollection->get_count(&lDriveCount);
    }

    return hr;
}

// lIndex refers to the index of the current drive,
// which must be less than the value retrieved by
// GetCdromDriveCount above.
HRESULT CMainDlg::GetCdromRipInterface (long lIndex)
{
    // Get the IWMPCdrom interface.
    m_spCdrom.Release();
    HRESULT hr = m_spCdromCollection->item(lIndex, &m_spCdrom);
    if (SUCCEEDED(hr))
    {
        // Get the IWMPCdromRip interface.
        m_spCdromRip.Release();
        hr = m_spCdrom->QueryInterface(&m_spCdromRip);
    }

    return hr;
}

```



## Related topics

<dl> <dt>

[**Ripping a CD**](ripping-a-cd.md)
</dt> <dt>

[**Starting the Rip Process**](starting-the-rip-process.md)
</dt> <dt>

[**Retrieving the Rip Status**](retrieving-the-rip-status.md)
</dt> <dt>

[**Selecting Items for Ripping**](selecting-items-for-ripping.md)
</dt> <dt>

[**IWMPCdromCollection Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromcollection)
</dt> </dl>

 

 




