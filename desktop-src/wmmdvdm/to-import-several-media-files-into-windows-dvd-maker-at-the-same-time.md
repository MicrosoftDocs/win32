---
title: To Import Several Media Files into Windows DVD Maker at the Same Time
description: To Import Several Media Files into Windows DVD Maker at the Same Time
ms.assetid: 'bf2a3f49-b81e-44a2-a0c9-6da08dc857de'
keywords: ["Windows DVD Maker,importing media files", "DVD Maker,importing media files", "programming reference,importing media files", "reference for Windows DVD Maker,importing media files", "command-line options for Windows DVD Maker,importing media files", "importing media files"]
---

# To Import Several Media Files into Windows DVD Maker at the Same Time

This option specifies an XML file that lists media files to be imported into Windows DVD Maker.

**Syntax**


```C++
dvdmaker 
importfilelist.xml
```



**Parameters**

*importfilelist.xml*

Specifies the path of an XML file that lists video, image, and audio files to import into Windows DVD Maker. The structure of the XML file is specified in Remarks.


```C++
<BurnWizard>
  <Content>
    <ContentFile Filename="C:\Users\johnevans\Pictures\ballard.jpg"/>
    <ContentFile 
DeleteOnClose="true" Filename="C:\Users\johnevans\Documents\shipcanal.wav"/>
    <ContentFile Filename="C:\Users\johnevans\Pictures\fremont.jpg"/>
    <ContentFile Filename="C:\Users\johnevans\Videos\u_district.wmv"/>
    <ContentFile 
DeleteOnClose="true" Filename="C:\Users\johnevans\Pictures\redmond.jpg"/>
  </Content>
  
<Title>My Seattle Trip
</Title>
  
<DeleteOnClose/>
</BurnWizard>
```



The **DeleteOnClose** attribute specifies whether the file indicated by the **Filename** attribute will be deleted when Windows DVD Maker is closed.

The **Title** element specifies a title for the disc. The string between the start and end tags will populate the **Disc Title** field in Windows DVD Maker.

The **DeleteOnClose** element at the end is optional; when present, it indicates that the XML file will be deleted when Windows DVD Maker is closed.

**Examples**


```C++
dvdmaker seattletrip.xml
```



## Remarks

The XML file you specify on the command line must be structured as follows:


```C++
<BurnWizard>
  <Content>
    <ContentFile Filename="C:\Users\johnevans\Pictures\ballard.jpg"/>
    <ContentFile 
DeleteOnClose="true" Filename="C:\Users\johnevans\Documents\shipcanal.wav"/>
    <ContentFile Filename="C:\Users\johnevans\Pictures\fremont.jpg"/>
    <ContentFile Filename="C:\Users\johnevans\Videos\u_district.wmv"/>
    <ContentFile 
DeleteOnClose="true" Filename="C:\Users\johnevans\Pictures\redmond.jpg"/>
  </Content>
  
<Title>My Seattle Trip
</Title>
  
<DeleteOnClose/>
</BurnWizard>
```



The **DeleteOnClose** attribute specifies whether the file indicated by the **Filename** attribute will be deleted when Windows DVD Maker is closed.

The **Title** element specifies a title for the disc. The string between the start and end tags will populate the **Disc Title** field in Windows DVD Maker.

The **DeleteOnClose** element at the end is optional; when present, it indicates that the XML file will be deleted when Windows DVD Maker is closed.

## Related topics

<dl> <dt>

[**Command-line Options for Windows DVD Maker**](command-line-options-for-windows-dvd-maker.md)
</dt> </dl>

 

 




