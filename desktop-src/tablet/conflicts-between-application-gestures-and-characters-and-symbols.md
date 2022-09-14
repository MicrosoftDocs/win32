---
description: Description of conflicts between application gestures and characters and symbols.
ms.assetid: c9b8c284-7c31-4fb0-8cc4-ff09c9c4f228
title: Conflicts Between Application Gestures and Characters and Symbols
ms.topic: article
ms.date: 05/31/2018
---

# Conflicts Between Application Gestures and Characters and Symbols

Some application gestures may conflict with characters, combinations of characters, symbols, combinations of characters and symbols or whole words written in a single stroke. Most of these conflicts are avoided by having a detailed understanding of the context in which the application gesture is performed.

For example, to distinguish a right gesture from a dash (-) or an underscore (\_), an application may filter for how close the gesture is to neighboring characters, the relative size as compared to characters, or other information contained in a packet. The timing of the application gesture may also be a determining factor in deciding between gestures and characters. There may be more of a pause before applying an application gesture than before inputting characters. Unless a user is performing a series of undo or backspace gestures, there may also be more of a pause after a gesture than a character.

The following topics detail these conflicts:

-   [Conflicts with Latin characters and symbols](conflicts-with-latin-characters-and-symbols.md)
-   [Conflicts with East-Asian Characters](conflicts-with-east-asian-characters.md)

 

 



