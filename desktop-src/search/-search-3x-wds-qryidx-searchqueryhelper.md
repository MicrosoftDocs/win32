---
description: You can use the ISearchQueryHelper interface to query the index. This interface is implemented as a helper class to ISearchCatalogManager (and ISearchCatalogManager2), and is obtained by calling ISearchCatalogManager::GetQueryHelper.
ms.assetid: 6e567c09-8763-4866-bf02-ad6651b454db
title: Querying the Index with ISearchQueryHelper
ms.topic: article
ms.date: 05/31/2018
---

# Querying the Index with ISearchQueryHelper

You can use the [**ISearchQueryHelper**](/windows/desktop/api/Searchapi/nn-searchapi-isearchqueryhelper) interface to query the index. This interface is implemented as a helper class to [**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) (and [**ISearchCatalogManager2**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager2)), and is obtained by calling [**ISearchCatalogManager::GetQueryHelper**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-getqueryhelper). This interface permits you to:

-   Obtain an OLE DB connection string to connect to the Windows Search database.
-   Convert Advanced Query Syntax (AQS) user queries to Windows Search Structured Query Language (SQL).
-   Specify query restrictions that can be expressed in SQL, but not in AQS.

This topic is organized as follows:

-   [Getting Started with ISearchQueryHelper](#getting-started-with-isearchqueryhelper)
-   [Using the GenerateSqlFromUserQuery Method](#using-the-generatesqlfromuserquery-method)
-   [Working with Locale Identifiers](#working-with-locale-identifiers)
-   [Working with Properties and Columns](#working-with-properties-and-columns)
-   [Working with Query Term Expansion](#working-with-query-term-expansion)
-   [Working with Other ISearchQueryHelper Methods](#working-with-other-isearchqueryhelper-methods)
-   [Related topics](#related-topics)

## Getting Started with ISearchQueryHelper

There are a few key interfaces and methods you should be aware of before you can start programmatically querying Windows Search using the [**ISearchQueryHelper**](/windows/desktop/api/Searchapi/nn-searchapi-isearchqueryhelper) interface. At a high level, you need to follow these steps:

1.  Instantiate an [**ISearchManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager) instance.
    ```
    // Create ISearchManager instance
    ISearchManager* pSearchManager;

    // Use library SearchSDK.lib for CLSID_CSearchManager.
    hr = CoCreateInstance(CLSID_CSearchManager, NULL, CLSCTX_LOCAL_SERVER, IID_PPV_ARGS(&pSearchManager));      
    ```

    

2.  Obtain an instance of [**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) using [**ISearchManager::GetCatalog**](/windows/desktop/api/Searchapi/nf-searchapi-isearchmanager-getcatalog). The name of the system catalog for Windows Search is `SYSTEMINDEX`.
    ```
    // Create ISearchCatalogManager instance 
    ISearchCatalogManager* pSearchCatalogManager;

    // Call ISearchManager::GetCatalog for "SystemIndex" to access the catalog to the ISearchCatalogManager
    hr = pSearchManager->GetCatalog(L"SystemIndex", &pSearchCatalogManager);
            
    ```

    

3.  Obtain an instance of [**ISearchQueryHelper**](/windows/desktop/api/Searchapi/nn-searchapi-isearchqueryhelper) using [**ISearchCatalogManager::GetQueryHelper**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-getqueryhelper).
    ```
    // Call ISearchCatalogManager::GetQueryHelper to get the ISearchQueryHelper interface
    ISearchQueryHelper* pQueryHelper;

    hr = pSearchCatalogManager->GetQueryHelper(&pQueryHelper);
            
    ```

    

4.  After you have an instance of [**ISearchQueryHelper**](/windows/desktop/api/Searchapi/nn-searchapi-isearchqueryhelper), you can then get the connection string used to connect to the Windows Search index OLE DB connector.
    ```
    // Call get_ConnectionString to get the OLE DB connection string
    LPWSTR pszConnectionString=NULL;

    hr = pQueryHelper->get_ConnectionString(&pszConnectionString);
    // NOTE: YOU MUST call CoTaskMemFree() on the string
        
    ```

    

## Using the GenerateSqlFromUserQuery Method

The [**ISearchQueryHelper::GenerateSQLFromUserQuery**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-generatesqlfromuserquery) method transforms user input into a SQL query string, which can then be submitted to the OLE DB provider for Windows Search. This method translates the [Advanced Query Syntax](-search-3x-advancedquerysyntax.md) (AQS) or Natural Query Syntax (NQS) query entered by the user into SQL, and lets you add other SQL fragments as needed.

The SQL query string is returned in the following form:


```
SELECT <QuerySelectColumns> 
FROM <CatalogName that created query helper>
WHERE <Result of interpreting the user query passed into this function according to QuerySyntax>
      [ AND|OR <QueryWhereRestrictions> ]
    
```



The following is an example of the SQL string returned from the call `GenerateSQLFromUserQuery("comput")`:


```
SELECT "System.ItemUrl" 
FROM "SystemIndex" 
WHERE ((CONTAINS(*,'"comput*"',1033) RANK BY COERCION(Absolute, 1)) OR 
       (FREETEXT(("System.ItemNameDisplay":0.9, *:0.1), 'comput', 1033) AND CONTAINS(*,'"comput"',1033)))
ORDER BY "System.ItemUrl"
```



> [!Note]  
> The method generates both the FREETEXT and the CONTAINS predicates because CONTAINS alone does not generate meaningful ranking.

 

## Working with Locale Identifiers



| Method                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ISearchQueryHelper::get\_QueryContentLocale**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-get_querycontentlocale)/<br/> [**ISearchQueryHelper::put\_QueryContentLocale**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-put_querycontentlocale)<br/> | Gets/Puts the language code identifier (LCID) of the query. This helps get the correct wordbreaker and stemmer to compare query terms against the catalog/inverted index. The default is the current input locale. |
| [**ISearchQueryHelper::get\_QueryKeywordLocale**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-get_querykeywordlocale)/<br/> [**ISearchQueryHelper::put\_QueryKeywordLocale**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-put_querykeywordlocale)<br/> | Gets/Puts the LCID for the language to use when parsing Advanced Query Syntax (AQS) keywords. The default is the default user locale.                                                                              |



 

The **content locale** and **keyword locale** are locale identifiers (LCID) that help the search engine use the correct word breakers by identifying the language of the query terms and the language the AQS keywords. These are not always the same LCIDs because Windows Search is offered in a number of international versions and also includes Multilingual User Interface (MUI) packs for more languages. The content locale identifies the LCID for the language users input their search query in, while the keyword locale identifies the LCID the search engine uses when parsing Advanced Query Syntax (AQS) keywords.

For example, if you have the English-US version with no MUI packs, both the content locale and keyword locale are 1033. If you have the German version with no MUI packs, then both the content locale and keyword locale are 1031 (gr-gr). However, if you have the English version with the Romanian MUI pack, the content locale is 2072 (ro) and the keyword locale is 1033 (en-us).

## Working with Properties and Columns



| Methods                                                                                                                                                                                                                                                  | Description                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ISearchQueryHelper::get\_QueryContentProperties**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-get_querycontentproperties)/<br/> [**ISearchQueryHelper::put\_QueryContentProperties**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-put_querycontentproperties)<br/> | Gets/Sets the content properties for the search (property column listed in the CONTAINS or FREETEXT clauses).                                   |
| [**ISearchQueryHelper::get\_QuerySelectColumns**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-get_queryselectcolumns)/<br/> [**ISearchQueryHelper::put\_QuerySelectColumns**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-put_queryselectcolumns)<br/>                 | Gets/Sets the columns (or properties) requested in the SELECT statement. The default is System.ItemUrl and properties used in the WHERE clause. |



 

Items are represented in the property store as a row. Each row contains a number of columns that represent properties for that item. Not all items will have a value for a given property. For example, an audio file would typically not contain a value for the System.Property.FromName property but may contain information regarding the System.Music.Artist.

With these methods, you access or modify the property with a comma delimited, null-terminated, Unicode string that specifies one or more column names of the property store: "System.Document.Author, System.Document.Title".

## Working with Query Term Expansion



| Methods                                                                                                                                                                                                                                 | Description                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [**ISearchQueryHelper::get\_QueryTermExpansion**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-get_querytermexpansion)<br/> [**ISearchQueryHelper::put\_QueryTermExpansion**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-put_querytermexpansion)<br/> | Gets/Sets the search term expansion flag. |



 

This method enables the expansion of some query terms with wild card characters, similar to regular expression expansion. Prefix expansion searches for words with the same prefix (fun/funnel). If not set, the default value is SEARCH\_TERM\_PREFIX\_ALL. The supported values of the [**SEARCH\_TERM\_EXPANSION**](/windows/desktop/api/Searchapi/ne-searchapi-search_term_expansion) enumeration are as follows:

-   SEARCH\_TERM\_PREFIX\_ALL - All search terms are expanded
-   SEARCH\_TERM\_NO\_EXPANSION - No search terms are expanded

## Working with Other ISearchQueryHelper Methods

Many of the methods in the [**ISearchQueryHelper**](/windows/desktop/api/Searchapi/nn-searchapi-isearchqueryhelper) interface are used to set query arguments or define the properties returned.



| Methods                                                                                                                                                                                                                                                 | Description                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ISearchQueryHelper::get\_ConnectionString**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-get_connectionstring)<br/>                                                                                                                                         | Returns the OLE DB connection string. This is the preferred method of getting a properly formatted and correct connection string.                                  |
| [**ISearchQueryHelper::get\_QueryMaxResults**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-get_querymaxresults)<br/> [**ISearchQueryHelper::put\_QueryMaxResults**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-put_querymaxresults)<br/>                             | Gets/Sets the maximum number of results to be returned by a query (that is, SELECT TOP n). The default is -1, meaning that no maximum results clause is generated. |
| [**ISearchQueryHelper::get\_QuerySorting**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-get_querysorting)<br/> [**ISearchQueryHelper::put\_QuerySorting**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-put_querysorting)<br/>                                         | Gets/Sets the sort order for the query result set (ORDER BY). If no ORDER BY clause exists, the results are returned in non-deterministic order.                   |
| [**ISearchQueryHelper::get\_QuerySyntax**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-get_querysyntax)<br/> [**ISearchQueryHelper::put\_QuerySyntax**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-put_querysyntax)<br/>                                             | Gets/Sets the syntax of the query: Advanced Query Syntax or Natural Query Syntax.                                                                                  |
| [**ISearchQueryHelper::get\_QueryWhereRestrictions**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-get_querywhererestrictions)<br/> [**ISearchQueryHelper::put\_QueryWhereRestrictions**](/windows/desktop/api/Searchapi/nf-searchapi-isearchqueryhelper-put_querywhererestrictions)<br/> | Gets/Sets the restrictions appended via WHERE clauses.                                                                                                             |



 

## Related topics

<dl> <dt>

[Querying the Index Programmatically](-search-3x-wds-qryidx-overview.md)
</dt> <dt>

[Using SQL and AQS Approaches to Query the Index](-search-3x-wds-qryidx-overview.md)
</dt> <dt>

[Querying the Index with the search-ms Protocol](-search-3x-wds-qryidx-searchms.md)
</dt> <dt>

[Querying the Index with Windows Search SQL Syntax](-search-sql-windowssearch-entry.md)
</dt> <dt>

[Using Advanced Query Syntax Programmatically](-search-3x-advancedquerysyntax.md)
</dt> </dl>

 

 




