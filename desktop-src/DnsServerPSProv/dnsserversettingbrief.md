---
title: DnsServerSettingBrief class
description: Represents general information about a DNS server.
audience: developer
ms.assetid: 1a9d833c-75cc-4b16-8096-3c40f159a400
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerSettingBrief class
- DnsServerSettingBrief class, described
topic_type:
- apiref
api_name:
- DnsServerSettingBrief
- DnsServerSettingBrief.ComputerName
- DnsServerSettingBrief.AllIPAddress
- DnsServerSettingBrief.ListeningIPAddress
- DnsServerSettingBrief.MajorVersion
- DnsServerSettingBrief.MinorVersion
- DnsServerSettingBrief.BuildNumber
- DnsServerSettingBrief.IsReadOnlyDC
- DnsServerSettingBrief.EnableDnsSec
- DnsServerSettingBrief.EnableIPv6
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerSettingBrief class

Represents general information about a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerSettingBrief
{
  string  ComputerName;
  string  AllIPAddress[];
  string  ListeningIPAddress[];
  uint32  MajorVersion;
  uint32  MinorVersion;
  uint32  BuildNumber;
  boolean IsReadOnlyDC;
  boolean EnableDnsSec;
  boolean EnableIPv6;
};
```

## Members

The **DnsServerSettingBrief** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerSettingBrief** class has these properties.

<dl> <dt>

**AllIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the IP addresses that are managed by the server.

</dd> <dt>

**BuildNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The build number of the server.

</dd> <dt>

**ComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the computer that runs the DNS server.

</dd> <dt>

**EnableDnsSec**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable DNSSEC validation by the server; otherwise, **false**.

</dd> <dt>

**EnableIPv6**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable IPV6 on the server; otherwise, **false**.

</dd> <dt>

**IsReadOnlyDC**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** to enable write operations on the directory server; otherwise, **false**.

</dd> <dt>

**ListeningIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the listening IP addresses for the server.

</dd> <dt>

**MajorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The major version of the server installation.

</dd> <dt>

**MinorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minor version of the server installation.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





