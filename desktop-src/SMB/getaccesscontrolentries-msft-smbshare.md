---
title: GetAccessControlEntries method of the MSFT\_SmbShare class
description: Retrieves the access rights that have been granted to the share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f7027655-f768-4f91-aece-6cf6796364d1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetAccessControlEntries method SMB", "GetAccessControlEntries method SMB , MSFT_SmbShare class", "MSFT_SmbShare class SMB , GetAccessControlEntries method"]
topic_type:
- apiref
api_name:
- MSFT_SmbShare.GetAccessControlEntries
api_location:
- SmbWmiV2.dll
api_type:
- COM
---

# GetAccessControlEntries method of the MSFT\_SmbShare class

Retrieves the access rights that have been granted to the share.

## Syntax


```mof
uint32 GetAccessControlEntries(
  [out] MSFT_SmbShareAccessControlEntry Output[]
);
```



## Parameters

<dl> <dt>

*Output* \[out\]
</dt> <dd>

An array of instances of the [**MSFT\_SmbShareAccessControlEntry**](msft-smbshareaccesscontrolentry.md) class that represent the access control entries for the share.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SmbShare**](msft-smbshare.md)
</dt> </dl>

 

 





