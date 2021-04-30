---
description: The Seek method selects the object from which (read/write) access will be done.
ms.assetid: 9e06df70-6415-46dd-b34f-59614d1cbee7
title: ISCardFileAccess::Seek method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardFileAccess.Seek
api_type: 
- COM
api_location: 
---

# ISCardFileAccess::Seek method

\[The **Seek** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Seek** method selects the object from which (read/write) access will be done.

## Syntax


```C++
HRESULT Seek(
  [in] HSCARD_FILE hFile,
  [in] SEEKTYPE    *Seek,
  [in] LONG        lOffset 
);
```



## Parameters

<dl> <dt>

*hFile* \[in\]
</dt> <dd>

Handle of the open file.

</dd> <dt>

*Seek* \[in\]
</dt> <dd>

Location where the seek should begin.



| Value                                                                                                | Meaning                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>SC\_SEEK\_FROM\_BEGINNING</dt> </dl> | Begin search at the beginning.<br/>          |
| <dl> <dt>SC\_SEEK\_FROM\_END </dt> </dl>      | Begin search from the end.<br/>              |
| <dl> <dt>SC\_SEEK\_RELATIVE</dt> </dl>        | Begin search from the current position.<br/> |



 

</dd> <dt>

*lOffset* \[in\]
</dt> <dd>

Number of data objects from the reference object.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                    |



 

## Remarks

To read to or write from a file, call [**Read**](iscardfileaccess-read.md) or [**Write**](iscardfileaccess-write.md) respectively.

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
</dt> <dt>

[**Read**](iscardfileaccess-read.md)
</dt> <dt>

[**Write**](iscardfileaccess-write.md)
</dt> </dl>

 

 
