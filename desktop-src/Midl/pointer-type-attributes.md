---
title: Pointer Type Attributes
description: The following attributes specify the characteristics of pointers.
ms.assetid: 310d0dfe-eef3-447e-89fb-40f620976d00
keywords:
- IDL MIDL , attributes, pointer-type
ms.topic: article
ms.date: 05/31/2018
---

# Pointer Type Attributes

The following attributes specify the characteristics of pointers.



| Attribute                                   | Usage                                                                                                                                                                                                |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ptr**](ptr.md)                          | Designates a pointer as a full pointer, with all the capabilities of a C-language pointer, including aliasing.                                                                                       |
| [**ref**](ref.md)                          | Designates the simplest type of pointer in MIDL—one that simply provides the address of some data. Reference pointers can never be null.                                                             |
| [**unique**](unique.md)                    | Lets a pointer be null, but does not support aliasing.                                                                                                                                               |
| [**pointer\_default**](pointer-default.md) | Applied to an interface to specify the default pointer type for all pointers in that interface, except for top-level parameter pointers, which automatically default to [**ref**](ref.md) pointers. |
| [**iid\_is**](iid-is.md)                   | Provides the interface identifier of the COM interface that is the object of the pointer.                                                                                                            |
| [**string**](string.md)                    | Specifies that the pointer points to a string.                                                                                                                                                       |



 

 

 




