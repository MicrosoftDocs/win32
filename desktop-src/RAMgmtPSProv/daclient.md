---
title: DAClient class
description: DirectAccess Client class.
audience: developer
ms.assetid: bf9fc446-8176-43f7-9298-edba76c07c92
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DAClient class
- DAClient class, described
topic_type:
- apiref
api_name:
- DAClient
- DAClient.ClientSettings
- DAClient.SecurityGroupNameList
- DAClient.GpoName
- DAClient.ClientEntrypoint
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DAClient class

DirectAccess Client class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAClient
{
  DAClientSettings   ClientSettings;
  string             SecurityGroupNameList[];
  string             GpoName[];
  DAClientEntrypoint ClientEntrypoint;
};
```

## Members

The **DAClient** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAClient** class has these properties.

<dl> <dt>

**ClientEntrypoint**
</dt> <dd> <dl> <dt>

Data type: **DAClientEntrypoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DAClientEntrypoint**](dacliententrypoint.md)")
</dt> </dl>

A [**DAClientEntrypoint**](dacliententrypoint.md) embedded instance

</dd> <dt>

**ClientSettings**
</dt> <dd> <dl> <dt>

Data type: **DAClientSettings**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DAClientSettings**](daclientsettings.md)")
</dt> </dl>

A [**DAClientSettings**](daclientsettings.md) embedded instance

</dd> <dt>

**GpoName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

List of client GPOs

</dd> <dt>

**SecurityGroupNameList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

List of client Security Groups

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





