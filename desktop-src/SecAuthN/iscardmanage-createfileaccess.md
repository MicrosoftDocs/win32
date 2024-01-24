---
description: Creates an ISCardFileAccess interface.
ms.assetid: 06a5948f-c7bd-49bf-9032-f40f3d0d330c
title: ISCardManage::CreateFileAccess method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardManage.CreateFileAccess
api_type: 
- COM
api_location: 
---

# ISCardManage::CreateFileAccess method

\[The **CreateFileAccess** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **CreateFileAccess** method creates an [**ISCardFileAccess**](iscardfileaccess.md) interface.

## Syntax


```C++
HRESULT CreateFileAccess(
  [out] ISCardFileAccess **ppISCardFileAccess
);
```



## Parameters

<dl> <dt>

*ppISCardFileAccess* \[out\]
</dt> <dd>

Returned pointer to the created [**ISCardFileAccess**](iscardfileaccess.md) interface.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                                  |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *ppISCardFileAccess* parameter is not valid.<br/>  |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *ppISCardFileAccess*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                                    |



 

## Remarks

For a list of all the methods defined by this interface, see [**ISCardManage**](iscardmanage.md).

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

[**ISCardManage**](iscardmanage.md)
</dt> </dl>

 

 
