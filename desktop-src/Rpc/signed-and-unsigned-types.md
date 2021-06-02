---
title: Signed and Unsigned Types (RPC)
description: Compilers that use different defaults for signed and unsigned types can cause software errors in your distributed application.
ms.assetid: 0464d465-84b7-49fc-968e-5efe037966c2
ms.topic: article
ms.date: 05/31/2018
---

# Signed and Unsigned Types (RPC)

Compilers that use different defaults for signed and unsigned types can cause software errors in your distributed application. You can avoid these problems by explicitly declaring your character types as **signed** or **unsigned**.

MIDL defines the [**small**](/windows/desktop/Midl/small) type to take the same default sign as the **char** type in the target C compiler. If the compiler assumes that **char** is unsigned, **small** will also be defined as unsigned. Many C compilers let you change the default as a command-line option. For example, the Microsoft C compiler **/J** command-line option changes the default sign of **char** from signed to unsigned.

You can also control the sign of variables of type **char** and **small** with the MIDL compiler command-line switch [**/char**](/windows/desktop/Midl/-char). This switch allows you to specify the default sign used by your compiler. The MIDL compiler explicitly declares the sign of all **char** types that do not match your C-compiler default type in the generated header file.

 

 
