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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Skin Definition File XML Structure

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




