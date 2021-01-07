---
description: Performs security checks on the specified ActiveX object and returns the location where the corresponding .cab file was downloaded.
ms.assetid: ba8e4f9b-1569-43f9-b27c-a987044fff41
title: IeAxiServiceCallback::VerifyFile method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IeAxiServiceCallback.VerifyFile
api_type: 
- COM
api_location: 
---

# IeAxiServiceCallback::VerifyFile method

The **VerifyFile** method performs security checks on the specified ActiveX object and returns the location where the corresponding .cab file was downloaded.

## Syntax


```C++
HRESULT VerifyFile(
  [in]  BSTR bstrFileUrl,
  [out] BSTR *bstrApprovedFileName
);
```



## Parameters

<dl> <dt>

*bstrFileUrl* \[in\]
</dt> <dd>

The URL of the ActiveX object to check.

</dd> <dt>

*bstrApprovedFileName* \[out\]
</dt> <dd>

The name of the file where the .cab file associated with the ActiveX object was downloaded.

</dd> </dl>

## Return value

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](/windows/desktop/SecCrypto/common-hresult-values).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Business, Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                 |
| IID<br/>                      | IID\_IeAxiServiceCallback is defined as 1823E7BA-EC36-447a-9B2E-B4912E15AFE7<br/>                   |



## See also

<dl> <dt>

[**IeAxiServiceCallback**](ieaxiservicecallback.md)
</dt> </dl>

 

