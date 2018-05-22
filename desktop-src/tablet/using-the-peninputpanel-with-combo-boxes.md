---
Description: 'Describes using the PenInputPanel object with combo boxes.'
ms.assetid: '19902bfa-504e-40cd-882a-4fac4bb7daf6'
title: Using the PenInputPanel with Combo Boxes
---

# Using the PenInputPanel with Combo Boxes

\[The [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic) object has been replaced by [Microsoft.Ink.TextInput](frlrfMicrosoftInkTextInput). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

If you attach a [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic) object to a [ComboBox](T:System.Windows.Forms.ComboBox) control, then tap your tablet pen on the edit control portion combo box at runtime, the PenInputPanel object does not appear. However, it does appear if you tap on the dropdown arrow. This is because the window of the edit control in the combo box is not the window that receives pen messages. Combo boxes have a child edit window. The solution to this problem is to determine whether the window the PenInputPanel object is attached to has a child window. If so, you can attach the PenInputPanel object to the child window.

Setting the [VerticalOffset](frlrfMicrosoftInkPenInputPanelClassVerticalOffsetTopic) property of the [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic) object to a value of -1 makes the panel appear on top of the combo box.

 

 



