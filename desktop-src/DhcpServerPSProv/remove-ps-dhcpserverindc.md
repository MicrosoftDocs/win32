---
title: Remove method of the PS\_DhcpServerInDC class
description: Deletes the specified DHCP server from the list of authorized servers in AD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b950f351-66cd-44cb-a1ac-8fa51f9654e8
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerInDC class
- PS_DhcpServerInDC class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerInDC.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DhcpServerInDC class

Deletes the specified DHCP server from the list of authorized servers in AD.

## Syntax


```mof
uint32 Remove(
  [in]  string         DnsName,
  [in]  string         IPAddress,
  [in]  boolean        PassThru,
  [out] DhcpServerInDC cmdletOutput
);
```



## Parameters

<dl> <dt>

*DnsName* \[in\]
</dt> <dd>

DNS name of the DHCP server which is to be de-authorized

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

IP address of the DHCP server which is to be de-authorized

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerInDC**](dhcpserverindc.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerInDC**](ps-dhcpserverindc.md)
</dt> </dl>

 

 





