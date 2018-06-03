---
Description: Describes of instantiating the Pen Input Panel.
ms.assetid: 185dbed4-8e2c-49a5-a1c8-23a9787ae2f0
title: Instantiating the PenInputPanel Class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Instantiating the PenInputPanel Class

\[[**PenInputPanel**](/windows/desktop/api/msinkaut/) has been replaced by [Microsoft.Ink.TextInput](https://www.bing.com/search?q=Microsoft.Ink.TextInput). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

You can instantiate multiple [**PenInputPanel**](/windows/desktop/api/msinkaut/) objects, attaching one to each control on a form, or you can instantiate one **PenInputPanel** object and move it between controls in focus event handlers. Because only one edit control can have focus at a time, the second method can save memory. A version of the Auto Claims sample called the [PenInputPanel Sample](peninputpanel-sample.md) has been implemented showing both techniques.

The following sections describe creating and displaying [**PenInputPanel**](/windows/desktop/api/msinkaut/) objects.

-   [Creating a PenInputPanel Object](creating-a-peninputpanel-object.md)
-   [Using the PenInputPanel with Combo Boxes](using-the-peninputpanel-with-combo-boxes.md)
-   [Displaying the Input Panel](displaying-the-input-panel.md)

 

 



