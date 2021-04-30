---
title: IBackgroundCopyFile2 GetFileRanges method (Deliveryoptimization.h)
description: Retrieves the ranges that you want to download from the remote file.
ms.assetid: 19B7B4FC-371F-482B-B997-C240B5483F4D
keywords:
- GetFileRanges method
- GetFileRanges method, IBackgroundCopyFile2 interface
- IBackgroundCopyFile2 interface, GetFileRanges method
topic_type:
- apiref
api_name:
- IBackgroundCopyFile2.GetFileRanges
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyFile2::GetFileRanges method

Retrieves the ranges that you want to download from the remote file.

## Syntax


```C++
HRESULT GetFileRanges(
  [in, out] DWORD         *RangeCount,
  [out]     BG_FILE_RANGE **Ranges
);
```



## Parameters

<dl> <dt>

*RangeCount* \[in, out\]
</dt> <dd>

Number of elements in *Ranges*.

</dd> <dt>

*Ranges* \[out\]
</dt> <dd>

Array of [**BG_FILE_RANGE**](bg-file-range.md) structures that specify the ranges to download. When done, call the [**CoTaskMemFree**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) function to free *Ranges*.

</dd> </dl>

## Return value

This method returns the following return values, as well as others.



| Return code                                                                              | Description                                                                                                                                   |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Success<br/>                                                                                                                            |
| <dl> <dt>**S_FALSE**</dt> </dl>  | No ranges were specified or the job is an upload or upload-reply job. *RangeCount* is set to zero and *Ranges* is set to **NULL**.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyFile2 is defined as 83e81b93-0873-474d-8a8c-f2018b1a939c<br/>             |



## See also

<dl> <dt>

[**BG_FILE_RANGE**](bg-file-range.md)
</dt> <dt>

[**IBackgroundCopyFile2**](ibackgroundcopyfile2.md)
</dt> </dl>

 

