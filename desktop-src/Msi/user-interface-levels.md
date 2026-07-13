---
description: Windows Installer provides package developers the capability to author an internal user interface that has multiple levels of functionality.
ms.assetid: 9f5796a7-e244-4fc8-af85-52a147bb2c0b
title: User Interface Levels
ms.topic: reference
ms.date: 05/31/2018
---

# User Interface Levels

Windows Installer provides package developers the capability to author an internal user interface that has multiple levels of functionality. Because the internal UI must be created by the author of the package, the behavior of the full UI, reduced UI, basic UI, and None levels depends on the installation package. The following table describes the functionality commonly ascribed to UI levels.




| UI Level | Description | 
|----------|-------------|
| Full UI | Displays modal and modeless dialog boxes that have been authored into the internal UI. Displays authored [Error Dialog](error-dialog.md) boxes. **Note:** Modal dialog boxes require user input before the installation can continue and are specified by setting the [Modal Dialog Style Bit](modal-dialog-style-bit.md) in the Attributes column of the [Dialog](dialog-table.md) table. A modeless dialog box does not require user input for the installation to continue.<br> A full UI commonly exhibits [User Interface Wizard Behavior](user-interface-wizard-behavior.md).<br> | 
| Reduced UI | Displays any modeless dialog boxes that have been authored into the UI. Does not display any authored modal dialog boxes. Displays authored <a href="error-dialog.md">Error Dialog</a> boxes. Displays <a href="authoring-disk-prompt-messages.md">Disk Prompt</a> messages. Displays <a href="filesinuse-dialog.md">FilesInUse Dialog</a> boxes. | 
| Basic UI | Displays the built-in modeless dialog boxes that show progress messages. Displays built-in error dialog boxes. Does not display any authored dialog boxes. Prompts users to insert a disk by displaying a dialog box containing the <a href="diskprompt.md"><strong>DiskPrompt</strong></a> property value. | 
| None | None means a silent installation that displays no UI. | 




 

The level of the internal UI can be set using [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui). The installer sets the [**UILevel**](uilevel.md) property to the current level of the UI.

If the [**LIMITUI**](limitui.md) property is set, the user interface (UI) level used when installing the package is restricted to Basic.

For an example of UI authoring, see [An Installation Example](an-installation-example.md).

 

 




