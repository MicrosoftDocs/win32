---
description: The Directory method retrieves a list of files of the specified type from the current directory.
ms.assetid: 0ae89811-7534-497b-af9f-ae37a48bc3e5
title: ISCardFileAccess::Directory method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardFileAccess.Directory
api_type: 
- COM
api_location: 
---

# ISCardFileAccess::Directory method

\[The **Directory** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Directory** method retrieves a list of files of the specified type from the current directory.

## Syntax


```C++
HRESULT Directory(
  [in]  FILETYPE    fileType,
  [out] LPSAFEARRAY *ppFileList
);
```



## Parameters

<dl> <dt>

*fileType* \[in\]
</dt> <dd>

Type of [*smart card*](../secgloss/s-gly.md) files to list.



| Value                                                                                                                                                                                      | Meaning                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <span id="SC_TYPE_DIRECTORIES"></span><span id="sc_type_directories"></span><dl> <dt>**SC\_TYPE\_DIRECTORIES**</dt> </dl>           | List directory files only.<br/>                |
| <span id="SC_TYPE_FILES"></span><span id="sc_type_files"></span><dl> <dt>**SC\_TYPE\_FILES**</dt> </dl>                             | List elementary files only.<br/>               |
| <span id="SC_TYPE_ALL_FILES"></span><span id="sc_type_all_files"></span><dl> <dt>**SC\_TYPE\_ALL\_FILES**</dt> </dl>                | List both directory and elementary files.<br/> |
| <span id="SC_TYPE_DIRECTORY_FILE"></span><span id="sc_type_directory_file"></span><dl> <dt>**SC\_TYPE\_DIRECTORY\_FILE**</dt> </dl> | Directory file.<br/>                           |
| <span id="SC_TYPE_TRANSPARENT_EF"></span><span id="sc_type_transparent_ef"></span><dl> <dt>**SC\_TYPE\_TRANSPARENT\_EF**</dt> </dl> | Transparent elementary file.<br/>              |
| <span id="SC_TYPE_FIXED_EF"></span><span id="sc_type_fixed_ef"></span><dl> <dt>**SC\_TYPE\_FIXED\_EF**</dt> </dl>                   | Linear fixed elementary file.<br/>             |
| <span id="SC_TYPE_CYCLIC_EF"></span><span id="sc_type_cyclic_ef"></span><dl> <dt>**SC\_TYPE\_CYCLIC\_EF**</dt> </dl>                | Cyclic elementary file.<br/>                   |
| <span id="SC_TYPE_VARIABLE_EF"></span><span id="sc_type_variable_ef"></span><dl> <dt>**SC\_TYPE\_VARIABLE\_EF**</dt> </dl>          | Linear variable elementary file.<br/>          |



 

</dd> <dt>

*ppFileList* \[out\]
</dt> <dd>

Array of BSTRs representing the list of files matching the specifier in *fileType*.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                               |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation was completed successfully.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                             |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | The interface has not implemented this method.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                                 |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in for *ppFileList*.<br/>  |



 

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

[**ISCardFileAccess**](iscardfileaccess.md)
</dt> </dl>

 

 
