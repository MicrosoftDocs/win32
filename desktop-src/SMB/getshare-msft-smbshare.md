---
title: GetShare method of the MSFT\_SmbShare class
description: Returns a specified share instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '42f56507-2c7d-42e1-a389-ba8d07fe1530'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetShare method SMB", "GetShare method SMB , MSFT_SmbShare class", "MSFT_SmbShare class SMB , GetShare method"]
topic_type:
- apiref
api_name:
- MSFT_SmbShare.GetShare
api_location:
- SmbWmiV2.dll
api_type:
- COM
---

# GetShare method of the MSFT\_SmbShare class

Returns a specified share instance.

## Syntax


```mof
uint32 GetShare(
  [in]  string        ScopeName,
  [in]  string        ShareName,
  [in]  boolean       GetAclNonAdmin,
  [out] MSFT_SmbShare Output
);
```



## Parameters

<dl> <dt>

*ScopeName* \[in\]
</dt> <dd>

Name of the endpoint to which the share is scoped.

</dd> <dt>

*ShareName* \[in\]
</dt> <dd>

Name of the share.

</dd> <dt>

*GetAclNonAdmin* \[in\]
</dt> <dd>

If this parameter is **True** and the caller has read access to the share, the share's security descriptor will be set, and the caller will be able to see it.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

An instance of the [**MSFT\_SmbShare**](msft-smbshare.md) class that represents the share.

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

 

 





