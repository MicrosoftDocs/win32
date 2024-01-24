---
description: 'Schema association queries use the same statements as are used in data association queries: ASSOCIATORS OF and REFERENCES OF.'
ms.assetid: b5fc2d86-702a-42cd-82e6-f15c905ba6aa
ms.tgt_platform: multiple
title: Schema Associations
ms.topic: article
ms.date: 05/31/2018
---

# Schema Associations

Schema association queries use the same statements as are used in data association queries: ASSOCIATORS OF and REFERENCES OF. However, with data association queries, class instances are returned, and with schema association queries, names of classes that can participate in association relationships are returned. For example, use a schema query to find all of the association classes defined in the schema that reference a source class.

The syntax for the ASSOCIATORS OF and REFERENCES OF statements is the same for schema association queries as it is for data association queries with the following exceptions:

-   The source object is a class rather than an instance.
-   There is an additional keyword, **SchemaOnly**, which identifies the query as applying to a schema rather than to data.
-   The **ClassDefsOnly** keyword is not valid.

The following example shows the complete syntax of the ASSOCIATORS OF statement for a schema query. For detailed syntax, see [ASSOCIATORS OF Statement](associators-of-statement.md).


```sql
ASSOCIATORS OF {SourceClass} WHERE 
    AssocClass = AssocClassName
    RequiredAssocQualifier = QualifierName
    RequiredQualifier = QualifierName
    ResultClass = ClassName
    ResultRole = PropertyName
    Role = PropertyName
    SchemaOnly
```



The following example shows a query that returns the **Protocol** and **Driver** classes, the two classes that refer to the source class.


```sql
ASSOCIATORS OF {Adapter} WHERE SchemaOnly
```



The following query returns only the **Driver** class because of the restriction placed by the **AssocClass** keyword.


```sql
ASSOCIATORS OF {Adapter} WHERE AssocClass = AdapterDriver SchemaOnly
```



The complete syntax of the REFERENCES OF statement for a schema query is as follows. For detailed syntax, see [REFERENCES OF Statement](references-of-statement.md).


```sql
REFERENCES OF {SourceClass} WHERE
    ResultClass = ClassName
    Role = PropertyName
    RequiredQualifier = QualifierName
    SchemaOnly
```



> [!Note]  
> Schema association queries may return duplicate objects.

 

For example, the following query will return the class [**CIM\_ComputerSystem**](/windows/desktop/CIMWin32Prov/cim-computersystem) several times when enumerating classes in the **root\\cimv2** namespace.


```sql
ASSOCIATORS OF {Win32_ComputerSystem} WHERE SchemaOnly
```



 

 
