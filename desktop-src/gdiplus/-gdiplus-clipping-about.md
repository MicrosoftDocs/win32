---
Description: Clipping involves restricting drawing to a certain region. The following illustration shows the string &\#0034;Hello&\#0034; clipped to a heart-shaped region.
ms.assetid: 58cc052d-31af-4410-81b9-defbad08a1dc
title: Clipping
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Clipping

Clipping involves restricting drawing to a certain region. The following illustration shows the string "Hello" clipped to a heart-shaped region.

![illustration showing parts of the string "hello" within a red heart](images/aboutgdip02-art30.png)

Regions can be constructed from paths, and paths can contain the outlines of strings, so you can use outlined text for clipping. The following illustration shows a set of concentric ellipses clipped to the interior of a string of text.

![illustration showing the string "hello" filled by a pattern of concentric circles](images/aboutgdip02-art31.png)

To draw with clipping, create a [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object, call its [SetClip](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(in const graphicspath_in combinemode)) method, and then call the drawing methods of that same **Graphics** object. The following example draws a line that is clipped to a rectangular region.


```
Region myRegion(Rect(20, 30, 100, 50));
myGraphics.DrawRectangle(&amp;myPen, 20, 30, 100, 50);  
myGraphics.SetClip(&amp;myRegion, CombineModeReplace);
myGraphics.DrawLine(&amp;myPen, 0, 0, 200, 200);
```



The following illustration shows the rectangular region along with the clipped line.

![illustration showing a rectangle with a diagonal line from top to bottom](images/aboutgdip02-art31a.png)

 

 



