---
title: RemoteAccessRadiusAccounting class
description: Remote Access Radius Accounting configuration Record.
audience: developer
ms.assetid: 'd45e1e86-f78d-4c60-88dc-31ef88b84f8f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoteAccessRadiusAccounting class", "RemoteAccessRadiusAccounting class, described"]
topic_type:
- apiref
api_name:
- RemoteAccessRadiusAccounting
- RemoteAccessRadiusAccounting.RadiusAccountingStatus
- RemoteAccessRadiusAccounting.RemoteServerList
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# RemoteAccessRadiusAccounting class

Remote Access Radius Accounting configuration Record

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessRadiusAccounting
{
  string                   RadiusAccountingStatus;
  RemoteAccessRadiusServer RemoteServerList[];
};
```

## Members

The **RemoteAccessRadiusAccounting** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessRadiusAccounting** class has these properties.

<dl> <dt>

**RadiusAccountingStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RADIUS accounting status

The possible values are.

<dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> <dt>

<span id="ExternalRadius"></span><span id="externalradius"></span><span id="EXTERNALRADIUS"></span>

**ExternalRadius** ("ExternalRadius")


</dt> <dd></dd> <dt>

<span id="Windows_Accounting"></span><span id="windows_accounting"></span><span id="WINDOWS_ACCOUNTING"></span>

**Windows Accounting** ("Windows Accounting")


</dt> <dd></dd> <dt>

<span id="Local_Nps"></span><span id="local_nps"></span><span id="LOCAL_NPS"></span>

**Local Nps** ("Local Nps")


</dt> <dd></dd> </dl>

</dd> <dt>

**RemoteServerList**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessRadiusServer** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessRadiusServer**](remoteaccessradiusserver.md)")
</dt> </dl>

An array of [**RemoteAccessRadiusServer**](remoteaccessradiusserver.md) embedded instances

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





