---
title: Retrieving the Drive and Disc Status
description: Retrieving the Drive and Disc Status
ms.assetid: 5e3e6107-d2bc-450c-a86e-5d3ef7b3092a
keywords:
- Windows Media Player,CD burning
- Windows Media Player object model,CD burning
- object model,CD burning
- Windows Media Player ActiveX control,CD burning
- ActiveX control,CD burning
- Windows Media Player Mobile ActiveX control,CD burning
- Windows Media Player Mobile,CD burning
- CD burning,retrieving drive and disc status
- burning CDs,retrieving drive and disc status
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Retrieving the Drive and Disc Status

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Before starting a CD burning operation, you must ensure that the selected CD-ROM drive supports the operation you want to perform. For instance, you must check that a CD is capable of being erased before calling [IWMPCdromBurn::erase](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-erase). The following code shows an example of using [IWMPCdromBurn::isAvailable](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-isavailable) to determine whether an operation is supported:


```C++
VARIANT_BOOL vbResult;
    
// Check whether this drive can burn CDs.
CComBSTR bstrItem;
HRESULT hr = bstrItem.Append("Burn");
if (SUCCEEDED(hr))
{
    hr = m_spCdromBurn->isAvailable(bstrItem, &vbResult);
}
if (SUCCEEDED(hr))
{
    if (VARIANT_TRUE == vbResult)
    {
        // The current drive can burn CDs.
    }
}

```



## Related topics

<dl> <dt>

[**Burning a CD**](burning-a-cd.md)
</dt> <dt>

[**Retrieving the CD Burning Interface**](retrieving-the-cd-burning-interface.md)
</dt> <dt>

[**Starting the Burn Process**](starting-the-burn-process.md)
</dt> <dt>

[**Erasing a Rewritable CD**](erasing-a-rewritable-cd.md)
</dt> <dt>

[**Retrieving the Burn Status**](retrieving-the-burn-status.md)
</dt> </dl>

 

 




