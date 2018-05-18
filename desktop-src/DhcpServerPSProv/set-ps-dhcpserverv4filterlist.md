---
title: Set method of the PS\_DhcpServerv4FilterList class
description: Enables or disables the allow and/or deny MAC address filter lists on the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '96939c55-559a-46a1-8b96-a7333a5ce471'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DhcpServerv4FilterList class", "PS_DhcpServerv4FilterList class, Set method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4FilterList.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Set method of the PS\_DhcpServerv4FilterList class

Enables or disables the allow and/or deny MAC address filter lists on the DHCP Server.

## Syntax


```mof
uint32 Set(
  [in]  string                 ComputerName,
  [in]  boolean                Allow,
  [in]  boolean                Deny,
  [in]  boolean                PassThru,
  [out] DhcpServerv4FilterList cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Allow* \[in\]
</dt> <dd>

Enable/Disable the MAC address filter allow list. Valid values are True, False.

</dd> <dt>

*Deny* \[in\]
</dt> <dd>

Enable/Disable the MAC address filter deny list. Valid values are True, False.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4FilterList**](dhcpserverv4filterlist.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4FilterList**](ps-dhcpserverv4filterlist.md)
</dt> </dl>

 

 





