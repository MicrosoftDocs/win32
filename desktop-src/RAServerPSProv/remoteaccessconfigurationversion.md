---
title: RemoteAccessConfigurationVersion class
description: Defines the object containing the server GPO versioning information.
audience: developer
ms.assetid: 89d9c8cb-432b-47ac-a70c-f0e50681b668
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessConfigurationVersion class
- RemoteAccessConfigurationVersion class, described
topic_type:
- apiref
api_name:
- RemoteAccessConfigurationVersion
- RemoteAccessConfigurationVersion.ReceivedConfigGlobalVersion
- RemoteAccessConfigurationVersion.ReceivedConfigSiteVersion
- RemoteAccessConfigurationVersion.ReceivedConfigTimestamp
- RemoteAccessConfigurationVersion.AppliedConfigGlobalVersion
- RemoteAccessConfigurationVersion.AppliedConfigSiteVersion
- RemoteAccessConfigurationVersion.AppliedConfigTimestamp
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteAccessConfigurationVersion class

Defines the object containing the server GPO versioning information.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class RemoteAccessConfigurationVersion
{
  string   ReceivedConfigGlobalVersion;
  string   ReceivedConfigSiteVersion;
  datetime ReceivedConfigTimestamp;
  string   AppliedConfigGlobalVersion;
  string   AppliedConfigSiteVersion;
  datetime AppliedConfigTimestamp;
};
```

## Members

The **RemoteAccessConfigurationVersion** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessConfigurationVersion** class has these properties.

<dl> <dt>

**AppliedConfigGlobalVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Applied configuration global version

</dd> <dt>

**AppliedConfigSiteVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Applied configuration site version

</dd> <dt>

**AppliedConfigTimestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Applied configuration timestamp

</dd> <dt>

**ReceivedConfigGlobalVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Received configuration global version

</dd> <dt>

**ReceivedConfigSiteVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Received configuration Site version

</dd> <dt>

**ReceivedConfigTimestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Received configuration timestamp

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





