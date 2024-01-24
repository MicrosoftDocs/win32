---
title: Ripping by Using the IWMPCdromRip Interface
description: Ripping by Using the IWMPCdromRip Interface
ms.assetid: 7622072e-82e1-4e31-ad80-ddc3473b5841
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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Ripping by Using the IWMPCdromRip Interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how to use the [IWMPCdromRip](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromrip) interface to rip music from a CD.

Ripping a CD by using the **IWMPCdromRip** interface has the same effect as ripping music by using the Windows Media Player user interface. Ripped content is automatically added to the library according to the user's preferences. For more information about CD ripping, see "Ripping music from CDs" in Windows Media Player Help.

The code examples in this section use Active Template Library (ATL) classes, such as **CComPtr**.

## Included Headers

To use the code in this section, include the following headers:


```C++
#include <atlbase.h>
#include <atlcom.h>
#include <atlwin.h>
#include <commctrl.h>
#include "wmp.h"
#include "wmpids.h"

```



## Interface Pointers

The interfaces for Windows Media Player are stored in the following member variables.


```C++
// Player interface.
CComPtr<IWMPPlayer>             m_spPlayer;

// CDROM interfaces.
CComPtr<IWMPCdromCollection>    m_spCdromCollection;
CComPtr<IWMPCdrom>              m_spCdrom;
CComPtr<IWMPCdromRip>           m_spCdromRip;
CComPtr<IWMPPlaylist>           m_spPlaylist;

```



The Following Sections Describe How to Use the IWMPCdromRip Interface

-   [Retrieving the Ripping Interface](retrieving-the-ripping-interface.md)
-   [Starting the Rip Process](starting-the-rip-process.md)
-   [Retrieving the Rip Status](retrieving-the-rip-status.md)
-   [Selecting Items for Ripping](selecting-items-for-ripping.md)

 

 




