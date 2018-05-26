---
title: GetUrlGroupAuthentication method of the BitsCompactServerUrlGroup class
description: This GetUrlGroupAuthentication method gets the authentication scheme for a URL group. The schemes are retrieved per URL group.
ms.assetid: 5efb1764-2dcf-4ac0-ab52-952a9a19426b
keywords:
- GetUrlGroupAuthentication method
- GetUrlGroupAuthentication method, BitsCompactServerUrlGroup class
- BitsCompactServerUrlGroup class, GetUrlGroupAuthentication method
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.GetUrlGroupAuthentication
api_location:
- Root\microsoft\bits
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetUrlGroupAuthentication method of the BitsCompactServerUrlGroup class

This **GetUrlGroupAuthentication** method gets the authentication scheme for a URL group. The schemes are retrieved per URL group.

## Syntax


```mof
uint32 GetUrlGroupAuthentication(
  [in]            uint16  Scheme,
  [out]           boolean Enable,
  [out, optional] uint32  Flag,
  [out, optional] string  DomainName,
  [out, optional] string  Realm
);
```



## Parameters

<dl> <dt>

*Scheme* \[in\]
</dt> <dd>

Specifies the authentication scheme for the URL group. The following authentication schemes are supported:



| Value                                                                        | Meaning              |
|------------------------------------------------------------------------------|----------------------|
| <dl> <dt>0</dt> </dl> | Negotiate<br/> |
| <dl> <dt>1</dt> </dl> | NTLM<br/>      |
| <dl> <dt>2</dt> </dl> | Reserved<br/>  |



 

</dd> <dt>

*Enable* \[out\]
</dt> <dd>

Specifies whether the authentication scheme is enabled. If set to 1, the scheme is enabled. Otherwise, this member is set to 0 and the scheme is disabled.

</dd> <dt>

*Flag* \[out, optional\]
</dt> <dd>

Reserved for future use. Must be 0.

</dd> <dt>

*DomainName* \[out, optional\]
</dt> <dd>

Reserved for future use. Must be **NULL**.

</dd> <dt>

*Realm* \[out, optional\]
</dt> <dd>

Reserved for future use. Must be **NULL**.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsCompactServerUrlGroup**](bitslightweightserverurlgroup.md)
</dt> </dl>

 

 





