---
description: Describes how to creates a PenInputPanel object.
ms.assetid: fd9ce912-5cec-4bec-b7d8-5a4f71000c95
title: Creating a PenInputPanel Object
ms.topic: article
ms.date: 05/31/2018
---

# Creating a PenInputPanel Object

\[[**PenInputPanel**](peninputpanel-class.md) has been replaced by [**TextInputPanel**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpanel) and [Microsoft.Ink.TextInput](/previous-versions/dotnet/netframework-3.5/ms581554(v=vs.90)). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

Managed code constructors provide a convenient way to create a [PenInputPanel](/previous-versions/ms583923(v=vs.100)) object and attach it to a control in one step. This C\# example creates a PenInputPanel object and attaches it to an existing [InkEdit](/previous-versions/ms835842(v=msdn.10)) control, `InkEdit1`, with one line of code.


```C++
PenInputPanel thePenInputPanel = new PenInputPanel(InkEdit1);
```



The same example in Visual Basic .NET looks like this:


```C++
Dim thePenInputPanel As New PenInputPanel(InkEdit1)
```



This technique is useful in cases where one [PenInputPanel](/previous-versions/ms583923(v=vs.100)) object will be associated with a single control throughout its lifetime. In cases where you want to use one PenInputPanel object and associate it with multiple controls, as demonstrated in the [PenInputPanel Sample](peninputpanel-sample.md), use the [AttachedEditControl](/previous-versions/ms582239(v=vs.100)) property to change the control to which the PenInputPanel object is associated.

To attach a [PenInputPanel](/previous-versions/ms583923(v=vs.100)) object to a control without using a constructor, use the [AttachedEditControl](/previous-versions/ms582239(v=vs.100)) property. Use this technique for languages that do not support the managed constructors, such as C++.

 

 
