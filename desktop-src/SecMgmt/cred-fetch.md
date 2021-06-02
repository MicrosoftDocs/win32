---
description: Defines values that determine how to fetch the credential of a Group Managed Service Account (gMSA).
ms.assetid: 90891448-22F6-497A-A612-3DAB8622C325
title: CRED_FETCH enumeration (Secpkg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRED_FETCH
api_type: 
- HeaderDef
api_location: 
- Secpkg.h
---

# CRED\_FETCH enumeration

Defines values that determine how to fetch the credential of a Group Managed Service Account (gMSA).

## Syntax


```C++
typedef enum _CRED_FETCH { 
  CredFetchDefault  = 0,
  CredFetchDPAPI    = 1,
  CredFetchForced   = 2
} CRED_FETCH;
```



## Constants

<dl> <dt>

<span id="CredFetchDefault"></span><span id="credfetchdefault"></span><span id="CREDFETCHDEFAULT"></span>**CredFetchDefault**
</dt> <dd>

Signifies that the operating system should first attempt to retrieve the password from the local cache. If it is time to fetch the password, then the operating system should contact a domain controller for the password. If that fails, then return any cached passwords with the status value of success.

</dd> <dt>

<span id="CredFetchDPAPI"></span><span id="credfetchdpapi"></span><span id="CREDFETCHDPAPI"></span>**CredFetchDPAPI**
</dt> <dd>

Returns the local DPAPI credential to the caller. [*Security support providers*](/windows/desktop/SecGloss/s-gly) (SSPs) generally would not require the use of this enumeration.

</dd> <dt>

<span id="CredFetchForced"></span><span id="credfetchforced"></span><span id="CREDFETCHFORCED"></span>**CredFetchForced**
</dt> <dd>

Forces the operating system to attempt to read the password from the domain controller. During the password rollover time, the password may have changed at the domain controller and other member hosts, but the gMSA member host recognizes the password as still valid. This can happen due to clock skew issues between different domain controllers. When this value is specified, the operating system determines if there could be a possible password change due to clock skew, and if so, retrieves the password. Otherwise, the cached credential is returned. If there is no cached credential, then the operating system attempts to get one from the domain controller.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Secpkg.h</dt> </dl> |



 

