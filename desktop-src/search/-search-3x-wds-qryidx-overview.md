---
description: There are several ways to use Windows Search to query the index.
ms.assetid: 2c161b7f-4e28-4e8a-add6-3c1cda00a622
title: Querying the Index Programmatically
ms.topic: article
ms.date: 05/31/2018
---

# Querying the Index Programmatically

There are several ways to use Windows Search to query the index.

This section provides the conceptual framework for querying the index programmatically:

-   [Using SQL and AQS Approaches to Query the Index](using-sql-and-aqs-to-query-the-index.md)
-   [Querying the Index with ISearchQueryHelper](-search-3x-wds-qryidx-searchqueryhelper.md)
-   [Querying the Index with the search-ms Protocol](-search-3x-wds-qryidx-searchms.md)
-   [Querying the Index with Windows Search SQL Syntax](-search-sql-windowssearch-entry.md)
-   [Using Advanced Query Syntax Programmatically](-search-3x-advancedquerysyntax.md)

> [!Note]  
> Legacy Microsoft Windows Desktop Search (WDS) 2x compatibility: On computers running Windows XP and later, [**ISearchDesktop**](/previous-versions//aa965729(v=vs.85)) is deprecated. Instead, developers should use [**ISearchQueryHelper**](/windows/win32/api/Searchapi/nn-searchapi-isearchqueryhelper) to get a connection string and to parse the user's query into Structured Query Language (SQL), and then query through Object Linking and Embedding Database (OLE DB).

 

## Additional Resources

-   For information on OLE DB, see [OLE DB Programming Overview](https://msdn.microsoft.com/library/Cc522830(v=VS.71).aspx). For information on the .NET Framework Data Provider for OLE DB, see the [System.Data.OleDb Namespace](/dotnet/api/system.data.oledb).
-   For additional background on using properties in querying, see the following topics:
    -   [Property System](../properties/building-property-handlers.md)
    -   [System Properties](https://msdn.microsoft.com/library/bb763010(VS.85).aspx)
-   For information on how to create and modify search folders, see [**ISearchFolderItemFactory Interface**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-isearchfolderitemfactory).
-   For community-supported question and discussion message boards on Search technologies, see [MSDN Forum: Windows Desktop Search Development](https://social.msdn.microsoft.com/Forums/windowsdesktopsearchdevelopment/threads).
-   To download the Search SDK Code Samples:
    -   For Windows 7: [Windows Search Samples on GitHub](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch)
    -   For Windows Vista: [Windows Search SDK Samples](https://www.microsoft.com/downloads/details.aspx?FamilyID=645300AE-5E7A-4CE7-95F0-49793F8F76E8)
-   To download the Windows SDK:
    -   For Windows 7: [Windows SDK for Windows 7 and .NET Framework](https://msdn.microsoft.com/windowsvista/bb980924.aspx)
    -   For Windows Vista: [Windows SDK for Windows Vista and .NET Framework](https://www.microsoft.com/download/details.aspx?id=31950)

## Related topics

<dl> <dt>

[Windows Search Development Guide](-search-developers-guide-entry-page.md)
</dt> <dt>

[Managing the Index](-search-3x-wds-mngidx-overview.md)
</dt> <dt>

[Extending the Windows Search Index](-search-3x-wds-extidx-overview.md)
</dt> <dt>

[Extending Language Resources](extending-language-resources-in-windows-search.md)
</dt> </dl>

 

 
