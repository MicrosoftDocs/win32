---
title: Constants and Enumerations
description: Reference documentation for the Windows Ribbon framework constants and enumerations.
ms.assetid: 8499a096-aac3-4af3-a4c9-eebf53698744
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Constants and Enumerations

Reference documentation for the Windows Ribbon framework constants and enumerations.

### Constants and Enumerations



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>UI_ALL_COMMANDS</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371543)<br/></td>
<td>Specifies a constant that identifies the collection of Commands declared in the Markup resource file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UI_COLLECTION_INVALIDINDEX</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371551)<br/></td>
<td>Specifies a constant that identifies an invalid index in a collection.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UI_COLLECTIONCHANGE</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371548)<br/></td>
<td>Specifies values that identify the types of changes that can be made to a collection.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UI_COMMANDCATEGORY</strong>](/windows/desktop/api/Uiribbon/)<br/></td>
<td>Specifies values that indicate whether a Command was defined at compile time or at run time.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UI_COMMANDTYPE</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371556)<br/></td>
<td>Specifies values that identify the type of Command associated with a Ribbon control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UI_CONTEXTAVAILABILITY</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371558)<br/></td>
<td>Specifies values that identify the availability of a [<strong>contextual tab</strong>](windowsribbon-element-ribbon-contextualtabs.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UI_CONTROLDOCK</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371560)<br/></td>
<td>Specifies values that identify the dock state of the Quick Access Toolbar (QAT). <br/></td>
</tr>
<tr class="even">
<td>[<strong>UI_EVENTLOCATION</strong>](/windows/desktop/api/Uiribbon/ne-uiribbon-ui_eventlocation)<br/></td>
<td>Identifies the locations where events associated with a Ribbon control can originate.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UI_EVENTTYPE</strong>](/windows/desktop/api/Uiribbon/ne-uiribbon-ui_eventtype)<br/></td>
<td>Identifies the types of events associated with a [<strong>Ribbon</strong>](windowsribbon-element-ribbon.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>UI_EXECUTIONVERB</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371563)<br/></td>
<td>Specifies values that identify the execution IDs that map to actions a user can initiate on a [<strong>Command</strong>](windowsribbon-element-command.md). <br/></td>
</tr>
<tr class="odd">
<td>[<strong>UI_FONTDELTASIZE</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371565)<br/></td>
<td>Specifies values that identify whether the font size of a highlighted text run should be incremented or decremented.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UI_FONTPROPERTIES</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371566)<br/></td>
<td>Specifies values that identify the font property state of a [<strong>FontControl</strong>](windowsribbon-element-fontcontrol.md), such as <strong>Strikethrough</strong>.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UI_FONTUNDERLINE</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371568)<br/></td>
<td>Specifies values that identify the underline state of a [<strong>FontControl</strong>](windowsribbon-element-fontcontrol.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>UI_FONTVERTICALPOSITION</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371571)<br/></td>
<td>Specifies values that identify the vertical-alignment state of a [<strong>FontControl</strong>](windowsribbon-element-fontcontrol.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UI_INVALIDATIONS</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371573)<br/></td>
<td>Specifies values that identify the aspect of a Command to invalidate.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UI_OWNERSHIP</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371576)<br/></td>
<td>Specifies values that identify the ownership conditions under which an image is created by the Ribbon framework.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UI_SWATCHCOLORMODE</strong>](/windows/desktop/api/Uiribbon/ne-uiribbon-ui_swatchcolormode)<br/></td>
<td>Specifies whether a swatch has normal or monochrome mode.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UI_SWATCHCOLORTYPE</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371583)<br/></td>
<td>Specifies the values that identify how a color swatch in a [<strong>DropDownColorPicker</strong>](windowsribbon-element-dropdowncolorpicker.md) or a [<strong>FontControl</strong>](windowsribbon-element-fontcontrol.md) color picker (<strong>Text color</strong> or <strong>Text highlight</strong>) is filled.<br/>
<blockquote>
[!Note]<br />
These are recommendations only. The application can associate any fill type with these values.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UI_VIEWTYPE</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371586)<br/></td>
<td>Specifies values that identify the Ribbon framework View.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UI_VIEWVERB</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371588)<br/></td>
<td>Specifies values that identify the type of action to complete on a Ribbon framework View.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Reference](windowsribbon-reference-entry.md)
</dt> </dl>

 

 





