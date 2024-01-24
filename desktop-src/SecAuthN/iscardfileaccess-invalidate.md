---
description: Makes the specified file (EF or DF) not valid. A file that is not valid cannot be accessed by other methods prior to using Rehabilitate.
ms.assetid: 5600fcf0-091c-437e-a45c-4de5b0a47d68
title: ISCardFileAccess::Invalidate method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardFileAccess.Invalidate
api_type: 
- COM
api_location: 
---

# ISCardFileAccess::Invalidate method

\[The **Invalidate** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Invalidate** method makes the specified file (EF or DF) not valid. A file that is not valid cannot be accessed by other methods prior to using [**Rehabilitate**](iscardfileaccess-rehabilitate.md).

## Syntax


```C++
HRESULT Invalidate(
  [in] BSTR        bstrPathSpec,
  [in] SCARD_FLAGS flags
);
```



## Parameters

<dl> <dt>

*bstrPathSpec* \[in\]
</dt> <dd>

File.

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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | A parameter is not valid.<br/>         |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                    |



 

## Remarks

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

[**ISCardFileAccess**](iscardfileaccess.md)
</dt> <dt>

[**Rehabilitate**](iscardfileaccess-rehabilitate.md)
</dt> </dl>

 

 
