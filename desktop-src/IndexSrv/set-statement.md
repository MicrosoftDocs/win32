---
title: SET Statement
description: SET Statement
ms.assetid: cf4483f5-c0f3-45b7-8e29-6fcc6c6d0117
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SET Statement

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **SET** statement maps column names to property IDs and GUIDs (**SET PROPERTYNAME**) or selects a ranking method for content searches (**SET RANKMETHOD**) for the duration of a session with Indexing Service.

``` syntax
SET Set_Property_Name_Clause | Set_Rank_Method_Clause
```

### Parameters

<dl> <dt>

<span id="Set_Property_Name_Clause"></span><span id="set_property_name_clause"></span><span id="SET_PROPERTY_NAME_CLAUSE"></span>*Set\_Property\_Name\_Clause*
</dt> <dd>

Specifies an association of a property set with a friendly name (column alias) and a data type. For details about this parameter, see [SET PROPERTYNAME](set-propertyname.md).

</dd> <dt>

<span id="Set_Rank_Method_Clause"></span><span id="set_rank_method_clause"></span><span id="SET_RANK_METHOD_CLAUSE"></span>*Set\_Rank\_Method\_Clause*
</dt> <dd>

Sets the ranking method to use when issuing [Weighted Match](https://www.bing.com/search?q=Weighted Match) (**ISABOUT**) queries. For details about this parameter, see [SET RANKMETHOD](set-rankmethod.md).

</dd> </dl>

### Remarks

You typically use a series of **SET** statements to define your friendly names for columns and the ranking method, prior to executing subsequent **SELECT** statements.

The assigning of aliases done with **SET** is similar to that in the \[Names\] section of the Indexing Service [Internet Data Query (.idq) files](internet-data-query-files.md), where you can define "friendly" column names for use in queries.

## Related topics

<dl> <dt>

[Batched Statements](batched-statements.md)
</dt> <dt>

[SET PROPERTYNAME](set-propertyname.md)
</dt> <dt>

[SET RANKMETHOD](set-rankmethod.md)
</dt> </dl>

 

 




