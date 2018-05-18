---
title: DhcpServerv4DnsSetting class
description: Dhcp Server v4 Dns Setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8cfaa197-60ac-410f-8d47-ba8852ba64c3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv4DnsSetting class", "DhcpServerv4DnsSetting class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv4DnsSetting
- DhcpServerv4DnsSetting.DynamicUpdates
- DhcpServerv4DnsSetting.DeleteDnsRROnLeaseExpiry
- DhcpServerv4DnsSetting.UpdateDnsRRForOlderClients
- DhcpServerv4DnsSetting.NameProtection
- DhcpServerv4DnsSetting.DisableDnsPtrRRUpdate
- DhcpServerv4DnsSetting.DnsSuffix
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv4DnsSetting class

Dhcp Server v4 Dns Setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4DnsSetting
{
  String  DynamicUpdates;
  boolean DeleteDnsRROnLeaseExpiry;
  boolean UpdateDnsRRForOlderClients;
  boolean NameProtection;
  boolean DisableDnsPtrRRUpdate;
  string  DnsSuffix;
};
```

## Members

The **DhcpServerv4DnsSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4DnsSetting** class has these properties.

<dl> <dt>

**DeleteDnsRROnLeaseExpiry**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if the server should delete DNS records on lease expiry.

</dd> <dt>

**DisableDnsPtrRRUpdate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if the PTR record registration has been disabled.

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**DnsSuffix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The domain under which the clients are to be registered.

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

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

Indicates if name protection (DHCIDRR Validation) is enabled for the scope.

</dd> <dt>

**UpdateDnsRRForOlderClients**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if the server should perform DNS registration for older clients which do not support dynamic DNS Update.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





