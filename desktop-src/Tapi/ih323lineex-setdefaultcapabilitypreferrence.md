---
description: Configures the preference of the default capabilities.
ms.assetid: 0afcb25a-2499-4baa-82ad-0706164e2e72
title: IH323LineEx::SetDefaultCapabilityPreferrence method (H323priv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IH323LineEx::SetDefaultCapabilityPreferrence method

\[**SetDefaultCapabilityPreferrence** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetDefaultCapabilityPreferrence** method configures the preference of the default capabilities. Capabilities have a default weight of 100. If the application specifies a higher weight for a capability, it will have a higher priority during the H.245 negotiation. If the application sets the weight of a capability to 0, it will not be used in the H.245 negotiation.

This method is cumulative. For example, if this method is called first to disable a capability and is called again to disable another, both capabilities will be disabled as the result of these two calls.

## Syntax


```C++
HRESULT SetDefaultCapabilityPreferrence(
  [in] DWORD           dwNumCaps,
  [in] H245_CAPABILITY *pCapabilities,
  [in] DWORD           *pWeights
);
```



## Parameters

<dl> <dt>

*dwNumCaps* \[in\]
</dt> <dd>

A **DWORD** value that contains the number of capabilities set with this method.

</dd> <dt>

*pCapabilities* \[in\]
</dt> <dd>

An array of capabilities. Each element of the array is an [**H245\_CAPABILITY**](h245-capability.md) value.

</dd> <dt>

*pWeights* \[in\]
</dt> <dd>

An array of weights associated with the capabilities.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                                                                                                                                                                                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>                                                                                                                                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pCapabilities* parameter is **NULL**, or the *pWeights* parameter is **NULL**, or both *pCapabilities* and *pWeights* are **NULL**, or the pCapabilities array contains an invalid H.245 capability object.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | Unable to read an element of the *pWeights* array or an element of the *pCapabilities* array.<br/>                                                                                                                    |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>H323priv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



 

 




