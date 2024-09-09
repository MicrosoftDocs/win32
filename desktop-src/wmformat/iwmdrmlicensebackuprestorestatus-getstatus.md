---
title: IWMDRMLicenseBackupRestoreStatus GetStatus method (Wmdrmsdk.h)
description: The GetStatus method retrieves detailed status information about a license backup or restore operation.
ms.assetid: 1a695baf-0971-4dbf-90fa-1b10178a3348
keywords:
- GetStatus method windows Media Format
- GetStatus method windows Media Format , IWMDRMLicenseBackupRestoreStatus interface
- IWMDRMLicenseBackupRestoreStatus interface windows Media Format , GetStatus method
topic_type:
- apiref
api_name:
- IWMDRMLicenseBackupRestoreStatus.GetStatus
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicenseBackupRestoreStatus::GetStatus method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetStatus** method retrieves detailed status information about a license backup or restore operation.

## Syntax


```C++
HRESULT GetStatus(
  [out] WM_BACKUP_RESTORE_STATUS *pStatus
);
```



## Parameters

<dl> <dt>

*pStatus* \[out\]
</dt> <dd>

Pointer to a [**WM\_BACKUP\_RESTORE\_STATUS**](wm-backup-restore-status.md) structure that receives the status information.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicenseBackupRestoreStatus Interface**](iwmdrmlicensebackuprestorestatus.md)
</dt> </dl>

 

 





