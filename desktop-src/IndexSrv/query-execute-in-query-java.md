---
title: Query.Execute in Query.java
description: Query.Execute in Query.java
ms.assetid: '2c8557d2-29bc-4449-be3e-ab19230e3abf'
---

# Query.Execute in Query.java

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment defines the **Execute** method of the **Query** class.


```Java
    void Execute()
    {
        m_RS = new Recordset();
        m_RS.Open( m_SqlText,
                   "provider=MSIDXS",
                   AdoEnums.CursorType.STATIC,
                   AdoEnums.LockType.BATCHOPTIMISTIC,
                   AdoEnums.CommandType.TEXT );
    }
```



The first executable line of the method creates a new ADO [**Recordset**](mdidxrecordsetjavasyntax) object, m\_RS. The next line executes the query in the **m\_SqlText** member with the [**Open**](mdmthrstopen) method of the m\_RS **Recordset** object. The first parameter of the **Open** method is the text of the SQL query. The second parameter sets the data provider to Indexing Service. The subsequent parameters, which are [ADO enumerated constants](mdmscadoenumerations), define the properties of the query.

 

 




