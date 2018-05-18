---
title: IsapiDefaultCatalogDirectory
description: IsapiDefaultCatalogDirectory
ms.assetid: '9a9ad9fa-bb8d-4f72-96ae-28680fb101b7'
---

# IsapiDefaultCatalogDirectory

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsapiDefaultCatalogDirectory** entry sets the default Indexing Service catalog name as it would be entered in the [CiCatalog](variables-in-forms-and-in-idq-files.md#-idxs-cicatalog-var) entry of an .idq file.

### Summary



|          |             |
|----------|-------------|
| Type:    | **REG\_SZ** |
| Default: | "System"    |



 

### Remarks

The value of the **IsapiDefaultCatalogDirectory** entry is also used by the [**Query**](iixssoquery.md) object when the [**Query.Catalog**](iixssoquery-catalog.md) property is not set.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




