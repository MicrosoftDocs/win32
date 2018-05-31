---
title: IixssoQuery OptimizeFor property
description: Controls whether queries are optimized for better performance or for a greater number of hits.
ms.assetid: 1fb853da-0e7a-4330-b722-346fcc469d78
keywords:
- OptimizeFor property Indexing Service
- OptimizeFor property Indexing Service , IixssoQuery interface
- IixssoQuery interface Indexing Service , OptimizeFor property
topic_type:
- apiref
api_name:
- IixssoQuery.OptimizeFor
- IixssoQuery.get_OptimizeFor
- IixssoQuery.put_OptimizeFor
api_location:
- Ixsso.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoQuery::OptimizeFor property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Controls whether queries are optimized for better performance or for a greater number of hits.

This property is read/write.

## Syntax


```C++
HRESULT put_OptimizeFor(
  [in]          BSTR val
);

HRESULT get_OptimizeFor(
  [out, retval] BSTR *val
);
```



## Property value

Specifies a string that has the following syntax:

"performance" \| "recall" \[, "hitcount" \| "nohitcount" \]

These components have the following effect:

<dl> <dt>

<span id="_performance_____recall_"></span><span id="_PERFORMANCE_____RECALL_"></span>"performance" \| "recall"
</dt> <dd>

The default is "recall". If "performance", Indexing Service first collects the maximum number of hits and then eliminates hits that don't meet the scope or security requirements.

> [!Note]  
> Optimizing for performance may result in less than the expected number of hits for queries in which scope checks or security checks remove hits.

 

</dd> <dt>

<span id="_hitcount_____nohitcount_"></span><span id="_HITCOUNT_____NOHITCOUNT_"></span>"hitcount" \| "nohitcount"
</dt> <dd>

The defaults is "nohitcount". This controls whether to request the Hitcount property, which represents the total number of hits matching the query, from the ADO query property collection. This property is a custom property supported by the OLE DB provider, accessed through the query object property set.

The "hitcount" and "nohitcount" options are not implemented for Indexing Service for Windows. It is used exclusively in the implementation of Indexing Service for Microsoft Site Server.

</dd> </dl>

## Remarks

If you choose the performance option, scope and security trimming are deferred until after the maximum number of hits is collected. If the option is set to recall, the result set trimming occurs while executing the query. The default is to optimize for recall.

For Web clients, the query string variable URLs associated with this property is op.

In former releases of Indexing Service, this property replaces the .idq parameter CiDeferNonIndexedTrimming.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoQuery**](iixssoquery.md)
</dt> </dl>

 

 





