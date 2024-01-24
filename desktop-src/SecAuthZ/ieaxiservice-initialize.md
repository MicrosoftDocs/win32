---
description: Checks and downloads an ActiveX object.
ms.assetid: a477c6dc-32a7-4d17-a997-6df4967d6c55
title: IeAxiService::Initialize method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IeAxiService.Initialize
api_type: 
- COM
api_location: 
---

# IeAxiService::Initialize method

The **Initialize** method checks and downloads an ActiveX object. If the object meets policy requirements, this method initializes a system object that installs the ActiveX object.

## Syntax


```C++
SECURITY_STATUS Initialize(
  [in]  HWND     hwndParent,
  [in]  DWORD    dwClientPID,
  [in]  BSTR     bstrDesktop,
  [in]  BSTR     bstrClsID,
  [in]  BSTR     bstrURL,
  [out] BSTR     *pbstrNonce,
  [out] IUnknown **ppISyncBrokerInterface
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

A handle to the parent window of the window that is attempting to install the ActiveX control.

</dd> <dt>

*dwClientPID* \[in\]
</dt> <dd>

The process ID of the calling process.

</dd> <dt>

*bstrDesktop* \[in\]
</dt> <dd>

The desktop for the object.

</dd> <dt>

*bstrClsID* \[in\]
</dt> <dd>

The class ID of the ActiveX object to install.

</dd> <dt>

*bstrURL* \[in\]
</dt> <dd>

The URL of the ActiveX object to install.

</dd> <dt>

*pbstrNonce* \[out\]
</dt> <dd>

A context that can be used to share state information in calls to other methods used to verify and download the ActiveX object.

</dd> <dt>

*ppISyncBrokerInterface* \[out\]
</dt> <dd>

A pointer to the instance of the [**IeAxiSystemInstaller**](ieaxisysteminstaller.md) interface that installs the ActiveX control.

</dd> </dl>

## Return value

If the function succeeds, the return value is S\_OK.

If the function fails, the return value can be one of the following error codes.



| Return code/value                                                                                                                                                              | Description                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>**TRUST\_E\_SUBJECT\_NOT\_TRUSTED**</dt> <dt>0x800B0004</dt> </dl> | The ActiveX object should not be installed.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Business, Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                 |
| IID<br/>                      | IID\_IeAxiService is defined as E9E92380-9ECD-4982-A0EB-6815A56CCF27<br/>                           |



## See also

<dl> <dt>

[**IeAxiService**](ieaxiservice.md)
</dt> </dl>

 

 




