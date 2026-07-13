---
description: Unblocking blocked browser by attesting to provide safe browsing to member accounts.
title: Parental Controls - unblocking blocked browser
ms.topic: concept-article
ms.date: 01/23/2024
---

# Unblocking blocked browser by attesting to provide safe browsing to member accounts

By attesting through this registry key, you are ensuring that your browser will provide safety measures and settings to a member account.

It is recommended that the browsers add this registry key and provide the self-attestation.

To determine if the user is a child, see [Using the Parental Controls Registry Key](using-parental-controls-reg-key.md).

## Child safety registry keys

To unblock your browser, please update the following registry keys:

32 bit registry key:

```
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\ChildSafety
```

64 bit registry key:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ChildSafety
```

:::image type="content" source="../images/child-safety-registry-keys.png" alt-text="Child safety registry keys":::

## Additional information

Some important points to note:

- The executable name in the registry entry should match the name of the browser's executable file (.exe).
- If the .exe name is changed in the future, please update the registry entry with the new executable name to ensure that the browser remains unblocked.

## See also

- [Using the Parental Controls Registry Key](using-parental-controls-reg-key.md)
