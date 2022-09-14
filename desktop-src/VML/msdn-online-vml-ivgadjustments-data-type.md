---
title: VML IVgAdjustments Data Type
description: VML IVgAdjustments Data Type
ms.assetid: d605632b-3ee2-44fd-8122-f38b1f91e965
ms.topic: article
ms.date: 05/31/2018
---

# VML IVgAdjustments Data Type

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Collection of adjustments to a shape that can be used in formulas. Adjustments can be used as temporary placeholders or for any reason you would use variables. There are only 8 adjustments in the collection.



| Attributes | Description                                                                                                                                                                                                                                                                                                                            |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Length     | **Integer**. Number of adjustments. Can be no greater than 8.                                                                                                                                                                                                                                                                          |
| Item       | **Long**. Array of adjustments indexed from 0 to 7. Note that adjustments may be sparcely specified; that is, intermediate array values may not always be filled. For example, item 1, 3, and 5 could have values for a length of 3, with item(0), item(2), and item(4) specified. To see if an item exists, use the Exists attribute. |
| Exists     | **IVgTriState**. Determines whether a specified adjustment exists. Note that an index must be used; that is, exists(item) must be used to retrieve the existence of an item.                                                                                                                                                           |
| Value      | **String**. Text representation of numeric values, with commas between each number.                                                                                                                                                                                                                                                    |



 

 

 