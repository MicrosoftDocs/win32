---
title: BG_FILE_PROGRESS structure (Deliveryoptimization.h)
description: The BG_FILE_PROGRESS structure provides file-related progress information, such as the number of bytes transferred.
ms.assetid: 49BDFEEE-D7BF-489A-8BC1-951549B06252
keywords:
- BG_FILE_PROGRESS structure
topic_type:
- apiref
api_name:
- BG_FILE_PROGRESS
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# BG_FILE_PROGRESS structure

The **BG_FILE_PROGRESS** structure provides file-related progress information, such as the number of bytes transferred.

## Syntax


```C++
typedef struct _BG_FILE_PROGRESS {
  UINT64 BytesTotal;
  UINT64 BytesTransferred;
  BOOL   Completed;
} BG_FILE_PROGRESS;
```



## Members

<dl> <dt>

**BytesTotal**
</dt> <dd>

Size of the file in bytes. If DO cannot determine the size of the file (for example, if the file or server does not exist), the value is DO_UNKNOWN_FILE_SIZE.

If you are downloading ranges from a file, **BytesTotal** reflects the total number of bytes you want to download from the file.

</dd> <dt>

**BytesTransferred**
</dt> <dd>

Number of bytes transferred.

</dd> <dt>

**Completed**
</dt> <dd>

For downloads, the value is **TRUE** if the file is available to the user; otherwise, the value is **FALSE**. Files are available to the user after calling the [**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md) method. If the **Complete** method generates a transient error, those files processed before the error occurred are available to the user; the others are not. Use the **Completed** member to determine if the file is available to the user when **Complete** fails.

</dd> </dl>

## Remarks

To determine if DO transferred the file, you can:

-   Compare **BytesTransferred** to **BytesTotal**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



## See also

<dl> <dt>

[**BG_JOB_PROGRESS**](bg-job-progress.md)
</dt> <dt>

[**IBackgroundCopyFile::GetProgress**](ibackgroundcopyfile-getprogress-method.md)
</dt> </dl>

 

 





