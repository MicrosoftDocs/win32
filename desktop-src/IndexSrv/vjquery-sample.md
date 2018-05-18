---
title: VJQuery Sample
description: VJQuery Sample
ms.assetid: '4eb99de1-1c3a-4ce5-a230-8b73a5c8ba24'
---

# VJQuery Sample

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The VJQuery sample is an example command-line application written in Microsoft Visual J++ that illustrates how to query Indexing Service using a SQL query language and the [ActiveX Data Objects (ADO) API](programming-apis.md#-idxs-activex-data-objects-api).

Source: mssdk\\samples\\winbase\\indexing\\VJQuery\\

**To build the sample**

1.  In the Visual J++ development environment, open the VJQuery.vjp project from the source path of the sample.
2.  In the **Build** menu, select **Build**.

**To execute a default query using the sample**

1.  Make sure that Indexing Service is started.
2.  In the **Debug** menu, select **Start**.
3.  In the JView window, read the results of the default SQL query
    ```
    SELECT Filename, Size, Write, Path
      FROM SCOPE('DEEP TRAVERSAL OF "\"')
      WHERE CONTAINS('"Indexing Service"')
    ```

    

**To specify a complete SQL statement for a query using the sample**

1.  Make sure that Indexing Service is started.
2.  Set the *PATH* environment variable to include "D:\\mssdk\\Bin", where D: is the drive on which you installed the Platform SDK.
3.  Open a command window and change the directory to the path of the built sample.
4.  Formulate a query that you know will succeed. You need to know the machine, catalog, scope, and query text.
5.  Submit a complete SQL statement by entering, at the command-line prompt, **jview /p /cp:p "&lt;JAVAPACKAGES&gt;" VJQuery -s &lt;Statement&gt;**

    where &lt;Statement&gt; is a complete SQL statement such as the default SQL query in the preceding section. You must escape any double-quote characters in the text of the &lt;Statement&gt; parameter.

**To specify only a WHERE clause for a query using the sample**

1.  Make sure that Indexing Service is started.
2.  Set the *PATH* environment variable to include "D:\\mssdk\\Bin", where D: is the drive on which you installed the Platform SDK.
3.  Open a command window and change the directory to the path of the built sample.
4.  Formulate a query that you know will succeed. You need to know values for the machine, catalog, scope, and query text.
5.  Submit text for a [WHERE](where-clause.md) clause that is concatenated to the following incomplete, fixed SQL statement

    ```
    SELECT Filename, Size, Write, Path
      FROM SCOPE('DEEP TRAVERSAL OF "\"')
      WHERE
    ```

    

    by entering, at the command-line prompt,

    **jview /p /cp:p "&lt;JAVAPACKAGES&gt;" VJQuery &lt;Where\_Text&gt;**

    where &lt;Where\_Text&gt; is the desired text to follow the **WHERE** keyword. You must escape any double quotes in the text of the &lt;Where\_Text&gt; parameter. For example, to duplicate the default SQL query, enter

    **jview /p /cp:p "&lt;JAVAPACKAGES&gt;" VJQuery CONTAINS('\\"Indexing Service\\"')**

## Programming Notes

The **Query** class of the sample has methods that set the text of the query, execute the query, and display the results of the query.

-   Either the **SetRawSql** method or the **SetSqlWhere** method sets the *m\_SqlText* variable to the specified SQL statement.
-   The **Execute** method executes the query. It creates an ADO **Recordset** object and executes the query by opening the object with the SQL text and the [OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md).
-   The **Display** method enumerates the resulting values of the fields from the **Recordset** object and prints them.

 

 




