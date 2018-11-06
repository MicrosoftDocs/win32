---
title: LoadUserSettings
description: Determines whether COM will load the user profile for COM servers running as the launching user application identity.
ms.assetid: 3e2b3249-3747-4d98-96da-f3e480a51d12
keywords:
- LoadUserSettings registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# LoadUserSettings

Determines whether COM will load the user profile for COM servers running as the launching user application identity.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      LoadUserSettings = value
```

## Remarks

This is a **REG\_DWORD** value. If *value* is nonzero, COM loads the profile of the user account with which it launches the COM server. If *value* is zero or not present, COM will not load the profile of the user account with which it launches the COM server.

This setting is ignored if a [**RunAs**](runas.md) entry is present.

 

 




