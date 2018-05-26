---
title: LPSAFEARRAY\_Size function
description: Calculates the wire size of the SAFEARRAY object, and gets its handle and data needed by the LPSAFEARRAY\_UserSize function.
ms.assetid: bc213e97-f885-4214-ac22-769891e92243
keywords:
- LPSAFEARRAY_Size function Automation
topic_type:
- apiref
api_name:
- LPSAFEARRAY_Size
api_location:
- OleAut32.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LPSAFEARRAY\_Size function

Calculates the wire size of the [**SAFEARRAY**](/windows/previous-versions/OaIdl/ns-oaidl-tagsafearray?branch=master) object, and gets its handle and data needed by the [**LPSAFEARRAY\_UserSize**](/windows/win32/wia_xp/nf-wia_xp-lpsafearray_usersize?branch=master) function.

## Syntax


```C++
unsigned long __stdcall LPSAFEARRAY_Size(
  _In_       unsigned long *pFlags,
  _In_       unsigned long Offset,
  _In_       LPSAFEARRAY   *ppSafeArray,
  _In_ const IID           *piid
);
```



## Parameters

<dl> <dt>

*pFlags* \[in\]
</dt> <dd>

The data used by RPC.

</dd> <dt>

*Offset* \[in\]
</dt> <dd>

Sets the buffer offset so that the safe array object is properly aligned when it is marshaled to the buffer.

</dd> <dt>

*ppSafeArray* \[in\]
</dt> <dd>

The safe array that contains the data to marshal.

</dd> <dt>

*piid* \[in\]
</dt> <dd>

Points to an IID for an [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) or [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. Used when the members of the safe array are **IDispatch** or **IUnknown**.

</dd> </dl>

## Return value

The value obtained from the returned **HRESULT** value is **S\_OK**.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>OleAut32.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>OleAut32.dll</dt> </dl> |



 

 





