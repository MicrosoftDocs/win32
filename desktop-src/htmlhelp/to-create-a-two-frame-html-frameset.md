---
title: To create a two-frame HTML frameset
description: To create a two-frame HTML frameset
ms.assetid: 0E674302-2B78-440f-80A1-F3C9DFB39E92
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To create a two-frame HTML frameset

1.  On the **File** menu, click **New**, and then click **HTML File**.
2.  Enter a title for this file, which is the file that controls your frameset.
3.  Within the `<BODY>` start and end tags, type:
    ```
    <Frameset cols="40%,*"> <Frame name="left" src="left.htm"> <Frame name="right" src="right.htm"> </Frameset> 
    ```

    

4.  Delete the `<BODY>` start and end tags from the file. Your frameset will not work if the file that controls the frameset uses them.
5.  Save the file as **frames.htm**.

## Related topics

<dl> <dt>

[Step 2: Add a Navigation Frame](to-add-a-navigation-frame.md)
</dt> </dl>

 

 




