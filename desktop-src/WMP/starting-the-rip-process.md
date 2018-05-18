---
title: Starting the Rip Process
description: Starting the Rip Process
ms.assetid: '82ffc114-ddad-41be-af80-6c1bd29cb0d4'
keywords: ["Windows Media Player,CD ripping", "Windows Media Player object model,CD ripping", "object model,CD ripping", "Windows Media Player ActiveX control,CD ripping", "ActiveX control,CD ripping", "Windows Media Player Mobile ActiveX control,CD ripping", "Windows Media Player Mobile,CD ripping", "CD ripping,starting rip process", "ripping CDs,starting rip process"]
---

# Starting the Rip Process

After you have retrieved the ripping interface as explained in the previous section, start the ripping process by calling [IWMPCdromRip::startRip](iwmpcdromrip-startrip.md).


```C++
// Start ripping.
HRESULT hr = m_spCdromRip->startRip();

```



You can stop the ripping operation by calling [IWMPCdromRip::stopRip](iwmpcdromrip-stoprip.md).


```C++
// Stop ripping.
HRESULT hr = m_spCdromRip->stopRip();

```



## Related topics

<dl> <dt>

[**Ripping a CD**](ripping-a-cd.md)
</dt> <dt>

[**Retrieving the Ripping Interface**](retrieving-the-ripping-interface.md)
</dt> <dt>

[**Retrieving the Rip Status**](retrieving-the-rip-status.md)
</dt> <dt>

[**Selecting Items for Ripping**](selecting-items-for-ripping.md)
</dt> </dl>

 

 




