---
title: Skin Definition File Structure
description: Skin Definition File Structure
ms.assetid: 6b9ea288-ec64-473b-b796-ab637517099a
keywords:
- Windows Media Player skins,skin definition files
- skins,skin definition files
- files for skins,skin definition
- skin definition files,structure
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Skin Definition File Structure

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The skin definition file must follow a specific structure. You start with a **THEME** element, create one or more **VIEW** elements, and then define each **VIEW** element with the user interface elements appropriate for the type of view you want to use.

## THEME Elements

At the top level, you must start the skin definition file with the **THEME** element and close with it.


```C++
<THEME>
    ...
</THEME>

```



The **THEME** element is the root element for your skin. There can be only one **THEME** element in a skin definition file, and it must be at the top level. **THEME** elements have specific and ambient attributes, though most of the time you will not need to use them. For more information about these attributes, see the [Skin Programming Reference](skin-programming-reference.md).

## VIEW Elements

Each **THEME** must have at least one **VIEW** element. The **VIEW** element governs the particular image you see on the screen. You may want to have more than one view, so you can switch back and forth. For example, you might want to have a large view for working with playlists, a medium view for watching visualizations, and a tiny view that fits in a corner of the screen.

If you are creating multiple views, you will want to make sure that each view has a unique **ID** attribute value that will be used to identify the view. You must define the **backgroundImage** attribute or your view will have no starting image. If you do not want to display a rectangular image, you will probably want to use the **clippingColor** attribute to define the areas of your skin that will not display, and you will probably want to set the **titleBar** attribute of the **VIEW** element.

Each **VIEW** element can also have one or more **SUBVIEW** elements. A **SUBVIEW** element is similar to a **VIEW** and can be used for parts of your skin that you want to move around, hide, or show. For example, a **SUBVIEW** element might be used to create a sliding tray that pops out of your skin to display a graphic equalizer. **SUBVIEW** elements can be aligned with the **VIEW** and have other special relationships to the **VIEW**.

## Initializing Windows Media Player

You can set certain initial properties of Windows Media Player by using the **PLAYER**, **SETTINGS**, and **CONTROLS** elements. For example, you could set the volume to an initial level or give a default value for a file name.

The following code shows how to set the **URL** value in a skin:


```C++
<PLAYER
  URL = "https://proseware.com/mellow.wma">
</PLAYER>

```



If you wanted to set the **autoStart** attribute of **SETTINGS** to False, you would use the following code:


```C++
<PLAYER>
  <SETTINGS
    autoStart = "False">
  </SETTINGS>
</PLAYER>

```



Note that the **SETTINGS** element is nested inside the **PLAYER** element.

Using these elements, the following attributes and events can be specified at design time:

**PLAYER Element Attributes**

-   **url**
-   **Buffering**
-   **Currentitemchange**
-   **Currentplaylistchange**
-   **Error**
-   **Markerhit**
-   **Mediachange**
-   **Mediacollectionchange**
-   **Modechange**
-   **Mpenstatechange**
-   **Mlaylistchange**
-   **Mlaystatechange**
-   **Mositionchange**
-   **Mcriptcommand**
-   **Mtatuschange**

**SETTINGS Element Attributes**

-   **autoStart**
-   **balance**
-   **baseURL**
-   **defaultFrame**
-   **enableErrorDialogs**
-   **invokeURLs**
-   **mute**
-   **playCount**
-   **rate**
-   **volume**

## CONTROLS Element Attributes

-   **currentMarker**
-   **currentPosition**

## Other User Interface Elements

Once you have defined your **THEME** and **VIEW** elements, you must populate your **VIEW** with specific user interface elements. You do not have to use all the available elements in a skin, just the ones you need.

If an element can be seen by the user, it is called a control. The following controls are available for skins:

-   Buttons
-   Sliders, custom sliders, and progress bars
-   Text boxes
-   Video windows
-   Visualization windows
-   Playlist windows
-   Subview windows

In addition, several elements can be used to further define Windows Media Player actions, but they require visual elements such as buttons or sliders:

-   Video settings
-   Equalizer Settings
-   Visualization settings

## Buttons

Buttons are the most popular part of a skin. You can use buttons to trigger actions such as play, stop, quit, minimize, and switch to different view. Windows Media Player provides the skin creator with two types of button elements: the **BUTTON** element and the **BUTTONGROUP** element. In addition, there are several predefined types of buttons.

-   **BUTTON element.** The **BUTTON** element is used for individual buttons. If you use the **BUTTON** element, you must supply an image for each button and define the exact location where you want the button to appear relative to the background image. One of the advantages of the **BUTTON** element is that you can change the button image dynamically.
-   **BUTTONGROUP element.** The **BUTTONGROUP** element is used for groups of buttons. In fact, you must enclose each **BUTTONGROUP** element with a pair of **BUTTONGROUP** tags. Using button groups is easier than using individual buttons because you do not have to specify the exact location for each button. Instead, you supply a separate image map that defines the actions that will take place when the mouse hovers over or clicks an area on your background. Using image maps is easy because you can take the art you created for your background and copy it to a mapping layer in your graphics editing program. Using your graphics editing program is faster and more precise than trying to define exactly where an individual button should be placed on your background.
-   **Predefined buttons.** There are several predefined buttons. For example, you can use a PLAYELEMENT button to play digital media files, and a STOPELEMENT to stop playback. See [BUTTONGROUP](buttongroup-element.md) Element and [BUTTON Element](button-element.md) in the Skin Programming Reference. The [IMAGEBUTTON](imagebutton.md) can be used to display images that can change in response to specific events.

## Sliders

Sliders are useful for working with information that changes over time. For example, you might use a slider to indicate the amount of music that has already played for a particular media file. Sliders can be horizontal or vertical, linear or circular, or any shape you can think of. Sliders come in three varieties: sliders, progress bars, and custom sliders.

-   **Sliders.** You can use the **SLIDER** element for volume controls or to allow the user to move to a different part of the media content.
-   **Progress bars.** Progress bars are similar to sliders. Progress bars are designed for graphically displaying the percentage of a particular process that has been completed, but not for a process that the user will want to interact with. For example, you might want to use a progress bar to indicate buffering progress.
-   **Custom sliders.** Custom slider functionality is provided so you can create controls such as knobs, or make unusual control mechanisms. For example, if you want to create a volume control that wraps around your skin, you can do it with a custom slider. To set up the custom slider, you must create an image map that contains grayscale images to define the locations of the values on the slider. This is relatively easy to do with a graphics editing program that supports layers.

## Text

You can use the **TEXT** element to display text on your skin, such as song titles.

## Video

You can display video in your skin. The **VIDEO** element allows you to set the size and position of the video window.

You can also allow the user to change the video settings with the **VIDEOSETTINGS** element. For example, you can create controls to adjust the brightness of the video.

If you do not supply a video element and the content contains video, Windows Media Player will return to full mode and your skin will not be displayed.

## Equalizer Settings

You can set the filtering for specific audio frequency bands by using the **EQUALIZERSETTINGS** element. You can boost the bass, tweak the treble, and set up your sounds to match your ears or your living room.

## Visualizations

You can display visualizations in your skin. Visualizations are visual effects that change over time as audio is playing through Windows Media Player. The **EFFECTS** element determines where the visualizations will play, what size the window will be, and which visualizations will be played.

## Playlists

You can use the **PLAYLIST** element to let the user select an item from a specific playlist.

## Subviews

You can use the **SUBVIEW** element to display secondary sets of interface controls, such as a playlist or video controls.

## Related topics

<dl> <dt>

[**Skin Files**](skin-files.md)
</dt> </dl>

 

 




