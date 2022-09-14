---
title: IVMParallelPortCollection Item property (VPCCOMInterfaces.h)
description: Retrieves the parallel port object that corresponds to the specified index.
ms.assetid: f67a4224-ca96-4d68-9f0f-4977ffff859e
keywords:
- Item property Virtual PC
- Item property Virtual PC , IVMParallelPortCollection interface
- IVMParallelPortCollection interface Virtual PC , Item property
topic_type:
- apiref
api_name:
- IVMParallelPortCollection.Item
- IVMParallelPortCollection.get_Item
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMParallelPortCollection::Item property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the parallel port object that corresponds to the specified index.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]          long            index,
  [out, retval] IVMParallelPort **vmParallelPort
);
```



## Property value

The [**IVMParallelPort**](ivmparallelport.md) object.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful. <br/>                                                      |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The *vmParallelPort* parameter is **NULL**. <br/>                                        |
| <dl> <dt>DISP\_E\_BADINDEX</dt> <dt>0x8002000B</dt> </dl>  | The index of the requested item does not correspond to an item in this collection. <br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl> | The configuration is unknown.<br/>                                                       |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                                                   |



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

[**IVMParallelPort**](ivmparallelport.md)
</dt> <dt>

[**IVMParallelPortCollection**](ivmparallelportcollection.md)
</dt> </dl>

 

