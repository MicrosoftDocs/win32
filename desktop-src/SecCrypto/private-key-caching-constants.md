---
description: Used to represent registry entries that control private key caching by Microsoft software-based CSPs.
ms.assetid: 67909072-72fe-4777-ae52-a7b9047c9dd5
title: Private Key Caching Constants (Wincrypt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Private Key Caching Constants

The following constants are used to represent registry entries that control [*private key*](../secgloss/p-gly.md) caching by Microsoft software-based CSPs.



| Constant/value                                                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| <span id="szKEY_CRYPTOAPI_PRIVATE_KEY_OPTIONS"></span><span id="szkey_cryptoapi_private_key_options"></span><span id="SZKEY_CRYPTOAPI_PRIVATE_KEY_OPTIONS"></span><dl> <dt>**szKEY\_CRYPTOAPI\_PRIVATE\_KEY\_OPTIONS**</dt> <dt>"Software\\\\Policies\\\\Microsoft\\\\Cryptography"</dt> </dl> | The path, under the **HKEY\_LOCAL\_MACHINE** root, of the private key caching registry entries.<br/> |



The following constants are used to identify registry values that control private key caching globally for a specific process by Microsoft software-based CSPs.



| Constant/value                                                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="szPRIV_KEY_CACHE_MAX_ITEMS"></span><span id="szpriv_key_cache_max_items"></span><span id="SZPRIV_KEY_CACHE_MAX_ITEMS"></span><dl> <dt>**szPRIV\_KEY\_CACHE\_MAX\_ITEMS**</dt> <dt>"PrivKeyCacheMaxItems"</dt> </dl>                                                                  | A **REG\_DWORD** value under the **szKEY\_CRYPTOAPI\_PRIVATE\_KEY\_OPTIONS** registry key that specifies the maximum number of private keys that can be cached at one time for a single process. This check is performed whenever a stored private key is read. If the maximum number is exceeded, the least recently used key is removed from the cache.<br/> If this value is zero, no keys are cached. If this value is not present, the **cPRIV\_KEY\_CACHE\_MAX\_ITEMS\_DEFAULT** value is used as the default.<br/> If a private key that is deleted from the cache is currently referenced in an open context, then the key is read from storage the next time an attempt is made to use the key.<br/> **Windows Server 2003 and Windows XP with SP1 and earlier:** This registry value is not supported.<br/>                                  |
| <span id="cPRIV_KEY_CACHE_MAX_ITEMS_DEFAULT"></span><span id="cpriv_key_cache_max_items_default"></span><span id="CPRIV_KEY_CACHE_MAX_ITEMS_DEFAULT"></span><dl> <dt>**cPRIV\_KEY\_CACHE\_MAX\_ITEMS\_DEFAULT**</dt> <dt>20</dt> </dl>                                                         | The default value of the **szPRIV\_KEY\_CACHE\_MAX\_ITEMS** registry entry if no value is specified.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="szPRIV_KEY_CACHE_PURGE_INTERVAL_SECONDS"></span><span id="szpriv_key_cache_purge_interval_seconds"></span><span id="SZPRIV_KEY_CACHE_PURGE_INTERVAL_SECONDS"></span><dl> <dt>**szPRIV\_KEY\_CACHE\_PURGE\_INTERVAL\_SECONDS**</dt> <dt>"PrivKeyCachePurgeIntervalSeconds"</dt> </dl> | A **REG\_DWORD** value under the **szKEY\_CRYPTOAPI\_PRIVATE\_KEY\_OPTIONS** registry key that specifies the maximum age, in seconds, of any cached private key. This check is performed whenever a stored private key is used or read. If this amount of time has elapsed since the last clearing occurred, all cached keys that have not been referenced since the last clearing will be removed from the cache.<br/> If this value is not present, the **cPRIV\_KEY\_CACHE\_PURGE\_INTERVAL\_SECONDS\_DEFAULT** value is used as the default.<br/> If a private key that is cleared from the cache is currently referenced in an open context, then the key will be read from storage the next time an attempt is made to use the key.<br/> **Windows Server 2003 and Windows XP with SP1 and earlier:** This registry value is not supported.<br/> |
| <span id="cPRIV_KEY_CACHE_PURGE_INTERVAL_SECONDS_DEFAULT"></span><span id="cpriv_key_cache_purge_interval_seconds_default"></span><span id="CPRIV_KEY_CACHE_PURGE_INTERVAL_SECONDS_DEFAULT"></span><dl> <dt>**cPRIV\_KEY\_CACHE\_PURGE\_INTERVAL\_SECONDS\_DEFAULT**</dt> <dt>86400</dt> </dl> | The default value of the **szPRIV\_KEY\_CACHE\_PURGE\_INTERVAL\_SECONDS** registry entry if no value is specified. This value is equivalent to one day.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |



The following constants are used to identify registry values that control private key caching for a single Microsoft software-based [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) instance.



| Constant/value                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>"AllowCachePW"</dt> </dl>                                                                                                                                                         | A **REG\_DWORD** value under the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Cryptography\\Protect** registry key that specifies whether password caching is enabled for password-protected keys in the Microsoft software-based CSPs. If this value is 0, then password caching is disabeld and the user is prompted for the password every time a password-protected key is used. Any other value, or the absence of this value, indicates that the password will be cached. In this scenario, the user is only prompted once per process for each such key. <br/> |
| <span id="szKEY_CACHE_ENABLED"></span><span id="szkey_cache_enabled"></span><span id="SZKEY_CACHE_ENABLED"></span><dl> <dt>**szKEY\_CACHE\_ENABLED**</dt> <dt>"CachePrivateKeys"</dt> </dl>          | A **REG\_DWORD** value under the **szKEY\_CRYPTOAPI\_PRIVATE\_KEY\_OPTIONS** registry key that specifies whether private key caching is enabled. If this value is 1, then private key caching is enabled. Any other value, or the absence of this value, indicates that private key caching is disabled.<br/> **Windows Vista with SP1, Windows Vista and Windows XP:** This registry value is not supported.<br/>                                                                                                                                                        |
| <span id="szKEY_CACHE_SECONDS"></span><span id="szkey_cache_seconds"></span><span id="SZKEY_CACHE_SECONDS"></span><dl> <dt>**szKEY\_CACHE\_SECONDS**</dt> <dt>"PrivateKeyLifetimeSeconds"</dt> </dl> | A **REG\_DWORD** value under the **szKEY\_CRYPTOAPI\_PRIVATE\_KEY\_OPTIONS** registry key that specifies the maximum age, in seconds, of any cached private key.<br/> **Windows XP:** This registry value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                          |



## Remarks

The differences between the **szKEY\_CACHE\_SECONDS** and the **szPRIV\_KEY\_CACHE\_PURGE\_INTERVAL\_SECONDS** values are as follows:

 **szKEY\_CACHE\_SECONDS**  

-   This value only applies to a specific CSP. After the CSP is released, the CSP's cache is released as well.  
-   This value is only applied when an attempt is made to use a specific private key with a specific context handle.  

**szPRIV\_KEY\_CACHE\_PURGE\_INTERVAL\_SECONDS**  

-   This value applies to all CSPs in a process. Even if the CSP is released, this cache is not released.  
-   This value applies whenever any stored private key is used or read from storage in a single process.  



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



 

 
