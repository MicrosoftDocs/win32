---
title: TfGuidAtom
description: The TfGuidAtom data type identifies a GUID within TSF. A TfGuidAtom is obtained by calling ITfCategoryMgr RegisterGUID.
ms.assetid: '813916f6-610f-4031-bb17-67d7f5ffed6f'
keywords: ["TfGuidAtom"]
---

# TfGuidAtom

The **TfGuidAtom** data type identifies a **GUID** within TSF. A **TfGuidAtom** is obtained by calling [**ITfCategoryMgr::RegisterGUID**](itfcategorymgr-registerguid.md).


```C++
typedef DWORD TfGuidAtom;
```



## Remarks

A **TfGuidAtom** value is only valid within the process that **ITfCategoryMgr::RegisterGUID** is called from.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITfCategoryMgr::GetGUID**](itfcategorymgr-getguid.md)
</dt> <dt>

[**ITfCategoryMgr::IsEqualTfGuidAtom**](itfcategorymgr-isequaltfguidatom.md)
</dt> <dt>

[**ITfCategoryMgr::RegisterGUID**](itfcategorymgr-registerguid.md)
</dt> </dl>

 

 





