---
title: DhcpServerv6DnsSetting class
description: Dhcp Server v6 Dns Setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 80acf81d-f76c-49b5-b34f-3cbbe3913723
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv6DnsSetting class
- DhcpServerv6DnsSetting class, described
topic_type:
- apiref
api_name:
- DhcpServerv6DnsSetting
- DhcpServerv6DnsSetting.DynamicUpdates
- DhcpServerv6DnsSetting.DeleteDnsRROnLeaseExpiry
- DhcpServerv6DnsSetting.NameProtection
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv6DnsSetting class

Dhcp Server v6 Dns Setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6DnsSetting
{
  String  DynamicUpdates;
  boolean DeleteDnsRROnLeaseExpiry;
  boolean NameProtection;
};
```

## Members

The **DhcpServerv6DnsSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6DnsSetting** class has these properties.

<dl> <dt>

**DeleteDnsRROnLeaseExpiry**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if the server should delete DNS records on lease expiry.

</dd> <dt>

**DynamicUpdates**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Dynamic Update behavior of the Dhcp Server.

<dt>

<span id="Always"></span><span id="always"></span><span id="ALWAYS"></span>

**Always** ("Always")


</dt> <dd></dd> <dt>

<span id="Never"></span><span id="never"></span><span id="NEVER"></span>

**Never** ("Never")


</dt> <dd></dd> <dt>

<span id="OnClientRequest"></span><span id="onclientrequest"></span><span id="ONCLIENTREQUEST"></span>

**OnClientRequest** ("OnClientRequest")


</dt> <dd></dd> </dl>

</dd> <dt>

**NameProtection**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if Name protection (DHCIDRR validating) is enabled for the scope.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





