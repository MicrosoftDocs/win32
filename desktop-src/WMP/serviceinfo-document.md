---
title: ServiceInfo Document
description: ServiceInfo Document
ms.assetid: 48f84dd7-e458-4da2-ae2b-5949e867cd3a
keywords:
- Windows Media Player online stores,ServiceInfo document
- online stores,ServiceInfo document
- type 1 online stores,ServiceInfo document
- type 2 online stores,ServiceInfo document
- ServiceInfo document
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ServiceInfo Document

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

Online stores must author the ServiceInfo.xml document. This is the document that the online store uses to configure the Windows Media Player user interface when Windows Media Player 10 or later is hosting the online store.

The following elements and their attributes are supported for Windows Media Player online stores.



| Element                                      | Description                                                                                                                                                                                                                                                                        |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AlbumInfo](albuminfo-element.md)           | Specifies the URL for the webpage that Windows Media Player displays when the user chooses to view more information about a particular media item.Type 1: optional<br/> Type 2 Music: required<br/> Type 2 Commerce: ignored<br/>                                |
| [ButtonText](buttontext-element.md)         | Specifies the text string that Windows Media Player displays for a task pane button.Type 1: required<br/> Type 2 Music: required<br/> Type 2 Commerce: required<br/>                                                                                             |
| [ButtonTip](buttontip-element.md)           | Specifies the tooltip that that is displayed when the user points to a task pane button.Type 1: optional<br/> Type 2 Music: optional<br/> Type 2 Commerce: optional<br/>                                                                                         |
| [BuyCD](buycd-element.md)                   | Specifies the URLs for webpages that Windows Media Player displays when the user chooses to make a purchase.Type 1: required<br/> Type 2 Music: required<br/> Type 2 Commerce: ignored<br/>                                                                      |
| [Color](color-element.md)                   | Specifies the background color for online stores navigation buttons.Type 1: optional<br/> Type 2 Music: optional<br/> Type 2 Commerce: optional<br/>                                                                                                             |
| [Description](description-element.md)       | Specifies a description of the online store that is displayed during the user's first experience with an installation of Windows Media Player. Requires Windows Media Player 11.Type 1: required<br/> Type 2 Music: optional<br/> Type 2 Commerce: optional<br/> |
| [DownloadStatus](downloadstatus-element.md) | Specifies a URL that the Windows Media Player displays as a link to enable users to view download status.Type 1: ignored<br/> Type 2 Music: optional<br/> Type 2 Commerce: optional<br/>                                                                         |
| [FriendlyName](friendlyname-element.md)     | Specifies the text string that Windows Media Player displays to the user to identify the online store.Type 1: required<br/> Type 2 Music: required<br/> Type 2 Commerce: required<br/>                                                                           |
| [HTMLView](htmlview-element.md)             | Specifies the base URL of an HTMLView webpage.Type 1: optional<br/> Type 2 Music: optional<br/> Type 2 Commerce: optional<br/>                                                                                                                                   |
| [Image](image-element.md)                   | Specifies the images that Windows Media Player displays to the user to represent the online store.Type 1: required<br/> Type 2 Music: optional<br/> Type 2 Commerce: optional<br/>                                                                               |
| [InfoCenter](infocenter-element.md)         | Specifies the URL of the webpage that Windows Media Player displays in the Info Center View feature of **Now Playing** when the online store is active.Type 1: required<br/> Type 2 Music: required<br/> Type 2 Commerce: ignored<br/>                           |
| [Install](install-element.md)               | Specifies values used by Windows Media Player setup to install the default online store.Type 1: required<br/> Type 2 Music: optional<br/> Type 2 Commerce: ignored<br/>                                                                                          |
| [Navigate](navigate-element.md)             | Specifies a base URL used by calls to **External.NavigateTaskPaneURL**.Type 1: optional<br/> Type 2 Music: optional<br/> Type 2 Commerce: optional<br/>                                                                                                          |
| [ServiceInfo](serviceinfo-element.md)       | Represents the main element for the ServiceInfo.xml document.Type 1: required<br/> Type 2 Music: required<br/> Type 2 Commerce: required<br/>                                                                                                                    |
| [ServiceTask1](servicetask1-element.md)     | Represents the first online store task pane.Type 1: required<br/> Type 2 Music: required<br/> Type 2 Commerce: required<br/>                                                                                                                                     |
| [ServiceTask2](servicetask2-element.md)     | Represents the second online store task pane.Type 1: ignored<br/> Type 2 Music: optional<br/> Type 2 Commerce: optional<br/>                                                                                                                                     |
| [ServiceTask3](servicetask3-element.md)     | Represents the third online store task pane.Type 1: ignored<br/> Type 2 Music: optional<br/> Type 2 Commerce: optional<br/>                                                                                                                                      |



 

## Related topics

<dl> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 2 Online Store**](example-serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> </dl>

 

 





