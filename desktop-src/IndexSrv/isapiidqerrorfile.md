---
title: ISAPIIDQErrorFile
description: ISAPIIDQErrorFile
ms.assetid: '320ca3a0-a2f7-4245-8541-1e342f58351b'
---

# ISAPIIDQErrorFile

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ISAPIIDQErrorFile** entry specifies the full virtual path to the HTML error page returned in response to errors in the .idq file.

### Summary



|          |             |
|----------|-------------|
| Type:    | **REG\_SZ** |
| Default: | ""          |



 

### Remarks

If a value for the **ISAPIIDQErrorFile** entry is not specified, the error page specified by the value of the [ISAPIDefaultErrorFile](isapidefaulterrorfile.md) entry is used.

The variables [CiRestriction](variables-in-forms-and-in-idq-files.md#-idxs-cirestriction-var), [CiErrorMessage](read-only-variables-available-in-htx-files.md#-idxs-cierrormessage-var), and [CiErrorNumber](read-only-variables-available-in-htx-files.md#-idxs-cierrornumber-var) can all be referenced.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[ISAPIDefaultErrorFile](isapidefaulterrorfile.md)
</dt> <dt>

[Language-Specific Registry Entries](language-specific-registry-entries.md)
</dt> </dl>

 

 




