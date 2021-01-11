---
description: Represents a histogram of a texture.
MS-HAID: vspixengine.PixEngineHistogram
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PixEngineHistogram structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: FC720568-6C8E-4B14-BCB1-5FA14D32C785
api_name: 
 - PixEngineHistogram
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.pixenginehistogram"></span>PixEngineHistogram structure

Represents a histogram of a texture.

## Syntax


```C++
} PixEngineHistogram;
```

## Members

**horizontalMin**  
The minimum values for each of the X, Y, Z, and W components in the horizontal axis (domain) of the histogram.

**horizontalMax**  
The maximum values for each of the X, Y, Z, and W components in the horizontal axis (domain) of the histogram.

**verticalMin**  
The minimum values for each of the X, Y, Z, and W components in the vertical axis (range) of the histogram.

**verticalMax**  
The maximum values for each of the X, Y, Z, and W components in the vertical axis (range) of the histogram.

**dataLength**  
The number of samples considered in the histogram.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



