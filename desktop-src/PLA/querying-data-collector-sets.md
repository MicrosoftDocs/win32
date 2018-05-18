---
title: Querying Data Collector Sets
description: Data collector sets are saved to disk when you call the IDataCollectorSet Commit method.
ms.assetid: '45412b36-5c2b-4113-89c7-69ccc83fb757'
---

# Querying Data Collector Sets

Data collector sets are saved to disk when you call the [**IDataCollectorSet::Commit**](idatacollectorset-commit.md) method. To retrieve a saved data collector set, call the [**IDataCollectorSet::Query**](idatacollectorset-query.md) method. For an example that shows how to use the **Query** method, see [Querying a Data Collector Set](querying-a-data-collector-set.md).

To retrieve all saved data collector sets on a computer or sets from a specific namespace on a computer, call the [**IDataCollectorSetCollection::GetDataCollectorSets**](idatacollectorsetcollection-getdatacollectorsets.md) method. For an example that shows how to use the **GetDataCollectorSets** method, see [Querying All Data Collector Sets](querying-all-data-collector-sets.md).

 

 




