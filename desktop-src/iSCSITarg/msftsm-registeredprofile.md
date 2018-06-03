---
title: MSFTSM\_RegisteredProfile class
description: Describes a set of Common Information Model (CIM) classes, properties, and methods, required to manage a real-world entity or usage scenario.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 20207a3f-3dcb-4df2-9a20-bef74f3c7997
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFTSM_RegisteredProfile class iSCSI Software Target API
- MSFTSM_RegisteredProfile class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSFTSM_RegisteredProfile
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFTSM\_RegisteredProfile class

Describes a set of Common Information Model (CIM) classes, properties, and methods, required to manage a real-world entity or usage scenario. Registered profiles can be named and defined by the Distributed Management Task Force (DMTF) or other standards organizations. The uses for a registered profile or sub-profile must be specified in the document that defines the profile.

The **MSFTSM\_RegisteredProfile** class is unrelated to the **CIM\_Profile** class, which serves a completely different purpose. A registered profile is a named specification for CIM-based management of a particular system, subsystem, service, or other entity, for a specified set of uses. It can be used as a standalone specification and it can proved the context for one or more [**MSFTSM\_RegisteredSubProfile**](msftsm-registeredsubprofile.md) instances, which can only be used in the scope of a registered profile.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), Provider("MSiSCSITargetProv")]
class MSFTSM_RegisteredProfile : CIM_RegisteredProfile
{
};
```

## Members

The **MSFTSM\_RegisteredProfile** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFTSM\_RegisteredProfile** class has these methods.



| Method                                                                                | Description                                                                                                                                                                                                                                                 |
|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CloseConformantInstances**](closeconformantinstances-msftsm-registeredprofile.md) | Closes an enumeration session opened by the [**OpenConformantInstances**](openconformantinstances-msftsm-registeredprofile.md) method.<br/> This method is inherited from [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375).<br/>        |
| [**OpenConformantInstances**](openconformantinstances-msftsm-registeredprofile.md)   | Opens a session to enumerate class instances of this registered profile instance, and optionally to retrieve a set of the requested instances.<br/> This method is inherited from [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375).<br/> |
| [**PullConformantInstances**](pullconformantinstances-msftsm-registeredprofile.md)   | Continues an enumeration session opened by the [**OpenConformantInstances**](openconformantinstances-msftsm-registeredprofile.md) method.<br/> This method is inherited from [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375).<br/>     |



 

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\Interop<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





