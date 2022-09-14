---
description: The Delete method deletes a file at a given location within the smart card file system.
ms.assetid: f51b0329-c5dc-4f70-a92e-19dc0dbc55f8
title: ISCardFileAccess::Delete method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardFileAccess.Delete
api_type: 
- COM
api_location: 
---

# ISCardFileAccess::Delete method

\[The **Delete** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Delete** method deletes a file at a given location within the [*smart card*](../secgloss/s-gly.md) file system.

## Syntax


```C++
HRESULT Delete(
  [in] REFTYPE     refType,
  [in] BSTR        bstrPathSpec,
  [in] SCARD_FLAGS flags
);
```



## Parameters

<dl> <dt>

*refType* \[in\]
</dt> <dd>

Type of reference used in *bstrPathSpec*.

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

Identifier of the file to be deleted.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Specifies whether secure messaging has to be used and data preallocated.

<dl><span id="SC_FL_SECURE_MESSAGING"></span><span id="sc_fl_secure_messaging"></span><dt>

**SC\_FL\_SECURE\_MESSAGING**
</dt><span id="SC_FL_PREALLOCATED"></span><span id="sc_fl_preallocated"></span><dt>

**SC\_FL\_PREALLOCATED**
</dt> </dl> </dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                  | Description                                               |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Operation was completed successfully.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid parameter.<br/>                             |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>    | The interface has not implemented this method.<br/> |



 

## Remarks

For a list of all the methods defined by this interface, see [**ISCardFileAccess**](iscardfileaccess.md).

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

[**Create**](iscardfileaccess-create.md)
</dt> <dt>

[**ISCardFileAccess**](iscardfileaccess.md)
</dt> </dl>

 

 
