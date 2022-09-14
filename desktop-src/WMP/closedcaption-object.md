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
ms.date: 05/31/2018
api_location: 
---

# ClosedCaption Object

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

 

 




