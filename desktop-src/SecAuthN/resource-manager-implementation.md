---
Description: The resource manager runs as a trusted service in a single process. All requests for smart card access are made to the resource manager, which routes them to the reader that contains the targeted card.
ms.assetid: 4a62588a-14d9-43dc-9572-25a9cbcd0efd
title: Resource Manager Implementation
ms.topic: article
ms.date: 05/31/2018
---

# Resource Manager Implementation

The [*resource manager*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) runs as a trusted service in a single process. All requests for [*smart card*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) access are made to the resource manager, which routes them to the [*reader*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) that contains the targeted card.

Smart cards are often used in conjunction with security and personal privacy. Wherever possible, the resource manager uses the security mechanisms existing within the underlying operating system when accessing a reader or smart card.

 

 



