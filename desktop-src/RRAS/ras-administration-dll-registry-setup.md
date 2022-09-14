---
title: About RAS Administration DLL Registry Setup
description: Understand the requirements for registering a third-party remote access service (RAS) administration DLL with RAS. RAS supports multiple RAS Administration DLLs.
ms.assetid: e83a5e37-a39d-4465-abc9-653cdd56893b
keywords:
- RAS Administration RRAS , DLL registry setup
ms.topic: article
ms.date: 05/31/2018
---

# About RAS Administration DLL Registry Setup

The setup program for a third-party RAS administration DLL must register the DLL with RAS by providing information under the following key in the registry.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         RAS
            AdminDll
```

To register the DLL, set the following values under this key.



| Value name    | Value data                                                                    |
|---------------|-------------------------------------------------------------------------------|
| *DisplayName* | A **REG\_SZ** string that contains the user-friendly display name of the DLL. |
| *DLLPath*     | A **REG\_SZ** string that contains the full path of the DLL.                  |



 

Because RAS supports multiple RAS Administration DLLs, the registry value **DLLPath** can contain a semi-colon delimited list of paths. For example, the registry entry for a RAS administration DLL from a fictional company named ProElectron, Inc., might be the following:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         RAS
            AdminDll
```

*DisplayName*: **REG\_SZ** : ProElectron RAS Admin DLL

*DLLPath*: **REG\_SZ** : C:\\nt\\system32\\ntwkadm.dll; C:\\nt\\system32\\ntwkadm2.dll

RAS calls the DLLs in the order in which they are listed in this registry value. The registry value *DisplayName* still contains only a single display name.

The setup program for a RAS administration DLL must also provide remove and uninstall functionality. If a user removes the DLL, the setup program must delete the registry entries for the DLL.

**Windows 2000/NT:** RAS supports only one RAS Administration DLL, so the registry value **DLLPath** cannot contain a semi-colon delimited list of paths.

 

 




