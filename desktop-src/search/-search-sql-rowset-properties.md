---
description: After a result is returned from a query, you can access several properties for the rowset.
ms.assetid: 71aa0ad6-ef34-47ee-945f-04bda20bf8a4
title: Rowset Properties
ms.topic: article
ms.date: 05/31/2018
---

# Rowset Properties

After a result is returned from a query, you can access several properties for the rowset.

In addition to the standard OLE-DB rowset properties, Windows Search SQL offers the following four custom properties. The GUID for this property set is {AA6EE6B0E828-11D0-B23E-00AA0047FC01}.

Windows Search supports the standard OLE-DB property DBPROP\_COMMANDTIMEOUT of the [DBPROPSET\_ROWSET](/previous-versions//ms691738(v=vs.85)) property set.



| Property name                  | PROPID/type | Description                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DONOTCOMPUTEEXPENSIVEPROPS     | 15/VT\_BOOL | Setting this to true prevents computing expensive properties like Results Found and Max Rank that require evaluating the whole query when any rowset property is accessed.                                                                                                                                                                         |
| Maximum Rank (MAX\_RANK)       | 6/VT\_I4    | The highest rank computed for any result.                                                                                                                                                                                                                                                                                                          |
| Results Found (RESULTS\_FOUND) | 7/VT\_I4    | The total number of unique items for this query. For a SELECT query, this is the number of items in the rowset. For a GROUP ON query, this is the number of unique leaf items. This property does not identify the number of rows in the top-level rowset (the number of top-level groups).                                                        |
| Where ID (WHEREID)             | 8/VT\_I4    | The identifier for the restrictions used for a query. If a rowset is open when a new query is executed, the new query can reuse the restrictions from the older query, thereby taking advantage of the work already completed. For more information on reusing WHERE restrictions, refer to the [ReuseWhere function](-search-sql-reusewhere.md). |



 

## Related topics

<dl> <dt>

[Indexing Prioritization and Rowset Events in Windows 7](indexing-prioritization-and-rowset-events.md)
</dt> </dl>

 

 
