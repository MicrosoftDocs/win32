---
Description: Represents a range of unassigned IP addresses in IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 28F6C05B-0C4A-4615-B31A-C8AE681710A9
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_IPAM\_FreeRange class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_IPAM\_FreeRange class

Represents a range of unassigned IP addresses in IPAM.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_FreeRange
{
  string StartIPAddress;
  string EndIPAddress;
  string NetworkId;
};
```

## Members

The **MSFT\_IPAM\_FreeRange** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_IPAM\_FreeRange** class has these properties.

<dl> <dt>

**EndIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last IP address in the range.

</dd> <dt>

**NetworkId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network ID of the range.

</dd> <dt>

**StartIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The first IP address in the range.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[IPAM Server WMI Provider Reference](ipam-server-wmi-provider-reference.md)
</dt> </dl>

 

 




