---
title: To create an image map
description: To create an image map
ms.assetid: DF47F304-AD2C-4ca3-BB4C-A4E50CB01FC4
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To create an image map

1.  Use an image mapping program to create regions on an image that you want to annotate. These will be the areas that users click to open pop-up windows.
2.  Insert your image in the HTML file using the following syntax:

    ```
    <img src="<i>file.gif</i>" usemap="#<i>map name</i>" BORDER=0 WIDTH=216 HEIGHT=216> 
    ```

    

    where *file.gif* is the name of your image file and *map name* is the name of the image map that you created in step 1, above. The WIDTH and HEIGHT attributes will vary depending on the size of your image.

## Example

The following code shows an image map named `test` that has four regions:


```
<MAP NAME="test"> 
<AREA SHAPE=RECT COORDS="4,2,108,103"> 
<AREA SHAPE=RECT COORDS="117,6,212,104"> 
<AREA SHAPE=RECT COORDS="3,111,105,213"> 
<AREA SHAPE=RECT COORDS="114,113,211,210"> 
</MAP> 
```



The following code inserts an image named test.gif and references the image map named test:


```
<img src="images/test.gif" USEMAP="#test" BORDER=0 WIDTH=216 HEIGHT=216> 
```



The resulting image has four "placeholder" regions that you will "hook-up" to pop-up windows in [Step 5](to-add-hyperlinks-to-each-region-of-the-image-map.md):

![](images/test.gif)

## Related topics

<dl> <dt>

[Step 2: Write Text for Pop-up Windows](to-write-text-for-pop-up-windows.md)
</dt> </dl>

 

 




