---
title: DBPROPSET\_QUERYEXT
description: DBPROPSET\_QUERYEXT
ms.assetid: 1732d90c-4402-44d4-bea1-dac90b867082
keywords:
- DBPROPSET_QUERYEXT
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBPROPSET\_QUERYEXT

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The DBPROPSET\_QUERYEXT property set contains several settings that give you control over the way Indexing Service satisfies a query.

``` syntax
#define DBPROPSET_QUERYEXT \
    { 0xA7AC77ED, 0xF8D7, 0x11CE, \
        { 0xA7, 0x98, 0x00, 0x20, 0xF8, 0x00, 0x80, 0x25 } }
```

### Remarks

The DBPROPSET\_QUERYEXT property set contains the following property constants.

<dl> <dt>

<span id="DBPROP_USECONTENTINDEX"></span><span id="dbprop_usecontentindex"></span>DBPROP\_USECONTENTINDEX
</dt> <dd>

Property ID 2. When this value is TRUE, all queries use the content index to resolve queries, even if the index is out of date (when there are files waiting to be indexed). This avoids the time-consuming enumeration of all files in a catalog's scopes to resolve the query. It is for use when your application can tolerate resolution of queries using the current state of the index.

</dd> <dt>

<span id="DBPROP_DEFERNONINDEXEDTRIMMING"></span><span id="dbprop_defernonindexedtrimming"></span>DBPROP\_DEFERNONINDEXEDTRIMMING
</dt> <dd>

Property ID 3. When this value is TRUE, Indexing Service first collects the maximum number of hits allowed for a query and then eliminates hits that don't meet the scope or security requirements. This can result in fewer-than-expected hits but better performance.

</dd> <dt>

<span id="DBPROP_USEEXTENDEDDBTYPES"></span><span id="dbprop_useextendeddbtypes"></span>DBPROP\_USEEXTENDEDDBTYPES
</dt> <dd>

Property ID 4. When this value is TRUE, data returned is in [**PROPVARIANT**](_stg_propvariant) structures instead of the default automation **VARIANT** types. This is useful in improving performance because it obviates the need for type conversions. It is unique to OLE DB Provider for Indexing Service.

</dd> </dl>

## Related topics

<dl> <dt>

[OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md)
</dt> <dt>

[**PROPVARIANT**](_stg_propvariant)
</dt> </dl>

 

 




