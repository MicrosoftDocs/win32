---
Description: Contains the network ID of the free IPAM subnet.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2bcd80e2-512a-43e5-9036-ff2b453aa10c
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_IPAM\_FreeSubnet class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_IPAM\_FreeSubnet class

Contains the network ID of the free IPAM subnet.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_FreeSubnet
{
  string NetworkId;
};
```

## Members

The **MSFT\_IPAM\_FreeSubnet** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_IPAM\_FreeSubnet** class has these properties.

<dl> <dt>

**NetworkId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the network ID of the free IPAM subnet.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



 

 




