---
Description: The Position Type of a Table of Contents
ms.assetid: 'cc2fbadc-43f7-470c-873b-de2dc9d84e5d'
title: The Position Type of a Table of Contents
---

# The Position Type of a Table of Contents

Some methods of the [**ITocParser**](itocparser.md) interface have a parameter named *enumTocPosType* that has a type of [**enum TOC\_POS\_TYPE**](toc-pos-type.md). This parameter specifies the position in a media file where a table of contents is stored. The intent was that the table of contents could be stored either in the file header or in the body of the file as a top level object. This functionality has not, as yet, been implemented.

Currently, tables of contents can only be stored as top level objects, so you must always set the *enumTocPosType* parameter to **TOC\_POS\_TOPLEVELOBJECT**. If you set *enumTocPosType* to **TOC\_POS\_INHEADER**, the method will return **E\_NOTIMPL**.

The following methods have an *enumTocPosType* parameter.

-   [**GetTocCount**](itocparser-gettoccount.md)
-   [**GetTocByIndex**](itocparser-gettocbyindex.md)
-   [**GetTocByType**](itocparser-gettocbytype.md)
-   [**AddToc**](itocparser-addtoc.md)
-   [**RemoveTocByIndex**](itocparser-removetocbyindex.md)
-   [**RemoveTocByType**](itocparser-removetocbytype.md)

## Related topics

<dl> <dt>

[Table of Contents Parser Programming Guide](toc-parser-programming-guide.md)
</dt> </dl>

 

 



