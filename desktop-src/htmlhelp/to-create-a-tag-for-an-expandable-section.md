---
title: To create a tag for an expandable section
description: To create a tag for an expandable section
ms.assetid: 'B2E1E94B-D37D-443f-8118-7E6B85544FC8'
---

# To create a tag for an expandable section

-   Insert the following tags in your topic file at the location you want the expanding section to appear:

    ```
    <a onclick="<i>doSection(foo)</i>" class="<i>anchorclass</i>" href="<i>filename.htm</i>"><i>Link text</i></a>
    <DIV CLASS="divclass" ID="foo" STYLE="display: none" onclick="noSection(foo)"> 
    This is where the text appears. 
    </DIV> 
    ```

    

    Where *doSection* is the name of the first JavaScript function, which opens the section if it is closed, and closes it if it is open. *noSection* is the name of the second JavaScript function, which closes the section when the user clicks inside it. *foo* is the unique ID for this instance of the section, and filename.htm is the target file for the link.

> [!Note]  
> If you are including more than one instance of this tag on the same page, be sure that each instance has a unique ID.

 

## Related topics

<dl> <dt>

[Step 2: Insert the JavaScript Code](to-insert-the-javascript-code.md)
</dt> </dl>

 

 




