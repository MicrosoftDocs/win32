---
description: Because of the footprint of statically linked DLLs, you should avoid using Microsoft Foundation Classes (MFCs) to write an expert.
ms.assetid: 634852fd-d0e0-42a7-90af-e93cc0e4ac84
title: Using Microsoft Foundation Classes
ms.topic: article
ms.date: 05/31/2018
---

# Using Microsoft Foundation Classes

Because of the footprint of statically linked DLLs, you should avoid using Microsoft Foundation Classes (MFCs) to write an expert. However, if you use the MFC, ensure access to any of the MFC DLL resources by including the following code immediately upon entry:

``` syntax
#ifdef _AFXDLL
      AFX_MANAGE_STATE(AfxGetStaticModuleState());
#endif
```

 

 



