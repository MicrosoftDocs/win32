---
description: Curved Paths
ms.assetid: 1ee9e6c6-5f8d-4727-b5f9-4b179c5371f1
title: Curved Paths
ms.topic: article
ms.date: 05/31/2018
---

# Curved Paths

An application can flatten the curves in a path by calling the [**FlattenPath**](/windows/desktop/api/Wingdi/nf-wingdi-flattenpath) function. This function is especially useful for applications that fit text onto the contour of a path which contains curves. To fit the text, the application must perform the following steps:

1.  Create the path where the text appears.
2.  Call the [**FlattenPath**](/windows/desktop/api/Wingdi/nf-wingdi-flattenpath) function to convert the curves in a path into line segments.
3.  Call the [**GetPath**](/windows/desktop/api/Wingdi/nf-wingdi-getpath) function to retrieve those line segments.
4.  Calculate the length of each line and the width of each character in the string.
5.  Use line-width and character-width data to position each character along the curve.

 

 



