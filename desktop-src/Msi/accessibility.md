---
description: Authors should be aware of the tables and fields in the following list when designing their UI to be in compliance with Active Accessibility guidelines.
ms.assetid: 516e504e-7895-4388-a38e-fd2fc7dfd61d
title: Accessibility (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# Accessibility (Windows Installer)

Authors should be aware of the tables and fields in the following list when designing their UI to be in compliance with Active Accessibility guidelines. The user interface of an installer package should facilitate accessibility of the application or product to all users.

-   Tooltip text is contained in the Help column of the [Control table](control-table.md). This text is shown by screen readers for controls containing a picture.
-   The Text field of the [Control table](control-table.md) for the [VolumeCostList](volumecostlist-control.md), [ListView](listview-control.md), [DirectoryList](directorylist-control.md) and [SelectionTree](selectiontree-control.md) controls is never displayed. Instead it can be read by screen review utilities as the description of the control. People who cannot use the visual information on the screen can interpret the information with the aid of a screen review utility. Screen review utilities (also referred to as a screen reader programs or speech access utilities) take the displayed information on the screen and direct it through alternative media, such as synthesized speech or a refreshable Braille display.
-   Controls in dialog boxes should be linked using the Control\_Next field of the [Control table](control-table.md). The controls need to be authored such that they can all be reached by using the TAB key.
-   Shortcut keys should be provided for gaining access to controls directly.
-   Text color displayed in the user interface is set in the [TextStyle table](textstyle-table.md). If the chosen text color is too close to the background's then the text's color choice is ignored.
-   Text size and font is set in the [TextStyle table](textstyle-table.md). Larger font sizes should be used for packages intended for the Asian market. For example, a font size of 10 points that is legible for English text may not necessarily be true for Chinese.
-   For [Edit](edit-control.md), [PathEdit](pathedit-control.md), [ListView](listview-control.md), [ComboBox](combobox-control.md) or [VolumeSelectCombo controls](volumeselectcombo-control.md), screen readers take accName and accKeyboardShortcut from a [Text Control](text-control.md) that must precede the control in the Control\_Next sequence of the dialog box. The screen reader takes accName from the Text field of the Text control and accKeyboardShortcut from the keyboard shortcut in the Text field, if a shortcut exists.
-   Because static text cannot take the focus, a [Text control](text-control.md) that describes an [Edit](edit-control.md), [PathEdit](pathedit-control.md), [ListView](listview-control.md), [ComboBox](combobox-control.md) or [VolumeSelectCombo control](volumeselectcombo-control.md) must be made the first control in the dialog box to ensure compatibility with screen readers.
-   For a [PushButton control](pushbutton-control.md) that displays an icon or bitmap image, accName and accKeyboardShortcut are specified in the Help field of the [Control table](control-table.md) record, to the left of the \| separator.
-   Avoid the use of text controls on top of white bitmaps because under High Contrast Black the text may become invisible.
-   Do not put a black text control on a background that is an all white bitmap image. This text is not visible to a user who changes the Windows display to High Contrast Black.
-   Do not put a white text control on a background that is an all black bitmap image. This text is not visible to a user who changes the Windows display to High Contrast White.
-   Do not place transparent [Text controls](text-control.md) on top of colored bitmaps. The text may not be visible if the user changes the display color scheme. For example, text may become invisible if the user sets the high contrast parameter for accessibility.
-   Note that the focus on a dialog box does not tab to a [RadioButtonGroup control](radiobuttongroup-control.md) until one of the buttons in the group has been selected. To make the focus tab to this button group, specify one of the buttons as a default setting for the control.
-   To provide screen reader programs with extra descriptive text about a [RadioButtonGroup control](radiobuttongroup-control.md). Follow the example provided in [Adding Extra Text to Radio Buttons](adding-extra-text-to-radio-buttons.md).
-   The relative size of dialogs, controls and fonts can change depending upon the font size chosen. For more information see [Installer Units](installer-units.md). To ensure the correct display of text and controls in the user interface, setup developers should always test their application using all font sizes that might be used.

 

 



