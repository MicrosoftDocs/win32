---
title: MSFT\_FSRMAdr class
description: Provides interfaces to determine why access was denied to a file and to send a request for access according to policies defined on the file server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fec0343f-4ab6-4b8c-b365-e510286af2be'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["MSFT_FSRMAdr class File Server Resource Manager", "MSFT_FSRMAdr class File Server Resource Manager , described"]
topic_type:
- apiref
api_name:
- MSFT_FSRMAdr
api_location:
- SrmSvc.dll
api_type:
- DllExport
---

# MSFT\_FSRMAdr class

Provides interfaces to determine why access was denied to a file and to send a request for access according to policies defined on the file server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMAdr
{
};
```

## Members

The **MSFT\_FSRMAdr** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_FSRMAdr** class has these methods.



| Method                                                    | Description                                                                                      |
|:----------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**GetFailureInfo**](msft-fsrmadr-getfailureinfo.md)     | Gets more information from the server when a client fails to obtain access to a file.<br/> |
| [**SendRequestEmail**](msft-fsrmadr-sendrequestemail.md) | Sends an email to request additional access to a file.<br/>                                |



 

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> <dt>

[**IFsrmAccessDeniedRemediationClient**](ifsrmaccessdeniedremediationclient.md)
</dt> </dl>

 

 





