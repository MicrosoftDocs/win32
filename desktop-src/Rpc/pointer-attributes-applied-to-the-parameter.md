---
title: Pointer Attributes Applied to the Parameter
description: Each pointer attribute (\ ref\ , \ unique\ , and \ ptr\ ) has characteristics that affect memory allocation. The following table summarizes these characteristics.
ms.assetid: 25a609cd-efe7-4cbb-b80e-b6a3ad8cda38
ms.topic: article
ms.date: 05/31/2018
---

# Pointer Attributes Applied to the Parameter

Each pointer attribute (\[ [ref](/windows/desktop/Midl/ref)\], \[ [unique](/windows/desktop/Midl/unique)\], and \[ [ptr](/windows/desktop/Midl/ptr)\]) has characteristics that affect memory allocation. The following table summarizes these characteristics.



| Pointer attribute       | Client                                                                                                                                                                                                            | Server                                                              |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Reference (\[**ref**\]) | Client application must allocate.                                                                                                                                                                                 | Special handling needed for **\[out\]**-only nontop-level pointers. |
| Unique (\[**unique**\]) | If a parameter, the client application must allocate; if embedded, can be null. Changing from null to non-null causes the client stub to allocate; changing from non-null to null can cause orphaning.<br/> |                                                                     |
| Full (\[**ptr**\])      | If a parameter, the client application must allocate; if embedded, can be null. Changing from null to non-null causes the client stub to allocate; changing from non-null to null can cause orphaning.<br/> |                                                                     |



 

The **\[ref\]** attribute indicates that the pointer points to valid memory. By definition, the client application must allocate all the memory that the reference pointers require.

The unique pointer can change from null to non-null. If the unique pointer changes from null to non-null, new memory is allocated on the client. If the unique pointer changes from non-null to null, orphaning can result. For more information, see [Memory Orphaning](memory-orphaning.md).

 

