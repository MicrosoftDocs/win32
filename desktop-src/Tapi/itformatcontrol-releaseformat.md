---
description: The ReleaseFormat method releases the structure associated with the format.
ms.assetid: 67181773-5a04-4e20-9814-b004d3b549f5
title: ITFormatControl::ReleaseFormat method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITFormatControl::ReleaseFormat method

\[ This method is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ReleaseFormat** method releases the structure associated with the format.

## Syntax


```C++
HRESULT ReleaseFormat(
  [in] AM_MEDIA_TYPE *pMediaType
);
```



## Parameters

<dl> <dt>

*pMediaType* \[in\]
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

 

 




