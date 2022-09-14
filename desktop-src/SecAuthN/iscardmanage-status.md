---
description: Gets the current status of the smart card or reader.
ms.assetid: ae285e2e-6591-43ab-b92f-1ec755872379
title: ISCardManage::Status method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardManage.Status
api_type: 
- COM
api_location: 
---

# ISCardManage::Status method

\[The **Status** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Status** method gets the current status of the [*smart card*](../secgloss/s-gly.md) or [*reader*](../secgloss/r-gly.md).

## Syntax


```C++
HRESULT Status(
  [out] SCARD_STATES    *pStatus,
  [out] SCARD_PROTOCOLS *pProtocols
);
```



## Parameters

<dl> <dt>

*pStatus* \[out\]
</dt> <dd>

Pointer to an SCARD\_STATES enumeration value. On return, contains the current status/state.

</dd> <dt>

*pProtocols* \[out\]
</dt> <dd>

Pointer to an SCARD\_PROTOCOLS enumeration value. On return, contains the current protocol.

</dd> </dl>

## Return value

The method returns one of the following possible values:



| Return code                                                                                   | Description                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                    |



 

## Remarks

For a list of all the methods defined by this interface, see [**ISCardManage**](iscardmanage.md).

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

[**ISCardManage**](iscardmanage.md)
</dt> </dl>

 

 
