---
Description: Describes using the PenInputPanel object with combo boxes.
ms.assetid: 19902bfa-504e-40cd-882a-4fac4bb7daf6
title: Using the PenInputPanel with Combo Boxes
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the PenInputPanel with Combo Boxes

\[The [PenInputPanel](https://www.bing.com/search?q=PenInputPanel) object has been replaced by [Microsoft.Ink.TextInput](https://www.bing.com/search?q=Microsoft.Ink.TextInput). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

If you attach a [PenInputPanel](https://www.bing.com/search?q=PenInputPanel) object to a [ComboBox](https://www.bing.com/search?q=ComboBox) control, then tap your tablet pen on the edit control portion combo box at runtime, the PenInputPanel object does not appear. However, it does appear if you tap on the dropdown arrow. This is because the window of the edit control in the combo box is not the window that receives pen messages. Combo boxes have a child edit window. The solution to this problem is to determine whether the window the PenInputPanel object is attached to has a child window. If so, you can attach the PenInputPanel object to the child window.

Setting the [VerticalOffset](https://www.bing.com/search?q=VerticalOffset) property of the [PenInputPanel](https://www.bing.com/search?q=PenInputPanel) object to a value of -1 makes the panel appear on top of the combo box.

 

 



