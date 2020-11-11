---
title: DCOMSCMRemoteCallFlags
description: Controls the behavior of calls from the local DCOM Service Control Manager (DCOMSCM) to a remote DCOMSCM.
ms.assetid: fb306da7-4b9a-4386-8525-7f78bd6bf728
keywords:
- DCOMSCMRemoteCallFlags registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# DCOMSCMRemoteCallFlags

Controls the behavior of calls from the local DCOM Service Control Manager (DCOMSCM) to a remote DCOMSCM.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   DCOMSCMRemoteCallFlags = value
```

## Remarks

This is a **REG\_DWORD** value.



| Value | Description                                       |
|-------|---------------------------------------------------|
| 0x1   | **DCOMSCM\_ACTIVATION\_USE\_ALL\_AUTHNSERVICES**  |
| 0x2   | **DCOMSCM\_ACTIVATION\_DISALLOW\_UNSECURE\_CALL** |
| 0x4   | **DCOMSCM\_RESOLVE\_USE\_ALL\_AUTHNSERVICES**     |
| 0x8   | **DCOMSCM\_RESOLVE\_DISALLOW\_UNSECURE\_CALL**    |
| 0x10  | **DCOMSCM\_PING\_USE\_MID\_AUTHNSERVICE**         |



 

## DCOMSCM\_ACTIVATION\_USE\_ALL\_AUTHNSERVICES Description

When the client issues an activation request that uses the default security settings, the local DCOMSCM uses the Negotiate authentication service when making the activation RPC call to the remote DCOMSCM. If the call fails, the local DCOMSCM makes the activation RPC call using no security.

**Windows Server 2003 and Windows XP/2000:** If the activation RPC call that uses the Negotiate authentication service fails, the local DCOMSCM makes the activation RPC call using Kerberos, NTLM, or other configured security providers. If no security providers work, the local DCOMSCM makes the activation RPC call using no security.

By setting this flag, the local DCOMSCM on Windows Vista or higher can be made to behave like pre-Vista systems. It is not recommended to set this flag unless required for compatibility reasons.

## DCOMSCM\_ACTIVATION\_DISALLOW\_UNSECURE\_CALL Description

If the **DCOMSCM\_ACTIVATION\_DISALLOW\_UNSECURE\_CALL** flag is set, the local DCOMSCM does not make an unsecure activation RPC call. To enable clients to make activation requests with non-default security settings, specify the [**COAUTHINFO**](/windows/desktop/api/wtypesbase/ns-wtypesbase-coauthinfo) structure when making the activation request. In this case, the **DCOMSCM\_ACTIVATION\_USE\_ALL\_AUTHNSERVICES** and **DCOMSCM\_ACTIVATION\_DISALLOW\_UNSECURE\_CALL** flags are ignored.

It is not recommended to set this flag unless all the clients and servers in the network are fully authenticated.

## DCOMSCM\_RESOLVE\_USE\_ALL\_AUTHNSERVICES Description

When the client unmarshals an object reference, the local DCOMSCM uses the Negotiate authentication service when making the OXID Resolution RPC call to the remote DCOMSCM. If the call fails, the local DCOMSCM makes the OXID Resolution RPC call using no security.

**Windows Server 2003 and Windows XP/2000:** If the OXID Resolution RPC call using the Negotiate authentication service fails, the local DCOMSCM makes the OXID Resolution RPC call by using Kerberos, NTLM, or other configured security providers. If no security providers work, then the local DCOMSCM makes the OXID Resolution RPC call using no security.

By setting this flag, the local DCOMSCM on Windows Vista or higher can be made to behave like pre-Vista systems. It is not recommended to set this flag unless required for compatibility reasons.

## DCOMSCM\_RESOLVE\_DISALLOW\_UNSECURE\_CALL Description

If the **DCOMSCM\_RESOLVE\_DISALLOW\_UNSECURE\_CALL** flag is set, the local DCOMSCM does not make an unsecure OXID Resolution RPC call. In addition, the local DCOMSCM does not make an unsecure garbage collection Ping RPC call. It is not recommended to set this flag unless all the clients and servers in the network are fully authenticated.

## DCOMSCM\_PING\_USE\_MID\_AUTHNSERVICE Description

The local DCOMSCM uses the Negotiate authentication service when making the garbage-collection Ping RPC call to the remote DCOMSCM. If the call fails, the local DCOMSCM makes the garbage-collection Ping RPC call using no security.

**Windows Server 2003 and Windows XP/2000:** If the garbage-collection Ping RPC call using the Negotiate authentication service fails, the local DCOMSCM makes the garbage collection Ping RPC call by using Kerberos, NTLM, and other configured security providers. If no security providers work, then the local DCOMSCM makes the garbage collection Ping RPC call using no security.

By setting this flag, the local DCOMSCM on Windows Vista or above can be made to behave like pre-Vista systems. It is not recommended to set the **DCOMSCM\_PING\_USE\_MID\_AUTHNSERVICE** flag unless required for compatibility reasons.

## Related topics

<dl> <dt>

[Authentication for Remote Connections](/windows/desktop/WinRM/authentication-for-remote-connections)
</dt> <dt>

[EnableDCOM](enabledcom.md)
</dt> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 