---
description: Developers of installation packages can author a user interface containing the controls discussed in this topic.
ms.assetid: ed9fa158-9dad-4d2d-8153-78122b19a34e
title: Controls (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# Controls (Windows Installer)

Developers of installation packages can author a user interface containing the controls discussed in this topic. For information on how to add a particular control to a dialog box, see the topic for that control and read the section [Adding Controls and Text](adding-controls-and-text.md).

Some controls, such as CheckBox and ComboBox, are associated with a property specified in the Property column of the [Control table](control-table.md). A user changes the value of this property by interacting with the control. Passive controls, such as Billboard and bitmap, are not associated with such a property.

For security, private properties cannot be changed by a user interacting with the user interface. For a property to be set by the user interface, it needs to be a public property and in uppercase. See also [About Properties](about-properties.md).

In some cases a control may be redrawn incorrectly when canceling out of a dialog. This has to do with the order in which the controls receive WM\_PAINT messages after the Cancel dialog is removed. To fix this, try changing the order of the controls in the Control table.



| Control name                                       | Associated property | Brief description of control                                                                                                                                                          |
|----------------------------------------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Billboard](billboard-control.md)                 | No                  | Displays billboards based on progress messages.                                                                                                                                       |
| [Bitmap](bitmap-control.md)                       | No                  | Displays a static picture of a bitmap.                                                                                                                                                |
| [CheckBox](checkbox-control.md)                   | Yes                 | A two-state check box.                                                                                                                                                                |
| [ComboBox](combobox-control.md)                   | Yes                 | A drop-down list with an edit field.                                                                                                                                                  |
| [DirectoryCombo](directorycombo-control.md)       | Yes                 | Select all except the last segment of the path.                                                                                                                                       |
| [DirectoryList](directorylist-control.md)         | Yes                 | Displays folders below the main part of path.                                                                                                                                         |
| [Edit](edit-control.md)                           | Yes                 | A regular edit field for any string or integer.                                                                                                                                       |
| [GroupBox](groupbox-control.md)                   | No                  | Displays a rectangle that groups other controls together.                                                                                                                             |
| [Hyperlink](hyperlink-control.md)                 | No                  | Displays a HTML link to an address, which opens in the default browser.**[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/> |
| [Icon](icon-control.md)                           | No                  | Displays a static picture of an icon.                                                                                                                                                 |
| [Line](line-control.md)                           | No                  | Displays a horizontal line.                                                                                                                                                           |
| [ListBox](listbox-control.md)                     | Yes                 | A drop-down list without an edit field.                                                                                                                                               |
| [ListView](listview-control.md)                   | Yes                 | Displays a column of values with icons for selection.                                                                                                                                 |
| [MaskedEdit](maskededit-control.md)               | Yes                 | An edit field with a mask in the text field.                                                                                                                                          |
| [PathEdit](pathedit-control.md)                   | Yes                 | Displays folder name or entire path in an edit field.                                                                                                                                 |
| [ProgressBar control](progressbar-control.md)     | No                  | Bar graph that changes length as it receives progress messages.                                                                                                                       |
| [PushButton](pushbutton-control.md)               | No                  | Displays a basic push button.                                                                                                                                                         |
| [RadioButtonGroup](radiobuttongroup-control.md)   | Yes                 | A group of radio buttons.                                                                                                                                                             |
| [ScrollableText](scrollabletext-control.md)       | No                  | Displays a long string of text.                                                                                                                                                       |
| [SelectionTree](selectiontree-control.md)         | Yes                 | Displays information from the Feature table and enables the user to change their selection state.                                                                                     |
| [Text](text-control.md)                           | No                  | Displays static text.                                                                                                                                                                 |
| [VolumeCostList](volumecostlist-control.md)       | No                  | Displays costing information on different volumes.                                                                                                                                    |
| [VolumeSelectCombo](volumeselectcombo-control.md) | Yes                 | Selects volume from an alphabetical list.                                                                                                                                             |



 

 

 




