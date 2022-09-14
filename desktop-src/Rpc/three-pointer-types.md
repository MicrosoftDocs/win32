---
title: Three Pointer Types
description: MIDL supports three types of pointers to accommodate a wide range of applications.
ms.assetid: 6684c252-6fbe-49ca-9967-6d4baf5dc298
ms.topic: article
ms.date: 05/31/2018
---

# Three Pointer Types

MIDL supports three types of pointers to accommodate a wide range of applications. The three different levels are called reference, unique, and full pointers, and are indicated by the attributes **\[**[**ref**](/windows/desktop/Midl/ref)**\]**, **\[**[**unique**](/windows/desktop/Midl/unique)**\]**, and **\[**[**ptr**](/windows/desktop/Midl/ptr)**\]**, respectively. The pointer classes described by these attributes are mutually exclusive. Pointer attributes can be applied to pointers in type definitions, function return types, function parameters, members of structures or unions, or array elements.

Embedded pointers are pointers that are members of structures or unions. They can also be elements of arrays. In the **\[**[**in**](/windows/desktop/Midl/in)**\]** direction, embedded **\[ref\]** pointers are assumed to be pointing to valid storage and must not be null. This situation is recursively applicable to any **\[ref\]** pointers they are pointing to. In the **\[in\]** direction, embedded **\[unique\]** and full pointers (pointers with the **\[ptr\]** attribute) may or may not be null.

Any pointer attribute placed on a parameter in the syntax of a function declaration affects only the rightmost pointer declarator for that parameter. To affect other pointer declarators, intermediate named types must be used.

Functions that return a pointer can have a pointer attribute as a function attribute. The **\[unique\]** and **\[ptr\]** attributes must be applied to function return types. Member declarations that are pointers can specify a pointer attribute as a field attribute. A pointer attribute can also be applied as a type attribute in [**typedef**](/windows/desktop/Midl/typedef) constructs.

When no pointer attribute is specified as a field or type attribute, pointer attributes are applied according to the rules for an unattributed pointer declaration as follows.

In DCE-compatibility mode, pointer attributes are determined in the defining IDL file. If there is a **\[**[**pointer\_default**](/windows/desktop/Midl/pointer-default)**\]**attribute specified in the defining interface, that attribute is used. If no **\[pointer\_default\]** attribute is present, all unattributed pointers are full pointers.

In Microsoft-extensions mode, pointer attributes can be determined by importing IDL files and are applied in the following order:

1.  An explicit pointer attribute applied at the use site.
2.  The **\[ref\]** attribute, when the unattributed pointer is a top-level pointer parameter.
3.  A **\[pointer\_default\]** attribute specified in the defining interface.
4.  A **\[pointer\_default\]** attribute specified in the base interface.
5.  The **\[unique\]** attribute.

The **\[**[**pointer\_default**](/windows/desktop/Midl/pointer-default)**\]** interface attribute specifies the default pointer attributes to be applied to a pointer declarator in a type, parameter, or return type declaration when that declaration does not have an explicit pointer attribute applied to it. The **\[pointer\_default\]** interface attribute does not apply to an unattributed top-level pointer of a parameter, which is assumed to be **\[ref\]**.

 

 