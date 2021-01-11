---
description: Specifies the name of the user on whose behalf the certificate enrollment is intended.
ms.assetid: e088af63-5064-4b1b-976f-047f52e56af8
title: ISCrdEnr::setUserName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.setUserName
- SCrdEnr.setUserName
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::setUserName method

The **setUserName** method specifies the name of the user on whose behalf the certificate enrollment is intended.

## Syntax


```C++
HRESULT setUserName(
  [in] DWORD dwFlags,
  [in] BSTR bstrUserName
);
```


```VB

SCrdEnr.setUserName( _
  ByVal dwFlags, _
  ByVal bstrUserName _
)
```





## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

This value must be either SCARD\_ENROLL\_UPN\_NAME (defined as 1) or SCARD\_ENROLL\_SAM\_COMPATIBLE\_NAME (defined as 2).

Set this value to SCARD\_ENROLL\_UPN\_NAME, if the name specified in *bstrUserName* is the user's Universal Principal Name, such as "someone@example.com". The user's UPN name must correspond to an existing security access manager (SAM) name.

Set this value to SCARD\_ENROLL\_SAM\_COMPATIBLE\_NAME, if the name specified in *bstrUserName* is the user's SAM name in the format of "DOMAIN\\USER".

</dd> <dt>

*bstrUserName* \[in\]
</dt> <dd>

Name of the user.

</dd> </dl>

## Return value

### VB

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Remarks

Call this method to specify the user name to be issued the [*smart card*](../secgloss/s-gly.md). An alternative to **setUserName** is [**ISCrdEnr::selectUserName**](iscrdenr-selectusername.md).

After a user name has been specified, its value can be retrieved by calling [**getUserName**](iscrdenr-getusername.md).

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

[**ISCrdEnr::getUserName**](iscrdenr-getusername.md)
</dt> <dt>

[**ISCrdEnr::resetUser**](iscrdenr-resetuser.md)
</dt> <dt>

[**ISCrdEnr::selectUserName**](iscrdenr-selectusername.md)
</dt> </dl>

 

 
