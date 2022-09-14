---
description: If this bit is set, the dialog box periodically calls the installer.
ms.assetid: 7798cb50-72e4-4530-bf06-1927dd963a01
title: TrackDiskSpace Dialog Style Bit
ms.topic: article
ms.date: 05/31/2018
---

# TrackDiskSpace Dialog Style Bit

If this bit is set, the dialog box periodically calls the installer. If the property changes, it notifies the controls on the dialog. This style can be used if there is a control on the dialog indicating disk space. If the user switches to another application, adds or removes files, or otherwise modifies available disk space, you can quickly implement the change using this style.

Any dialog box relying on the [**OutOfDiskSpace**](outofdiskspace.md) property to determine whether to bring up a dialog must set the TrackDiskSpace Dialog Style Bit for the dialog to dynamically update space on the target volumes.

## Value



| Decimal | Hexadecimal | Constant                                |
|---------|-------------|-----------------------------------------|
| 32      | 0x00000020  | **msidbDialogAttributesTrackDiskSpace** |



 

 

 



