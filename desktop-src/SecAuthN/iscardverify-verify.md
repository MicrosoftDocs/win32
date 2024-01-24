---
description: Requests a verification of the user.
ms.assetid: e8b7155c-3444-4aa8-8a15-3b3624a44a77
title: ISCardVerify::Verify method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardVerify.Verify
api_type: 
- COM
api_location: 
---

# ISCardVerify::Verify method

\[The **Verify** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Verify** method requests a verification of the user.

## Syntax


```C++
HRESULT Verify(
  [in] LPBYTEBUFFER pCode,
  [in] SCARD_FLAGS  Flags,
  [in] LONG         lRef
);
```



## Parameters

<dl> <dt>

*pCode* \[in\]
</dt> <dd>

Contains the code to be presented to the [*smart card*](../secgloss/s-gly.md) in the CHV (card holder verification) process.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Indicates whether the code is global or local.

<dl><span id="SC_FL_IHV_GLOBAL"></span><span id="sc_fl_ihv_global"></span><dt>

**SC\_FL\_IHV\_GLOBAL**
</dt><span id="SC_FL_IHV_LOCAL"></span><span id="sc_fl_ihv_local"></span><dt>

**SC\_FL\_IHV\_LOCAL**
</dt> </dl> </dd> <dt>

*lRef* \[in\]
</dt> <dd>

Smart card specific reference.

</dd> </dl>

## Return value

The **Verify** method returns one of the following values:



| Return code                                                                                   | Description                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                    |



 

## Remarks

For a list of all the methods defined by this interface, see [**ISCardVerify**](iscardverify.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows XP<br/>                                |
| End of server support<br/>    | Windows Server 2003<br/>                       |



## See also

<dl> <dt>

[**ISCardVerify**](iscardverify.md)
</dt> </dl>

 

 
