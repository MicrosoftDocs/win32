---
title: Running the Sample Project
description: Running the Sample Project
ms.assetid: d0c32a75-4d30-408b-8da8-3917f6fd6ea4
keywords:
- Windows Media Player online stores,running sample projects
- online stores,running sample projects
- type 2 online stores,running sample projects
- Windows Media Player online stores,sample projects
- online stores,sample projects
- type 2 online stores,sample projects
- running sample projects
- samples,type 2 online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Running the Sample Project

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The sample COM component demonstrates the functionality provided by the methods of **IWMPSubscriptionServices** by displaying a dialog box whenever Windows Media Player calls one of the methods. To see this happen, you must first add some content to the library that contains a **ContentDistributor** attribute that matches your service. See [Adding the ContentDistributor Attribute](adding-the-contentdistributor-attribute.md). Then, use Windows Media Player 10 or later to open your online store, play your premium content, and copy your premium content to a device. Windows Media Player will instantiate the sample COM component and call methods when appropriate.

## Related topics

<dl> <dt>

[**Building the Plug-in for a Type 2 Online Store**](building-the-plug-in-for-a-type-2-online-store.md)
</dt> </dl>

 

 




