---
title: Signed and Unsigned Types (MIDL)
description: Learn about signed and unsigned types in MIDL. Compilers that use different defaults types can cause software errors in your distributed application.
ms.assetid: a4c2d811-6cf4-4c0b-af12-bf8247152984
keywords:
- data types MIDL , signed and unsigned
ms.topic: article
ms.date: 05/31/2018
---

# Signed and Unsigned Types (MIDL)

Compilers that use different defaults for signed and unsigned types can cause software errors in your distributed application. You can avoid these problems by explicitly declaring your character types as signed or unsigned. Note that DCE IDL compilers do not recognize the keyword [**signed**](signed.md). Therefore, this feature is not available when you use the MIDL compiler /**osf** switch.

MIDL defines the [**small**](small.md) type to take the same default sign as the [**char**](char-idl.md) type in the target C compiler. If the compiler assumes that **char** is unsigned, **small** will also be defined as unsigned. Many C compilers let you change the default as a command-line option. For example, in the Microsoft Visual C++ development environment, the **/J** command-line option changes the default sign of **char** from signed to unsigned.

You can also control the sign of variables of type [**char**](char-idl.md) and [**small**](small.md) with the MIDL compiler command-line switch [**/char**](-char.md). This switch allows you to specify the default sign used by your compiler. The MIDL compiler explicitly declares the sign of all **char** types that do not match your C-compiler default type in the generated header file.

 

 




