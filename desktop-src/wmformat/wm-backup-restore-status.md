---
title: WM_BACKUP_RESTORE_STATUS structure (Wmdrmsdk.h)
description: The WM\_BACKUP\_RESTORE\_STATUS structure holds information about a pending license backup or restore operation.
ms.assetid: 74e94bc6-376b-4848-a9f9-11c9cb4005f2
keywords:
- WM_BACKUP_RESTORE_STATUS structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WM_BACKUP_RESTORE_STATUS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_BACKUP\_RESTORE\_STATUS structure

The **WM\_BACKUP\_RESTORE\_STATUS** structure holds information about a pending license backup or restore operation.

## Syntax


```C++
typedef struct WM_BACKUP_RESTORE_STATUS {
  MSDRM_STATUS eStatus;
  BSTR         bstrError;
} ;
```



## Members

<dl> <dt>

**eStatus**
</dt> <dd>

Member of the [**MSDRM\_STATUS**](msdrm-status.md) enumeration specifying the status.

</dd> <dt>

**bstrError**
</dt> <dd>

String containing the error.

</dd> </dl>

## Remarks

This structure is received when you call the [**IWMDRMLicenseBackupRestoreStatus::GetStatus**](iwmdrmlicensebackuprestorestatus-getstatus.md) method. It contains the status of the pending backup or restore operation at the time of the call.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





