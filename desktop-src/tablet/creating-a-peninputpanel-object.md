---
Description: Describes how to creates a PenInputPanel object.
ms.assetid: fd9ce912-5cec-4bec-b7d8-5a4f71000c95
title: Creating a PenInputPanel Object
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a PenInputPanel Object

\[[**PenInputPanel**](/windows/win32/msinkaut/?branch=master) has been replaced by [**TextInputPanel**](/windows/win32/peninputpanel/nn-peninputpanel-itextinputpanel?branch=master) and [Microsoft.Ink.TextInput](frlrfMicrosoftInkTextInput). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

Managed code constructors provide a convenient way to create a [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic) object and attach it to a control in one step. This C\# example creates a PenInputPanel object and attaches it to an existing [InkEdit](frlrfMicrosoftInkInkEditClassTopic) control, `InkEdit1`, with one line of code.


```C++
PenInputPanel thePenInputPanel = new PenInputPanel(InkEdit1);
```



The same example in Visual Basic .NET looks like this:


```C++
Dim thePenInputPanel As New PenInputPanel(InkEdit1)
```



This technique is useful in cases where one [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic) object will be associated with a single control throughout its lifetime. In cases where you want to use one PenInputPanel object and associate it with multiple controls, as demonstrated in the [PenInputPanel Sample](peninputpanel-sample.md), use the [AttachedEditControl](frlrfMicrosoftInkPenInputPanelClassAttachedEditControlTopic) property to change the control to which the PenInputPanel object is associated.

To attach a [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic) object to a control without using a constructor, use the [AttachedEditControl](frlrfMicrosoftInkPenInputPanelClassAttachedEditControlTopic) property. Use this technique for languages that do not support the managed constructors, such as C++.

 

 



