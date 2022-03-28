---
description: Demonstrates how to create a verb that operates on a selected Shell item or container to create a playlist.
title: Playlist Creator Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: B35B7A18-2163-4860-BC50-8918056C9F4A
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Playlist Creator Sample

Demonstrates how to create a verb that operates on a selected Shell item or container to create a playlist.

This topic contains the following sections.

- [Requirements](#requirements)
- [Downloading the Sample](#downloading-the-sample)
- [Building the Sample](#building-the-sample)
- [Running the Sample](#running-the-sample)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [PlaylistCreator sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/PlaylistCreator) |

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **PlaylistCreator** project directory.
2.  Enter `msbuild PlaylistCreator.sln`.

To build the sample using Microsoft Visual Studio (preferred):

> [!Note]  
> This sample can also be used with the Visual C++ Express Edition if the full Visual Studio is not available.

 

1.  Open Windows Explorer and navigate to the **PlaylistCreator** project directory.
2.  Double-click the icon for the PlaylistCreator.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.
    > [!Note]  
    > If you are compiling 64-bit using the Visual C++ Express Edition, you must to use the x64 cross-compiler supplied with the Windows SDK.

     

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt or Windows Explorer.
2.  At the command line, enter `PlaylistCreator.exe`. Alternatively, from Windows Explorer double-click the icon for PlaylistCreator.exe.
3.  Right-click any music file or folder containing music files in Windows Explorer to create a playlist to bring up the context menu
4.  You can create a .m3u or .wpl playlist. Playlists are created in the `%userprofile%\Music\Playlists` folder.
    > [!Note]  
    > New verbs in the context menu can be found in the **Music** folder, music stacks, stacks in the **Music Library**, and collections of music files.

     

 

 



