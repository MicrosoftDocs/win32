---
description: Allows an application to reconnect to a smart card or reader without having to issue a Detach call followed by an AttachByHandle or AttachByIFD call respectively.
ms.assetid: 450e817d-2cb2-4752-a86e-50cc8e434723
title: ISCardManage::Reconnect method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardManage.Reconnect
api_type: 
- COM
api_location: 
---

# ISCardManage::Reconnect method

\[The **Reconnect** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Reconnect** method allows an application to reconnect to a [*smart card*](../secgloss/s-gly.md) or [*reader*](../secgloss/r-gly.md) without having to issue a [**Detach**](iscardmanage-detach.md) call followed by an [**AttachByHandle**](iscardmanage-attachbyhandle.md) or [**AttachByIFD**](iscardmanage-attachbyifd.md) call respectively.

## Syntax


```C++
HRESULT Reconnect();
```



## Parameters

This method has no parameters.

## Return value

The method returns one of the following possible values:



| Return code                                                                                   | Description                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                    |



 

## Remarks

To attach a smart card call [**AttachByHandle**](iscardmanage-attachbyhandle.md) or [**AttachByIFD**](iscardmanage-attachbyifd.md).

To detach a smart card, call [**Detach**](iscardmanage-detach.md).

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

[**AttachByHandle**](iscardmanage-attachbyhandle.md)
</dt> <dt>

[**AttachByIFD**](iscardmanage-attachbyifd.md)
</dt> <dt>

[**Detach**](iscardmanage-detach.md)
</dt> <dt>

[**ISCardManage**](iscardmanage.md)
</dt> </dl>

 

 
