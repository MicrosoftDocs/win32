---
title: Best Practices for MI Provider and Client Development
description: This topic explains some of the best practices for developing Windows Management Infrastructure (MI) providers and clients.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5260B4BB-FF3B-47AF-9936-65ED3045AF4D
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Best Practices for MI Provider and Client Development

This topic explains some of the best practices for developing Windows Management Infrastructure (MI) providers and clients.

## CIM Classes and Namespaces

-   **Interop namespace**—It is strongly recommended that you not update or delete CIM classes in the **root/interop** namespace unless Microsoft updates them.

## Providers

-   **Implementing a Custom OperationOption**— It is recommended that you not use **UINT16** or **UINT32** as a data type for a custom Operation Option. While these data types are supported, they are converted to **SINT32** on the provider. Therefore, you should use the **SINT32** data type instead.
-   **Localizing MOF Files**— When localizing providers for PowerShell, it is recommended that you do not localize elements that users will use on which to base PowerShell script decisions. However, the **Convert-MofToProvider** tool always sets the **value/valuemap** to Translatable, which implies that all elements are localized. To avoid this, you can do one of two things:

    -   Choose not to localize the MOF. If you do not specify the localization flag, **Convert-MofToProvider** will not generate the references.
    -   Alternately, you can localize the MOF, and then remove the Translatable qualifier from the generated schema. Note that you must also remove the reference ID.

 

 




