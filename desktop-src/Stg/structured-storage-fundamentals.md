---
title: Structured Storage Fundamentals
description: Structured Storage provides the equivalent of a complete file system for storing objects.
ms.assetid: 7e2d6211-2ea0-4cad-9388-c789b12446ab
keywords:
- Structured Storage Strctd Stg , fundamentals
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Structured Storage Fundamentals

Structured Storage provides the equivalent of a complete file system for storing objects through the elements listed in the following table.



| Element                                                                  | Description                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Structured Storage Interfaces](structured-storage-interfaces.md)       | The [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage), [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream), [**ILockBytes**](/windows/desktop/api/Objidl/nn-objidl-ilockbytes), and [**IRootStorage**](/windows/desktop/api/Objidl/nn-objidl-irootstorage) interfaces, along with a set of related interfaces —[**IPersistStorage**](https://msdn.microsoft.com/windows/desktop/1c1a20fc-c101-4cbc-a7a6-30613aa387d7), [**IPersist**](https://msdn.microsoft.com/windows/desktop/932eb0e2-35a6-482e-9138-00cff30508a9), [**IPersistFile**](https://msdn.microsoft.com/windows/desktop/7d34507f-8a16-43b4-8225-010798abc546), and [**IPersistStream**](https://msdn.microsoft.com/windows/desktop/97ea64ee-d950-4872-add6-1f532a6eb33f). |
| [Structured Storage API Functions](structured-storage-api-functions.md) | Helper APIs that facilitate an implementation of structured storage, as well as a second set of APIs for compound files; that is the COM implementation of the structured storage interfaces. COM also provides a set of supporting structures and enumeration values used to organize parameters for interface methods and APIs.                              |
| [Structured Storage Access Modes](structured-storage-access-modes.md)   | A set of access modes for regulating access to compound files.                                                                                                                                                                                                                                                                                                 |



 

 

 




