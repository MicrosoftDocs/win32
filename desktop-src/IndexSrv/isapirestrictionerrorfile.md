---
title: ISAPIRestrictionErrorFile
description: ISAPIRestrictionErrorFile
ms.assetid: 62c21cbb-ea89-467a-af89-96315b762add
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISAPIRestrictionErrorFile

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ISAPIRestrictionErrorFile** entry specifies the full virtual path to the HTML error page returned in response to errors in a query restriction ([CiRestriction](variables-in-forms-and-in-idq-files.md#-idxs-cirestriction-var)).

### Summary



|          |             |
|----------|-------------|
| Type:    | **REG\_SZ** |
| Default: | ""          |



 

### Remarks

The value of the **ISAPIRestrictionErrorFile** entry is the HTML error page that is most often seen by users.

If a value for this entry is not specified, the error page specified by the value of the [ISAPIDefaultErrorFile](isapidefaulterrorfile.md) entry is used.

The variables [CiRestriction](variables-in-forms-and-in-idq-files.md#-idxs-cirestriction-var), [CiErrorMessage](read-only-variables-available-in-htx-files.md#-idxs-cierrormessage-var), and [CiErrorNumber](read-only-variables-available-in-htx-files.md#-idxs-cierrornumber-var) can all be referenced.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[ISAPIDefaultErrorFile](isapidefaulterrorfile.md)
</dt> <dt>

[Language-Specific Registry Entries](language-specific-registry-entries.md)
</dt> </dl>

 

 




