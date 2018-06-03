---
title: DhcpServerInDC class
description: Authorized Dhcp Server In DC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 22ba819b-e183-4212-88c2-844e8c424f66
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerInDC class
- DhcpServerInDC class, described
topic_type:
- apiref
api_name:
- DhcpServerInDC
- DhcpServerInDC.DnsName
- DhcpServerInDC.IPAddress
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerInDC class

Authorized Dhcp Server In DC.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerInDC
{
  string DnsName;
  string IPAddress;
};
```

## Members

The **DhcpServerInDC** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerInDC** class has these properties.

<dl> <dt>

**DnsName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Dns name of the Dhcp server.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

IP Address of the Dhcp server.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





