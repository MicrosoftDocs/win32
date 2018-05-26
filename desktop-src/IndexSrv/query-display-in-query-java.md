---
title: Query.Display in Query.java
description: Query.Display in Query.java
ms.assetid: ab67ea53-e41b-4c63-a406-5815b171c5f9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Query.Display in Query.java

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment displays the results of the query. It gets the count of the number of fields in the m\_RS [**Recordset**](mdidxrecordsetjavasyntax) object and then reads through the **Recordset** object, printing the values of the fields, until it encounters an end of file.


```Java
    void Display( PrintStream PS )
...
            int cFields = m_RS.getFields().getCount();

            while ( !m_RS.getEOF() )
            {
                for ( int j = 0; j < cFields; j++ )
                    PS.print( m_RS.getFields().getItem(j).getValue() + "\t" );

                PS.print( "\n" );

                m_RS.moveNext();
            }
...
```



 

 




