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
// Creating registry key path
constexpr const wchar_t kBaseRegKeyPath[] =
    L"Software\\Microsoft\\Windows\\CurrentVersion\\Parental Controls\\Users\\";
constexpr const wchar_t kBaseRegKayPathSuffix[] = L\\Web;
 
static const std::wstring* reg_key_path = []() {
    std::wstring user_sid;
    bool got_user_sid_string = base::win::GetUserSidString(&user_sid);
    DCHECK(got_user_sid_string);
    return new std::wstring{kBaseRegKeyPath + user_sid + kBaseRegKayPathSuffix};
  }();
 
// opening registry path
HRESULT hresult =
      reg_key->Open(HKEY_LOCAL_MACHINE, reg_key_path->c_str(),
                    KEY_READ | KEY_WOW64_64KEY);
 
if (hresult == ERROR_SUCCESS) {
    // Registry key exists for user
}
```