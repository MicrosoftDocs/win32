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

\[The [PenInputPanel](https://msdn.microsoft.com/library/Aa514041(v=MSDN.10).aspx) object has been replaced by [Microsoft.Ink.TextInput](https://msdn.microsoft.com/library/ms581554(v=VS.100).aspx). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

If you attach a [PenInputPanel](https://msdn.microsoft.com/library/Aa514041(v=MSDN.10).aspx) object to a [ComboBox](https://msdn.microsoft.com/library/t14e0ws8(v=VS.90).aspx) control, then tap your tablet pen on the edit control portion combo box at runtime, the PenInputPanel object does not appear. However, it does appear if you tap on the dropdown arrow. This is because the window of the edit control in the combo box is not the window that receives pen messages. Combo boxes have a child edit window. The solution to this problem is to determine whether the window the PenInputPanel object is attached to has a child window. If so, you can attach the PenInputPanel object to the child window.

Setting the [VerticalOffset](https://msdn.microsoft.com/library/ms571983(v=VS.90).aspx) property of the [PenInputPanel](https://msdn.microsoft.com/library/Aa514041(v=MSDN.10).aspx) object to a value of -1 makes the panel appear on top of the combo box.

 

 



