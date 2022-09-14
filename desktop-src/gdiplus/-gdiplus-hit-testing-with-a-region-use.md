---
description: The purpose of hit testing is to determine whether the cursor is over a given object, such as an icon or a button.
ms.assetid: 9776b73e-191e-4a8e-9abe-e485ffed954c
title: Hit Testing with a Region
ms.topic: article
ms.date: 05/31/2018
---

# Hit Testing with a Region

The purpose of hit testing is to determine whether the cursor is over a given object, such as an icon or a button. The following example creates a plus-shaped region by forming the union of two rectangular regions. Assume that the variable **point** holds the location of the most recent click. The code checks to see whether **point** is in the plus-shaped region. If **point** is in the region (a hit), the region is filled with an opaque red brush. Otherwise, the region is filled with a semitransparent red brush.


```
Point point(60, 10);
// Assume that the variable "point" contains the location
// of the most recent click.
// To simulate a hit, assign (60, 10) to point.
// To simulate a miss, assign (0, 0) to point.
SolidBrush solidBrush(Color());
Region region1(Rect(50, 0, 50, 150));
Region region2(Rect(0, 50, 150, 50));
// Create a plus-shaped region by forming the union of region1 and region2.
// The union replaces region1.
region1.Union(&region2);
if(region1.IsVisible(point, &graphics))
{
   // The point is in the region. Use an opaque brush.
   solidBrush.SetColor(Color(255, 255, 0, 0));
}
else
{
   // The point is not in the region. Use a semitransparent brush.
   solidBrush.SetColor(Color(64, 255, 0, 0));
}
graphics.FillRegion(&solidBrush, &region1);
```



 

 



