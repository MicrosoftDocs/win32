---
title: ClosedCaption Object
description: The ClosedCaption object provides a way to include captions with a media clip. The captioning text is in a Synchronized Accessible Media Interchange (SAMI) file.
ms.assetid: '5e192aa4-0ecd-4bda-8dad-1750039c7898'
keywords:
- ClosedCaption Object Windows Media Player
topic_type:
- apiref
api_name:
- ClosedCaption Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# ClosedCaption Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ClosedCaption** object provides a way to include captions with a media clip. The captioning text is in a Synchronized Accessible Media Interchange (SAMI) file.

The **ClosedCaption** object supports the following properties.



| Property                                           | Description                                                                                          |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [captioningID](closedcaption-captioningid.md)     | Specifies or retrieves the name of the frame or control displaying the captioning.                   |
| [SAMIFileName](closedcaption-samifilename.md)     | Specifies or retrieves the name of the file containing the information needed for closed captioning. |
| [SAMILang](closedcaption-samilang.md)             | Specifies or retrieves the language displayed for closed captioning.                                 |
| [SAMILangCount](closedcaption-samilangcount.md)   | Retrieves the number of languages supported by the current SAMI file.                                |
| [SAMIStyle](closedcaption-samistyle.md)           | Specifies or retrieves the closed captioning style.                                                  |
| [SAMIStyleCount](closedcaption-samistylecount.md) | Retrieves the number of styles supported by the current SAMI file.                                   |



 

The **ClosedCaption** object supports the following methods.



| Method                                                 | Description                                                                              |
|--------------------------------------------------------|------------------------------------------------------------------------------------------|
| [getSAMILangID](closedcaption-getsamilangid.md)       | Retrieves the locale identifier (LCID) of a language supported by the current SAMI file. |
| [getSAMILangName](closedcaption-getsamilangname.md)   | Retrieves the name of a language supported by the current SAMI file.                     |
| [getSAMIStyleName](closedcaption-getsamistylename.md) | Retrieves the name of a style supported by the current SAMI file.                        |



 

The **ClosedCaption** object is accessed through the following property.



| Object                      | Property                                  |
|-----------------------------|-------------------------------------------|
| [Player](player-object.md) | [closedCaption](player-closedcaption.md) |



 

## See also

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




