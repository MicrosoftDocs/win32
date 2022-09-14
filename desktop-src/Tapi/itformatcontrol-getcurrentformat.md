---
description: The GetCurrentFormat method retrieves the media format of the current stream.
ms.assetid: 02d1b3b5-3639-4864-9b72-623bf94acf69
title: ITFormatControl::GetCurrentFormat method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITFormatControl::GetCurrentFormat method

\[ This method is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **GetCurrentFormat** method retrieves the media format of the current stream.

## Syntax


```C++
HRESULT GetCurrentFormat(
  [out] AM_MEDIA_TYPE **ppMediaType
);
```



## Parameters

<dl> <dt>

*ppMediaType* \[out\]
</dt> <dd>

Pointer to an **AM\_MEDIA\_TYPE** descriptor of the terminal format. For more information on **AM\_MEDIA\_TYPE**, see the DirectX documentation.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                         |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITFormatControl**](itformatcontrol.md)
</dt> </dl>

 

 




