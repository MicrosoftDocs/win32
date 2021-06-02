---
description: 'There are a number of formats in which ink data can be stored, including:'
ms.assetid: b08fba71-46cb-4419-9da5-a33a5b9a5ec0
title: Ink Data Formats
ms.topic: article
ms.date: 05/31/2018
---

# Ink Data Formats

There are a number of formats in which ink data can be stored, including:

-   Ink serialized format (ISF)
-   HTML
-   Rich Text Format (RTF)
-   Binary format
-   Extensible Markup Language (XML) based formats

Different formats are applicable under different circumstances. To interact most successfully with the Clipboard, applications should be able to recognize and generate as many different formats as possible.

The most important and basic format that can be used to store ink is Ink Serialized Format (ISF). ISF provides a compact but complete representation of a single [**Ink**](inkdisp-class.md) object.

An equally important format is HTML. Ink data can be represented in HTML in such a way that it can be viewed as an image by applications that do not recognize ink. In addition, the full fidelity of the ink is maintained. For these reasons, and because it is a commonly understood format that allows for the representation of many different types of content, Microsoft recommends HTML as the format for sharing ink.

It is possible to store ink in other formats, as well. By using RTF as the format, you can paste ink into applications that do not recognize ink, such as Microsoft Word 2002. This is done by embedding OLE objects that contain ink within the RTF. Still other formats, such as binary or XML-based formats, can be used.

The formats you choose for a particular application to copy, paste, or serialize ink should be based on that applications specific needs and resources. At a minimum, an application should be able to copy and paste ISF, which allows for the lowest level of ink interoperability. Both ISF and the ability to copy and paste ISF are built into the Tablet PC platform. However, many applications need to represent more complex content, such as a selection containing multiple ink objects or formatted text. In such a case, an application can copy and paste HTML. This allows for a maximum amount of flexibility. HTML is widely understood and easy to generate. Finally, applications that already produce RTF or have a strong need to communicate with older applications should produce an RTF format as well.

> [!Note]  
> Throughout the discussion of ink interoperability, bitmap, ISF, and GIF are image formats. The text ink object (tInk) and sketch ink object (sInk) are OLE objects. Binary, HTML, XML, and RTF are document formats in which the images are consumed.

 

The Tablet PC platform provides APIs to help you generate and interpret these formats. There are many options that together should fit the interoperability and persistence needs of any application. For more information about ink formats, see [Persistence Formats](persistence-formats.md).

 

 



