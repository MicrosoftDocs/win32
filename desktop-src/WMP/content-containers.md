---
title: Content Containers
description: Content Containers
ms.assetid: bed0293b-4765-4d1b-861c-f0c0a064df5f
keywords:
- Windows Media Player online stores,content containers
- online stores,content containers
- type 1 online stores,content containers
- Windows Media Player online stores,IWMPContentContainer interface
- online stores,IWMPContentContainer interface
- type 1 online stores,IWMPContentContainer interface
- Windows Media Player,content containers
- Windows Media Player,IWMPContentContainer interface
- content containers
- IWMPContentContainer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Content Containers

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player uses content containers to represent digital media content in a subscription download or purchase transaction. A content container is represented by the **IWMPContentContainer** interface. A content container might contain a list of related content, such as an album, or a set of unrelated content items, or *tracks*. You can use the **IWMPContentContainer** interface to enumerate the tracks of the content container and retrieve the price of each track. You can also retrieve information about the content container itself, such as the container ID, the type of content in the container, and the total price for the tracks in the container (which might differ from the sum of the prices of the individual tracks, as in the case of an album purchase).

To provide a mechanism for packaging multiple content containers into a single object, Windows Media Player supports the **IWMPContentContainerList** interface. **IWMPContentContainerList** provides methods to enumerate and retrieve the content containers in the list. To discover whether the content container list represents a purchase or a subscription download, call [IWMPContentContainerList::GetTransactionType](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentcontainerlist-gettransactiontype) to retrieve a [WMPTransactionType](/previous-versions/windows/desktop/api/contentpartner/ne-contentpartner-wmptransactiontype) value.

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> <dt>

[**IWMPContentContainer Interface**](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentcontainer)
</dt> <dt>

[**IWMPContentContainerList Interface**](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentcontainerlist)
</dt> </dl>

 

 




