---
description: Extends properties defined for the Rowset APIs.
ms.assetid: C1A2DF19-C68D-42CC-9CB2-190F22CB4158
title: DBPROPSET_MSIDXS_ROWSETEXT
ms.topic: article
ms.date: 05/31/2018
---

# DBPROPSET\_MSIDXS\_ROWSETEXT

Extends properties defined for the Rowset APIs.

``` syntax
#define DBPROPSET_MSIDXS_ROWSETEXT \
    { 0xaa6ee6b0, 0xe828, 0x11d0, \
        { 0xb2, 0x3e, 0x00, 0xaa, 0x00, 0x47, 0xfc, 0x01 } }
```

The DBPROPSET\_MSIDXS\_ROWSETEXT property set contains the following property constants:

<dl> <dt>

<span id="MSIDXSPROP_ROWSETQUERYSTATUS"></span><span id="msidxsprop_rowsetquerystatus"></span>MSIDXSPROP\_ROWSETQUERYSTATUS
</dt> <dd>

Property ID 2. Query status for the rowset. The STAT\_\* constants indicate the execution and reliability status.

</dd> <dt>

<span id="MSIDXSPROP_COMMAND_LOCALE_STRING"></span><span id="msidxsprop_command_locale_string"></span>MSIDXSPROP\_COMMAND\_LOCALE\_STRING
</dt> <dd>

Property ID 3. Locale string that represents the language and locale setting to use for this rowset.

</dd> <dt>

<span id="MSIDXSPROP_QUERY_RESTRICTION"></span><span id="msidxsprop_query_restriction"></span>MSIDXSPROP\_QUERY\_RESTRICTION
</dt> <dd>

Property ID 4. The query string associated with this rowset.

</dd> <dt>

<span id="MSIDXSPROP_PARSE_TREE"></span><span id="msidxsprop_parse_tree"></span>MSIDXSPROP\_PARSE\_TREE
</dt> <dd>

Property ID 5.

</dd> <dt>

<span id="MSIDXSPROP_MAX_RANK___"></span><span id="msidxsprop_max_rank___"></span>MSIDXSPROP\_MAX\_RANK 
</dt> <dd>

Property ID 6.

</dd> <dt>

<span id="MSIDXSPROP_RESULTS_FOUND"></span><span id="msidxsprop_results_found"></span>MSIDXSPROP\_RESULTS\_FOUND
</dt> <dd>

Property ID 7.

</dd> <dt>

<span id="MSIDXSPROP_WHEREID"></span><span id="msidxsprop_whereid"></span>MSIDXSPROP\_WHEREID
</dt> <dd>

Property ID 8.

</dd> <dt>

<span id="MSIDXSPROP_SERVER_VERSION_"></span><span id="msidxsprop_server_version_"></span>MSIDXSPROP\_SERVER\_VERSION 
</dt> <dd>

New for Windows 7. Property ID 9. The server version.

</dd> <dt>

<span id="MSIDXSPROP_SERVER_WINVER_MAJOR"></span><span id="msidxsprop_server_winver_major"></span>MSIDXSPROP\_SERVER\_WINVER\_MAJOR
</dt> <dd>

Property ID 10.

</dd> <dt>

<span id="MSIDXSPROP_SERVER_WINVER_MINOR"></span><span id="msidxsprop_server_winver_minor"></span>MSIDXSPROP\_SERVER\_WINVER\_MINOR
</dt> <dd>

Property ID 11.

</dd> <dt>

<span id="MSIDXSPROP_SERVER_NLSVERSION"></span><span id="msidxsprop_server_nlsversion"></span>MSIDXSPROP\_SERVER\_NLSVERSION
</dt> <dd>

Property ID 12.

</dd> <dt>

<span id="MSIDXSPROP_SERVER_NLSVER_DEFINED_"></span><span id="msidxsprop_server_nlsver_defined_"></span>MSIDXSPROP\_SERVER\_NLSVER\_DEFINED 
</dt> <dd>

Property ID 13.

</dd> <dt>

<span id="MSIDXSPROP_SAME_SORTORDER_USED_"></span><span id="msidxsprop_same_sortorder_used_"></span>MSIDXSPROP\_SAME\_SORTORDER\_USED 
</dt> <dd>

Property ID 14.

</dd> </dl>

## Remarks

To query MSIDXSPROP\_SERVER\_VERSION, it is necessary to issue the dummy query to server, such as the following example.

`SELECT top 1 workid from servername.systemindex`

After the rowset has been returned, call [**IUnknown::QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) for the capabilities of the rowset and then call [IRowsetInfo::GetProperties](/previous-versions/windows/desktop/ms719611(v=vs.85)) for the new property (MSIDXSPROP\_SERVER\_VERSION). The property has a type of **VT\_I4** and can be one of the following values:

\#define CI\_VERSION\_WDS30 0x102 // 258

\#define CI\_VERSION\_WDS40 0x109 // 265

\#define CI\_VERSION\_WIN70 0x700 // 1792

Once the value is known, the client can form a query which is supported by the server and issue a real query.

DBPROPSET\_MSIDXS\_ROWSETEXT is declared in ntquery.h.

 

 
