---
Description: A GraphicsPath object stores a sequence of lines and B&\#233;zier splines.
ms.assetid: 8ce77146-dc28-4c0b-bcf0-dad4bf3d86e8
title: Flattening Paths
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Flattening Paths

A [**GraphicsPath**](/windows/win32/gdipluspath/nl-gdipluspath-graphicspath?branch=master) object stores a sequence of lines and Bézier splines. You can add several types of curves (ellipses, arcs, cardinal splines) to a path, but each curve is converted to a Bézier spline before it is stored in the path. Flattening a path consists of converting each Bézier spline in the path to a sequence of straight lines.

To flatten a path, call the [**GraphicsPath::Flatten**](/windows/win32/Gdipluspath/nf-gdipluspath-graphicspath-flatten?branch=master) method of a [**GraphicsPath**](/windows/win32/gdipluspath/nl-gdipluspath-graphicspath?branch=master) object. The **GraphicsPath::Flatten** method receives a flatness argument that specifies the maximum distance between the flattened path and the original path. The following illustration shows a path before and after flattening.

![illustration showing a sequence of connected bezier splines in blue and the corresponding lines in red](images/aboutgdip02-art32a.png)

 

 



