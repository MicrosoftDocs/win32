---
description: Application contexts can be used to create side-by-side Windows classes.
ms.assetid: 4941ae1b-f9c6-45ff-b39b-a4078a12a58c
title: Creating Side-By-Side Windows Classes
ms.topic: article
ms.date: 05/31/2018
---

# Creating Side-By-Side Windows Classes

Application contexts can be used to create side-by-side Windows classes. By using side-by-side Windows classes, your application can have different versions of a class active at the same time in a lone parent window. To create a side-by-side Windows class, your application must activate an activation context before calling [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) to obtain a handle to the new window.

For example, Windows Common Controls version 5.82 and version 6.0 both had an Edit control. Windows defaults to using the version 5.82 Edit control. To obtain a side-by-side window that has the version 6.0 Edit control, before calling [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) as usual, your application can reference an assembly that exposes named window classes and then activate the activation context that references the version 6.0 controls.

 

 
