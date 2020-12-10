---
title: IDeliveryOptimizationJob2 AddFile method
description: The AddFile method adds a single file to an existing DO job.
keywords:
- AddFile method
- AddFile method, IDeliveryOptimizationJob2 interface
- IDeliveryOptimizationJob2 interface, AddFile method
topic_type:
- apiref
api_name:
- IDeliveryOptimizationJob2.AddFile
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 01/18/2018
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationJob2::AddFileWithRanges method

The AddFile method adds a single file to an existing DO job.

## Syntax

```C++
HRESULT AddFile(
  [in]                              LPCWSTR       fileId,
  [in, unique]                      LPCWSTR       remoteUrl,
  [in]                              DWORD         rangeCount,
  [in, size_is(rangeCount), unique] BG_FILE_RANGE ranges[],
  [in]                              REFIID        riid,
  [out]                             void          **object
);
```

## Parameters

<dl> <dt>

*fileId* \[in\]
</dt> <dd>

The file ID string, which uniquely identifies the file to be downloaded.

</dd> <dt>

*remoteUrl* \[in\]
</dt> <dd>

The file URL that DO will attempt to connect to download the file.

</dd> <dt>

*rangeCount* \[in\]
</dt> <dd>

The number of items contained in *ranges*. A zero value means that no ranges are used for the file.

</dd> <dt>

*ranges* \[in\]
</dt> <dd>

The optional range list. Each range in the list is a [**BG_FILE_RANGE**](bg-file-range.md) structure.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

The type of object contained in object. This must by of type IID_IDeliveryOptimizationFile.

</dd> <dt>

*object* \[out\]
</dt> <dd>

The IDeliveryOptimizationFile object, which represents the download file. 

</dd> </dl>

## Return value

This method returns S_OK on success or one of the standard HRESULT values on error.

## Requirements

| Requirement | Value |
|---------------------------|---------------------------------------------------------------------------------|
| Minimum supported client  | Windows 10, version 1803 \[desktop apps only\]                                  |
| Minimum supported server  | Windows Server, version 1709 \[desktop apps only\]                              |
| Header                    | Deliveryoptimization.h                                                          |
| IDL                       | DeliveryOptimization.idl                                                        |
| Library                   | Dosvc.lib                                                                       |
| DLL                       | Dosvc.dll                                                                       |
| IID                       | IID_IDeliveryOptimizationJob is defined as EE2584CF-A69C-4848-B633-2649962B3EF7 |

## See also

[**IDeliveryOptimizationJob2**](ideliveryoptimizationjob2.md)
