---
title: BcdLibrary\_SafeBoot enumeration
description: Specifies the safe boot options.
ms.assetid: 1739c0bd-6957-44de-8214-a4da9f9fc7df
keywords:
- BcdLibrary_SafeBoot enumeration Boot Config
topic_type:
- apiref
api_name:
- BcdLibrary_SafeBoot
api_type:
- NA
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BcdLibrary\_SafeBoot enumeration

Specifies the safe boot options.

## Syntax


```C++
typedef enum BcdLibrary_SafeBoot { 
  SafemodeMinimal   = 0,
  SafemodeNetwork   = 1,
  SafemodeDsRepair  = 2
} BcdLibrary_SafeBoot;
```



## Constants

<dl> <dt>

<span id="SafemodeMinimal"></span><span id="safemodeminimal"></span><span id="SAFEMODEMINIMAL"></span>**SafemodeMinimal**
</dt> <dd>

Load the drivers and services specified by name or group under the following registry key: **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Minimal**.

</dd> <dt>

<span id="SafemodeNetwork"></span><span id="safemodenetwork"></span><span id="SAFEMODENETWORK"></span>**SafemodeNetwork**
</dt> <dd>

Load the drivers and services specified by name or group under the following registry key: **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Network**

</dd> <dt>

<span id="SafemodeDsRepair"></span><span id="safemodedsrepair"></span><span id="SAFEMODEDSREPAIR"></span>**SafemodeDsRepair**
</dt> <dd>

Boot the system into a repair mode that restores the Active Directory service from backup medium.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[BCD WMI Provider Enumerations](bcd-enumerations.md)
</dt> <dt>

[**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)
</dt> </dl>

 

 





