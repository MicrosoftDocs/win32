---
title: Remove method of the MSFT\_SmbMapping class
description: Removes an SMB mapping.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2C27613D-B863-4FCC-80D0-228F1E254823
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method SMB
- Remove method SMB , MSFT_SmbMapping interface
- MSFT_SmbMapping interface SMB , Remove method
topic_type:
- apiref
api_name:
- MSFT_SmbMapping.Remove
api_location:
- SmbWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the MSFT\_SmbMapping class

Removes an SMB mapping.

## Syntax


```mof
uint32 Remove(
  [in] boolean UpdateProfile,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*UpdateProfile* \[in\]
</dt> <dd>

**True** if the mapping will be persistently removed. **False** if the mapping will reappear when the computer is restarted.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** if the mapping will be removed even if it is in use, which may cause data loss.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SmbMapping**](msft-smbmapping.md)
</dt> </dl>

 

 





