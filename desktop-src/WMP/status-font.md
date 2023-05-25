---
title: Status Font
description: Status Font
ms.assetid: eba697e8-8be5-4692-b7b2-a52c5642022a
keywords:
- Windows Media Player Mobile skins,status display
- skins,status display
- reference for skins,status display
- status display in skins,fonts
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Status Font

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must define the font used by the status display you wish to use. The font is defined by three values, separated by commas, representing the face, size, and weight of the font.

**Typeface Values**

Any typeface name can be used if it is likely to be installed on the user's machine. If a typeface is not found on the machine, an alternate will be selected by the operating system. The following table shows the typefaces that are usually found on Windows Mobile 2003-based devices.



| Typeface       | Description              |
|----------------|--------------------------|
| Tahoma         | A sans-serif typeface.   |
| Lucida Console | A square-serif typeface. |



 

**Size Values**

This is the size of the typeface in points. Any positive integer value is valid, though numbers between 10 and 18 are recommended. Sizes smaller than 10 may be difficult to read, and sizes above 18 may not leave enough space to display more than a few letters at a time.

**Weight Values**

The only values allowed are shown in the following table.



| Value | Description |
|-------|-------------|
| B     | Bold        |
| N     | Normal      |



 

## Related topics

<dl> <dt>

[**Status**](status.md)
</dt> </dl>

 

 




