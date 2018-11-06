---
title: Translating COM Object Syntax for Programming Languages
description: Translating COM Object Syntax for Programming Languages
ms.assetid: 021e0085-c720-401e-9637-76580e67b307
ms.topic: article
ms.date: 05/31/2018
---

# Translating COM Object Syntax for Programming Languages

To call a COM object from an application written in a programming language other than the one used to write the COM object, you must first translate the object's syntax to your programming language. This can be done using the following steps:

1.  View the COM object's type library in your programming language's syntax. Doing this provides you with descriptions of the object's classes, interfaces, methods, properties and events in the language syntax you use.

    Microsoft developer products provide several tools to assist you in viewing and converting type libraries. For more information, see [Type Library Viewers and Conversion Tools](type-library-viewers-and-conversion-tools.md) and [How Developer Tools Use Type Libraries](how-developer-tools-use-type-libraries.md).

    Once you can view the object's type library in your preferred programming language, you can compare its syntax to that in the documentation for the object. If the object is documented in a programming language other than the one you are using, the data types and syntax may differ, but descriptions of parameters, return values, and the object's functionality should be the same.

2.  Take into account any special considerations for translating to your programming language.

    Because each programming language defines concepts that may not have an equivalent in other languages, some of an object's functionality may work differently in another language, or not be available at all. For example, the Visual Basic programming language does not recognize C++ unsigned data types, such as **unsignedÂ long**. An application written in Visual Basic cannot use COM methods that accept or return unsigned data type variables.

3.  Add the COM object's compiled code to your project. The compiled code is typically contained in a .dll or .ocx file. This step is necessary for the compiler to recognize the COM object's classes. After you add the COM object, your application can use its classes and interfaces.

The following topics describe how to translate and use COM objects in a variety of programming languages:

-   [Translating to C++](translating-to-c--.md)
-   [Translating to Visual Basic](translating-to-visual-basic.md)
-   [Translating to Java](translating-to-java.md)

These topics describe conversion tools and processes provided by Microsoft developer products. For instructions on how to program COM objects using development tools created by other companies, see those development tools' documentation.

 

 




