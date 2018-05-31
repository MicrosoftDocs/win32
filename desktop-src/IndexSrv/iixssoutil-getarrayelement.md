---
title: IixssoUtil GetArrayElement method
description: Accesses a variant array element.
ms.assetid: 84e8995e-df44-465c-b1ae-bc11246dacb1
keywords:
- GetArrayElement method Indexing Service
- GetArrayElement method Indexing Service , IixssoUtil interface
- IixssoUtil interface Indexing Service , GetArrayElement method
topic_type:
- apiref
api_name:
- IixssoUtil.GetArrayElement
api_location:
- Ixsso.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoUtil::GetArrayElement method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Accesses a variant array element.

## Syntax


```C++
HRESULT GetArrayElement(
  [in]          VARIANT *pVarIn,
  [in]          LONG    iElement,
  [out, retval] VARIANT *pVarOut
);
```



## Parameters

<dl> <dt>

*pVarIn* \[in\]
</dt> <dd>

An array containing a singly dimensioned safe array.

</dd> <dt>

*iElement* \[in\]
</dt> <dd>

Identifies the array element to be returned.

</dd> <dt>

*pVarOut* \[out, retval\]
</dt> <dd>

Receives the array element.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If *pVarIn* is not a safe array, or *iElement* is either less than the lower limit of the array or more than its upper limit, the type returned is VT\_EMPTY. This method exists due to restrictions in Visual Basic Scripting Edition (VBScript).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoUtil**](iixssoutil.md)
</dt> </dl>

 

 





