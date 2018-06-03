---
title: DAMgmtChangedHost class
description: Changed host.
audience: developer
ms.assetid: af2fb1eb-96b9-4bbf-ba54-bf93a85ecdeb
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DAMgmtChangedHost class
- DAMgmtChangedHost class, described
topic_type:
- apiref
api_name:
- DAMgmtChangedHost
- DAMgmtChangedHost.Host
- DAMgmtChangedHost.IPAddresses
- DAMgmtChangedHost.Type
- DAMgmtChangedHost.Change
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DAMgmtChangedHost class

Changed host

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAMgmtChangedHost : DAMgmtHostEx
{
  string Host;
  string IPAddresses[];
  string Type[];
  string Change;
};
```

## Members

The **DAMgmtChangedHost** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAMgmtChangedHost** class has these properties.

<dl> <dt>

**Change**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Change.

The possible values are.

<dt>

<span id="Unchanged"></span><span id="unchanged"></span><span id="UNCHANGED"></span>

**Unchanged** ("Unchanged")


</dt> <dd></dd> <dt>

<span id="Added"></span><span id="added"></span><span id="ADDED"></span>

**Added** ("Added")


</dt> <dd></dd> <dt>

<span id="Removed"></span><span id="removed"></span><span id="REMOVED"></span>

**Removed** ("Removed")


</dt> <dd></dd> <dt>

<span id="AddressChanged"></span><span id="addresschanged"></span><span id="ADDRESSCHANGED"></span>

**AddressChanged** ("AddressChanged")


</dt> <dd></dd> </dl>

</dd> <dt>

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

This property is inherited from [**DAMgmtHostEx**](damgmthostex.md).

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



 

 





