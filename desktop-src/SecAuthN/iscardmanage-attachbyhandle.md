---
description: Creates a communication link to a smart card (ICC) using a handle returned by the smart card resource manager.
ms.assetid: dfd05dce-4416-4881-92ca-c85baccf3b86
title: ISCardManage::AttachByHandle method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardManage.AttachByHandle
api_type: 
- COM
api_location: 
---

# ISCardManage::AttachByHandle method

\[The **AttachByHandle** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **AttachByHandle** method creates a communication link to a [*smart card*](../secgloss/s-gly.md) (ICC) using a handle returned by the smart card [*resource manager*](../secgloss/r-gly.md).

## Syntax


```C++
HRESULT AttachByHandle(
  [in] HSCARD hICC
);
```



## Parameters

<dl> <dt>

*hICC* \[in\]
</dt> <dd>

A handle to a smart card.

</dd> </dl>

## Return value

The method returns one of the following possible values:



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *hICC* parameter is not valid.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                     |



 

## Remarks

To attach a [*reader*](../secgloss/r-gly.md) call [**AttachByIFD**](iscardmanage-attachbyifd.md).

To release an attachment call [**Detach**](iscardmanage-detach.md).

To reconnect with the smart card without calling [**Detach**](iscardmanage-detach.md) and **AttachByHandle**, call [**Reconnect**](iscardmanage-reconnect.md).

For a list of all the methods defined by the [**ISCardManage**](iscardmanage.md) interface, see [**ISCardManage**](iscardmanage.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For information about smart card error codes, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows XP<br/>                                |
| End of server support<br/>    | Windows Server 2003<br/>                       |



## See also

<dl> <dt>

[**AttachByIFD**](iscardmanage-attachbyifd.md)
</dt> <dt>

[**Detach**](iscardmanage-detach.md)
</dt> <dt>

[**ISCardManage**](iscardmanage.md)
</dt> <dt>

[**Reconnect**](iscardmanage-reconnect.md)
</dt> </dl>

 

 
