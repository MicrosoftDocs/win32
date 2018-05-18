---
title: DLLsToRegister
description: DLLsToRegister
ms.assetid: 'aaf7ab48-1db5-4485-9512-0d2ce824ff9e'
---

# DLLsToRegister

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DLLsToRegister** entry determines which DLLs Indexing Service registers with a call to [**DllRegisterServer**](_com_dllregisterserver).

### Summary



|          |                                                                                                                           |
|----------|---------------------------------------------------------------------------------------------------------------------------|
| Type:    | **REG\_MULTI\_SZ**                                                                                                        |
| Default: | In the system default directory, QUERY.DLL, CIADMIN.DLL, IXSSO.DLL, CIODM.DLL, INFOSOFT.DLL, NLHTML.DLL, and OFFFILT.DLL. |
| Range:   | May include any filter DLLs, including ones supplied by independent software vendors.                                     |



 

### Remarks

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




