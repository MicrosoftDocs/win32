---
description: The GetCurrentDir method returns an absolute path to the currently selected directory.
ms.assetid: 12196143-a98a-4772-a803-d0c9b95a66e4
title: ISCardFileAccess::GetCurrentDir method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardFileAccess.GetCurrentDir
api_type: 
- COM
api_location: 
---

# ISCardFileAccess::GetCurrentDir method

\[The **GetCurrentDir** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **GetCurrentDir** method returns an absolute path to the currently selected directory.

## Syntax


```C++
HRESULT GetCurrentDir(
  [out] BSTR *pbstrPathSpec
);
```



## Parameters

<dl> <dt>

*pbstrPathSpec* \[out\]
</dt> <dd>

Pointer to a BSTR that will contain the path.

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

To change the current directory, call [**ChangeDir**](iscardfileaccess-changedir.md).

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

[**ChangeDir**](iscardfileaccess-changedir.md)
</dt> <dt>

[**ISCardFileAccess**](iscardfileaccess.md)
</dt> </dl>

 

 
