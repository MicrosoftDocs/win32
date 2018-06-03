---
title: Remove method of the Ps\_DnsServerClientSubnet class
description: Deletes a client subnet record from the client subnet database on the DNS server.
audience: developer
ms.assetid: AA49AED3-6A7C-4FB8-BC7D-18E3EC2FB524
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, Ps_DnsServerClientSubnet class
- Ps_DnsServerClientSubnet class, Remove method
topic_type:
- apiref
api_name:
- Ps_DnsServerClientSubnet.Remove
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the Ps\_DnsServerClientSubnet class

Deletes a client subnet record from the client subnet database on the DNS server.

## Syntax


```mof
uint32 Remove(
  [in]  string                Name,
  [in]  boolean               PassThru,
  [in]  boolean               Force,
  [in]  string                ComputerName,
  [out] DnsServerClientSubnet cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the client subnet record.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the client subnet record in the *cmdletOutput* parameter; otherwise, **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Name of the client subnet record

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name of the remote computer on which to execute the command.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, this parameter receives an embedded instance of the [**DnsServerClientSubnet**](dnsserverclientsubnet.md) object that represents the deleted subnet record.

</dd> </dl>

## Return value

If this operation succeeds, this method returns "0"; otherwise, it returns a WMI error code.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**Ps\_DnsServerClientSubnet**](ps-dnsserverclientsubnet.md)
</dt> </dl>

 

 





