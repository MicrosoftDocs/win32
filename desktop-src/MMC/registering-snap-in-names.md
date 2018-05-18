---
title: Registering Snap-in Names
description: Prior to MMC 2.0, a snap-in was directed to register its name string as a hard-coded string in the registry (under the NameString value).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '272d99ff-287a-48ad-9d92-25342f6126f1'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Registering Snap-in Names

Prior to MMC 2.0, a snap-in was directed to register its name string as a hard-coded string in the registry (under the **NameString** value). MMC 2.0 offers greater support for Multilanguage User Interface (MUI), and in addition to registering the **NameString** value, an MUI-compliant MMC 2.0 snap-in must register a value named **NameStringIndirect**. The value data for **NameStringIndirect** provides the resource DLL name and string identifier as the indirect means to retrieve the snap-in's name. For more information about the **NameStringIndirect** string format, see [SnapIns Key](snapins-key.md).

> [!Note]  
> Whether or not a snap-in provides the **NameStringIndirect** value, a snap-in must always provide the **NameString** value.

 

## Related topics

<dl> <dt>

[Providing MUI-Compliant Help Files](providing-mui-compliant-help-files.md)
</dt> <dt>

[SnapIns Key](snapins-key.md)
</dt> </dl>

 

 




