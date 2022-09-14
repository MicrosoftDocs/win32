---
title: Network Management Function Buffer Lengths
description: This topic discusses the requirements for function buffer lengths when used with the network management APIs.
ms.assetid: 08599966-68a1-420b-bbc7-6daac833d08f
ms.topic: article
ms.date: 05/31/2018
---

# Network Management Function Buffer Lengths

This topic discusses the requirements for function buffer lengths when used with the network management APIs.

Applications that specify buffer sizes when calling network management enumeration functions (and various data retrieval functions) must specify buffers large enough to hold the returned information structure (or structures) plus the strings to which their members point. If you do not specify a large enough buffer to receive all the available entries, the function returns ERROR\_MORE\_DATA. Enumeration calls do not return partial entries.

Some network management functions take an advisory maximum data-length parameter, *prefmaxlen*. This parameter allows an application to suggest the number of bytes the server should return from a function call.

If you specify the value MAX\_PREFERRED\_LENGTH in the *prefmaxlen* parameter, the network management functions allocate the amount of memory required for the data.

For more information, see [Network Management Function Buffers](network-management-function-buffers.md).

 

 




