---
title: IDeliveryOptimizationJob AddFileWithRanges method (Deliveryoptimization.h)
description: Adds a file to a download job and specifies the ranges of the file you want to download.
ms.assetid: 23F0A39F-670F-4030-A3B3-4F9277FFA8AB
keywords:
- AddFileWithRanges method
- AddFileWithRanges method, IDeliveryOptimizationJob interface
- IDeliveryOptimizationJob interface, AddFileWithRanges method
topic_type:
- apiref
api_name:
- IDeliveryOptimizationJob.AddFileWithRanges
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationJob::AddFileWithRanges method

Adds a file to a download job and specifies the ranges of the file you want to download.

## Syntax


```C++
HRESULT AddFileWithRanges(
  [in]           LPCWSTR       fileId,
  [in]           LPCWSTR       remoteUrl,
  [in]           LPCWSTR       localName,
  [in, optional] DWORD         rangeCount,
  [in, optional] BG_FILE_RANGE ranges[],
  [in, optional] ULONG64       fileSize
);
```



## Parameters

<dl> <dt>

*fileId* \[in\]
</dt> <dd>

Null terminated string that s an unique identifier of the published content. For non-published content, this can be any unique string that caller can use to identify files within a job.

</dd> <dt>

*remoteUrl* \[in\]
</dt> <dd>

Null-terminated string that contains the name of the file on the server.

</dd> <dt>

*localName* \[in\]
</dt> <dd>

Null-terminated string that contains the name of the file on the client.

</dd> <dt>

*rangeCount* \[in, optional\]
</dt> <dd>

Number of elements in *Ranges*.

</dd> <dt>

*ranges* \[in, optional\]
</dt> <dd>

Array of one or more [**BG_FILE_RANGE**](/windows/desktop/api/bits2_0/ns-bits2_0-bg_file_range) structures that specify the ranges to download. Do not specify duplicate or overlapping ranges.

</dd> <dt>

*fileSize* \[in, optional\]
</dt> <dd>

Size of the file in bytes. Pass in **DO_UNKNOWN_FILE_SIZE** if size is not known to the caller application.

</dd> </dl>

## Return value

This method returns the following return values, as well as others.




| Return code | Description | 
|-------------|-------------|
| <dl><dt><strong><strong>S_OK</strong></strong></dt></dl> | Success.<br /> | 
| <dl><dt><strong>E_INVALIDARG</strong></dt></dl> | The local file name is NULL or empty string. <br /> | 
| <dl><dt><strong>E_ACCESSDENIED</strong></dt></dl> | User does not have permission to write to the specified directory on the client.<br /> | 
| <dl><dt><strong>DO_E_INVALID_RANGE</strong></dt></dl> | One of the ranges is invalid. For example, InitialOffset is set to <strong>BG_LENGTH_TO_EOF</strong>.<br /> | 
| <dl><dt><strong>DO_E_OVERLAPPING_RANGES</strong></dt></dl> | You cannot specify duplicate or overlapping ranges. <br /><blockquote>[!Note]<br />The ranges are sorted by the offset of the value, not the length. If ranges are entered that have the same offset, but are in reverse order, then this error will be returned. For example, if 100.5 and 100.0 are entered in that order, then you will not be able to add the file to the job.</blockquote><br /> | 
| <dl><dt><strong>DO_E_INVALID_STATE</strong></dt></dl> | The state of the job cannot be <strong>BG_JOB_STATE_CANCELLED</strong> or <strong>BG_JOB_STATE_ACKNOWLEDGED</strong>.<br /> | 




 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IDeliveryOptimizationJob is defined as EE2584CF-A69C-4848-B633-2649962B3EF7<br/>         |



## See also

<dl> <dt>

[**IDeliveryOptimizationJob**](ideliveryoptimizationjob.md)
</dt> </dl>

 

