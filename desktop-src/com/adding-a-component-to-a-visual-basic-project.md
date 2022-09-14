---
title: Adding a Component to a Visual Basic Project
description: Adding a Component to a Visual Basic Project
ms.assetid: 7e78853a-b134-46d7-a230-3ee8d80d05c0
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Component to a Visual Basic Project

The following procedure describes how to add a COM object as a component to a Visual Basic project. Your application can then use the classes of that object.

Adding a control as a component exposes the Visual Basic extender properties and methods as if they were part of the control. In contrast, when you add an object as a reference you can only use the type library provided by the control, or the "raw" type library.

**To insert a control into a Visual Basic project**

1.  On the **Project** menu, click **Components**.
2.  Click to select the check box next to the component you want to add. If the component is not listed, locate the .dll or .ocx file using **Browse**.
3.  Click **OK**.

The component is now part of the project and appears in the object toolbar. Your application can create instances of the control by dragging the control from the toolbar and dropping it onto a form or dialog box.

## Related topics

<dl> <dt>

[Adding a Reference to a Visual Basic Project](adding-a-reference-to-a-visual-basic-project.md)
</dt> <dt>

[Translating to Visual Basic](translating-to-visual-basic.md)
</dt> </dl>

 

 




