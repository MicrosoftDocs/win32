---
title: MpErrorMessageFormat function (MpClient.h)
description: Returns a formatted error message based on an error code.
ms.assetid: C125FCE4-3BB0-4608-BBF3-E7FEF17D0807
keywords:
- MpErrorMessageFormat function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpErrorMessageFormat
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpErrorMessageFormat function

Returns a formatted error message based on an error code.

## Syntax


```C++
HRESULT WINAPI MpErrorMessageFormat(
  _In_  MPHANDLE hMpHandle,
  _In_  HRESULT  hrError,
  _Out_ LPWSTR   *pwszErrorDesc
);
```



## Parameters

<dl> <dt>

*hMpHandle* \[in\]
</dt> <dd>

Type: **MPHANDLE**

Handle to the malware protection manager interface. This handle is returned by the [**MpManagerOpen**](mpmanageropen.md) function.

</dd> <dt>

*hrError* \[in\]
</dt> <dd>

Type: **HRESULT**

An **HRESULT**-based error code.

</dd> <dt>

*pwszErrorDesc* \[out\]
</dt> <dd>

Type: **LPWSTR\***

Returns a formatted error message based on *hrError*. This string must be freed using [**MpFreeMemory**](mpfreememory.md).

</dd> </dl>

## Return value

Type: **HRESULT**

If the function succeeds the return value is **S\_OK**.

If the function fails then the return value is a failed **HRESULT** code.

## Remarks

This function is capable of formatting system error codes in addition to specific error codes returned by malware protection functions. The **HRESULT** error codes specific to malware protection functions have a facility of 0x50. Below is a list of a subset of the malware protection-specific error codes that can be returned by various malware protection functions. Using the macro **HRESULT\_FROM\_MP\_STATUS**, the following error codes can be converted to **HRESULT**. See also [Forefront Client Security anti-malware engine error codes](https://support.microsoft.com/kb/939359) for a list of other possible error codes.



| Error Code                              | Description                                                                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ERROR\_MP\_NOENGINE                     | No engine is loaded in antimalware service to perform the requested operation.                                              |
| ERROR\_MP\_NO\_MEMORY                   | The antimalware engine has encountered a no memory situation.                                                               |
| ERROR\_MP\_REMOVE\_FAILED               | Remove operation failed for a specific threat.                                                                              |
| ERROR\_MP\_QUARANTINE\_FAILED           | Quarantine operation failed for a specific threat.                                                                          |
| ERROR\_MP\_THREAT\_NOT\_FOUND           | The specific threat no longer exists in the system.                                                                         |
| ERROR\_MP\_REMOVE\_NOT\_SUPPORTED       | Remove operation for a specific threat inside the container type is not supported.                                          |
| ERROR\_MP\_REMOVE\_IMMUTABLE\_CONTAINER | Due to engine policy, a remove operation of a specific threat inside a blocked container is not supported. (Mail archives.) |
| ERROR\_MP\_BADDB\_OLDENGINE             | Signature update request provided an older engine or signature files(s).                                                    |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MpClient.dll</dt> </dl> |



## See also

<dl> <dt>

[**MpFreeMemory**](mpfreememory.md)
</dt> <dt>

[**MpManagerOpen**](mpmanageropen.md)
</dt> <dt>

[Forefront Client Security anti-malware engine error codes](https://support.microsoft.com/kb/939359)
</dt> </dl>

 

 





