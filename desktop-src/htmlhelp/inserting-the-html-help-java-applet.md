---
title: Inserting the HTML Help Java Applet
description: Inserting the HTML Help Java Applet into a help topic or Web page involves adding the APPLET tag, and specifying the commands you would like the applet to perform.
ms.assetid: '6F68853F-4395-478f-A9CC-89B7293B6129'
---

# Inserting the HTML Help Java Applet

Inserting the HTML Help Java Applet into a help topic or Web page involves adding the APPLET tag, and specifying the commands you would like the applet to perform.

## To insert the HTML Help Java Applet into an HTML file

1.  Open an HTML file, and then position the cursor at the location where you would like the HTML Help Java Applet to appear.
2.  Use the following syntax to add the applet:

    ```
    <APPLET code="HHCtrl.class" width=200 height=200 codebase="code base">
    <PARAM name="Command" value="command type">
    <PARAM name="Item1" value="text data">
    </APPLET> 
    ```

    

## Notes

-   The **CODEBASE** attribute must point to the location of the applet's class files.
-   The following commands can be specified:

    | Command        | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
    |----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Contents       | Specifies that a table of contents will appear based on the information supplied in the site map file specified in the *Item1* parameter (normally an .hhc file). The specified file must reside in the same directory as the document containing the applet. If the **Flags** parameter is specified, the first number is an extended window style, and the second is a TreeView or standard window style.<br/> |
    | Index          | Specifies that an index will appear based on the information supplied in the site map file specified in the *Item1* parameter.                                                                                                                                                                                                                                                                                         |
    | Related Topics | Specifies that related topics will appear based on the information supplied in the site map file specified in the *Item1* parameter.                                                                                                                                                                                                                                                                                   |

    

     

## Related topics

<dl> <dt>

[About the HTML Help Java Applet](about-the-html-help-java-applet.md)
</dt> </dl>

 

 





