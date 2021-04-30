---
description: The SaveBookmark method saves the current disc position and state of the MSWebDVD object so the user can return to the same place later.
ms.assetid: 975687c5-f93e-4473-b23b-63e0ae6bbb5d
title: SaveBookmark Method (Segment.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SaveBookmark Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SaveBookmark` method saves the current disc position and state of the **MSWebDVD** object so the user can return to the same place later.

``` syntax
MSWebDVD.SaveBookmark()
```

## Return Value

No return value.

## Remarks

A bookmark is a snapshot of the DVD Navigator's current state. This includes information such as where it is playing on the disc, and which audio and subpictures streams are selected. By saving a bookmark, the user can close the application, shut down the computer, and come back later to continue viewing the disc right where he or she left off, with all settings just as they were before. Only one bookmark can be saved at any given time. When you call `SaveBookmark`, the old bookmark is overwritten.

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Segment.h</dt> </dl> |



## See also

<dl> <dt>

[**RestoreBookmark**](restorebookmark-method.md)
</dt> </dl>

 

 




