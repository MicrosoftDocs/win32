---
description: Using the Parental Controls Registry Key
title: Using the Parental Controls Registry Key
ms.topic: article
ms.date: 08/17/2023
---

# Using the Parental Controls Registry Key

The following registry key can be used to determine if a user is a child. If this is the case, safety precautions need to be applied.

```
HKLM\Software\Microsoft\Windows\CurrentVersion\Parental Controls\Users\{user-sid-here}\Web
```


 

## Example code

```C++
  base::win::RegKey reg_key;
  bool policy_enabled = false;
 
  FamilySafetyStatus result = OpenRegKey(&reg_key);
 
  if (result.IsOk()) {
    std::wstring name = GetPolicyString(policy);
    result = ReadRegKey(reg_key, name, &policy_enabled);
  }
```