---
title: IixssoQuery DefineColumn method
description: Defines a new friendly name for a column to be included in queries. By defining an alias for an existing property, you create a shorthand term to refer to it.
ms.assetid: 'ff969b4f-9695-45aa-a522-e702d2a09c46'
keywords: ["DefineColumn method Indexing Service", "DefineColumn method Indexing Service , IixssoQuery interface", "IixssoQuery interface Indexing Service , DefineColumn method"]
topic_type:
- apiref
api_name:
- IixssoQuery.DefineColumn
api_location:
- Ixsso.dll
api_type:
- COM
---

# IixssoQuery::DefineColumn method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Defines a new friendly name for a column to be included in queries. By defining an alias for an existing property, you create a shorthand term to refer to it.

## Syntax


```C++
HRESULT DefineColumn(
  [in] BSTR pwszColDefinition
);
```



## Parameters

<dl> <dt>

*pwszColDefinition* \[in\]
</dt> <dd>

A column definition string. The syntax is as follows:

*fname* \[ ( *type* ) \] = *propset-id* \[ *prop-id* \| " *prop-name* " \]

The components are defined as follows:

<dl> <dt>

<span id="fname"></span><span id="FNAME"></span>*fname*
</dt> <dd>

The friendly name given to the property.

</dd> <dt>

<span id="type"></span><span id="TYPE"></span>*type*
</dt> <dd>

The DBTYPE of the column (used in query restrictions).

</dd> <dt>

<span id="propset-id"></span><span id="PROPSET-ID"></span>*propset-id*
</dt> <dd>

Globally unique identifier (GUID) of the property set ID for the column.

</dd> <dt>

<span id="prop-id"></span><span id="PROP-ID"></span>*prop-id*
</dt> <dd>

The numeric ID of the property ID for the column.

</dd> <dt>

<span id="prop-name"></span><span id="PROP-NAME"></span>*prop-name*
</dt> <dd>

The property name for the column.

</dd> </dl> </dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The *fname* can mask some previously defined or predefined column name. Also, **DefineColumn** can define an alternative friendly name (an alias) for some existing column.

If the **[DefaultColumnFile](defaultcolumnfile.md)** registry value is set, the file named in the setting is read for a set of column definitions available for every query. Otherwise, the column names in [List of Property Names](list-of-property-names-for-a-web-catalog.md) become the default column settings.

## Examples


```VB
strNewColumn = """dc.source.type.category""(dbtype_wstr|dbtype_byref) = CF2EAF90-9311-11CF-BF8C-0020AFE50508 dc.source.type.category"
objQuery.DefineColumn(strNewColumn)
objQuery.Columns = "path, ""dc.source.type.category"""
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoQuery**](iixssoquery.md)
</dt> </dl>

 

 





