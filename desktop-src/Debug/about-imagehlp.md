---
description: The ImageHlp functions are used mostly by programming tools, application setup utilities, and other programs that need access to the data contained in a PE image.
ms.assetid: 831d7bb2-bf01-4422-a940-173f9856a513
title: About ImageHlp
ms.topic: article
ms.date: 05/31/2018
---

# About ImageHlp

The ImageHlp functions are used mostly by programming tools, application setup utilities, and other programs that need access to the data contained in a PE image. All ImageHlp functions are single threaded. Therefore, calls from more than one thread to this function will likely result in unexpected behavior or memory corruption. To avoid this, you must synchronize all concurrent calls from more than one thread to this function.

The following topics describe PE images and the functionality provided by the ImageHlp functions.

-   [PE Format](pe-format.md)
-   [Image Access Functions](image-access-functions.md)
-   [Image Integrity Functions](image-integrity-functions.md)
-   [Image Modification Functions](image-modification-functions.md)

 

 



