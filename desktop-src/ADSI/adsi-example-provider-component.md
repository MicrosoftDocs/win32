---
title: ADSI Example Provider Component
description: Active Directory Service Interfaces provider writers will find this section of particular interest, because it describes the ADSI example provider component in depth.
ms.assetid: 1ca73817-7a21-4a39-b496-fc82db26ea4e
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# ADSI Example Provider Component

Active Directory Service Interfaces provider writers will find this section of particular interest, because it describes the ADSI example provider component in depth. ADSI provider writers can install the example provider and use the code framework as a basis to create their own implementation. The following topics are discussed:

[Installing the Example Provider Component](installing-the-example-provider-component.md) describes how to install the ADSI sample provider and its mock directory. This section includes a list of the registry settings.

[Directory Definition](directory-definition.md) describes the directory entries defined by the example provider component.

[Schema Management](schema-management.md) describes how each element in the example provider component directory service can be represented by a specific type of Active Directory object.

[Binding to an Active Directory Object](binding-to-an-active-directory-object.md) describes how, given an ADsPath string, the example provider component identifies that element, creates the appropriate type of Active Directory object for it, and retrieves the requested type of interface pointer on that object to pass back to the ADs client software.

[Enumerator Objects](enumerator-objects.md) lists the specific types of enumerations supplied by the example provider component and in which source code the implementations can be found.

[Code Overview](code-overview.md) provides a task-level description of each part of the example provider component.

[Code Details](code-details.md) lists the software modules and their contents.

 

 




