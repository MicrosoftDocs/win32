---
title: The Character Window
description: The Character Window
ms.assetid: 92b6111f-b52d-4720-8bd9-59585d826bf5
ms.topic: article
ms.date: 05/31/2018
---

# The Character Window

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Microsoft Agent displays animated characters in their own windows that always appear at the top of the window z-order (that is, always on top). A user can move a character's window by dragging the character with the left mouse button. The character image moves with the pointer. In addition, an application can move a character using the [**MoveTo**](moveto-method.md) method.

When the user right-clicks a character, a pop-up menu appears that displays the following commands:

Open \| Close <span class="underline">V</span>oice Commands Window

<span class="underline">H</span>ide

----------------------------…

Command\*


*OtherHostingApplicationCaption\*\**

\*Commands listed are based on the input-active client. For more information on defining commands that appear in the pop-up menu, see The Microsoft Agent Programming Interface Overview.

\*\*Entries listed are all other applications currently hosting the character. For more information on defining this entry, see The Microsoft Agent Programming Interface Overview.

The Open \| Close Voice Commands Window command controls the display of the Commands Window of the current active character. If speech recognition services are disabled, this command is disabled. If speech recognition services are not installed, this command does not appear.

The Hide command hides the character. The animation assigned to the character's **Hiding** state plays and hides the character. The letter "H" in hide is the command's access key (mnemonic).

The commands for the application(s) currently hosting the character follow the Hide command, preceded by a separator. Then the names of other applications using the character appear, also preceded by a separator.

 

 




