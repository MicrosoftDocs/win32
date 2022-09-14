---
description: ICE95 checks the Control table and BBControl table to verify that the billboard controls fit onto all the billboards.
ms.assetid: 8ba73536-65a5-4658-846c-76356f16b81c
title: ICE95
ms.topic: article
ms.date: 05/31/2018
---

# ICE95

ICE95 checks the [Control table](control-table.md) and [BBControl table](bbcontrol-table.md) to verify that the billboard controls fit onto all the billboards.

## Result

If any of the following are true, a billboard control fails to fit on a billboard. ICE95 posts the following warnings.



| ICE95 warning                                                                                                                                                                                                              | Description                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| The BBControl item '\[1\].\[2\]' in the BBControl table does not fit in all the billboard controls in the Control table. The X coordinate exceeds the boundary of the minimum billboard control width %s                   | The control's X coordinate is outside the width of the billboard.                          |
| The BBControl item '\[1\].\[2\]' in the BBControl table does not fit in all the billboard controls in the Control table. The Y coordinate exceeds the boundary of the minimum billboard control height %s                  | The control's Y coordinate is below the bottom of the billboard.                           |
| The BBControl item '\[1\].\[2\]' in the BBControl table does not fit in all the billboard controls in the Control table. The X coordinate and the width combined together exceeds the minimum billboard control width %s   | The control's X coordinate plus the control's width is outside the width of the billboard. |
| The BBControl item '\[1\].\[2\]' in the BBControl table does not fit in all the billboard controls in the Control table. The Y coordinate and the height combined together exceeds the minimum billboard control height %s | The control's Y coordinate plus the control's height is below the bottom of the billboard. |



 

## Example

ICE95 reports the following warnings for the example:

``` syntax
The BBControl item 'billboard1.bbcontrol1' in the BBControl table does not fit in all the billboard controls in the Control table. The X coordinate exceeds the boundary of the minimum billboard control width 100
The BBControl item 'billboard1.bbcontrol2' in the BBControl table does not fit in all the billboard controls in the Control table. The Y coordinate exceeds the boundary of the minimum billboard control height 100
The BBControl item 'billboard1.bbcontrol3' in the BBControl table does not fit in all the billboard controls in the Control table. The X coordinate and the width combined together exceeds the minimum billboard control width 100
The BBControl item 'billboard1.bbcontrol4' in the BBControl table does not fit in all the billboard controls in the Control table. The Y coordinate and the height combined together exceeds the minimum billboard control height 100
```

Control Table (partial) (partial)



| Control  | Type      | Width | Height |
|----------|-----------|-------|--------|
| control1 | Billboard | 300   | 100    |
| Control2 | Billboard | 100   | 300    |



 

[BBControl table](bbcontrol-table.md)



| Billboard\_ | BBControl  | X   | Y   | Width | Height |
|-------------|------------|-----|-----|-------|--------|
| billboard1  | bbcontrol1 | 200 | 0   | 100   | 100    |
| billboard1  | bbcontrol2 | 0   | 200 | 100   | 100    |
| billboard1  | bbcontrol3 | 50  | 0   | 100   | 50     |
| billboard1  | bbcontrol4 | 0   | 50  | 50    | 100    |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



