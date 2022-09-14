---
description: Use the following code to set the callback frequency.
ms.assetid: fdcad3c2-7e36-4194-83c7-dccbd50762d5
title: Setting the Callback Frequency
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Callback Frequency

Use the following code to set the callback frequency:

**DWORD** Value = 1;


```C++
rc = SetDwordInBlob(hNPPBlob, OWNER_NPP, CATEGORY_CONFIG,
                    TAG_UPDATE_FREQUENCY, Value);
```



This code fragment sets the callback frequency to 1 second (the minimum value). The maximum value must be much larger than 1. If the network packet provider (NPP) buffer is full, the NPP calls the monitor back sooner.

 

 



