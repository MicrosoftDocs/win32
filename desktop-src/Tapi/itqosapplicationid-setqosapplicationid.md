---
description: The SetQOSApplicationID method sets the QOS identifier for the application.
ms.assetid: e25cf749-6673-47eb-b843-4066f475b8f1
title: ITQOSApplicationID::SetQOSApplicationID method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITQOSApplicationID::SetQOSApplicationID method

\[ This method is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetQOSApplicationID** method sets the QOS identifier for the application.

## Syntax


```C++
HRESULT SetQOSApplicationID(
  [in] BSTR pApplicationID,
  [in] BSTR pApplicationGUID,
  [in] BSTR pSubIDs
);
```



## Parameters

<dl> <dt>

*pApplicationID* \[in\]
</dt> <dd>

Unique identifier for the application process.

</dd> <dt>

*pApplicationGUID* \[in\]
</dt> <dd>

Application GUID.

</dd> <dt>

*pSubIDs* \[in\]
</dt> <dd>

Sub-IDs associated with the current call.

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

[**ITQOSApplicationID**](itqosapplicationid.md)
</dt> </dl>

 

 




