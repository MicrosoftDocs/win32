---
title: Creating a Skin Definition File
description: Creating a Skin Definition File
ms.assetid: ea7f8e7c-a505-478d-80c3-cb3a3f67859d
keywords:
- Windows Media Player Mobile skins,skin definition files
- skins,skin definition files
- files for skins,skin definition
- skin definition files,creating
- creating skins,about
- creating skins,Windows Media Player Mobile
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating a Skin Definition File

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A skin definition file is a text file that defines a skin and all its composite parts. The file name extension must be .skn.

Every skin definition file must start with the following line, which specifies the skin file version number. The following table shows Windows Media Player versions and the code line that should be used to identify each in a skin definition file. Although some of the numbers in the code lines are not what you would expect, they are correct as shown in the following table.



| Windows Media Player version | First line of skin definition file |
|------------------------------|------------------------------------|
| 1.01.1<br/>            | \[Pocket WMP Skin File v1.0\]      |
| 1.2                          | \[Pocket WMP Skin File v1.2\]      |
| 7.0                          | \[Pocket WMP Skin File v2.0\]      |
| 7.1                          | \[Pocket WMP Skin File v8.0\]      |
| 9 Series                     | \[Pocket WMP Skin File v9.0.1\]    |
| 10 Mobile                    | \[Pocket WMP Skin File v9.0.1\]    |
| 10.1 Mobile                  | \[Pocket WMP Skin File v9.0.1\]    |



 

The version number 9.0.1 is for skins created specifically for Windows Media Player 9 Series or later. Skins having an earlier version number are opened by Windows Media Player 9 Series or later as portrait mode, 96 dots per inch (DPI) skins.

The skin definition file consists of several sections. Each section defines a particular area of the skin. The sections must be placed in the following order:

1.  Description
2.  Bitmaps
3.  Video
4.  Buttons
5.  Status
6.  Text
7.  Marquee
8.  Trackbars

Each section starts with the name of the section in square brackets, for example:


```C++
[ Bitmaps ]

```



> [!Note]  
> Your skin definition file will not be parsed correctly unless you include spaces between the brackets and the name of the section.

 

Then, one or more lines define individual images, buttons, and so on. For example, a Bitmaps section might include the following:


```C++
    Background  Background.bmp  0,0
    Disabled    Disabled.bmp    0,0
    Pushed      Pushed.bmp      0,0
    Region      Region.bmp      0,0
    Super       Super.bmp       0,0

```



It is not necessary to line up the values in columns, but it will help your code to be more readable. For more details about each section of the skin definition file, see the [Skin Reference](skin-reference.md).

> [!Note]  
> Do not use tabs anywhere in the file; use extra spaces instead. This is very important, because pressing the TAB key while writing or editing your skin definition file will cause the entire skin to fail. Each line must be complete and cannot continue onto a second line. Also, the Region and Super values are deprecated for skins used with Windows Media Player 10 Mobile or later.

 

## Related topics

<dl> <dt>

[**Skin Definition File**](skin-definition-file-mobile.md)
</dt> </dl>

 

 





