---
description: Releases exclusive use of the connected smart card.
ms.assetid: a236743a-1d12-44db-853d-f757f43a7e8f
title: ISCardManage::SCardUnlock method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardManage.SCardUnlock
api_type: 
- COM
api_location: 
---

# ISCardManage::SCardUnlock method

\[The **SCardUnlock** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **SCardUnlock** method releases exclusive use of the connected [*smart card*](../secgloss/s-gly.md).

## Syntax


```C++
HRESULT SCardUnlock(
  [in] SCARD_DISPOSITIONS Disposition
);
```



## Parameters

<dl> <dt>

*Disposition* \[in\]
</dt> <dd>

The state to leave the smart card in when the lock is released.

<dl><span id="LEAVE"></span><span id="leave"></span><dt>

**LEAVE**
</dt><span id="RESET"></span><span id="reset"></span><dt>

**RESET**
</dt><span id="UNPOWER"></span><span id="unpower"></span><dt>

**UNPOWER**
</dt><span id="EJECT"></span><span id="eject"></span><dt>

**EJECT**
</dt> </dl> </dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                  | Description                                          |
|----------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Operation completed successfully.<br/>         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *Disposition* parameter is not valid.<br/> |



 

## Remarks

To lock the connected smart card, call [**SCardLock**](iscardmanage-scardlock.md).

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

[**SCardLock**](iscardmanage-scardlock.md)
</dt> </dl>

 

 
