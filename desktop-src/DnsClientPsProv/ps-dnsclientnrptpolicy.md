---
title: PS\_DnsClientNrptPolicy class
description: CIM class for Nrpt policy configured on machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9099e6c0-9dc0-4414-9969-8a644922ff89
ms.prod: windows-server-dev
ms.technology:
- dns-client
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsClientNrptPolicy class
- PS_DnsClientNrptPolicy class, described
topic_type:
- apiref
api_name:
- PS_DnsClientNrptPolicy
api_location:
- DnsClientPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsClientNrptPolicy class

CIM class for Nrpt policy configured on machine.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsClientPSProvider"), AMENDMENT]
class PS_DnsClientNrptPolicy
{
};
```

## Members

The **PS\_DnsClientNrptPolicy** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsClientNrptPolicy** class has these methods.



| Method                                    | Description                                                                  |
|:------------------------------------------|:-----------------------------------------------------------------------------|
| [**Get**](get-ps-dnsclientnrptpolicy.md) | Retrieves Name Resolution Policy Table configured on the machine.<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientPSProvider.dll</dt> </dl> |



 

 





