---
description: The ReOrderCapabilities method sets a new order for format capabilities.
ms.assetid: 05785d64-a22f-411f-9fae-318828d30c52
title: ITFormatControl::ReOrderCapabilities method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITFormatControl::ReOrderCapabilities method

\[ This method is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ReOrderCapabilities** method sets a new order for format capabilities.

## Syntax


```C++
HRESULT ReOrderCapabilities(
  [in] DWORD *pdwIndices,
  [in] BOOL  *pfEnabled,
  [in] BOOL  *pfPublicize,
  [in] DWORD dwNumIndices
);
```



## Parameters

<dl> <dt>

*pdwIndices* \[in\]
</dt> <dd>

Index of the format being reordered.

</dd> <dt>

*pfEnabled* \[in\]
</dt> <dd>

Indicates whether the format should be enabled or disabled.

</dd> <dt>

*pfPublicize* \[in\]
</dt> <dd>

Indicates whether the format should be made available.

</dd> <dt>

*dwNumIndices* \[in\]
</dt> <dd>

New index number for the format.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |



 

## Remarks

The [**GetNumberOfCapabilities**](itformatcontrol-getnumberofcapabilities.md) method must be called prior to using this method.

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
</dt> <dt>

[**GetNumberOfCapabilities**](itformatcontrol-getnumberofcapabilities.md)
</dt> </dl>

 

 




