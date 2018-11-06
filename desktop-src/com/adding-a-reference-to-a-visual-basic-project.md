---
title: Adding a Reference to a Visual Basic Project
description: Adding a Reference to a Visual Basic Project
ms.assetid: 635b1fe9-e592-42d7-a0ee-34fea205f412
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Reference to a Visual Basic Project

The following procedure describes how to add a reference to a COM object to a Visual Basic project. Your application can then use the classes of that object.

When you add an object as a reference, you can only use the type library provided by the control, or the "raw" type library. In contrast, adding a control as a component also exposes the Visual Basic extender properties and methods as if they were part of the control.

**To make a Visual Basic reference to a component**

1.  On the **Project** menu, click **References**.
2.  Click to select the check box next to the component you want to add. If the component is not listed, locate the .dll or .ocx file using **Browse**.
3.  Click **OK**.

The component is now part of the project. Your application can create class instances using the **New** keyword.

## Related topics

<dl> <dt>

[Adding a Component to a Visual Basic Project](adding-a-component-to-a-visual-basic-project.md)
</dt> <dt>

[Translating to Visual Basic](translating-to-visual-basic.md)
</dt> </dl>

 

 




