---
title: LPSAFEARRAY\_Unmarshal function
description: Unmarshals a SAFEARRAY object from the RPC buffer using information passed in by the LPSAFEARRAY\_UserUnmarshal function.
ms.assetid: 70696467-23dc-4227-aa2a-2c451edb68d1
keywords:
- LPSAFEARRAY_Unmarshal function Automation
topic_type:
- apiref
api_name:
- LPSAFEARRAY_Unmarshal
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

# LPSAFEARRAY\_Unmarshal function

Unmarshals a [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object from the RPC buffer using information passed in by the [**LPSAFEARRAY\_UserUnmarshal**](/windows/desktop/api/wia_xp/nf-wia_xp-lpsafearray_userunmarshal) function.

## Syntax


```C++
unsigned char* __stdcall LPSAFEARRAY_Unmarshal(
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

Receives the safe array that contains the data.

</dd> <dt>

*piid* \[in\]
</dt> <dd>

Points to an IID for an [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) or [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. Used when the members of the safe array are **IDispatch** or **IUnknown**.

</dd> </dl>

## Return value

The value obtained from the returned **HRESULT** value is one of the following.



| Return code                                                                                             | Description                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                   | Success.<br/>                                                                                                                                             |
| <dl> <dt>**RPC\_X\_BAD\_STUB\_DATA** </dt> </dl> | The stub has received bad data. <br/>                                                                                                                     |
| <dl> <dt>**E\_UNEXPECTED** </dt> </dl>           | The array could not be found.<br/>                                                                                                                        |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>          | Insufficient memory for this function to perform.<br/>                                                                                                    |
| <dl> <dt>**DISP\_E\_BADCALLEE** </dt> </dl>      | The [**SAFEARRAY**](/previous-versions/windows/desktop/api/OaIdl/ns-oaidl-tagsafearray) object does not have the correct dimensions, does not have the correct features, or memory cannot be reallocated.<br/> |



 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>OleAut32.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>OleAut32.dll</dt> </dl> |



 

 





