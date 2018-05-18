---
title: ISAPIDefaultErrorFile
description: ISAPIDefaultErrorFile
ms.assetid: 'a540d7d2-a238-4bbd-b0f7-d56c902a2db1'
---

# ISAPIDefaultErrorFile

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ISAPIDefaultErrorFile** entry specifies the full virtual path to the generic error template.

### Summary



|          |             |
|----------|-------------|
| Type:    | **REG\_SZ** |
| Default: | ""          |



 

### Remarks

The value of the **ISAPIDefaultErrorFile** is the .htx template to process when none of the specific HTML error pages ([ISAPIHTXErrorfile](isapihtxerrorfile.md), [ISAPIIDQErrorFile](isapiidqerrorfile.md), [ISAPIRestrictionErrorFile](isapirestrictionerrorfile.md)) apply.

If a value for this entry is not specified, a generic error page is used.

The variables [CiRestriction](variables-in-forms-and-in-idq-files.md#-idxs-cirestriction-var), [CiErrorMessage](read-only-variables-available-in-htx-files.md#-idxs-cierrormessage-var), and [CiErrorNumber](read-only-variables-available-in-htx-files.md#-idxs-cierrornumber-var) can all be referenced.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[ISAPIHTXErrorfile](isapihtxerrorfile.md)
</dt> <dt>

[ISAPIIDQErrorFile](isapiidqerrorfile.md)
</dt> <dt>

[ISAPIRestrictionErrorFile](isapirestrictionerrorfile.md)
</dt> <dt>

[Language-Specific Registry Entries](language-specific-registry-entries.md)
</dt> </dl>

 

 




