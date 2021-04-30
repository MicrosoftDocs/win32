---
description: Clears the user name from the smart card control.
ms.assetid: fff50db5-0610-4985-94c6-96d7ce990219
title: ISCrdEnr::resetUser method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.resetUser
- SCrdEnr.resetUser
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::resetUser method

The **resetUser** method clears the user name from the smart card control.

## Syntax


```C++
HRESULT resetUser();
```



## Parameters

This method has no parameters.

## Remarks

This method clears any existing user name and previously enrolled certificate from memory. The previously enrolled certificate is not removed from the smart card, however.

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

[**ISCrdEnr::selectUserName**](iscrdenr-selectusername.md)
</dt> <dt>

[**ISCrdEnr::setUserName**](iscrdenr-setusername.md)
</dt> </dl>

 

 




