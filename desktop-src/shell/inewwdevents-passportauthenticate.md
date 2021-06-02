---
description: Enables server-side pages hosted in a wizard to verify that the user has been authenticated through a Microsoft account.
ms.assetid: 8b99eb84-c434-489a-b177-1e00f18d2dcc
title: NewWDEvents.PassportAuthenticate method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NewWDEvents.PassportAuthenticate
api_type: 
- COM
api_location: 
- Shell32.dll
---

# NewWDEvents.PassportAuthenticate method

Enables server-side pages hosted in a wizard to verify that the user has been authenticated through a Microsoft account.

## Syntax


```JScript
bRetVal = NewWDEvents.PassportAuthenticate(
  bstrSignInUrl
)
```



## Parameters

<dl> <dt>

*bstrSignInUrl* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A string containing the URL of a webpage that redirects to the Microsoft account log on UI.

</dd> </dl>

## Return value

Type: **Boolean**

Set to **true** if authentication succeeds, **false** otherwise.

## Remarks

This method may be called even if a user is already logged on to a Microsoft account. In that case, the method returns **true** without displaying the Microsoft account log on UI.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 6.0 or later)</dt> </dl> |



 

 
