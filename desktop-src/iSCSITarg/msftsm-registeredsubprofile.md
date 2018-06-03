---
title: MSFTSM\_RegisteredSubProfile class
description: Describes a subset of Common Information Model (CIM) classes, properties, and methods, which are required to manage a real-world entity or usage scenario.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9b3f2647-faa6-48f2-ac97-f455824d5dd3
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFTSM_RegisteredSubProfile class iSCSI Software Target API
- MSFTSM_RegisteredSubProfile class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSFTSM_RegisteredSubProfile
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFTSM\_RegisteredSubProfile class

Describes a subset of Common Information Model (CIM) classes, properties, and methods, which are required to manage a real-world entity or usage scenario. A registered subprofile must be associated with a [**MSFTSM\_RegisteredProfile**](msftsm-registeredprofile.md) instance by using a **MSFTSM\_RegisteredSubProfile** association.

Registered profiles and subprofiles can be named and defined by the Distributed Management Task Force (DMTF) or other standards organizations. The uses for a registered profile or subprofile must be specified in the document that defines the profile.

The [**MSFTSM\_RegisteredProfile**](msftsm-registeredprofile.md) and **MSFTSM\_RegisteredSubProfile** classes are unrelated to the **CIM\_Profile** class, which serves a completely different purpose. A registered profile is a named specification for CIM-based management of a particular system, subsystem, service or other entity, for a specified set of uses. A **MSFTSM\_RegisteredSubProfile** instance requires the context of a **MSFTSM\_RegisteredProfile** instance, which can stand alone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), Provider("MSiSCSITargetProv")]
class MSFTSM_RegisteredSubProfile : CIM_RegisteredSubProfile
{
};
```

## Members

The **MSFTSM\_RegisteredSubProfile** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFTSM\_RegisteredSubProfile** class has these methods.



| Method                                                                                   | Description                                                                                                                                                                                                                                                               |
|:-----------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CloseConformantInstances**](closeconformantinstances-msftsm-registeredsubprofile.md) | Closes an enumeration session that is opened by the [**OpenConformantInstances**](openconformantinstances-msftsm-registeredsubprofile.md) method.<br/> This method is inherited from [**CIM\_RegisteredSubProfile**](cim-registeredsubprofile.md).<br/>     |
| [**OpenConformantInstances**](openconformantinstances-msftsm-registeredsubprofile.md)   | Opens a session to enumerate class instances of this registered profile instance, and optionally to retrieve a set of the requested instances.<br/> This method is inherited from [**CIM\_RegisteredSubProfile**](cim-registeredsubprofile.md).<br/>         |
| [**PullConformantInstances**](pullconformantinstances-msftsm-registeredsubprofile.md)   | Continues an enumeration session that is opened by the [**OpenConformantInstances**](openconformantinstances-msftsm-registeredsubprofile.md) method.<br/> This method is inherited from -[**CIM\_RegisteredSubProfile**](cim-registeredsubprofile.md).<br/> |



 

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

[**CIM\_RegisteredSubProfile**](cim-registeredsubprofile.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





