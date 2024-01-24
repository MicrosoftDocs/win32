---
description: Some application gestures may conflict with East Asian characters or combinations of East Asian characters.
ms.assetid: 56ff773f-ef95-47f8-ba04-2593330867ee
title: Conflicts with East-Asian Characters
ms.topic: article
ms.date: 05/31/2018
---

# Conflicts with East-Asian Characters

Some *application gestures* may conflict with East Asian characters or combinations of East Asian characters. The following table lists possible conflicts between application gestures and characters in applications that have specific East Asian character input.



| Gesture                 | Chinese (Simplified) | Chinese (Traditional) | Japanese     | Korean       |
|-------------------------|----------------------|-----------------------|--------------|--------------|
| Down<br/>         | X<br/>         | X<br/>          | X<br/> | X<br/> |
| Right<br/>        | X<br/>         | X<br/>          | X<br/> | X<br/> |
| DownRight<br/>    | -<br/>         | X<br/>          | -<br/> | X<br/> |
| RightDown<br/>    | -<br/>         | -<br/>          | X<br/> | X<br/> |
| Circle<br/>       | -<br/>         | -<br/>          | -<br/> | X<br/> |
| ChevronRight<br/> | -<br/>         | -<br/>          | -<br/> | X<br/> |



 

Microsoft remains committed to developing *gestures*. Microsoft recognizes that in building applications, independent software vendors (ISVs) need to know which actions will be mapped to gestures. [Unimplemented Glyphs](unimplemented-glyphs.md) lists a set of pen actions that Microsoft plans to map to gestures, as well as gestures that are being reserved for actions. This information is given so that you know which actions and gestures will be provided for in the future.

In addition to using gestures that are provided in Microsoft Windows XP Tablet PC Edition, applications are free to create their own gestures. These gestures may then be recognized by a *Microsoft gesture recognizer* that the application developer builds. If you plan to implement any of your own gestures, consult [Unimplemented Glyphs](unimplemented-glyphs.md) to avoid overlapping with gestures that Microsoft plans to implement.

 

 




