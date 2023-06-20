---
title: BITS
description: BITS
ms.assetid: 67159ad9-e11b-4fea-bff2-468d5a7447be
keywords:
- Windows Media Player online stores,Background Intelligent Transfer Service (BITS)
- online stores,Background Intelligent Transfer Service (BITS)
- type 2 online stores,Background Intelligent Transfer Service (BITS)
- Background Intelligent Transfer Service (BITS)
- BITS (Background Intelligent Transfer Service)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BITS

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [Background Intelligent Transfer Service](/windows/desktop/Bits/background-intelligent-transfer-service-portal) is a feature of the Windows operating system. BITS transfers files (downloads or uploads) between a client and server, and provides progress information related to the transfers. If you want to transfer files using C++ code, BITS is the correct technology to use. If you want to transfer files using JScript code in your online store webpage, use the Download Manager instead.

Because the Windows Media Player Download Manager uses BITS, you can take steps to configure your BITS copy jobs in such a way that Windows Media Player manages the jobs for you. To do this, you must follow the convention described in the [Windows Media Player BITS Job Convention](windows-media-player-bits-job-convention.md) section when adding your jobs to the BITS transfer queue. This section also describes a mechanism for retrieving information about your BITS jobs from your online stores webpage.

## Related topics

<dl> <dt>

[**Using the Download Manager**](using-the-download-manager.md)
</dt> <dt>

[**About Type 2 Online Stores**](about-type-2-online-stores.md)
</dt> </dl>

 

 