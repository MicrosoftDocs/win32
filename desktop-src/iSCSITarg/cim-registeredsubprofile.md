---
title: CIM\_RegisteredSubProfile class
description: A RegisteredSubProfile subclasses RegisteredProfile to indicate that a scoping profile is required to provide context. The latter is specified by the mandatory association, SubProfileRequiresProfile.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f60e8ee7-0168-4fb9-956b-cd0c17930408
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_RegisteredSubProfile class iSCSI Software Target API
- CIM_RegisteredSubProfile class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_RegisteredSubProfile
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_RegisteredSubProfile class

A RegisteredSubProfile subclasses RegisteredProfile to indicate that a scoping profile is required to provide context. The latter is specified by the mandatory association, SubProfileRequiresProfile.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("2.8.0"), UMLPackagePath("CIM::Interop")]
class CIM_RegisteredSubProfile : CIM_RegisteredProfile
{
};
```

## Members

The **CIM\_RegisteredSubProfile** class does not define any members.

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



 

 





