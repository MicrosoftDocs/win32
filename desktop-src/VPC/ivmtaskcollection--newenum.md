---
title: IVMTaskCollection _NewEnum property
description: Retrieves an enumerator for the collection.
ms.assetid: 15c36bdb-5d26-4f67-aa7e-73b9bde2aa22
keywords:
- _NewEnum property Virtual PC
- _NewEnum property Virtual PC , IVMTaskCollection interface
- IVMTaskCollection interface Virtual PC , _NewEnum property
topic_type:
- apiref
api_name:
- IVMTaskCollection._NewEnum
- IVMTaskCollection.get__NewEnum
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMTaskCollection::\_NewEnum property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](https://msdn.microsoft.com/library/windows/desktop/hh850319).\]

Retrieves an enumerator for the collection.

This property is read-only.

## Syntax


```C++
HRESULT get__NewEnum(
  [out, retval] IUnknown **enumerator
);
```



## Property value

The [IEnumVARIANT](http://go.microsoft.com/fwlink/p/?linkid=120799) enumerator.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>    |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error occurred.<br/> |



## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMTaskCollection is defined as 5c4387c8-0e8b-4b97-8058-84679adf4c40<br/>          |



## See also

<dl> <dt>

[**IVMTaskCollection**](ivmtaskcollection.md)
</dt> </dl>

 

 





