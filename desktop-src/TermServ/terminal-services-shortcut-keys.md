---
title: Remote Desktop Services Shortcut Keys
description: A list of the Remote Desktop Services shortcut keys.
ms.assetid: 03a94323-2616-4f35-a5c0-3c238acb7693
ms.tgt_platform: multiple
keywords:
- Remote Desktop Services Remote Desktop Services , shortcut keys
- Remote Desktop Services Remote Desktop Services , keyboard shortcuts
ms.topic: article
ms.date: 09/10/2021
---

# Remote Desktop Services Shortcut Keys

The following is a list of the Remote Desktop Services shortcut keys.

A note regarding missing keys: Many compact keyboards do not contain some keys. For example, many laptops do not have a dedicated BREAK key. However, they usually have keyboard shortcuts that replace dedicated keys. These key replacements are specified by the manufacturer of the keyboard, so you may need to look up key replacements in the documentation provided by your keyboard or laptop manufacturer.

There are two different sets of shortcut key combinations you can use on a remote desktop connection: the default Windows shortcut keys, or the shortcut keys originally designed for the remote desktop. You can set which shortcut keys you use on the local and remote machine through the Remote Desktop Connection client (ie, the dialog that appears when you click on the **Remote Desktop Connection** icon). From there, click **Show Options** (if you cannot see the options), and then click the **Local Resources** tab. In the **Apply Windows key combinations** drop-down, you have three options:

| Option | Description |
|--------|-------------|
| **On this computer** | The default key combinations will work on your local machine only. You must use the alternate combinations on the remote desktop.|
| **On the remote computer** | The default key combinations will work only on the remote desktop. You must use the alternate combinations on the local machine. Note that once you close down the Remote Desktop Connection, your local machine will once again use the default windows shortcuts. |
| **Only when using the full screen** | The default key combinations will work on whichever machine has the full desktop; functionally, this means that the default key combinations work for the local machine, unless you have the Remote Desktop Connection window in full-screen mode. |

For more user information about Remote Desktop connection, See [How to use Remote Desktop](https://windows.microsoft.com/windows/remote-desktop-connection-faq#1TC=windows-8).




| Shortcut key | Description | 
|--------------|-------------|
| CTRL+ALT+HOME<br /> | Activates the <strong>connection</strong> bar.<br /> | 
| CTRL+ALT+BREAK or one of these shortcuts:<br /><ul><li>CTRL+ALT+PAUSE<br /></li><li>CTRL+ALT+PRTSCN<br /></li><li>CTRL+ALT+FN+SCRLK<br /></li></ul> | Switches the client between full-screen mode and window mode.<br /> If these shortcuts don't work, or the keys aren't available, you can try the following alternative:<br /><ul><li>Press CTRL+ALT+HOME, TAB, TAB, TAB, TAB, TAB, ENTER. This activates the <strong>connection</strong> bar, and then presses the <strong>Restore down</strong> button.<br /></li></ul> | 
| CTRL+ALT+END<br /> | Brings up the <strong>Windows Security</strong> dialog box for the Remote Desktop Session Host (RD Session Host) (provides the same functionality as pressing CTRL+ALT+DEL on the local computer).<br /> | 




 

The following table describes the standard Windows shortcut keys and their equivalent Remote Desktop shortcuts that are different. (For example, Ctrl+Z is generally the 'Undo' shortcut on both standard Windows and Remote Desktop.)



| Windows shortcut                                         | Remote Desktop shortcut            | Description                                                                             |
|----------------------------------------------------------|------------------------------------|-----------------------------------------------------------------------------------------|
| ALT+TAB<br/>                                       | ALT+PAGE UP<br/>             | Switches between programs from left to right.<br/>                                |
| ALT+SHIFT+TAB<br/>                                 | ALT+PAGE DOWN<br/>           | Switches between programs from right to left.<br/>                                |
|                                                          | ALT+INSERT<br/>              | Cycles through the programs in the order they were started.<br/>                  |
| Windows key<br/> or<br/> CTRL+ESC<br/> | ALT+HOME<br/>                | Displays the **Start** menu.<br/>                                                 |
| ALT+SPACE BAR<br/>                                 | ALT+DELETE<br/>              | Displays the **system** menu.<br/>                                                |
| ALT+PRINT SCREEN<br/>                              | CTRL+ALT+MINUS SIGN (-)<br/> | Places a snapshot of the active window, within the client, on the clipboard.<br/> |
| PRINT SCREEN<br/>                                  | CTRL+ALT+PLUS SIGN (+)<br/>  | Places a snapshot of the entire client windows area on the clipboard .<br/>       |



 

## Related topics

<dl> <dt>

[Remote Desktop Services](terminal-services-portal.md)
</dt> </dl>

 

 





