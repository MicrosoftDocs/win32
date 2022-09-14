---
title: Checking the State of an Accessibility Parameter
description: The following code fragment uses the GetSystemMetrics function to check the ShowSounds parameter. If GetSystemMetrics returns TRUE, the application should present all important information in visual form.
ms.assetid: fb6a0adf-ca38-4e21-9edd-1abb2efd59e5
ms.topic: article
ms.date: 05/31/2018
---

# Checking the State of an Accessibility Parameter

The following code fragment uses the [**GetSystemMetrics**](/windows/desktop/api/winuser/nf-winuser-getsystemmetrics) function to check the ShowSounds parameter. If **GetSystemMetrics** returns **TRUE**, the application should present all important information in visual form.


```C++
BOOL fShowSounds; 
fShowSounds = GetSystemMetrics(SM_SHOWSOUNDS); 
```



 

 