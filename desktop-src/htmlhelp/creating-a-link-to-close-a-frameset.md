---
title: Creating a Link to Close a Frameset
description: Currently the HTML Help ActiveX Control Close command does not work properly with Web pages that contain frames.
ms.assetid: '75862CC6-D690-48e4-B467-D6CA41EBF29B'
---

# Creating a Link to Close a Frameset

Currently the HTML Help ActiveX Control [Close](close.md) command does not work properly with Web pages that contain frames. Because of this, you will need to create a special link to close such pages. This link will close the main browser window and all of the frames it contains.

## To close a window that contains a frameset

1.  Open the HTML file in which you want to include the link.
2.  Position your cursor where you want the link to appear.
3.  Add the link using the following syntax:

    ```
    <A HREF=JavaScript:window.top.close()>Close</A>
    ```

    

 

 




