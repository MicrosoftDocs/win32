---
Description: Represents an unassigned IP address in IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 13e4a2f4-1f6a-4bcf-bac9-b427d9ee9327
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_IPAM\_FreeAddress class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_IPAM\_FreeAddress class

Represents an unassigned IP address in IPAM.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_FreeAddress
{
  string Address;
  uint16 PingStatus;
  uint16 DnsRecordStatus;
};
```

## Members

The **MSFT\_IPAM\_FreeAddress** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_IPAM\_FreeAddress** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The unassigned IP address.

</dd> <dt>

**DnsRecordStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether a DNS record exists for this IP address.

The possible values are:

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Undetected"></span><span id="undetected"></span><span id="UNDETECTED"></span>

**Undetected** (1)


</dt> <dd></dd> <dt>

<span id="Reachable"></span><span id="reachable"></span><span id="REACHABLE"></span>

**Reachable** (2)


</dt> <dd></dd> <dt>

<span id="Unreachable"></span><span id="unreachable"></span><span id="UNREACHABLE"></span>

**Unreachable** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**PingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The results of the ping operation that was sent from the IPAM server to this IP address.

The possible values are:

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Undetected"></span><span id="undetected"></span><span id="UNDETECTED"></span>

**Undetected** (1)


</dt> <dd></dd> <dt>

<span id="Reachable"></span><span id="reachable"></span><span id="REACHABLE"></span>

**Reachable** (2)


</dt> <dd></dd> <dt>

<span id="Unreachable"></span><span id="unreachable"></span><span id="UNREACHABLE"></span>

**Unreachable** (3)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[IPAM Server WMI Provider Reference](ipam-server-wmi-provider-reference.md)
</dt> </dl>

 

 




