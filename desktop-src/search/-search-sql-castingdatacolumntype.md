---
description: "Learn more about: Casting the Data Type of a Column"
ms.assetid: 78a137a9-ef69-4ce3-8a96-73e722951300
title: Casting the Data Type of a Column
ms.topic: article
ms.date: 05/31/2018
---

# Casting the Data Type of a Column

At times you may need to cast string data extracted from documents as another data type, so that an appropriate comparison can be made. Cast an identifier or literal as another data type using the following syntax:


```
CAST (<identifier> | <literal> AS <datatype>)
```



For example:


```
CAST ('10000' AS DBTYPE_I4)
            
CAST (System.DateCreated AS DBTYPE_WSTR)
```



## Related topics

<dl> <dt>

[Data Type Mappings](-search-sql-datatypemappings.md)
</dt> </dl>

 

 



