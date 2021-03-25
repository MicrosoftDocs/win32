---
description: The SetAlias method configures a default H.323 alias for the address. This alias will be used in the H.323 call setup exchange so that the other party knows the name of this party.
ms.assetid: 09608214-7346-4ee8-bbfd-0877d3ad0766
title: IH323LineEx::SetAlias method (H323priv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IH323LineEx::SetAlias method

\[**SetAlias** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetAlias** method configures a default H.323 alias for the address. This alias will be used in the H.323 call setup exchange so that the other party knows the name of this party.

Calling this method a second time will overwrite the previous alias.

The alias set on this interface will be used only when there is no other way for the TSP to find a proper alias. In the future, when gatekeeper support is added into the TSP, the alias registered to the gatekeeper or assigned by the gatekeeper will override whatever is set through this method.

## Syntax


```C++
HRESULT SetAlias(
  [in] WCHAR *strAlias,
  [in] DWORD dwLength
);
```



## Parameters

<dl> <dt>

*strAlias* \[in\]
</dt> <dd>

The alias to be used, in Unicode. **Null** termination is not required.

</dd> <dt>

*dwLength* \[in\]
</dt> <dd>

The length of the alias name in number of characters, including the **null** terminator.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                               | Description                                                                                                                      |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Method succeeded.<br/>                                                                                                     |
| <dl> <dt>**E\_POINTER**</dt> </dl> | The number of characters indicated in *dwLength* exceeds the actual number of characters in the *strAlias* parameter.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>H323priv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



 

 




