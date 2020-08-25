---
title: Src Attribute (VMLFrame)(VML)
description: Src Attribute (VMLFrame)(VML)
ms.assetid: 6ac7a3b5-3c1d-43a0-ab92-a03e3bd45733
ms.topic: article
ms.date: 05/31/2018
---

# Src Attribute (VMLFrame)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the source of data for the frame. Read/write. **String**.

**Applies To**

[VMLFrame](msdn-online-vml-vmlframe-element.md)

**Tag Syntax**

<v: *element* src=" *expression* ">

**Script Syntax**

*element* .src="*expression*"

*expression*=*element*.src

**Remarks**

The **Src** attribute can involve the following syntaxes:

-   URL to external file. The file must be an XML file with the following format:
    ```HTML
       <xml xmlns:v = "urn:schemas-microsoft-com:vml">
       .
       .
       .
       </xml>
    ```

    

-   Inside the file you must have one or more VML shapes with valid IDs that can be referenced by using this syntax:
    ```HTML
       filename#shapename
    ```

    

-   In the following reference, external files have the .vml extension, but any extension can be used:
    ```HTML
       external.vml#image01
    ```

    

-   You can reference a shape within the same file by using the following syntax:
    ```HTML
       #shapename
    ```

    

If **Clip** is **False**, the shape will scale to fit the frame. If **True**, any parts of the shape that are outside the frame will not be displayed.

Note that [Origin](origin-attribute--vmlframe--vml.md) and [Size](size-attribute--vmlframe.md) won't be used unless **Clip** is **True**.

**VML Standard Attribute**

**Example**

The image defined in the external file will be clipped.


```HTML
   <v:vmlframe id="frame01" clip="True"
   origin="100pt,100pt" size="50pt,50pt"
   src="external.vml#shape01"
   style='top:160pt; left:100pt; width:50pt; height:50pt'>
   </v:vmlframe>
```



 

 