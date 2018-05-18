---
title: CoCreateOutlookExpress function
description: Do not use. Returns an instance of Microsoft Outlook Express.
ms.assetid: '0206354d-8a49-40e3-a441-ac53daa62379'
keywords: ["CoCreateOutlookExpress function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- CoCreateOutlookExpress
api_location:
- Msoe.dll
api_type:
- DllExport
---

# CoCreateOutlookExpress function

Do not use. Returns an instance of Microsoft Outlook Express.

## Syntax


```C++
HRESULT CoCreateOutlookExpress(
  _In_  IUnknown *pUnkOuter,
  _Out_ IUnknown **ppUnknown
);
```



## Parameters

<dl> <dt>

*pUnkOuter* \[in\]
</dt> <dd>

Type: **[IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp)\***

Must be **NULL**.

</dd> <dt>

*ppUnknown* \[out\]
</dt> <dd>

Type: **[IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp)\*\***

The address of a pointer to [**IOutlookExpress**](oe-ioutlookexpress.md).

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                       |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msoe.dll</dt> </dl>  |



 

 





