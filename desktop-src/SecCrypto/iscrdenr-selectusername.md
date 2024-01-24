---
description: Displays a Select User interface, allowing a user name to be selected.
ms.assetid: 0a02d9e5-b2cf-4818-a2e1-89e6019e53d4
title: ISCrdEnr::selectUserName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.selectUserName
- SCrdEnr.selectUserName
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::selectUserName method

The **selectUserName** method displays a **Select User** interface, allowing a user name to be selected.

The user name applies to the user on whose behalf the certificate enrollment is intended.

## Syntax


```C++
HRESULT selectUserName(
  [in] DWORD dwFlags
);
```


```VB

SCrdEnr.selectUserName( _
  ByVal dwFlags _
)
```





## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved for future use. Set this value to zero.

</dd> </dl>

## Return value

### VB

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Remarks

Use this method to select the name of the user. After a user name has been selected, its value can be retrieved by calling the [**ISCrdEnr::getUserName**](iscrdenr-getusername.md) method.

An alternative to using the 'Select User' interface is to specify a user by calling the [**ISCrdEnr::setUserName**](iscrdenr-setusername.md) method.

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

[**ISCrdEnr::setUserName**](iscrdenr-setusername.md)
</dt> </dl>

 

 




