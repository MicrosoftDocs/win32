---
title: IBackgroundCopyFile GetProgress method
description: Retrieves information on the progress of the file transfer.
ms.assetid: '3D8AFD65-AF34-4000-A4A9-8A187427E85C'
keywords: ["GetProgress method", "GetProgress method, IBackgroundCopyFile interface", "IBackgroundCopyFile interface, GetProgress method"]
topic_type:
- apiref
api_name:
- IBackgroundCopyFile.GetProgress
api_location:
- dosvc.dll
api_type:
- COM
---

# IBackgroundCopyFile::GetProgress method

Retrieves information on the progress of the file transfer.

## Syntax


```C++
HRESULT GetProgress(
  [out] BG_FILE_PROGRESS *pProgress
);
```



## Parameters

<dl> <dt>

*pProgress* \[out\]
</dt> <dd>

Structure whose members indicate the progress of the file transfer. For details on the type of progress information available, see the [**BG\_FILE\_PROGRESS**](bg-file-progress.md) structure.

</dd> </dl>

## Return value

This method returns **S\_OK** on success or one of the standard COM **HRESULT** values on error.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID\_IBackgroundCopyFile is defined as 01B7BD23-FB88-4A77-8490-5891D3E4653A<br/>              |



## See also

<dl> <dt>

[**BG\_FILE\_PROGRESS**](bg-file-progress.md)
</dt> <dt>

[**IBackgroundCopyFile**](ibackgroundcopyfile.md)
</dt> <dt>

[**IBackgroundCopyJob::GetProgress**](ibackgroundcopyjob-getprogress.md)
</dt> </dl>

 

 





