---
description: Describes using the PenInputPanel object with combo boxes.
ms.assetid: 19902bfa-504e-40cd-882a-4fac4bb7daf6
title: Using the PenInputPanel with Combo Boxes
ms.topic: article
ms.date: 05/31/2018
---

# Using the PenInputPanel with Combo Boxes

\[The [PenInputPanel](/previous-versions/aa514041(v=msdn.10)) object has been replaced by [Microsoft.Ink.TextInput](/previous-versions/ms581554(v=vs.100)). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

If you attach a [PenInputPanel](/previous-versions/aa514041(v=msdn.10)) object to a [ComboBox](/dotnet/api/system.windows.forms.combobox?view=netcore-3.1) control, then tap your tablet pen on the edit control portion combo box at runtime, the PenInputPanel object does not appear. However, it does appear if you tap on the dropdown arrow. This is because the window of the edit control in the combo box is not the window that receives pen messages. Combo boxes have a child edit window. The solution to this problem is to determine whether the window the PenInputPanel object is attached to has a child window. If so, you can attach the PenInputPanel object to the child window.

Setting the [VerticalOffset](/previous-versions/ms571983(v=vs.100)) property of the [PenInputPanel](/previous-versions/aa514041(v=msdn.10)) object to a value of -1 makes the panel appear on top of the combo box.

 

 
