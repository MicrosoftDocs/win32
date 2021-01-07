---
description: Retrieves the primitive data referred by TLVs (tag, length, value) for the specified object.
ms.assetid: 135aeb9a-b851-4522-862f-02a7e020c36b
title: ISCardFileAccess::GetProperties method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardFileAccess.GetProperties
api_type: 
- COM
api_location: 
---

# ISCardFileAccess::GetProperties method

\[The **GetProperties** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **GetProperties** method retrieves the primitive data referred by TLVs (tag, length, value) for the specified object.

## Syntax


```C++
HRESULT GetProperties(
  [in]      REFTYPE     refType,
  [in]      BSTR        bstrPathSpec,
  [in]      SCARD_FLAGS flags,
  [in, out] LPTLV_TABLE *ppTLV
);
```



## Parameters

<dl> <dt>

*refType* \[in\]
</dt> <dd>

Type of reference used in *bstrNewDir*.

<dl><span id="SC_TYPE_BY_NAME"></span><span id="sc_type_by_name"></span><dt>

**SC\_TYPE\_BY\_NAME**
</dt><span id="SC_TYPE_BY_ID"></span><span id="sc_type_by_id"></span><dt>

**SC\_TYPE\_BY\_ID**
</dt><span id="SC_TYPE_BY_SHORT"></span><span id="sc_type_by_short"></span><dt>

**SC\_TYPE\_BY\_SHORT**
</dt><span id="SC_TYPE_BY_ANY"></span><span id="sc_type_by_any"></span><dt>

**SC\_TYPE\_BY\_ANY**
</dt> </dl> </dd> <dt>

*bstrPathSpec* \[in\]
</dt> <dd>

File.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Specifies whether secure messaging should be used.

<dl><span id="SC_FL_SECURE_MESSAGING"></span><span id="sc_fl_secure_messaging"></span><dt>

**SC\_FL\_SECURE\_MESSAGING**
</dt> </dl> </dd> <dt>

*ppTLV* \[in, out\]
</dt> <dd>

Pointer to TLV structures whose value has been retrieved.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                |
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
</dt> </dl>

 

 
