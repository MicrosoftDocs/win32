---
description: The Write method writes data to a current opened file.
ms.assetid: 0c92af34-a9db-4242-8b6e-d1010a0d7afa
title: ISCardFileAccess::Write method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardFileAccess.Write
api_type: 
- COM
api_location: 
---

# ISCardFileAccess::Write method

\[The **Write** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Write** method writes data to a current opened file.

## Syntax


```C++
HRESULT Write(
  [in] HSCARD_FILE  hFile,
  [in] LPBYTEBUFFER pData,
  [in] SCARD_FLAGS  flags
);
```



## Parameters

<dl> <dt>

*hFile* \[in\]
</dt> <dd>

A handle to an open file.

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Object/data to be written.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Specifies whether secure messaging should be used.

<dl><span id="SC_FL_SECURE_MESSAGING"></span><span id="sc_fl_secure_messaging"></span><dt>

**SC\_FL\_SECURE\_MESSAGING**
</dt> </dl> </dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                    |



 

## Remarks

To open or close a file, call [**Open**](iscardfileaccess-open.md) or [**Close**](iscardfileaccess-close.md), respectively.

For a list of all the methods defined by this interface, see [**ISCardFileAccess**](iscardfileaccess.md).

In addition to the COM error codes listed above, this interface may return a [*smart card*](../secgloss/s-gly.md) error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows XP<br/>                                |
| End of server support<br/>    | Windows Server 2003<br/>                       |



## See also

<dl> <dt>

[**Close**](iscardfileaccess-close.md)
</dt> <dt>

[**ISCardFileAccess**](iscardfileaccess.md)
</dt> <dt>

[**Open**](iscardfileaccess-open.md)
</dt> </dl>

 

 
