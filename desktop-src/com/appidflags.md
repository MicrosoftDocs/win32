---
title: AppIDFlags
description: A set of flags that control the activation behavior of a COM server.
ms.assetid: ab98e7d3-85c6-4328-84c4-1d4583df69ce
keywords:
- AppIDFlags registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# AppIDFlags

A set of flags that control the activation behavior of a COM server.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      AppIDFlags = flags
```

## Remarks

This is a **REG\_DWORD** value.



| Flag Value | Constant                                              |
|------------|-------------------------------------------------------|
| 0x1        | APPIDREGFLAGS\_ACTIVATE\_IUSERVER\_INDESKTOP          |
| 0x2        | APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND |
| 0x4        | APPIDREGFLAGS\_ISSUE\_ACTIVATION\_RPC\_AT\_IDENTIFY   |



 

### APPIDREGFLAGS\_ACTIVATE\_IUSERVER\_INDESKTOP Description

If the **APPIDREGFLAGS\_ACTIVATE\_IUSERVER\_INDESKTOP** flag is cleared in **AppIDFlags** or if **AppIDFlags** is not present, the client in a terminal server session making an activation request for an [Interactive User](interactive-user.md) COM server, will either bind to, or launch and bind to, the COM server in the "default" desktop of the "winsta0" [window station](/windows/desktop/winstation/window-stations) of the session in the activation request. For example, if the client is running "winsta0\\desktop1" of session 3, the activation request for session 3 will either bind to, or launch and bind to, the COM server in "winsta0\\default" of session 3, even if an instance of the COM server is already running in "winsta0\\desktop1" of session 3.

If the **APPIDREGFLAGS\_ACTIVATE\_IUSERVER\_INDESKTOP** flag is set in the **AppIDFlags** value, COM will either bind to, or launch and bind to, the server process running in the client's desktop and the session in the activation request. For example, if the client is running "winsta0\\desktop1" in session 3, the activation request for session 3 will either bind to, or launch and bind to, the COM server in "winsta0\\desktop1" in session 3, even if an instance of the COM server is already running in "winsta0\\default" in session 3.

The client can use the [session moniker](/windows/desktop/TermServ/session-monikers) to specify a session different than the client's session when it makes the activation request.

The **APPIDREGFLAGS\_ACTIVATE\_IUSERVER\_INDESKTOP** flag applies only to COM servers that are configured to RunAs "[Interactive User](interactive-user.md)".

### APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND Description

If the **APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND** flag is set in **AppIDFlags**, COM servers that are configured to RunAs "Activator" will be launched with a process security descriptor that allows [PROCESS\_ALL\_ACCESS](/windows/desktop/ProcThread/process-security-and-access-rights) to the LogonID SID of the process token. In addition, the owner of the security descriptor will be set to the LogonID SID of the process token.

If the **APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND** flag is set in **AppIDFlags**, COM servers that are configured to RunAs "This User" will be launched with a process security descriptor that allows [PROCESS\_ALL\_ACCESS](/windows/desktop/ProcThread/process-security-and-access-rights) in the LogonID SID of the process token. In addition, the owner of the security descriptor will be set to the LogonID SID of the process token. Further, the COM Service Control Manager (SCM) modifies the token of the COM server process as follows:

-   It adds an APPID SID to the token. It grants the APPID SID full access in the token default discretionary access control list (DACL). In Windows Vista and later versions of Windows, it grants the OwnerRights SID READ\_CONTROL permission in the token default DACL. In pre-Windows Vista versions of Windows, it sets the token owner to the APPID SID.

The following security considerations must be taken into account when using the **APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND** flag:

-   The **APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND** flag is meant to be set by COM servers that are launched under one of the built-in service security contexts; either the NetworkService or the LocalService accounts. If the servers impersonate privileged clients and if the **APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND** flag is not set, malicious code running in other processes with the same security context can elevate privilege by hijacking the impersonation tokens of the privileged clients from the COM server process.
-   When the **APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND** flag is set, COM hardens the security descriptor of the process object in the case of RunAs "Activator" COM servers. For such servers, the COM client is expected to harden the token that it uses for the COM activation.
-   When the **APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND** flag is set, COM hardens the security descriptor of the process object in the case of RunAs "This User" COM servers. It also hardens the process token of the COM server since the COM SCM is the entity that creates the token.

The **APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND** flag is supported in Windows XP, Windows Server 2003, Windows Vista, and Windows Server 2008 only when the MSRC8322 patch ([security bulletin MS09-012](https://support.microsoft.com/kb/959454)) is applied. It is natively supported in Windows 7 and later versions of Windows.

The **APPIDREGFLAGS\_SECURE\_SERVER\_PROCESS\_SD\_AND\_BIND** flag applies only to COM servers that are configured to RunAs "Activator" or "This User". It does not apply to COM servers that are NT services.

### APPIDREGFLAGS\_ISSUE\_ACTIVATION\_RPC\_AT\_IDENTIFY Description

If the **APPIDREGFLAGS\_ISSUE\_ACTIVATION\_RPC\_AT\_IDENTIFY** flag is set in **AppIDFlags**, the COM SCM will issue object activation requests to the COM server process using an impersonation level of [RPC\_C\_IMP\_LEVEL\_IDENTIFY](impersonation-levels.md).

If the **APPIDREGFLAGS\_ISSUE\_ACTIVATION\_RPC\_AT\_IDENTIFY** flag is not set, the COM SCM will issue object activation requests to the COM server processes using an impersonation level of [RPC\_C\_IMP\_LEVEL\_IMPERSONATE](impersonation-levels.md).

The following security considerations must be taken into account when using the **APPIDREGFLAGS\_ISSUE\_ACTIVATION\_RPC\_AT\_IDENTIFY** flag:

-   The **APPIDREGFLAGS\_ISSUE\_ACTIVATION\_RPC\_AT\_IDENTIFY** flag is meant to be used by COM servers that do not perform work on behalf of clients in object activation requests. For such servers, having the COM SCM issue object activation requests at [RPC\_C\_IMP\_LEVEL\_IDENTIFY](impersonation-levels.md) minimizes the chances of privileged tokens with [**SE\_IMPERSONATE\_NAME**](/windows/desktop/SecAuthZ/privilege-constants) level appearing in the process.

The **APPIDREGFLAGS\_ISSUE\_ACTIVATION\_RPC\_AT\_IDENTIFY** flag is supported in Windows 7 and later versions of Windows.

## Related topics

<dl> <dt>

[Desktops](/windows/desktop/winstation/desktops)
</dt> <dt>

[Impersonation Levels](impersonation-levels.md)
</dt> <dt>

[Interactive User](interactive-user.md)
</dt> <dt>

[Session Monikers](/windows/desktop/TermServ/session-monikers)
</dt> <dt>

[Window Stations](/windows/desktop/winstation/window-stations)
</dt> </dl>

 

 