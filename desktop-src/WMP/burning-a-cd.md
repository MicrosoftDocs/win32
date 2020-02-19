---
title: Burning a CD
description: Burning a CD
ms.assetid: df55479e-d8a7-443d-bf2c-c988bfd0b1be
keywords:
- Windows Media Player,CD burning
- Windows Media Player object model,CD burning
- object model,CD burning
- Windows Media Player ActiveX control,CD burning
- ActiveX control,CD burning
- Windows Media Player Mobile ActiveX control,CD burning
- Windows Media Player Mobile,CD burning
- CD burning,about
- burning CDs,about
ms.topic: article
ms.date: 05/31/2018
---

# Burning a CD

This section describes how to use the [IWMPCdromBurn](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromburn) interface to burn music to a CD. The **IWMPCdromBurn** interface provides functionality for burning playlists to CDs as either data or audio tracks, as well as erasing CD-RWs.

Code Usage

The code examples in this section use Active Template Library (ATL) classes, such as **CComPtr**.

Included Headers

To use the code in this section, include the following headers:


```C++
#include <atlbase.h>
#include <atlcom.h>
#include <atlwin.h>
#include <commctrl.h>
#include "wmp.h"
#include "wmpids.h"

```



Interface Pointers

The interfaces for Windows Media Player are stored in the following member variables:


```C++
// Player interface.
CComPtr<IWMPPlayer>             m_spPlayer;

// CDROM interfaces.
CComPtr<IWMPCdromCollection>    m_spCdromCollection;
CComPtr<IWMPCdrom>              m_spCdrom;
CComPtr<IWMPCdromBurn>          m_spCdromBurn;
CComPtr<IWMPPlaylist>           m_spPlaylist;

```



The following topics describe how to use the CD burning API.

-   [Retrieving the CD Burning Interface](retrieving-the-cd-burning-interface.md)
-   [Starting the Burn Process](starting-the-burn-process.md)
-   [Erasing a Rewritable CD](erasing-a-rewritable-cd.md)
-   [Retrieving the Drive and Disc Status](retrieving-the-drive-and-disc-status.md)
-   [Retrieving the Burn Status](retrieving-the-burn-status.md)

## Related topics

<dl> <dt>

[**Player Control Guide**](player-control-guide.md)
</dt> </dl>

 

 




