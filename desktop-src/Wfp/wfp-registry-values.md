---
description: 'WFP registry values are located in the following registry key: HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon.'
ms.assetid: d4da7f24-1e5d-4ea2-98e8-049e7eaefae1
title: WFP Registry Values
ms.topic: article
ms.date: 05/31/2018
---

# WFP Registry Values

\[WFP registry values are not supported as of Windows Vista.\]

WFP uses several registry values for customization settings. The WFP registry values are located in the following registry key:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows NT
            CurrentVersion
               Winlogon
```

The following are the WFP registry values.

<dl> <dt>

<span id="SFCDllCacheDir"></span><span id="sfcdllcachedir"></span><span id="SFCDLLCACHEDIR"></span>**SFCDllCacheDir**
</dt> <dd>

Location of the cache. This must be a local path. The default value is %systemroot%\\system32\\dllcache.

</dd> <dt>

<span id="SFCQuota"></span><span id="sfcquota"></span><span id="SFCQUOTA"></span>**SFCQuota**
</dt> <dd>

Quota options. This registry value can be one of the following values.



| Value                  | Meaning                                                  |
|------------------------|----------------------------------------------------------|
| SFC\_QUOTA\_ALL\_FILES | Size of the DLL cache is unlimited. This is the default. |
| Other values           | Size of the DLL cache, in files.                         |



 

</dd> <dt>

<span id="SFCScan"></span><span id="sfcscan"></span><span id="SFCSCAN"></span>**SFCScan**
</dt> <dd>

Scan options. This registry value can be one of the following values.



| Value             | Meaning                                                   |
|-------------------|-----------------------------------------------------------|
| SFC\_SCAN\_NORMAL | Do not scan protected files at boot. This is the default. |
| SFC\_SCAN\_ALWAYS | Scan protected files at every boot.                       |
| SFC\_SCAN\_ONCE   | Scan protected files at the next boot.                    |



 

</dd> </dl>

 

 



