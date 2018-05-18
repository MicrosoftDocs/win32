---
title: Create method of the MSFT\_SmbMapping class
description: Creates an SMB mapping.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '865175CD-E054-409A-B810-FEDC5899B915'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Create method SMB", "Create method SMB , MSFT_SmbMapping interface", "MSFT_SmbMapping interface SMB , Create method"]
topic_type:
- apiref
api_name:
- MSFT_SmbMapping.Create
api_location:
- SmbWmiV2.dll
api_type:
- COM
---

# Create method of the MSFT\_SmbMapping class

Creates an SMB mapping.

## Syntax


```mof
uint32 Create(
  [in]  string          LocalPath,
  [in]  string          RemotePath,
  [in]  string          UserName,
  [in]  string          Password,
  [in]  boolean         Persistent,
  [in]  boolean         SaveCredentials,
  [in]  boolean         HomeFolder,
  [out] MSFT_SmbMapping CreatedMapping
);
```



## Parameters

<dl> <dt>

*LocalPath* \[in\]
</dt> <dd>

The local path for the shared resource. This parameter is optional.

</dd> <dt>

*RemotePath* \[in\]
</dt> <dd>

The remote path for the shared resource.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

The user name. This parameter is optional.

</dd> <dt>

*Password* \[in\]
</dt> <dd>

The password associated with the user name.

</dd> <dt>

*Persistent* \[in\]
</dt> <dd>

Controls whether the mapping will survive computer restarts.

</dd> <dt>

*SaveCredentials* \[in\]
</dt> <dd>

Determines whether or not credentials are saved and used when a mapping is created against the same server.

</dd> <dt>

*HomeFolder* \[in\]
</dt> <dd>

Controls whether the connection will be made to the user’s home folder.

</dd> <dt>

*CreatedMapping* \[out\]
</dt> <dd>

An instance of the [**MSFT\_SmbMapping**](msft-smbmapping.md) class that represents the mapping.

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

[**MSFT\_SmbMapping**](msft-smbmapping.md)
</dt> </dl>

 

 





