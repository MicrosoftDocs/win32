---
title: Set method of the MSFT\_FileStorageTier class
description: Pins a volume or file to a storage tier.
ms.assetid: 9F235321-2013-49F8-91AF-7A6369BB739A
keywords:
- Set method Windows Storage Management API
- Set method Windows Storage Management API , MSFT_FileStorageTier class
- MSFT_FileStorageTier class Windows Storage Management API , Set method
topic_type:
- apiref
api_name:
- MSFT_FileStorageTier.Set
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Set method of the MSFT\_FileStorageTier class

Pins a volume or file to a storage tier.

## Syntax


```mof
UInt32 Set(
  [in] String FilePath,
  [in] String DesiredStorageTierFriendlyName,
  [in] String DesiredStorageTierUniqueId,
  [in] String DesiredStorageTier
);
```



## Parameters

<dl> <dt>

*FilePath* \[in\]
</dt> <dd>

The path of a file.

</dd> <dt>

*DesiredStorageTierFriendlyName* \[in\]
</dt> <dd>

The friendly name of the desired storage tier.

</dd> <dt>

*DesiredStorageTierUniqueId* \[in\]
</dt> <dd>

The unique ID of the desired storage tier.

</dd> <dt>

*DesiredStorageTier* \[in\]
</dt> <dd>

The desired storage tier, an [**MSFT\_StorageTier**](msft-storagetier.md) object.

</dd> </dl>

## Remarks

Only one of the input parameters is required to specify the file storage tier.

The actual movement of the file to this tier will happen only when the optimizer runs (or is invoked).

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_FileStorageTier**](msft-filestoragetier.md)
</dt> </dl>

 

 





