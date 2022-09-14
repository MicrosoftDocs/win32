---
title: ROTFlags
description: Controls the registration of a COM server in the running object table (ROT).
ms.assetid: a27c04e5-b1d3-4cb5-9b2c-9ae45663cf56
keywords:
- ROTFlags registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# ROTFlags

Controls the registration of a COM server in the running object table (ROT).

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      ROTFlags = flags
```

## Remarks

This is a **REG\_DWORD** value.



| Flag Value | Constant                        |
|------------|---------------------------------|
| 0x1        | **ROTREGFLAGS\_ALLOWANYCLIENT** |



 

### ROTREGFLAGS\_ALLOWANYCLIENT Description

If a COM server wants to register in the ROT and allow any client to access the registration, it must use the **ROTFLAGS\_ALLOWANYCLIENT** flag. An "Activate As Activator" COM server cannot specify **ROTFLAGS\_ALLOWANYCLIENT** because the DCOM service control manager (DCOMSCM) enforces a spoof check against this flag. Therefore, in Windows Vista and later, COM adds support for the **ROTFlags** registry entry that allows the server to stipulate that its ROT registrations be made available to any client.

The entry must exist in the **HKEY\_LOCAL\_MACHINE** hive. This entry provides an "Activate As Activator" server with the same functionality that **ROTFLAGS\_ALLOWANYCLIENT** provides for a RunAs server.

## Related topics

<dl> <dt>

[AppID Key](appid-key.md)
</dt> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




