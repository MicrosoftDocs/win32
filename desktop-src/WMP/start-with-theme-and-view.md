---
title: Start with THEME and VIEW
description: Start with THEME and VIEW
ms.assetid: 1ac92f3a-463a-4343-a269-5230c644b57f
keywords:
- creating skins,THEME element
- Windows Media Player skins,THEME element
- skins,THEME element
- skin definition files,THEME element
- THEME element
- creating skins,VIEW element
- Windows Media Player skins,VIEW element
- skins,VIEW element
- skin definition files,VIEW element
- VIEW element
- elements,VIEW
- elements,THEME
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Start with THEME and VIEW

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Every skin must have exactly one **THEME** element and at least one **VIEW** element.

Using your text editor, create the following text:


```C++
<THEME>
    <VIEW
        clippingColor = "#CCCC00"
        backgroundImage = "background.bmp"
        titleBar = "False">


    </VIEW>
</THEME>

```



Leave some blank lines before the closing **VIEW** tag because you'll be adding more code here later.

Save your file with any file name you wish, but be sure that the extension is .wms. For example, a typical file name might be skinone.wms.

Every skin must start with &lt;THEME&gt; and end with </THEME>. You can only have one **THEME** element in your skin, but you must have one.

You must also have at least one **VIEW** element. You can have more than one **VIEW**, but this example only has one. You must have an opening &lt;VIEW&gt; and a closing &lt;VIEW&gt;. Notice that the opening &lt;/VIEW&gt; tag does not close the tag right away, but includes several attributes before the closing angle bracket (>). The following attributes are used in the **THEME** element in this example:

**clippingColor**

You will not always need the **clippingColor** attribute if the edges of your skin are rectangular. The skin in this example is oval-shaped, so you need a clipping color for the parts of the skin that you want to see the desktop through; essentially all parts outside the oval. In this example skin, we will use a dark yellow, specified as "\#CCCC00" in Web format. The reasons for this choice are given in [Creating the Primary Art File](creating-the-primary-art-file.md). Essentially, this value will always be a number that you get from your art program.

**backgroundImage**

This is the name of the primary art file. It should be the exact file name and path of your primary art file. Only BMP, JPG, GIF, and PNG files are supported, and BMP is recommended.

**titleBar**

This skin does not have a **titleBar**, so the value will be "false". You will only want a title bar if you want your skin to have a background color and be rectangular.

Be sure that you put the closing angle bracket (>) after the **titleBar** value to indicate that you are finished defining the **VIEW**. Leave a few blank lines before the closing **VIEW** and **THEME** tags. You will need the lines for code that you will add later.

## Related topics

<dl> <dt>

[**Creating the Skin Definition File**](creating-the-skin-definition-file.md)
</dt> </dl>

 

 




