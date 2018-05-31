---
title: To insert the HTML Help ActiveX control in your HTML file
description: To insert the HTML Help ActiveX control in your HTML file
ms.assetid: E7BFC959-C17C-49b5-9A08-CE91A8DBE847
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

    

    where *popup* is the ID of the control, which you will reference in [step 3](to-create-a-hyperlink-to-open-the-pop-up-window.md). If your HTML file already includes an instance of the control, you can reference that one.

## Notes

-   You can also insert the control by using the HTML Help ActiveX Control Wizard, and then delete the &lt;PARAM&gt; tags manually.
-   You can place the HTML Help ActiveX control syntax anywhere within the &lt;BODY&gt; start and end tags of your HTML file.
-   If you have inserted multiple instances of the HTML Help ActiveX control in the same HTML file, be sure that each instance has a unique ID.

## Related topics

<dl> <dt>

[Step 3: Create a Hyperlink to Open the Pop-up Window](to-create-a-hyperlink-to-open-the-pop-up-window.md)
</dt> </dl>

 

 




