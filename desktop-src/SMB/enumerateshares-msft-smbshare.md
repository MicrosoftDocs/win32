---
title: EnumerateShares method of the MSFT\_SmbShare class
description: Enumerates the specified shares.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3e6e28c8-892b-41dd-b10f-71546cc7faa8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["EnumerateShares method SMB", "EnumerateShares method SMB , MSFT_SmbShare class", "MSFT_SmbShare class SMB , EnumerateShares method"]
topic_type:
- apiref
api_name:
- MSFT_SmbShare.EnumerateShares
api_location:
- SmbWmiV2.dll
api_type:
- COM
---

# EnumerateShares method of the MSFT\_SmbShare class

Enumerates the specified shares.

## Syntax


```mof
uint32 EnumerateShares(
  [in]  string        ScopeName,
  [in]  boolean       PopulateVolumeProperty,
  [out] MSFT_SmbShare Output[]
);
```



## Parameters

<dl> <dt>

*ScopeName* \[in\]
</dt> <dd>

Name of the endpoint to which the shares are scoped.

</dd> <dt>

*PopulateVolumeProperty* \[in\]
</dt> <dd>

Set to **True** to populate the **Volume** property of the [**MSFT\_SmbShare**](msft-smbshare.md) objects.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

An array of instances of the [**MSFT\_SmbShare**](msft-smbshare.md) class that represents the shares.

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

 

 





