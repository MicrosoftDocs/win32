---
Description: An API Set is a strong name for a list of Win32 APIs.
ms.assetid: 0767BEA4-14C5-481A-8784-D3070C2E61DE
title: Windows API Sets
ms.topic: article
ms.date: 05/31/2018
---

# Windows API Sets

An API Set is a strong name for a list of Win32 APIs. The convention for assigning a strong name to an API Set is to use what appears to be a dll name. But the purpose of an API Set is to provide architectural separation between the API Set's name and its associated host DLL implementation for improved portability of your app, so you should think of an API Set's name as just a unique character string, and not as a dll name. For delay load, you use the name of the API Set.

API Sets rely on operating system support in the library loader to effectively introduce a namespace redirection component into the library binding process. Subject to various inputs, including the API Set name and the binding (import) context, the library loader performs a runtime redirection of the reference to a target host binary that houses the appropriate implementation of the API Set.

The decoupling between implementation and interface contracts provided by API Sets offers many engineering advantages, but can also potentially reduce the number of DLLs loaded in a process.

## In this section



| Topic                                                      | Description                                                              |
|------------------------------------------------------------|--------------------------------------------------------------------------|
| [Windows 8.1 API Sets](windows-81-api-sets.md)<br/> | API Sets available in Windows 8.1 and Windows Server 2012 R2.<br/> |
| [Windows 8 API Sets](windows-8-api-sets.md)<br/>    | API Sets available in Windows 8 and Windows Server 2012.<br/>      |



 

 

 




