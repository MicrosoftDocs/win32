---
title: Oversize Data Structures
description: Oversize Data Structures
ms.assetid: a548c33a-e83d-497e-98ca-465347ddb67b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Oversize Data Structures

Care must be taken to not oversize data structures. Oversized data structures can result in an inordinately large outstanding footprint. Having no call paths that lead to the growth of a data structure is an indication that data structures are oversized. However, further analysis may be necessary for a complete understanding of the issue of no call paths leading to data structure growth.

 

 




