---
title: IWMPStringCollection2 (VB and C ) interface (Wmp.h)
description: Provides methods that supplement the IWMPStringCollection interface.
ms.assetid: be93ff47-7f76-4b5e-ad30-3094a75147c8
keywords:
- IWMPStringCollection2 (VB and C ) interface Windows Media Player
- IWMPStringCollection2 (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPStringCollection2 (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPStringCollection2 (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides methods that supplement the **IWMPStringCollection** interface.

## Members

The **IWMPStringCollection2 (VB and C#)** interface has these types of members:

-   [Methods](#methods)

### Methods

The **IWMPStringCollection2 (VB and C#)** interface has these methods.



| Method                                                                                                                 | Description                                                                                                                           |
|:-----------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| [**getAttributeCountByType**](wmplibiwmpstringcollection2-iwmpstringcollection2-getattributecountbytype--vb-and-c.md) | Returns the number of attributes associated with the specified string collection item index, attribute name, and language.<br/> |
| [**getItemInfo**](wmplibiwmpstringcollection2-iwmpstringcollection2-getiteminfo--vb-and-c.md)                         | Returns the string corresponding to the specified string collection item index and name.<br/>                                   |
| [**getItemInfoByType**](wmplibiwmpstringcollection2-iwmpstringcollection2-getiteminfobytype--vb-and-c.md)             | Returns the value corresponding to the specified string collection item index, name, language, and attribute index.<br/>        |
| [**isIdentical**](wmplibiwmpstringcollection2-iwmpstringcollection2-isidentical--vb-and-c.md)                         | Returns a value indicating whether the supplied object is the same as the current one.<br/>                                     |



 

Get an **IWMPStringCollection2** interface by casting the value returned by the [**IWMPMediaCollection.getAttributeStringCollection**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpmediacollection-getattributestringcollection) method.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPStringCollection Interface (VB and C#)**](iwmpstringcollection--vb-and-c.md)
</dt> </dl>

 

 





