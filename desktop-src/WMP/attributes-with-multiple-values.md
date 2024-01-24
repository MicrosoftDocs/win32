---
title: Attributes with Multiple Values (Windows Media Player SDK)
description: Learn about attributes with multiple values in the Windows Media Player SDK. Some media item attributes can have multiple values.
ms.assetid: 8405481c-47f5-4752-9dab-d3c84711fbb4
keywords:
- Windows Media Player,attributes for media items
- Windows Media Player object model,attributes for media items
- object model,attributes for media items
- Windows Media Player Mobile,attributes for media items
- Windows Media Player ActiveX control,attributes for media items
- Windows Media Player Mobile ActiveX control,attributes for media items
- ActiveX control,attributes for media items
- Windows Media Player library,attributes for media items
- library,attributes for media items
- attributes,multiple values
- multiple attribute values
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Attributes with Multiple Values (Windows Media Player SDK)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Some media item attributes can have multiple values. For example, the **Author**, **WM/Composer**, and **WM/Genre** attributes can each have more than one value. The data type of such attributes is **multi-valued string**.

In Windows Media Player, the library displays multiple values in a single field, separating the values with semicolons. However, each value is actually a separate attribute in the Windows Media item.

You can write code that will determine whether a given attribute has multiple values and then retrieve all of those values. You must use *Media*.**getItemInfoByType**. If you use the *Media*.**getItemInfo** method to retrieve a multi-valued attribute, you will only retrieve the first value.

The final example in the [Reading Attribute Values](reading-attribute-values.md) topic demonstrates the use of the *Media*.**getAttributeCountByType** and *Media*.**getItemInfoByType** methods to retrieve multiple values for a given attribute.

## Related topics

<dl> <dt>

[**Media Item Attributes**](media-item-attributes.md)
</dt> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Reading Attribute Values from a CD or DVD**](reading-attribute-values-from-a-cd-or-dvd.md)
</dt> </dl>

 

 




