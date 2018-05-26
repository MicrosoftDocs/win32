---
title: Querying Data Collector Sets
description: Data collector sets are saved to disk when you call the IDataCollectorSet Commit method.
ms.assetid: 45412b36-5c2b-4113-89c7-69ccc83fb757
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Querying Data Collector Sets

Data collector sets are saved to disk when you call the [**IDataCollectorSet::Commit**](/windows/previous-versions/Pla/nf-pla-idatacollectorset-commit?branch=master) method. To retrieve a saved data collector set, call the [**IDataCollectorSet::Query**](/windows/previous-versions/Pla/nf-pla-idatacollectorset-query?branch=master) method. For an example that shows how to use the **Query** method, see [Querying a Data Collector Set](querying-a-data-collector-set.md).

To retrieve all saved data collector sets on a computer or sets from a specific namespace on a computer, call the [**IDataCollectorSetCollection::GetDataCollectorSets**](/windows/previous-versions/Pla/nf-pla-idatacollectorsetcollection-getdatacollectorsets?branch=master) method. For an example that shows how to use the **GetDataCollectorSets** method, see [Querying All Data Collector Sets](querying-all-data-collector-sets.md).

 

 




