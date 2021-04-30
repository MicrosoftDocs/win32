---
description: Creates the specified interface.
ms.assetid: f4cfc407-b006-46a2-9751-834b532309ec
title: ISCardManage::CreateInterface method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardManage.CreateInterface
api_type: 
- COM
api_location: 
---

# ISCardManage::CreateInterface method

\[The **CreateInterface** method is available for use in the operating systems specified in the Requirements section. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **CreateInterface** method creates the specified interface.

## Syntax


```C++
HRESULT CreateInterface(
  [in]  LPGUID    pguidInterface,
  [in]  BSTR      bstrName,
  [in]  LONG      *pUserData,
  [out] LPUNKNOWN *ppInterface
);
```



## Parameters

<dl> <dt>

*pguidInterface* \[in\]
</dt> <dd>

The GUID value of the interface to create.

</dd> <dt>

*bstrName* \[in\]
</dt> <dd>

The name of the interface to create if the GUID is unavailable. Standard values are "CryptoProvider".

</dd> <dt>

*pUserData* \[in\]
</dt> <dd>

Pointer to user-specific data to use in the creation of an interface.

</dd> <dt>

*ppInterface* \[out\]
</dt> <dd>

Pointer to the returned interface.

</dd> </dl>

## Return value

The possible return values are the following:



| Return code                                                                                   | Description                                                                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | One of the supplied parameters are not valid.<br/>                                         |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in either the *pguidInterface* or the *pUserData* parameter.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                                                                        |



 

## Remarks

For a list of all the methods defined by the [**ISCardManage**](iscardmanage.md) interface, see **ISCardManage**.

In addition to the COM error codes listed above, this interface may return a [*smart card*](../secgloss/s-gly.md) error code if a smart card function was called to complete the request. For information about smart card error codes, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows XP<br/>                                |
| End of server support<br/>    | Windows Server 2003<br/>                       |



## See also

<dl> <dt>

[**ISCardManage**](iscardmanage.md)
</dt> </dl>

 

 
