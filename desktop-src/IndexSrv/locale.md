---
title: Locale
description: Locale
ms.assetid: 'a7bf3d15-4532-4719-b50d-a35ff10c3482'
---

# Locale

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **Locale** entry specifies the LCID used for the language represented by the language subkey.

### Summary



|        |                                                                                           |
|--------|-------------------------------------------------------------------------------------------|
| Type:  | **REG\_DWORD**                                                                            |
| Range: | Any LCID made from a language identifier using the [**MAKELCID**](_win32_makelcid) macro. |



 

### Remarks

The Indexing Service ISAPI implementation variable [CiLocale](variables-in-forms-and-in-idq-files.md#-idxs-cilocale-var) selects a language subkey to use with a specific query.

## Related topics

<dl> <dt>

[Language-Specific Registry Entries](language-specific-registry-entries.md)
</dt> <dt>

[MAKELCID](_win32_makelcid)
</dt> </dl>

 

 




