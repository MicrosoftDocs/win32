---
Description: 'Windows Installer provides package developers the capability to author an internal user interface that has multiple levels of functionality.'
ms.assetid: '9f5796a7-e244-4fc8-af85-52a147bb2c0b'
title: User Interface Levels
---

# User Interface Levels

Windows Installer provides package developers the capability to author an internal user interface that has multiple levels of functionality. Because the internal UI must be created by the author of the package, the behavior of the full UI, reduced UI, basic UI, and None levels depends on the installation package. The following table describes the functionality commonly ascribed to UI levels.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>UI Level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Full UI</td>
<td>Displays modal and modeless dialog boxes that have been authored into the internal UI. Displays authored [Error Dialog](error-dialog.md) boxes.
<blockquote>
[!Note]<br />
Modal dialog boxes require user input before the installation can continue and are specified by setting the [Modal Dialog Style Bit](modal-dialog-style-bit.md) in the Attributes column of the [Dialog](dialog-table.md) table. A modeless dialog box does not require user input for the installation to continue.
</blockquote>
<br/> A full UI commonly exhibits [User Interface Wizard Behavior](user-interface-wizard-behavior.md).<br/></td>
</tr>
<tr class="even">
<td>Reduced UI</td>
<td>Displays any modeless dialog boxes that have been authored into the UI. Does not display any authored modal dialog boxes. Displays authored [Error Dialog](error-dialog.md) boxes. Displays [Disk Prompt](authoring-disk-prompt-messages.md) messages. Displays [FilesInUse Dialog](filesinuse-dialog.md) boxes.</td>
</tr>
<tr class="odd">
<td>Basic UI</td>
<td>Displays the built-in modeless dialog boxes that show progress messages. Displays built-in error dialog boxes. Does not display any authored dialog boxes. Prompts users to insert a disk by displaying a dialog box containing the [<strong>DiskPrompt</strong>](diskprompt.md) property value.</td>
</tr>
<tr class="even">
<td>None</td>
<td>None means a silent installation that displays no UI.</td>
</tr>
</tbody>
</table>



 

The level of the internal UI can be set using [**MsiSetInternalUI**](msisetinternalui.md). The installer sets the [**UILevel**](uilevel.md) property to the current level of the UI.

If the [**LIMITUI**](limitui.md) property is set, the user interface (UI) level used when installing the package is restricted to Basic.

For an example of UI authoring, see [An Installation Example](an-installation-example.md).

 

 




