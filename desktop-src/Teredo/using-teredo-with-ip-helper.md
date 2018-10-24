---
title: Using Teredo with IP Helper
description: Internet Protocol Helper (IP Helper) API is utilized by an application to gather and provide important information regarding the networking configuration of the local machine.
ms.assetid: 67dbe639-aff5-4628-9471-63f50504962d
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Teredo with IP Helper

The [Internet Protocol Helper](https://msdn.microsoft.com/library/windows/desktop/aa365798) (IP Helper) API is utilized by an application to gather and provide important information regarding the networking configuration of the local machine. When operating on the Windows Vista platform, this information includes the dynamic UDP port assigned to the Teredo interface and changes that may occur to the designated port.

The following functions are utilized by the IP Helper API to facilitate the use of the Teredo interface:

-   [**GetTeredoPort**](https://msdn.microsoft.com/library/windows/desktop/aa814426)
-   [**NotifyTeredoPortChange**](https://msdn.microsoft.com/library/windows/desktop/aa814453)
-   [**NotifyStableUnicastIpAddressTable**](https://msdn.microsoft.com/library/windows/desktop/aa814452)

 

 




