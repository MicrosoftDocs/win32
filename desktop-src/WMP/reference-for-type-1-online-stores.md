---
title: Reference for Type 1 Online Stores
description: Reference for Type 1 Online Stores
ms.assetid: e6f45a50-029e-4347-9b25-10e9e32a56eb
keywords:
- Windows Media Player online stores,reference
- online stores,reference
- type 1 online stores,reference
- reference for type 1 online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Reference for Type 1 Online Stores

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

Windows Media Player 11 provides a catalog compiler, an object, and several interfaces that support type 1 online stores. The following sections document these in detail.



| Section                                                                                    | Description                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Catalog Compiler for Type 1 Online Stores](catalog-compiler-for-type-1-online-stores.md) | Provides reference material for the compiler that an online store uses to compile its music catalog.                                                                                                                               |
| [IWMPContentContainer Interface](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentcontainer)                                 | Provides reference pages for methods that the online store's plug-in calls to inspect a content container. A content container represents a set of media items to be downloaded or purchased. Implemented by Windows Media Player. |
| [IWMPContentContainerList Interface](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentcontainerlist)                         | Provides reference pages for methods that the online store's plug-in calls to inspect a list of content containers. Implemented by Windows Media Player.                                                                           |
| [IWMPContentPartner Interface](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentpartner)                                     | Provides reference pages for methods that Windows Media Player calls to get information from the online store and to notify the online store about the user's actions. Implemented by the online store's plug-in.                  |
| [IWMPContentPartnerCallback Interface](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentpartnercallback)                     | Provides reference pages for methods that the online store's plug-in calls to notify Windows Media Player about the completion of asynchronous operations. Implemented by Windows Media Player.                                    |
| [External Object for Type 1 Online Stores](external-object-for-type-1-online-stores.md)   | Provides reference pages for properties, methods, and events used by script in webpages provided by the online store.                                                                                                              |
| [Enumerations for Type 1 Online Stores](enumerations-for-type-1-online-stores.md)         | Provides reference pages for the enumerations used in the communication between Windows Media Player and the online store's plug-in.                                                                                               |
| [Structures for Type 1 Online Stores](structures-for-type-1-online-stores.md)             | Provides reference pages for the structures used in the communication between Windows Media Player and the online store's plug-in.                                                                                                 |



 

## Related topics

<dl> <dt>

[**Type 1 Online Stores**](type-1-online-stores.md)
</dt> </dl>

 

 




