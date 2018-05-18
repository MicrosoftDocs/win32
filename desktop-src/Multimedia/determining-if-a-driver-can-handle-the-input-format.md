---
title: Determining If a Driver Can Handle the Input Format
description: Determining If a Driver Can Handle the Input Format
ms.assetid: '456eab43-d830-4a28-b724-3ef35b852372'
keywords: ["video compression manager (VCM),input format", "VCM (video compression manager),input format", "ICDrawQuery macro"]
---

# Determining If a Driver Can Handle the Input Format

The following example shows how to check the input format with the [**ICDrawQuery**](icdrawquery.md) macro.


```C++
// lpbiIn points to BITMAPINFOHEADER structure indicating the input 
// format. 

if (ICDrawQuery(hIC, lpbiIn) == ICERR_OK) 
{ 
    // Driver recognizes the input format. 
} 
else 
{ 
    // Need a different decompressor. 
} 
 
```



 

 




