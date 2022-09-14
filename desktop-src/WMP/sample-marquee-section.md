---
title: Sample Marquee Section
description: Sample Marquee Section
ms.assetid: 44ed3257-2e1a-4b8d-9d55-a13b0400422d
keywords:
- Windows Media Player Mobile skins,marquees
- skins,marquees
- reference for skins,marquees
- marquees in skins,Marquee section
- skin definition files,Marquee section
ms.topic: article
ms.date: 05/31/2018
---

# Sample Marquee Section

The following lines show a typical Marquee section of a skin definition file:


```C++
//  <Location>   <Font>       <Color>      <Text item combinations>

//  ----------   ------       -------      ------------------------

    3,2,234,20   Tahoma,12,N  255,0,0    Title+Author, Title, Author


```



This defines a marquee display box that shows the title and author if both are defined, the title if only Title is defined, or the name of the author if only Author is defined. If neither is defined, nothing will be displayed.

## Related topics

<dl> <dt>

[**Marquee**](marquee.md)
</dt> </dl>

 

 




