---
title: IixssoQuery CreateRecordset method
description: Executes a query and creates an ADO recordset to navigate through query results.
ms.assetid: 'c79f62c2-21d3-4b62-928f-80012329a7ca'
keywords: ["CreateRecordset method Indexing Service", "CreateRecordset method Indexing Service , IixssoQuery interface", "IixssoQuery interface Indexing Service , CreateRecordset method"]
topic_type:
- apiref
api_name:
- IixssoQuery.CreateRecordset
api_location:
- Ixsso.dll
api_type:
- COM
---

# IixssoQuery::CreateRecordset method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Executes a query and creates an ADO recordset to navigate through query results.

## Syntax


```C++
HRESULT CreateRecordset(
  [in]          BSTR      pwszSequential,
  [out, retval] IDispatch *ppDisp
);
```



## Parameters

<dl> <dt>

*pwszSequential* \[in\]
</dt> <dd>

Either "sequential" or "nonsequential" to create an [**IRowset**](b14147c4-8b03-49c6-ab5d-00186643a6b4) (sequential) or an [**IRowsetScroll**](3319b1ef-736c-41da-a09b-aaf9e239b69c) (nonsequential) recordset.

</dd> <dt>

*ppDisp* \[out, retval\]
</dt> <dd>

The ADO recordset object for iterating the results of a query.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Before calling **CreateRecordset**, you must set any required parameters for a query, such as the [**Query**](iixssoquery-query.md) property and the [**Columns**](iixssoquery-columns.md) property.

## Examples


```VB
' Create a sequential recordset
objQuery.Query = "$contents " & chr(34) & SrchStr & chr(34)"
objQuery.Columns = "DocTitle, VPath, Characterization, HitCount"
Set objRecordset = objQuery.CreateRecordset("sequential")
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

 

 





