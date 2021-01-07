---
description: Retrieves the name of the user on whose behalf the certificate enrollment is intended.
ms.assetid: 7bd71944-f7dd-4c92-a71c-ecc5c0afd5b2
title: ISCrdEnr::getUserName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.getUserName
- SCrdEnr.getUserName
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::getUserName method

The **getUserName** method retrieves the name of the user on whose behalf the certificate enrollment is intended.

Before calling this method, you must specify the user name in a call to [**ISCrdEnr::selectUserName**](iscrdenr-selectusername.md) or [**ISCrdEnr::setUserName**](iscrdenr-setusername.md).

## Syntax


```C++
HRESULT getUserName(
  [in]  DWORD     dwFlags,
  [out] BSTR *pbstrUserName
);
```


```VB

SCrdEnr.getUserName( _
  ByVal dwFlags, _
  ByRef pbstrUserName _
)
```





## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

This value must be either zero (0), SCARD\_ENROLL\_UPN\_NAME, or SCARD\_ENROLL\_SAM\_COMPATIBLE\_NAME.

If this value is SCARD\_ENROLL\_UPN\_NAME, **getUserName** returns the user's Universal Principal Name (UPN), such as "someone@example.com".

If this value is SCARD\_ENROLL\_SAM\_COMPATIBLE\_NAME, the method returns the user's security access manager (SAM) name in the format "DOMAIN\\USER".

If this value is zero, the method returns the user's UPN name if it exists. If the user does not have a UPN name, the method returns the user's SAM name.

</dd> <dt>

*pbstrUserName* \[out\]
</dt> <dd>

A pointer to a string that returns the name of the user.

</dd> </dl>

## Return value

### C++

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

### VB

String that represents the name of the user.

## Remarks

You can specify the name of the user to whom the [*smart card*](../secgloss/s-gly.md) is issued by calling either [**ISCrdEnr::setUserName**](iscrdenr-setusername.md) or [**ISCrdEnr::selectUserName**](iscrdenr-selectusername.md). After a user name has been specified, its value can be retrieved by calling **getUserName**.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Scrdenrl.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCrdEnr is defined as 753988a1-1357-436d-9cf5-f089bdd67d64<br/>             |



## See also

<dl> <dt>

[**ISCrdEnr**](iscrdenr.md)
</dt> <dt>

[**ISCrdEnr::resetUser**](iscrdenr-resetuser.md)
</dt> <dt>

[**ISCrdEnr::selectUserName**](iscrdenr-selectusername.md)
</dt> <dt>

[**ISCrdEnr::setUserName**](iscrdenr-setusername.md)
</dt> </dl>

 

 
