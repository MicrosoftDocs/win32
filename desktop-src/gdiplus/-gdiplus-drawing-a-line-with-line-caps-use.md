---
description: You can draw the start or end of a line in one of several shapes called line caps. Windows GDI+ supports several line caps, such as round, square, diamond, and arrowhead.
ms.assetid: c9d90114-3913-486c-a808-b08dd473d9a1
title: Drawing a Line with Line Caps
ms.topic: article
ms.date: 05/31/2018
---

# Drawing a Line with Line Caps

You can draw the start or end of a line in one of several shapes called line caps. Windows GDI+ supports several line caps, such as round, square, diamond, and arrowhead.

You can specify line caps for the start of a line (start cap), the end of a line (end cap), or the dashes of a dashed line (dash cap).

The following example draws a line with an arrowhead at one end and a round cap at the other end:


```
Pen pen(Color(255, 0, 0, 255), 8);
stat = pen.SetStartCap(LineCapArrowAnchor);
stat = pen.SetEndCap(LineCapRoundAnchor);
stat = graphics.DrawLine(&pen, 20, 175, 300, 175);
```



The following illustration shows the resulting line.

![illustration showing a horizontal line with an arrow at the left end and a circle at the right end](images/pens4.png)

**LineCapArrowAnchor** and **LineCapRoundAnchor** are elements of the [**LineCap**](/windows/desktop/api/Gdiplusenums/ne-gdiplusenums-linecap) enumeration.

 

 



