---
title: About HTML Help URLs
description: About HTML Help URLs
ms.assetid: 'DB3F1302-6933-45e8-9AF7-E3C075549B51'
---

# About HTML Help URLs

Many of the HTML Help API commands require that you specify an HTML Help URL in the *pszURL* parameter.

An HTML Help URL specifies a compiled help (.chm) file or a topic within a help file. Usually, a [window type](window-types.md) in which to display the HTML Help URL is also specified.

### Specifing an HTML Help URL

The following example shows the syntax to display a compiled help file:


```
Helpfile.chm[>Window name] 
```



where Helpfile.chm is the name of the compiled help file and Window name is the name of the help window in which you want the topic to appear.

To specify a topic within a compiled help file, use the following syntax:


```
Helpfile.chm::/Topic.htm[>Window name] 
```



where Helpfile.chm is the name of the compiled help file, Topic.htm is the name of the HTML file that you want to open and Window name is the name of the help window in which you want the topic to appear.

### Specifying a topic file path

A compiled help file retains the folder structure in which it was organized before compilation, unless the option to compile flat has been selected.

For example, if a project is organized in three folders (one for HTML files, one for images, and one for style sheets), the help file will contain those same folders internally. The folder in which the project file resides is considered the root.

To correctly link to a topic file, you must specify the full path. The following example specifies an overview topic:


```
Helpfile.chm::/Html/Overview/Topic.htm[>Window name] 
```



where Overview is a folder within the Html folder.

### Notes

-   When coding an HTML &lt;A&gt; tag in an HTML file, or when specifying a compiled help file path in the HTML Help ActiveX control, you must include the prefix ms-its, which determines where the help file resides on a user's computer. The prefix ms-its is a pluggable protocol that follows standards set up by the [World Wide Web Consortium (W3C)](http://www.w3.org). The ms-its protocol works with Microsoft Internet Explorer 4.0 or later, but is not supported in all browsers.
-   The prefix mk:@MSITStore is an earlier version of the ms-its protocol that works with Microsoft Internet Explorer 3.0 or later.
-   The following examples show the syntax to use when including the prefix:
    ```
    ms-its:Helpfile.chm::/Topic.htm[>Window name]
    mk:@MSITStore:Helpfile.chm::/Topic.htm[>Window name]
    ```

    

## Related topics

<dl> <dt>

[About the HTML Help API](html-help-api-overview.md)
</dt> </dl>

 

 




