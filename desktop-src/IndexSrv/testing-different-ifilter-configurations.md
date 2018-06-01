---
Description: Testing Different IFilter Configurations
ms.assetid: 5a0c9694-eb73-42c8-a264-4981e85cbc0f
title: Testing Different IFilter Configurations
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Testing Different IFilter Configurations

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The ifilttst.exe program releases the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface and rebinds, this time initializing it with the next set of parameters. The test repeats the cycle: validation test, consistency test, and invalid input test, until all the desired **IFilter** configurations, as specified in [ifilttst.ini](the-ifilttst-ini-file.md), have been tested.

 

 



