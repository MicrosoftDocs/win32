---
title: Buttons (Windows Media Player SDK)
description: Buttons
ms.assetid: 1212e2d9-e8f8-45d8-8c7f-20865c9c9c94
keywords:
- Windows Media Player Mobile skins,button overview
- skins,button overview
- reference for skins,buttons
- buttons in skins,about
ms.topic: article
ms.date: 05/31/2018
---

# Buttons (Windows Media Player SDK)

You will want to use one or more buttons in your skin, and each button must be defined in the skin definition file. If you do not define a button in this section, your skin will not be able to use it.

The buttons section of the skin definition file begins with this line:


```C++
[ Buttons ]

```



You then must add one or more lines that contain information about each of the buttons in your skin. A typical line might be:


```C++
    PlayPause  2PushHit   84,99,67,67   Pushed @ 44,50    Disabled @ 44,50     0,255,255  Pushed @ 160,5      Pushed @ 160,98

```



Note that this code should be typed as one line starting with "PlayPause" and ending with "Pushed @ 160,98".

You can use the following template for the Button section of your skin definition file:


```C++
//  <Function> <Type>     <Location>     <Push Image Src> <Dis Image Src>    <Hit R,G,B> <Norm 2 Image Src> <Push 2 Image Src>
//  ---------- ------     ----------     ---------------- ---------------    ----------- ------------------ ------------------

```



Again, note that these should be typed as single lines, the first starting with "// <Function>" and ending with "&lt;Push 2 Image Src&gt;". The second line starts with "// ----------" and ends with "------------------."

Button information for each line in the Button section must appear in the following order. Only the first six parts of the line are required. Secondary images are not included unless they are needed.

1.  [Button Function](button-function.md)
2.  [Button Type](button-type.md)
3.  [Button Location](button-location.md)
4.  [Pushed Image Source](pushed-image-source.md)
5.  [Image Source for Disabled Button](image-source-for-disabled-button.md)
6.  [Hit RGB Color](hit-rgb-color.md)
7.  [Normal Secondary Image Source](normal-secondary-image-source.md)
8.  [Normal Tertiary Image Source](normal-tertiary-image-source.md)
9.  [Pushed Secondary Image Source](pushed-secondary-image-source.md)
10. [Pushed Tertiary Image Source](pushed-tertiary-image-source.md)

For an example of button code, see [Sample Button Section](sample-button-section.md).

## Related topics

<dl> <dt>

[**Skin Reference**](skin-reference.md)
</dt> </dl>

 

 




