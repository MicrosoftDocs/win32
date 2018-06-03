---
title: SetUrlGroupAuthentication method of the BitsCompactServerUrlGroup class
description: TheSetUrlGroupAuthentication method sets the authentication scheme for a URL group.
ms.assetid: afa97278-cb36-492f-be90-7c0f9bf7d6d8
keywords:
- SetUrlGroupAuthentication method
- SetUrlGroupAuthentication method, BitsCompactServerUrlGroup class
- BitsCompactServerUrlGroup class, SetUrlGroupAuthentication method
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.SetUrlGroupAuthentication
api_location:
- Root\microsoft\bits
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetUrlGroupAuthentication method of the BitsCompactServerUrlGroup class

The**SetUrlGroupAuthentication** method sets the authentication scheme for a URL group. This scheme is set per URL group

## Syntax


```mof
uint32 SetUrlGroupAuthentication(
  [in]           uint16  Scheme,
  [in]           boolean Enable,
  [in, optional] uint32  Flag,
  [in, optional] string  DomainName,
  [in, optional] string  Realm
);
```



## Parameters

<dl> <dt>

*Scheme* \[in\]
</dt> <dd>

Specifies the authentication scheme. The following authentication schemes are supported:



| Value                                                                        | Meaning              |
|------------------------------------------------------------------------------|----------------------|
| <dl> <dt>0</dt> </dl> | Negotiate<br/> |
| <dl> <dt>1</dt> </dl> | NTLM<br/>      |
| <dl> <dt>2</dt> </dl> | Reserved<br/>  |



 

</dd> <dt>

*Enable* \[in\]
</dt> <dd>

Determines whether the authentication scheme is enabled. If set to 1, the scheme is enabled. Otherwise, this member is set to 0 and the scheme is disabled.

</dd> <dt>

*Flag* \[in, optional\]
</dt> <dd>

Reserved for future use. Must be 0.

</dd> <dt>

*DomainName* \[in, optional\]
</dt> <dd>

Reserved for future use. Must be **NULL**.

</dd> <dt>

*Realm* \[in, optional\]
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

 

 





