---
title: Private Online Stores
description: Private Online Stores
ms.assetid: c1e241f5-6d29-4b53-8be0-264597e03de7
keywords:
- Windows Media Player online stores,private
- online stores,private
- type 1 online stores,private
- type 2 online stores,private
- private online stores
- registry,private online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Private Online Stores

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player 10 or later supports private online stores; that is, stores that are visible only to certain users. For a private online store to be visible to the current user, there must be an entry that represents the private online store under the following registry key.

HKEY\_CURRENT\_USER\\Software\\Microsoft\\MediaPlayer\\PrivateServices

The required registry entry must have the following format.



| Name                                                         | Type           | Value                                                                     |
|--------------------------------------------------------------|----------------|---------------------------------------------------------------------------|
| Any name chosen by the person who creates the registry entry | **REG\_DWORD** | A number, provided by Microsoft, that identifies the private online store |



 

The Windows Media Player 10 ActiveX control supports private online stores only if the control is running in remote mode. The Windows Media Player 11 ActiveX control supports private online stores regardless of whether the control is running in remote mode.

## Related topics

<dl> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> </dl>

 

 




