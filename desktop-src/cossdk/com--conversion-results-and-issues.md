---
description: Whether you choose to convert your MTS packages to COM+ applications manually or let the Microsoft Windows setup process do it for you automatically, you should be aware of the results of conversion as well as the issues.
ms.assetid: 5b85aa5c-0409-4802-9335-04217ef5ddb9
title: COM+ Conversion Results and Issues
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Conversion Results and Issues

Whether you choose to convert your MTS packages to COM+ applications manually or let the Microsoft Windows setup process do it for you automatically, you should be aware of the results of conversion as well as the issues.

## What Is Converted

During conversion, the MTSTOCOM utility converts roles, role assignments, interfaces, methods, users, the computer list, and most computer settings. The MTSTOCOM utility also converts the identity and password for an MTS package.

The new COM+ attributes that were not available in MTS are automatically set to the following defaults for all converted MTS components. These defaults can be changed using either the Component Services administrative tool or the COM+ administrative interfaces.

-   JIT activation enabled.
-   Object pooling disabled.
-   Synchronization same as Transaction setting.

## Conversion Issues

COM+ is automatically installed when you install Windows. It is not possible to uninstall COM+. Issues related to upgrades of existing MTS and COM+ installations include the following:

-   If you are currently using MTS 1.0, MTS is automatically upgraded to COM+. However, user-defined packages will be lost and you must re-create them.
-   If you are currently using MTS 2.0, MTS is automatically upgraded to COM+. All user-defined packages will be upgraded to COM+ applications. All components should work as they did under MTS 2.0.
-   If you are using MTS 1.0 and MTS 2.0 and have installed the SDK option, the SDK files will be removed. You can install the latest COM+ SDK through the Microsoft Windows SDK.
-   You cannot manage a remote MTS computer from a COM+ computer.

## Related topics

<dl> <dt>

[Automatic Conversion from MTS](automatic-conversion-from-mts.md)
</dt> <dt>

[Manual Conversion from MTS](manual-conversion-from-mts.md)
</dt> <dt>

[MTS Administration Library](mts-administration-library.md)
</dt> </dl>

 

 



