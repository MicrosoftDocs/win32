---
title: DAMgmtHostEx class
description: Extended host information.
audience: developer
ms.assetid: 592e327d-560a-410e-aa95-0b5ec3ca9caf
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DAMgmtHostEx class
- DAMgmtHostEx class, described
topic_type:
- apiref
api_name:
- DAMgmtHostEx
- DAMgmtHostEx.Host
- DAMgmtHostEx.IPAddresses
- DAMgmtHostEx.Type
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DAMgmtHostEx class

Extended host information

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAMgmtHostEx : DAMgmtHost
{
  string Host;
  string IPAddresses[];
  string Type[];
};
```

## Members

The **DAMgmtHostEx** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAMgmtHostEx** class has these properties.

<dl> <dt>

**Host**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name or IP address

This property is inherited from [**DAMgmtHost**](damgmthost.md).

</dd> <dt>

**IPAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

IP Addresses

This property is inherited from [**DAMgmtHost**](damgmthost.md).

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Server Type

The possible values are.

<dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>

**Manual** ("Manual")


</dt> <dd></dd> <dt>

<span id="SCCM"></span><span id="sccm"></span>

**SCCM** ("SCCM")


</dt> <dd></dd> <dt>

<span id="DC"></span><span id="dc"></span>

**DC** ("DC")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





