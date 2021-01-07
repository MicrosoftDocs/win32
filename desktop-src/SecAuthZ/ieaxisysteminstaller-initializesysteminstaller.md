---
description: Installs the specified ActiveX object.
ms.assetid: c5d460d8-0df4-437a-a59e-707bf868a339
title: IeAxiSystemInstaller::InitializeSystemInstaller method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IeAxiSystemInstaller.InitializeSystemInstaller
api_type: 
- COM
api_location: 
---

# IeAxiSystemInstaller::InitializeSystemInstaller method

The **InitializeSystemInstaller** method installs the specified ActiveX object.

## Syntax


```C++
HRESULT InitializeSystemInstaller(
  [in]  BSTR     bstrUrl,
  [in]  DWORD    dwClientPID,
  [in]  IUnknown *pCallback,
  [out] BSTR     *pbstrNonce
);
```



## Parameters

<dl> <dt>

*bstrUrl* \[in\]
</dt> <dd>

The URL of the ActiveX object to install.

</dd> <dt>

*dwClientPID* \[in\]
</dt> <dd>

The process ID of the calling process.

</dd> <dt>

*pCallback* \[in\]
</dt> <dd>

A pointer to an instance of the [**IeAxiServiceCallback**](ieaxiservicecallback.md) interface that verifies whether the ActiveX object is allowed to be installed.

</dd> <dt>

*pbstrNonce* \[out\]
</dt> <dd>

A context that can be used to share state information in calls to other methods used to verify and download the ActiveX object.

</dd> </dl>

## Return value

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](/windows/desktop/SecCrypto/common-hresult-values).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Business, Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                 |
| IID<br/>                      | IID\_IeAxiSystemInstaller is defined as a50ea6f8-4764-4299-b309-022b2a8b4d8d<br/>                   |



## See also

<dl> <dt>

[**IeAxiSystemInstaller**](ieaxisysteminstaller.md)
</dt> </dl>

 

