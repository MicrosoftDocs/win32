---
title: User-Defined Data Types
description: User-defined data types (UDT) are groups of related data items declared as one type of information.
ms.assetid: '66fde40c-1e22-4697-a658-fa1e749cebb3'
---

# User-Defined Data Types

User-defined data types (called *user-defined types* (UDT) in Microsoft Visual Basic, *structures* in languages like C and C++, and often referred to as *records* in general scenarios) are groups of related data items declared as one type of information. User-defined data types are very useful when you want to group several related pieces of information in a structured way.

There are limitations on using UDTs in Automation-based applications on computers running Microsoft Windows 95 without DCOM 1.2 or later or running Microsoft Windows NT 4.0 SP3 and earlier. Because user-defined types cannot be marshaled by these versions of Automation, UDTs could not be passed to generic Automation interface methods or functions. For example, if you had written interfaces that are available to Automation languages, such as Visual Basic, you could not use UDTs in those interfaces, because user-defined data types are unknown types to Automation and the remote procedure call subsystem (RPC). As a result, type-library driven marshaling was not possible for UDTs.

There are other ways to marshal UDTs. One way is to break down each field of the structure to an individual property. Unfortunately, this technique is relatively inefficient for the client and server because it requires each field in the structure to be passed one at a time. Another technique is to serialize the structure into a flat buffer that is placed into a safearray. This requires both the client and the server to deserialize the buffer back into the structure, a process that is tedious and prone to errors.

Beginning with Windows NT 4.0 SP4, Windows 95 with DCOM 1.2, and Windows 98, Automation now supports passing UDTs in variants and safearrays of user defined types as arguments to methods. This allows methods to return UDTs and allows programmers of Automation controllers (Automation clients) to call methods requiring pointers to structures.

For information on how to pass single UDTs and safearrays of UDTs, see [Passing UDTs](passing-udts.md).

For the methods, [**GetRecordInfoFromTypeInfo**](getrecordinfofromtypeinfo.md) and **GetRecordInfoFromGUID**, used to create a self-describing array of records, see [Support Functions for User-Defined Data Types](BADF90A3-82B6-4F2D-8F85-DA159E5A1988).

For the member functions and descriptions of the **IRecordInfo** interface, see [**IRecordInfo**](irecordinfo.md).

 

 




