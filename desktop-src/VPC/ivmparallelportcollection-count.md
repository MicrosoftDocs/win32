---
title: IVMParallelPortCollection Count property (VPCCOMInterfaces.h)
description: Number of parallel ports in this collection.
ms.assetid: f2f4cac4-bb63-4ac2-ba6e-321a8a29c6d4
keywords:
- Count property Virtual PC
- Count property Virtual PC , IVMParallelPortCollection interface
- IVMParallelPortCollection interface Virtual PC , Count property
topic_type:
- apiref
api_name:
- IVMParallelPortCollection.Count
- IVMParallelPortCollection.get_Count
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMParallelPortCollection::Count property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the number of parallel ports in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out, retval] long *count
);
```



## Property value

The number of parallel ports.

## Error codes



| Name/value                                                                                                                                            | Meaning                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>               | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl> | The parameter is **NULL**.<br/>    |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMParallelPortCollection is defined as 27c3e036-198f-430c-8735-6e652f7203fd<br/>  |



## See also

<dl> <dt>

[**IVMParallelPortCollection**](ivmparallelportcollection.md)
</dt> </dl>

 

