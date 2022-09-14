---
title: Translating to Visual Basic
description: Translating to Visual Basic
ms.assetid: 48672d0c-b0d7-4820-91d4-d985030396f6
ms.topic: article
ms.date: 05/31/2018
---

# Translating to Visual Basic

You can add a COM object to your Visual Basic project either as a reference or a component. Once the object is added to your project, your application can access its classes and interfaces. You can then use the Visual Basic Object Browser to view the object's type library information in Visual Basic syntax.

Typically, controls are added to a project as a components and noncontrols are added as references. When a COM object is added as a component, it appears in the Visual Basic toolbox. New instances of that object are created by dragging the object icon from the toolbox onto a Visual Basic form or other type of container. New instances of COM objects added as references are created using the **new** keyword.

The distinction between using a class as a reference versus a component is subtle but important. When you add an object as a reference, you can use only the type library that the control provides, or the "raw" type library.

If you add a control as a component, Visual Basic merges the extender properties and methods of the form in which the control is embedded with the control's type library, thus providing a wrapped, extended version of the type library. With this version of the type library, you can use extender properties such as Top and Left as if they were part of the control, instead of the control's container.

Visual Basic does not currently support multiple type libraries built into a single .dll file. If you run into a DLL that incorporates multiple type libraries, you should get stand-alone copies of the type libraries from the source that supplied the object in order to use the object with Visual Basic.

For more information, see the following topics:

-   [Translating to Visual Basic from C++](translating-to-visual-basic-from-c--.md)
-   [Translating to Visual Basic from Java](translating-to-visual-basic-from-java.md)
-   [Adding a Component to a Visual Basic Project](adding-a-component-to-a-visual-basic-project.md)
-   [Adding a Reference to a Visual Basic Project](adding-a-reference-to-a-visual-basic-project.md)
-   [Visual Basic Object Browser](visual-basic-object-browser.md)

## Related topics

<dl> <dt>

[Translating to C++](translating-to-c--.md)
</dt> <dt>

[Translating to Java](translating-to-java.md)
</dt> </dl>

 

 




