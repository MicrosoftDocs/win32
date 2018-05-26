---
title: To insert the HTML Help ActiveX control in your HTML file
description: To insert the HTML Help ActiveX control in your HTML file
ms.assetid: 9EB03159-FCB8-481E-A7B0-F68FC886AA53
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To insert the HTML Help ActiveX control in your HTML file

-   Copy the following HTML Help ActiveX control syntax in your file:

    ```
    <OBJECT
       id=<i>popup</i>
       type="application/x-oleobject"
       classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
    >
    </OBJECT>
    ```

    

    where *popup* is the ID of the control, which you will reference in [step 5](to-create-a-hyperlink-to-open-the-pop-up-window.md). If your HTML file already includes an instance of the control, you can reference that one.

## Notes

-   You can also insert the control by using the HTML Help ActiveX Control Wizard, and then delete the &lt;PARAM&gt; tags manually.
-   You can place the HTML Help ActiveX control syntax anywhere within the &lt;BODY&gt; start and end tags of your HTML file.
-   If you have inserted multiple instances of the HTML Help ActiveX control in the same HTML file, be sure that each instance has a unique ID.

## Related topics

<dl> <dt>

[Step 5: Add hyperlinks to each region of the image map](to-create-a-hyperlink-to-open-the-pop-up-window.md)
</dt> </dl>

 

 




