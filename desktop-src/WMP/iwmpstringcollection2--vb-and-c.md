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
ms.date: 05/31/2018
---

# IWMPStringCollection2 (VB and C#) interface

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

 

 





