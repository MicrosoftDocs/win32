---
title: IResultsViewer IsUpdateNeeded property
description: This returns TRUE if the views query has been modified and needs updating.
ms.assetid: 68ae1f68-0585-4bc5-bea4-eb55f3626093
keywords:
- IsUpdateNeeded property Legacy Windows Environment Features
- IsUpdateNeeded property Legacy Windows Environment Features , IResultsViewer interface
- IResultsViewer interface Legacy Windows Environment Features , IsUpdateNeeded property
topic_type:
- apiref
api_name:
- IResultsViewer.IsUpdateNeeded
api_location:
- WdsView.h
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IResultsViewer::IsUpdateNeeded property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

This returns TRUE if the views query has been modified and needs updating.

## Syntax

## Property value

When called this will return a pointer to the flag noting if the query has changed.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                        |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                        |
| Header<br/>                   | <dl> <dt>WdsView.h</dt> </dl> |



 

 





