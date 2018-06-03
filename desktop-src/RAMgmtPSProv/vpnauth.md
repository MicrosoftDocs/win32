---
title: VpnAuth class
description: Virtual Private Network (VPN) authentication settings.
audience: developer
ms.assetid: 85fb4666-ab5e-44af-a9fe-8a8c719bc0b7
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnAuth class
- VpnAuth class, described
topic_type:
- apiref
api_name:
- VpnAuth
- VpnAuth.Type
- VpnAuth.RadiusServerList
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VpnAuth class

Virtual Private Network (VPN) authentication settings

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnAuth
{
  string Type;
  string RadiusServerList[];
};
```

## Members

The **VpnAuth** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnAuth** class has these properties.

<dl> <dt>

**RadiusServerList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of Radius Servers

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Authentication type used in the VPN

The possible values are.

<dt>

<span id="Windows"></span><span id="windows"></span><span id="WINDOWS"></span>

**Windows** ("Windows")


</dt> <dd></dd> <dt>

<span id="ExternalRadius"></span><span id="externalradius"></span><span id="EXTERNALRADIUS"></span>

**ExternalRadius** ("ExternalRadius")


</dt> <dd></dd> <dt>

<span id="LocalNps"></span><span id="localnps"></span><span id="LOCALNPS"></span>

**LocalNps** ("LocalNps")


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



 

 





