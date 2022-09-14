---
description: A numeric constant that specifies the maximum number of characters that some of the Microsoft cryptographic providers will use when obtaining the user ID.
ms.assetid: cc15a166-9a0c-41ce-9cb1-ecdc922565c0
title: MAXUIDLEN (Wincrypt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MAXUIDLEN

MAXUIDLEN is a numeric constant that specifies the maximum number of characters that some of the Microsoft cryptographic providers will use when obtaining the user ID.MAXUIDLEN is defined in Wincrypt.h.



| Constant/value                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MAXUIDLEN"></span><span id="maxuidlen"></span><dl> <dt>**MAXUIDLEN**</dt> <dt>64 (0x40)</dt> </dl> | When the *pszContainer* parameter of the [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) function is **NULL**, some of the Microsoft cryptographic providers use the logon name of the currently logged on user as the key container name. MAXUIDLEN specifies the maximum number of characters, including the terminating **NULL** character, that these providers will use for the user name.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



## See also

<dl> <dt>

[**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta)
</dt> <dt>

[**CPAcquireContext**](https://www.bing.com/search?q=**CPAcquireContext**)
</dt> </dl>

 

 




