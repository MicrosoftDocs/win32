---
title: To Import Several Media Files into Windows Movie Maker at the Same Time
description: To Import Several Media Files into Windows Movie Maker at the Same Time
ms.assetid: d804c711-a3d2-4e41-94a2-3ceeed543a09
keywords:
- Windows Movie Maker,importing media files
- Movie Maker,importing media files
- programming reference,importing media files
- reference for Windows Movie Maker,importing media files
- command-line options for Windows Movie Maker,importing media files
- importing media files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To Import Several Media Files into Windows Movie Maker at the Same Time

This option specifies an XML file that lists media files to be imported into Windows Movie Maker.

**Syntax**


```C++
moviemk 
importfilelist.xml
```



**Parameters**

*importfilelist.xml*

Specifies the path of an XML file that lists the video, image, and audio files to import into Windows Movie Maker. The structure of the XML file is specified in Remarks.

The XML file you specify on the command line must be structured as follows:


```C++
<?xml version="1.0" encoding="utf-16" ?> 
<MovieMk>
  <Content>
    <ContentFile Filename="C:\Users\johnevans\Pictures\cake.jpg" />
    <ContentFile Filename="C:\Users\johnevans\Videos\crowdcheer.wmv" /> 
    <ContentFile Filename="C:\Users\johnevans\Pictures\mom_and_dad.jpg" /> 
    <ContentFile Filename="C:\Users\johnevans\Music\Happy60th.wma" /> 
  </Content>
  <AutoEdit Style="FadeReveal" />
  
<DeleteOnClose/>
</MovieMk>
```



The **AutoEdit** element and the **DeleteOnClose** element are optional.

The **AutoEdit** element, when present, instructs Windows Movie Maker to run the AutoEdit feature on the files after they are imported. Valid styles for the **AutoEdit** element are "FadeReveal", "FlipAndSlide", "Highlights", "MusicVideo", "OldMovie", and "SportsHighlights".

The **DeleteOnClose** element, when present, indicates that the XML file will be deleted when Windows Movie Maker is closed.

**Examples**


```C++
moviemk C:\Users\johnevans\bdayfiles.xml
moviemk C:\Users\johnevans\bdayfiles.tmp
```



## Remarks

**Note**

The file name extension of the XML file can be .xml or .tmp.

The XML file you specify on the command line must be structured as follows:


```C++
<?xml version="1.0" encoding="utf-16" ?> 
<MovieMk>
  <Content>
    <ContentFile Filename="C:\Users\johnevans\Pictures\cake.jpg" />
    <ContentFile Filename="C:\Users\johnevans\Videos\crowdcheer.wmv" /> 
    <ContentFile Filename="C:\Users\johnevans\Pictures\mom_and_dad.jpg" /> 
    <ContentFile Filename="C:\Users\johnevans\Music\Happy60th.wma" /> 
  </Content>
  <AutoEdit Style="FadeReveal" />
  
<DeleteOnClose/>
</MovieMk>
```



The **AutoEdit** element and the **DeleteOnClose** element are optional.

The **AutoEdit** element, when present, instructs Windows Movie Maker to run the AutoEdit feature on the files after they are imported. Valid styles for the **AutoEdit** element are "FadeReveal", "FlipAndSlide", "Highlights", "MusicVideo", "OldMovie", and "SportsHighlights".

The **DeleteOnClose** element, when present, indicates that the XML file will be deleted when Windows Movie Maker is closed.

## Related topics

<dl> <dt>

[**Command-line Options for Windows Movie Maker**](command-line-options-for-windows-movie-maker.md)
</dt> </dl>

 

 




