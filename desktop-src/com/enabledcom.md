---
title: EnableDCOM
description: Controls the global activation and call policies of the machine. Only administrators and the system have full access to this portion of the registry. All other users have read-only access.
ms.assetid: 8533270d-f1b0-42b9-a50d-b05a0dfeee22
keywords:
- EnableDCOM registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# EnableDCOM

Controls the global activation and call policies of the machine. Only administrators and the system have full access to this portion of the registry. All other users have read-only access.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   EnableDCOM = value
```

## Remarks

This is a **REG\_SZ** value.



| Value    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| N (or n) | No remote clients may launch servers or connect to objects on this computer. Local clients cannot access remote DCOM servers; all DCOM traffic is blocked. Local launching of class code and connecting to objects are allowed on a per-class basis according to the value and access permissions of the class's [**LaunchPermission**](launchpermission.md) registry value and the global [**DefaultLaunchPermission**](defaultlaunchpermission.md) registry value. |
| Y (or y) | Launching of servers and connecting to objects by remote clients is allowed on a per-class basis according to the value and access permissions of the class's [**LaunchPermission**](launchpermission.md) registry value and the global [**DefaultLaunchPermission**](defaultlaunchpermission.md) registry value.                                                                                                                                                    |



 

## Related topics

<dl> <dt>

[**DefaultLaunchPermission**](defaultlaunchpermission.md)
</dt> <dt>

[**LaunchPermission**](launchpermission.md)
</dt> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




