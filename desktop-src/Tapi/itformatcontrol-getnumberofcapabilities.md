---
description: The GetNumberOfCapabilities method retrieves the number of capabilities associated with the current format.
ms.assetid: 26e51c0d-c1cb-410f-ab19-eb884afa8431
title: ITFormatControl::GetNumberOfCapabilities method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITFormatControl::GetNumberOfCapabilities method

\[ This method is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **GetNumberOfCapabilities** method retrieves the number of capabilities associated with the current format.

## Syntax


```C++
HRESULT GetNumberOfCapabilities(
  [out] DWORD *pdwCount
);
```



## Parameters

<dl> <dt>

*pdwCount* \[out\]
</dt> <dd>

Count of the capabilities.

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

 

 




