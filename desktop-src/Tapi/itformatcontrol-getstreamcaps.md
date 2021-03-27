---
description: The GetStreamCaps method retrieves the capabilities associated with a given format index.
ms.assetid: 4c375369-51d9-44ac-a8f0-c2a96fc10805
title: ITFormatControl::GetStreamCaps method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITFormatControl::GetStreamCaps method

\[ This method is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **GetStreamCaps** method retrieves the capabilities associated with a given format index.

## Syntax


```C++
HRESULT GetStreamCaps(
  [in]  DWORD                   dwIndex,
  [out] AM_MEDIA_TYPE           **ppMediaType,
  [out] TAPI_STREAM_CONFIG_CAPS *pStreamConfigCaps,
  [out] BOOL                    *pfEnabled
);
```



## Parameters

<dl> <dt>

*dwIndex* \[in\]
</dt> <dd>

Index of the format being probed.

</dd> <dt>

*ppMediaType* \[out\]
</dt> <dd>

Pointer to an **AM\_MEDIA\_TYPE** descriptor of the terminal format. For more information on **AM\_MEDIA\_TYPE**, see the DirectX documentation.

</dd> <dt>

*pStreamConfigCaps* \[out\]
</dt> <dd>

A [**TAPI\_STREAM\_CONFIG\_CAPS**](tapi-stream-config-caps.md) structure that gives detailed information concerning stream capabilities.

</dd> <dt>

*pfEnabled* \[out\]
</dt> <dd>

Indicates whether the format associated with the current index is enabled.

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
</dt> <dt>

[**TAPI\_STREAM\_CONFIG\_CAPS**](tapi-stream-config-caps.md)
</dt> </dl>

 

 




