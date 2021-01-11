---
description: The APP\_Auth method authenticates the application. It allows an application to authenticate itself (using a challenge/signature protocol) when authentication is requested by a smart card.
ms.assetid: 0b86ce09-ca17-4d74-bc14-46b17262e669
title: ISCardAuth::APP_Auth method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardAuth.APP_Auth
api_type: 
- COM
api_location: 
---

# ISCardAuth::APP\_Auth method

\[The **APP\_Auth** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **APP\_Auth** method authenticates the application. It allows an application to authenticate itself (using a challenge/signature protocol) when authentication is requested by a [*smart card*](../secgloss/s-gly.md).

## Syntax


```C++
HRESULT APP_Auth(
  [in] LONG         lAlgoID,
  [in] LPBYTEBUFFER pParam,
  [in] LPBYTEBUFFER pBuffer
);
```



## Parameters

<dl> <dt>

*lAlgoID* \[in\]
</dt> <dd>

Algorithm to be used in the authentication process.

</dd> <dt>

*pParam* \[in\]
</dt> <dd>

An [**IByteBuffer**](ibytebuffer.md) containing vendor-specific parameters of the authentication process.

</dd> <dt>

*pBuffer* \[in\]
</dt> <dd>

Data required for the calculation.

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

For a list of all the methods provided by this interface, see [**ISCardAuth**](iscardauth.md).

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

[**ISCardAuth**](iscardauth.md)
</dt> <dt>

[**IByteBuffer**](ibytebuffer.md)
</dt> </dl>

 

 
