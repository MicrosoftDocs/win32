---
title: Skin Definition File XML Structure
description: Skin Definition File XML Structure
ms.assetid: 93325b94-667a-42a6-92f8-78288d36da81
keywords:
- creating skins,skin definition files
- Windows Media Player skins,skin definition files
- skins,skin definition files
- files for skins,skin definition
- skin definition files,XML structure
- XML structure for skin definition files
ms.topic: article
ms.date: 05/31/2018
---

# Skin Definition File XML Structure

The skin definition file is written in XML. One of the important features of XML is that it is completely structured, and is similar to an outline. The XML code is simply a series of elements such as **VIEW** and **BUTTONGROUP**. You will start with the elements and then define them with attributes. The rest of this tutorial will give you details on the attributes, but here is the outline of the elements that will be used:


```C++
<THEME>
    <VIEW>
        <BUTTONGROUP>
            <BUTTONELEMENT/>
            <BUTTONELEMENT/>
        </BUTTONGROUP>
    </VIEW>
<THEME>

```



By keeping in mind the simple structure of the elements, you can make sense of the attributes that make each element unique. Details of each element will be covered in the remaining topics of this section. For more information about elements and attributes, see the [Skin Programming Reference](skin-programming-reference.md).

## Related topics

<dl> <dt>

[**Creating the Skin Definition File**](creating-the-skin-definition-file.md)
</dt> </dl>

 

 




