---
title: Abstract Data Models
description: Every application and every operating system has an abstract data model.
ms.assetid: c670d92b-e64d-4d4c-a30c-cd4fb4f2d0b9
keywords:
- abstract data models 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Abstract Data Models

Every application and every operating system has an abstract data model. Many applications do not explicitly expose this data model, but the model guides the way in which the application's code is written. In the 32-bit programming model (known as the ILP32 model), integer, long, and pointer data types are 32 bits in length. Most developers have used this model without realizing it. For the history of the Win32 API, this has been a valid (although not necessarily safe) assumption to make.

In 64-bit Windows, this assumption of parity in data type sizes is invalid. Making all data types 64 bits in length would waste space, because most applications do not need the increased size. However, applications do need pointers to 64-bit data, and they need the ability to have 64-bit data types in selected cases. These considerations led to the selection of an abstract data model called LLP64 (or P64). In the LLP64 data model, only pointers expand to 64 bits; all other basic data types (integer and long) remain 32 bits in length.

Initially, most applications that run on 64-bit Windows will have been ported from 32-bit Windows. It is a goal that the same source, carefully written, should run on both 32- and 64-bit Windows. Defining the data model does not make this task easier. However, ensuring that the data model affects only pointer data types is the first step. The second step is to define a set of new data types that allow developers to automatically size their pointer-related data. This allows data associated with pointers to change size as the pointer size changes from 32 bits to 64 bits. Basic data types remain 32 bits in length, so there is no change in the size of data on the disk, data shared over a network, or data shared through memory-mapped files. This relieves developers of much of the effort involved in porting 32-bit code to 64-bit Windows.

These new data types have been added to the Windows API header files. Therefore, you can start using the new types now. For more information, see [The New Data Types](the-new-data-types.md).

 

 




