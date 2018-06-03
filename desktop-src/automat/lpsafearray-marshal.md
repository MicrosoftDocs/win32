---
title: LPSAFEARRAY\_Marshal function
description: Marshals a SAFEARRAY object to a user's RPC buffer on the server using information passed in by the LPSAFEARRAY\_UserMarshal function.
ms.assetid: f68c86f3-afef-46ea-a15b-99e81e4383bd
keywords:
- LPSAFEARRAY_Marshal function Automation
topic_type:
- apiref
api_name:
- LPSAFEARRAY_Marshal
api_location:
- OleAut32.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LPSAFEARRAY\_Marshal function

Marshals a [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object to a user's RPC buffer on the server using information passed in by the [**LPSAFEARRAY\_UserMarshal**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_usermarshal) function.

## Syntax


```C++
unsigned char* __stdcall LPSAFEARRAY_Marshal(
  _In_          unsigned long *pFlags,
  _Inout_       unsigned char *pBuffer,
  _In_          LPSAFEARRAY   *ppSafeArray,
  _In_    const IID           *piid
);
```



## Parameters

<dl> <dt>

*pFlags* \[in\]
</dt> <dd>

The data used by RPC.

</dd> <dt>

*pBuffer* \[in, out\]
</dt> <dd>

The current buffer. This pointer may or may not be aligned on entry. The function aligns the buffer pointer, marshals the data, and returns the new buffer position, which is the address of the first byte after the marshaled object.

</dd> <dt>

*ppSafeArray* \[in\]
</dt> <dd>

The safe array that contains the data to marshal.

</dd> <dt>

*piid* \[in\]
</dt> <dd>

Points to an IID for an [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) or [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. Used when the members of the safe array are **IDispatch** or **IUnknown**.

</dd> </dl>

## Return value

The value obtained from the returned **HRESULT** value is one of the following.



| Return code                                                                                   | Description                                                        |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>         | Success. <br/>                                               |
| <dl> <dt>**E\_INVALIDARG** </dt> </dl> | The *ppSafeArray* parameter is not a valid safe array. <br/> |
| <dl> <dt>**E\_UNEXPECTED** </dt> </dl> | The array could not be locked.<br/>                          |



 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>OleAut32.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>OleAut32.dll</dt> </dl> |



 

 





