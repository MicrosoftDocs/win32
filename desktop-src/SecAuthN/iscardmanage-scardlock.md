---
description: Locks a connected smart card for exclusive use.
ms.assetid: c39a7cfe-04b6-4298-927a-4280664cf769
title: ISCardManage::SCardLock method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardManage.SCardLock
api_type: 
- COM
api_location: 
---

# ISCardManage::SCardLock method

\[The **SCardLock** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **SCardLock** method locks a connected [*smart card*](../secgloss/s-gly.md) for exclusive use.

## Syntax


```C++
HRESULT SCardLock();
```



## Parameters

This method has no parameters.

## Return value

The method returns one of the following possible values:



| Return code                                                                            | Description                                  |
|----------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Operation completed successfully.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Operation failed to complete.<br/>     |



 

## Remarks

To releases exclusive use of the connected smart card, call [**SCardUnlock**](iscardmanage-scardunlock.md).

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
</dt> <dt>

[**SCardUnlock**](iscardmanage-scardunlock.md)
</dt> </dl>

 

 
