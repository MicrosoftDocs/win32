---
title: Storage Object Naming Conventions
description: Storage and stream objects are named according to a set of conventions.
ms.assetid: 72e87c6a-cce5-4456-8336-c657e65c0a34
keywords:
- Structured Storage Strctd Stg ,fundamentals,storage object naming conventions
ms.topic: article
ms.date: 05/31/2018
---

# Storage Object Naming Conventions

Storage and stream objects are named according to a set of conventions.

The name of a root storage object is the actual name of the file in the underlying file system. It conforms to the conventions and restrictions that the file system imposes. File name strings passed to storage-related methods and functions are passed on, uninterpreted and unchanged, to the file system.

The name of a nested element contained within a storage object is managed by the implementation of the particular storage object. All implementations of storage objects must support nested element names 32 characters in length (including the **NULL** terminator), although some implementations might support longer names. Whether the storage object does any case conversion is implementation-defined. As a result, applications that define element names must choose names that are acceptable whether or not case conversion is performed. The COM implementation of compound files supports names with a maximum length of 32 characters, and does not perform any case conversion.

 

 




