---
title: RAS Administration DLL Registry Setup
description: Understand the requirements for registering a third-party remote access service (RAS) administration DLL with RAS.
ms.assetid: 8108a0ac-8562-4251-99be-5f2b2f5c67c4
ms.topic: article
ms.date: 05/31/2018
---

# RAS Administration DLL Registry Setup

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



 

For example, the registry entry for a RAS administration DLL from a fictional company named ProElectron, Inc. might be:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         RAS
            AdminDll
```

*DisplayName* : **REG\_SZ** : ProElectron RAS Admin DLL

*DLLPath* : **REG\_SZ** : C:\\nt\\system32\\ntwkadm.dll

The setup program for a RAS administration DLL should also provide remove/uninstall functionality. If a user removes the DLL, the setup program should delete the DLL's registry entries.

 

 




