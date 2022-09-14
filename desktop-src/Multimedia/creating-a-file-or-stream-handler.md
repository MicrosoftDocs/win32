---
title: Creating a File or Stream Handler
description: Creating a File or Stream Handler
ms.assetid: 9ec1af9a-f428-4323-a4f8-3eb923ce78d7
ms.topic: article
ms.date: 05/31/2018
---

# Creating a File or Stream Handler

In an application written in the C programming language, a file or stream handler usually creates a function for each method. Your application accesses these functions through an array of function pointers the stream handler creates. An **IAVIStreamVtbl** structure contains the array of function pointers. A stream handler can assign any name it wants to functions it creates for the methods. The position of the function pointer in the structure implies the correspondence of the function to the method. For example, the first function pointer in the structure corresponds to the **QueryInterface** method. Your stream handler must provide all the functions of an interface.

 

 




