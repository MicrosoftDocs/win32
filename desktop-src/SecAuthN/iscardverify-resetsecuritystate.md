---
Description: Resets the current security context of the smart card.
ms.assetid: fcd55b65-a741-4244-8597-ec61cea3f4b7
title: ISCardVerify::ResetSecurityState method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardVerify.ResetSecurityState
api_type: 
- COM
api_location: 
---

# ISCardVerify::ResetSecurityState method

\[The **ResetSecurityState** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](https://msdn.microsoft.com/en-us/library/Dd627652(v=VS.85).aspx) provide similar functionality.\]

The **ResetSecurityState** method resets the current [*security context*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) of the [*smart card*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx).

## Syntax


```C++
HRESULT ResetSecurityState();
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

To re-enable the [*security context*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) without resetting, call [**Unblock**](https://msdn.microsoft.com/en-us/library/Aa377269(v=VS.85).aspx).

For a list of all the methods defined by this interface, see [**ISCardVerify**](iscardverify.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows XP<br/>                                |
| End of server support<br/>    | Windows Server 2003<br/>                       |



## See also

<dl> <dt>

[**ISCardVerify**](iscardverify.md)
</dt> <dt>

[**Unblock**](https://msdn.microsoft.com/en-us/library/Aa377269(v=VS.85).aspx)
</dt> </dl>

 

 




