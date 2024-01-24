---
description: A Browse dialog box enables the user to select a directory. The directory does not have to exist and may be created by using this control.
ms.assetid: 35b991b8-d291-44ef-b1c0-8128bed3c3c8
title: Browse Dialog
ms.topic: article
ms.date: 05/31/2018
---

# Browse Dialog

A Browse dialog box enables the user to select a directory. The directory does not have to exist and may be created by using this control.

This type of dialog box commonly contains the following three controls. These controls are connected to the same property. That property is the path being selected.

-   A [PathEdit control](pathedit-control.md) to select the tail section of the path. This control cannot lose focus if the entered tail is not valid on the present volume.
-   A [DirectoryCombo control](directorycombo-control.md) to show the presently selected path that is displayed by the PathEdit control. This control does not show the last segment of the path.
-   A [DirectoryList control](directorylist-control.md) to show the folders below the directory currently displayed by the DirectoryCombo. This can also show a folder that is not yet created.

A Browse dialog box also usually contains a [DirectoryCombo control](directorycombo-control.md) that specifies the volume types to display. It is common for all volume types to be displayed on a Browse dialog box.

Browse dialog boxes commonly contain three [PushButton controls](pushbutton-control.md). These buttons are linked to their respective ControlEvents in [ControlEvent table](controlevent-table.md). These buttons are used for activating the following control options.



| Control option | ControlEvent                                            |
|----------------|---------------------------------------------------------|
| Up One Level   | [DirectoryListUp](directorylistup-controlevent.md)     |
| New Folder     | [DirectoryListNew](directorylistnew-controlevent.md)   |
| Open           | [DirectoryListOpen](directorylistopen-controlevent.md) |



 

For the New Folder option to work with a non-default folder name, the new folder's path must be specified in the [UIText table](uitext-table.md). The path string should use the "short file name\|long file name" form for the file name. For example, use a file name such as "MyProd~1\|My Fabulous Product". See the [Filename](filename.md) column data type for more information about the file name format. If the path is not present in the UIText table, or if it is set to an invalid value, then it is set to a value of "Fldr\|New Folder" by default. The **New Folder** button can be omitted if the dialog box only need to search for existing folders.

 

 



