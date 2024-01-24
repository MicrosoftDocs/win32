---
title: Requirements for Online Music Stores
description: Requirements for Online Music Stores
ms.assetid: 0595e7e0-6da9-4caa-a305-cfedd81e217e
keywords:
- Windows Media Player Online Stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Requirements for Online Music Stores

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

All of the requirements that your online store must meet are detailed in the Online Media Service Listing Agreement for Windows Media Player. To ensure that your online store provides a great user experience, we've highlighted some key requirements regarding customization and playback.

-   The initial page of the store exposed in the Windows Media Player user interface must be functional without requiring the user to log in.
-   Pop-up ads that launch a separate browser window are prohibited.
-   The entire browse, purchase, and playback experience must be rendered within the user interface of the Windows Media Player, and not within a separate pop-up browser window or an embedded media player.
-   Systray installation of an application and background processes that run continuously are prohibited.
-   Discrete actions such as log-in, billing, purchase of physical CDs, or other related features outside of the primary digital media service may link to a browser instance outside of the player for the non-digital-media feature.
-   Licenses provided by the store must remain valid regardless of the store's connection to Windows Media Player. For details see the Term and Termination section of the Online Media Service Listing Agreement for Windows Media Player.

From time to time Microsoft may update the Eligibility and On-Boarding Requirements and post them on the [Windows Media website](https://www.microsoft.com/windows/windowsmedia/default.mspx) (https://www.microsoft.com/windows/windowsmedia/default.mspx).

## Related topics

<dl> <dt>

[Online Stores Welcome Kit](online-stores-welcome-kit.md)
</dt> </dl>

 

 




