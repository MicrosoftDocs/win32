---
Description: The Position Type of a Table of Contents
ms.assetid: cc2fbadc-43f7-470c-873b-de2dc9d84e5d
title: The Position Type of a Table of Contents
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The Position Type of a Table of Contents

Some methods of the [**ITocParser**](/windows/win32/wmcodecdsp/nn-wmcodecdsp-itocparser?branch=master) interface have a parameter named *enumTocPosType* that has a type of [**enum TOC\_POS\_TYPE**](/windows/win32/wmcodecdsp/ne-wmcodecdsp-toc_pos_type?branch=master). This parameter specifies the position in a media file where a table of contents is stored. The intent was that the table of contents could be stored either in the file header or in the body of the file as a top level object. This functionality has not, as yet, been implemented.

Currently, tables of contents can only be stored as top level objects, so you must always set the *enumTocPosType* parameter to **TOC\_POS\_TOPLEVELOBJECT**. If you set *enumTocPosType* to **TOC\_POS\_INHEADER**, the method will return **E\_NOTIMPL**.

The following methods have an *enumTocPosType* parameter.

-   [**GetTocCount**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itocparser-gettoccount?branch=master)
-   [**GetTocByIndex**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itocparser-gettocbyindex?branch=master)
-   [**GetTocByType**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itocparser-gettocbytype?branch=master)
-   [**AddToc**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itocparser-addtoc?branch=master)
-   [**RemoveTocByIndex**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itocparser-removetocbyindex?branch=master)
-   [**RemoveTocByType**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itocparser-removetocbytype?branch=master)

## Related topics

<dl> <dt>

[Table of Contents Parser Programming Guide](toc-parser-programming-guide.md)
</dt> </dl>

 

 



