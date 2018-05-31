---
title: Proximity Unit Constants
description: Proximity Unit Constants
ms.assetid: 11c8bfdc-62e7-4404-bb0b-ec47341ec875
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Proximity Unit Constants

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The proximity unit constants specify the unit of measurement for text when applying the proximity operator.

``` syntax
#define PROXIMITY_UNIT_WORD      ( 0 )
#define PROXIMITY_UNIT_SENTENCE  ( 1 )
#define PROXIMITY_UNIT_PARAGRAPH ( 2 )
#define PROXIMITY_UNIT_CHAPTER   ( 3 )
```

### Remarks

The **dwProximityUnit** member of the [**DBCONTENTPROXIMITY**](dbcontentproximity.md) structure uses these constants.

The OLE DB Provider for Indexing Service currently uses only the PROXIMITRY\_UNIT\_WORD constant. The other constants are reserved for future use.

 

 




