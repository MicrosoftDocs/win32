---
title: Windows DVD Maker Project File Format
description: Windows DVD Maker Project File Format
ms.assetid: '13195a7a-a91f-4b9b-8889-acb7aaeb8b5c'
keywords: ["Windows DVD Maker,project file format", "DVD Maker,project file format", "programming reference,Windows DVD Maker project file format", "reference for Windows DVD Maker,project file format", "project file format for Windows DVD Maker"]
---

# Windows DVD Maker Project File Format

This section contains reference information for the Windows DVD Maker Project File Format. A project file is a simple XML-based file consisting of elements that describe the media content, title, menu style, button names, and other information about a Windows DVD Maker project.

The following XML code defines the elements that make up the project file format.


```C++
<BurnWizard>
    <Content>
        <ContentFile Filename="c:\content\video1.avi"/>
        <ContentFile Filename="c:\content\video2.wmv"/>
        <ContentFile Filename="c:\content\sunset.jpg"/>
        <ContentFile Filename="c:\content\winter.jpg"/>
        <ContentFile Filename="c:\content\mysong.wma"/>
    </Content>
    <Title>4/27/2006</Title>
    <Drive>D:</Drive>
    <Style>Bandwidth</Style>
    <Font Name="" Color="0xFF00FF00" Bold="1" Italic="0"/>
    <Button Play="Play" Scenes="Scenes" Notes="Notes"/>
    <Notes></Notes>
    <InsetVideo></InsetVideo>
    <BackgroundVideo></BackgroundVideo>
    <MenuAudio></MenuAudio>
    <SceneButtonName></SceneButtonName>
    <SlideShow Transition="Cross fade" PanZoom="0" MatchMusic="0" Length="75.000000"/>
</BurnWizard>
```



The following table describes the elements in the project file format.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Content</strong></td>
<td>Denotes the content block. Only <strong>ContentFile</strong> elements are allowed inside.</td>
</tr>
<tr class="even">
<td><strong>ContentFile</strong></td>
<td>A media file to add to DVD Maker. A file in the content block is treated exactly the same as if it were added through the <strong>Add Items</strong> dialog box. Video files are added to the main list, still images are added to a slide show folder, and audio is added to the slide show.</td>
</tr>
<tr class="odd">
<td><strong>Title</strong></td>
<td>The title of the disc.</td>
</tr>
<tr class="even">
<td><strong>Drive</strong></td>
<td>The drive letter of the DVD burner to use.</td>
</tr>
<tr class="odd">
<td><strong>Style</strong></td>
<td>The name of the style to use. If blank, the default style is used.</td>
</tr>
<tr class="even">
<td><strong>Font</strong></td>
<td>The name and color of the font, and whether it is bold or italic. For the color value, the first two characters must be &quot;FF&quot;, and the values for the red, green, and blue components are defined by two character hexadecimal values. For example, &quot;0xFF00FF00&quot; is pure green, and &quot;0xFF0000FF&quot; is pure blue.</td>
</tr>
<tr class="odd">
<td><strong>Button</strong></td>
<td>The names of the buttons used on the main DVD menu.</td>
</tr>
<tr class="even">
<td><strong>Notes</strong></td>
<td>The text that shows up on the notes page. The maximum number of characters supported is 256.</td>
</tr>
<tr class="odd">
<td><strong>InsetVideo</strong></td>
<td>The setting of the <strong>Foreground video</strong> combo box on the <strong>Customize</strong> page.</td>
</tr>
<tr class="even">
<td><strong>BackgroundVideo</strong></td>
<td>The setting of the <strong>Background video</strong> combo box on the <strong>Customize</strong> page.</td>
</tr>
<tr class="odd">
<td><strong>MenuAudio</strong></td>
<td>The setting of the <strong>Menu audio</strong> combo box on the <strong>Customize</strong> page.</td>
</tr>
<tr class="even">
<td><strong>SceneButtonName</strong></td>
<td>The name of the scene button style set on the <strong>Customize</strong> page.</td>
</tr>
<tr class="odd">
<td><strong>SlideShow</strong></td>
<td>Attributes for slide show settings. <strong>Transition</strong> sets the name of the transition to use, <strong>Length</strong> is the amount of time each slide will be on the screen, and <strong>PanZoom</strong> and <strong>MatchMusic</strong> are used to set the following settings:
<ul>
<li><strong>Use pan and zoom effects for pictures</strong></li>
<li><strong>Change slide show length to match music length</strong></li>
</ul></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[**Windows DVD Maker Programming Reference**](windows-dvd-maker-programming-reference.md)
</dt> </dl>

 

 




