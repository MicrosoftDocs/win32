---
Description: PSGUID\_QUERY
ms.assetid: 7549f814-85c4-4dec-a2d1-083d69309ce6
title: PSGUID\_QUERY
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PSGUID\_QUERY

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The PSGUID\_QUERY property set contains query properties computed or made available by the query engine in Indexing Service.

``` syntax
extern const GUID PSGUID_QUERY = {0x49691c90,0x7e17,0x101a,{0xa9,0x1c,0x08,0x00,0x2b,0x2e,0xcd,0xa9}};
```

### Remarks

The PSGUID\_QUERY property set contains the following property constants:

<dl> <dt>

<span id="PROPID_QUERY_RANKVECTOR"></span><span id="propid_query_rankvector"></span>PROPID\_QUERY\_RANKVECTOR
</dt> <dd>

Property ID 2. The array of ranks for each term in a vector query. Default type is VT\_VECTOR \| VT\_UI4. The Indexing Service friendly name is "rankvector".

</dd> <dt>

<span id="PROPID_QUERY_RANK"></span><span id="propid_query_rank"></span>PROPID\_QUERY\_RANK
</dt> <dd>

Property ID 3. A file's rank, which indicates how well the query matched the file. This value is between zero and 1000. Default type is VT\_I4. The Indexing Service friendly name is "rank".

</dd> <dt>

<span id="PROPID_QUERY_HITCOUNT"></span><span id="propid_query_hitcount"></span>PROPID\_QUERY\_HITCOUNT
</dt> <dd>

Property ID 4. The count of query hits in a file. Default type is VT\_I4. The Indexing Service friendly name is "hitcount".

</dd> <dt>

<span id="PROPID_QUERY_WORKID"></span><span id="propid_query_workid"></span>PROPID\_QUERY\_WORKID
</dt> <dd>

Property ID 5. Value used to track objects.

</dd> <dt>

<span id="PROPID_QUERY_ALL"></span><span id="propid_query_all"></span>PROPID\_QUERY\_ALL
</dt> <dd>

Property ID 6. Refers to all properties of the file. This property is for query restrictions only; it cannot be retrieved in a query result. Default type is VT\_LPWSTR. The Indexing Service friendly name is "all".

</dd> <dt>

<span id="PROPID_QUERY_UNFILTERED"></span><span id="propid_query_unfiltered"></span>PROPID\_QUERY\_UNFILTERED
</dt> <dd>

Property ID 7. Filtered state of the file. Default type is VT\_BOOL. There is no Indexing Service name for this property; it must be defined manually.

</dd> <dt>

<span id="PROPID_QUERY_VIRTUALPATH"></span><span id="propid_query_virtualpath"></span>PROPID\_QUERY\_VIRTUALPATH
</dt> <dd>

Property ID 9. The Internet Information Services (IIS) virtual path of a file. The path can be in the World Wide Web (WWW), Network News Transfer Protocol (NNTP), or Internet Message Access Protocol (IMAP) namespaces. Default type is VT\_LPWSTR. The Indexing Service friendly name is "vpath".

</dd> <dt>

<span id="PROPID_QUERY_LASTSEENTIME"></span><span id="propid_query_lastseentime"></span>PROPID\_QUERY\_LASTSEENTIME
</dt> <dd>

Property ID 10. Time-stamp value used for caching queries.

</dd> </dl>

## Related topics

<dl> <dt>

[OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md)
</dt> </dl>

 

 



