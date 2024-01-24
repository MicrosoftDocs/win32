---
title: Creating the Mapping File
description: Creating the Mapping File
ms.assetid: d882cd5b-1404-4dfd-8b51-a61e1505fae1
keywords:
- creating skins,mapping files
- Windows Media Player skins,art files
- skins,art files
- files for skins,art
- art files for skins,mapping images
- Windows Media Player skins,mapping images
- skins,mapping images
- mapping images in skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating the Mapping File

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Once you have created the pieces of your primary art file, it is relatively easy to create a mapping file. You will create the new mapping file by combining the art from the two button layers you already created.

1.  You will need to take the two buttons you created for the primary art file and copy them to a new layer. Use the following steps: Copy the Close button layer, remove any Layer effects, and rename it "Close map". The art should look flat, with no bevels.
2.  Use the Color Picker to create a foreground color of pure red. Be sure the color number value is "\#FF0000". Then use the Paint Bucket tool to fill the inside of the circle of the Close map layer.
3.  Copy the Play button layer, remove any Layer effects, and rename it "Play map". Again, the art should look flat. You do not want any effects in the mapping layer because you are just defining regions of the bitmap that Windows Media Player will use to determine where the mouse performs an action and what you want to do with it.
4.  Use the Color Picker to create a foreground color of pure green. Be sure the color number value is "\#00FF00". Then use the Paint Bucket tool to fill the inside of the circle of the Play map layer.

You are now ready to create the mapping art file. Hide all layers, and then show only the following layers, in this order (top to bottom):

Play map

Close map

Save to a new file using the Save a Copy command from the File menu. Select the BMP option in the Save As portion of the Save a Copy dialog box and type a file name that you will refer to later in your skin definition file. Ideally it should be in the same directory as your skin definition file. For example, you could call this file map.bmp. Choose the default settings and save the file.

Your mapping file should look like the following illustration.

![mapping file](images/g01map.png)

As you might guess, the green area will be used to determine when to make Windows Media Player start and the red area is for telling it to stop. Any two colors can be used, as long as you use the color numbers when you set up the skin definition file. Be sure the colors in the map are pure colors for the region you want to use and have distinct edges. A pure color would be one where every single pixel in the area has the same color value. Using an effect may blur or distort the edge, thereby slightly modifying the colors of some of the pixels. The mapping file is only seen by the mouse, not a human, so do not bother decorating it, and remove any layer effects you may have carried over from other layers.

When you save your file, the file name you choose will later be used as the value for the **mappingImage** attribute of the **BUTTONGROUP** element in your skin definition file.

## Related topics

<dl> <dt>

[**Building Your First Skin**](building-your-first-skin.md)
</dt> </dl>

 

 




