---
title: RemoteAccessRadiusServer class
description: Represents a Remote Authentication Dial-In User Service (RADIUS) server.
audience: developer
ms.assetid: 3add55a9-9cd6-4ed4-8f5d-3ad668a69e19
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessRadiusServer class
- RemoteAccessRadiusServer class, described
topic_type:
- apiref
api_name:
- RemoteAccessRadiusServer
- RemoteAccessRadiusServer.ServerPurpose
- RemoteAccessRadiusServer.Score
- RemoteAccessRadiusServer.Timeout
- RemoteAccessRadiusServer.Port
- RemoteAccessRadiusServer.SharedSecret
- RemoteAccessRadiusServer.AccountingOnOffMsg
- RemoteAccessRadiusServer.MsgAuthenticator
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessRadiusServer class

Represents a Remote Authentication Dial-In User Service (RADIUS) server

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessRadiusServer
{
  RemoteAccessRadiusServerPurpose ServerPurpose;
  uint32                          Score;
  uint32                          Timeout;
  uint32                          Port;
  string                          SharedSecret;
  string                          AccountingOnOffMsg;
  string                          MsgAuthenticator;
};
```

## Members

The **RemoteAccessRadiusServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessRadiusServer** class has these properties.

<dl> <dt>

**AccountingOnOffMsg**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether sending accounting ON-OFF messages is enabled

The possible values are.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl>

</dd> <dt>

**MsgAuthenticator**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether the use of message authenticator is enabled

The possible values are.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl>

</dd> <dt>

**Port**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Port number on which RADIUS is listening

</dd> <dt>

**Score**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Initial Score

</dd> <dt>

**ServerPurpose**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessRadiusServerPurpose**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessRadiusServerPurpose**](remoteaccessradiusserverpurpose.md)")
</dt> </dl>

A [**RemoteAccessRadiusServerPurpose**](remoteaccessradiusserverpurpose.md) embedded instance

</dd> <dt>

**SharedSecret**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The shared Secret

</dd> <dt>

**Timeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Time out in seconds

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





