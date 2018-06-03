---
title: PS\_DnsServerSigningKey class
description: DNS Server Signing Key Task Definition.
audience: developer
ms.assetid: 4c72a317-31aa-4833-9328-532c082141c6
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerSigningKey class
- PS_DnsServerSigningKey class, described
topic_type:
- apiref
api_name:
- PS_DnsServerSigningKey
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerSigningKey class

DNS Server Signing Key Task Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerSigningKey
{
};
```

## Members

The **PS\_DnsServerSigningKey** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerSigningKey** class has these methods.



| Method                                          | Description                                              |
|:------------------------------------------------|:---------------------------------------------------------|
| [**Add**](add-ps-dnsserversigningkey.md)       | Adds a KSK or ZSK to the input zone.<br/>          |
| [**Get**](get-ps-dnsserversigningkey.md)       | Retrieves Zone signing key<br/>                    |
| [**Remove**](remove-ps-dnsserversigningkey.md) | Deletes one or more input keys from the zone.<br/> |
| [**Set**](set-ps-dnsserversigningkey.md)       | Modified input key for the zone.<br/>              |



 

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

 

 





