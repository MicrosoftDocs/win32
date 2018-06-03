---
Description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4b401fc1-f620-40de-8ea6-c0777d003391
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_IPAM\_AccessScope class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_IPAM\_AccessScope class

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_AccessScope
{
};
```

## Members

The **MSFT\_IPAM\_AccessScope** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_IPAM\_AccessScope** class has these methods.



| Method                                                                                                       | Description                                                                      |
|:-------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**SetAddressSpaceAccessScope**](msft-ipam-accessscope-setaddressspaceaccessscope.md)                       | Set access scope on an array of IP address spaces from IPAM.<br/>          |
| [**SetBlockAccessScope**](msft-ipam-accessscope-setblockaccessscope.md)                                     | Set access scope on an array of IP Blocks from IPAM.<br/>                  |
| [**SetDhcpScopeAccessScope**](msft-ipam-accessscope-setdhcpscopeaccessscope.md)                             | Set access scope on an array of DHCP scopes from IPAM.<br/>                |
| [**SetDhcpServerAccessScope**](msft-ipam-accessscope-setdhcpserveraccessscope.md)                           | Set access scope on an array of DHCP servers from IPAM.<br/>               |
| [**SetDhcpSuperscopeAccessScope**](msft-ipam-accessscope-setdhcpsuperscopeaccessscope.md)                   | Set access scope on an array of DHCP superscopes from IPAM.<br/>           |
| [**SetDnsConditionalForwarderAccessScope**](msft-ipam-accessscope-setdnsconditionalforwarderaccessscope.md) | Set access scope on an array of DNS conditional forwarders from IPAM.<br/> |
| [**SetDnsResourceRecordAccessScope**](msft-ipam-accessscope-setdnsresourcerecordaccessscope.md)             | Set access scope on an array of DNS resource records from IPAM.<br/>       |
| [**SetDnsServerAccessScope**](msft-ipam-accessscope-setdnsserveraccessscope.md)                             | Set access scope on an array of DNS servers from IPAM.<br/>                |
| [**SetDnsZoneAccessScope**](msft-ipam-accessscope-setdnszoneaccessscope.md)                                 | Set access scope on an array of DNS zones from IPAM.<br/>                  |
| [**SetRangeAccessScope**](msft-ipam-accessscope-setrangeaccessscope.md)                                     | Set access scope on an array of IP Ranges from IPAM.<br/>                  |
| [**SetSubnetAccessScope**](msft-ipam-accessscope-setsubnetaccessscope.md)                                   | Set access scope on an array of IP Subnets from IPAM.<br/>                 |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



 

 




