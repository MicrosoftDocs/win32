---
title: RemoteAccessRadiusConfig class
description: Manages a Remote Authentication Dial-In User Service (RADIUS) server configuration.
audience: developer
ms.assetid: '4a1d7ab8-267f-46ba-a934-908a2e0f7984'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoteAccessRadiusConfig class", "RemoteAccessRadiusConfig class, described"]
topic_type:
- apiref
api_name:
- RemoteAccessRadiusConfig
- RemoteAccessRadiusConfig.RadiusServerConfig
- RemoteAccessRadiusConfig.SharedSecret
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# RemoteAccessRadiusConfig class

Manages a Remote Authentication Dial-In User Service (RADIUS) server configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessRadiusConfig
{
  object RadiusServerConfig;
  string SharedSecret;
};
```

## Members

The **RemoteAccessRadiusConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessRadiusConfig** class has these properties.

<dl> <dt>

**RadiusServerConfig**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **EmbeddedObject**
</dt> </dl>

The RADIUS server configuration as an embedded object

</dd> <dt>

**SharedSecret**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The shared secret of the RADIUS server

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





