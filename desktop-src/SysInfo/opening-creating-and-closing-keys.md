---
description: Before an application can add data to the registry, it must create or open a key.
ms.assetid: 7b0b24d2-b54f-4243-95d0-2adbd87cb4df
title: Opening, Creating, and Closing Keys
ms.topic: article
ms.date: 05/31/2018
---

# Opening, Creating, and Closing Keys

Before an application can add data to the registry, it must create or open a key. To create or open a key, an application always refers to the key as a subkey of a currently open key. The following predefined keys are always open: **HKEY\_LOCAL\_MACHINE**, **HKEY\_CLASSES\_ROOT**, **HKEY\_USERS**, and **HKEY\_CURRENT\_USER**. An application uses the [**RegOpenKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regopenkeyexa) function to open a key and the [**RegCreateKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regcreatekeyexa) function to create a key. A registry tree can be 512 levels deep. You can create up to 32 levels at a time through a single registry API call.

An application can use the [**RegCloseKey**](/windows/desktop/api/Winreg/nf-winreg-regclosekey) function to close a key and write the data it contains into the registry. **RegCloseKey** does not necessarily write the data to the registry before returning; it can take as much as several seconds for the cache to be flushed to the hard disk. If an application must explicitly write registry data to the hard disk, it can use the [**RegFlushKey**](/windows/desktop/api/Winreg/nf-winreg-regflushkey) function. **RegFlushKey**, however, uses many system resources and should be called only when absolutely necessary.

 

 



