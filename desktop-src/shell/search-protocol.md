---
description: 'The search: application protocol is an extensible convention for calling the desktop search application on Windows Vista with Service Pack 1 (SP1) and later versions.'
title: Using the search Protocol
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 91a1ec25-f6ab-4377-8478-20bc51a1d5df
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Using the search Protocol

The **search:** [application protocol](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767916(v=vs.85)) is an extensible convention for calling the desktop search application on Windows Vista with Service Pack 1 (SP1) and later versions. The protocol was created in Windows Vista with SP1 to give Windows a way to determine and call the default desktop search application.

The protocol syntax provides a number of parameters useful for performing common desktop searches, such as user-entered search terms or the location on which the search was begun. When users search from one of the two available search entry points (either the **Start** menu or Windows Explorer), the operating system uses the search protocol to launch the default desktop search application. It does this by adding the user-entered search terms to the standard search protocol syntax and passing that information to the application registered as the default search application.

If no other desktop search applications are installed, a search entered into these entry points launches the Windows Search Explorer. However, third-party developers can create, install, and register their applications to handle the search protocol and to be the default search application. Such applications need to support the search protocol syntax and register with the [Default Programs](default-programs.md) feature to ensure a seamless experience with Windows.

If you develop an application that is intended to use or build upon a specific desktop search application, you should not depend exclusively on the **search:** protocol. Because many applications could own the **search:** protocol, there is no guarantee that your targeted desktop search application will own it at any given time. Instead, you should use a private search protocol defined by that targeted desktop search application. This means that desktop search applications intended to be a platform for third-party applications should support both the **search:** protocol and their own proprietary search protocol.

> [!Note]  
> The **search:** protocol does not replace the proprietary [search-ms:](../search/-search-3x-wds-qryidx-searchms.md) protocol. Applications can still use the **search-ms:** protocol to launch Window Search Explorer or to silently query the Windows Search indexer.

 

This topic covers the following:

-   [Syntax](#syntax)
-   [Windows Vista with SP1 use of the search: protocol](#windows-vista-with-sp1-use-of-the-search-protocol)
-   [Examples](#examples)
-   [Registering the Application that Handles the Protocol](#registering-the-application-that-handles-the-protocol)
    -   [Registry Entries](#registry-entries)
-   [Related topics](#related-topics)

## Syntax

The search protocol uses the following standard URL-encoded syntax:


```C++
search:parameter=value[&parameter=value]&
```



The syntax begins by identifying the protocol itself (**search:**). The parameter/value pairs are arguments passed to the Search engine, as described in the following table, which shows all of the possible parameters for the search protocol syntax.



| Parameter                                              | Value                                                         | Description                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| query                                                  | URL-encoded text                                              | The query text entered by the user.                                                                                                                                                                                                                                                            |
| [inputlocale](search-protocol-localeidentifiers.md)   | Any valid language code identifier (LCID)                     | The LCID that identifies the input language for the query.                                                                                                                                                                                                                                     |
| [keywordlocale](search-protocol-localeidentifiers.md) | Any valid LCID                                                | The LCID that identifies the language of the international version of the Indexer. The default is 1033 (en-us).                                                                                                                                                                                |
| [crumb](search-protocol-crumb.md)                     | AQS statement                                                 | This argument restricts the scope being searched. In Windows Vista, the search protocol supports full AQS as well as a special implementation for a `location` argument. In Windows XP, the search protocol also supports full AQS, except for a special implementation of `kind` and `store`. |
| [syntax](search-protocol-syntaxargument.md)           | NQS, AQS (not case sensitive)                                 | The query syntax to use to search the index: either Natural Query Syntax or Advanced Query Syntax (AQS). AQS is the default and is always assumed parsed and supported.                                                                                                                        |
| [stackedby](search-protocol-stackedby.md)             | Any valid property from the property system                   | A property that specifies the column to stack results by.                                                                                                                                                                                                                                      |
| [subquery](search-protocol-subquery.md)               | A fully specified path for a Saved Search file (\*.search-ms) | The results of the subquery are used as the source for the query. That is, the query terms are searched for against the results of the subquery.                                                                                                                                               |
| displayname                                            | URL-encoded string                                            | The name of the current search.                                                                                                                                                                                                                                                                |



 

## Windows Vista with SP1 use of the search: protocol

Windows Vista with SP1 has several entry points from which it calls the **search:** protocol. These entry points are outlined below as well as the common syntax associated with each.



| Search protocol entry point | Location         | Query called                                                         |
|-----------------------------|------------------|----------------------------------------------------------------------|
| **Search Everywhere**       | **Start** menu   | search:query=<*Search Term*>                                   |
| **Search Everywhere**       | Windows Explorer | search:query=<*Search Term*>&crumb=location:<*LOCATION*> |
| Windows logo key+F          | Anywhere         | search:                                                              |
| CTRL+F                      | Windows Explorer | search:query=<*Search Term*>&crumb=location:<*LOCATION*> |
| F3                          | **Start** menu   | search:                                                              |
| F3                          | Windows Explorer | search:query=<*Search Term*>&crumb=location:<*LOCATION*> |



 

The Windows Vista with SP1 search protocol entry points do not take advantage of all the possible parameters in the search protocol. Applications that are only concerned with handling search protocol calls from Windows Vista with SP1 can use the following table as a guide to the minimum they need to implement.



| Parameter                                              | Used by Windows? | How Windows Vista with SP1 uses it when calling search:                                                                                                                                                                                                                     |
|--------------------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| query                                                  | Yes              | The query text entered by the user.                                                                                                                                                                                                                                         |
| [crumb](search-protocol-crumb.md)                     | Yes              | [crumb](search-protocol-crumb.md) uses the `location` argument to specify where the query came from.                                                                                                                                                                       |
| [subquery](search-protocol-subquery.md)               | Yes              | The results of the [Subquery](search-protocol-subquery.md) argument are used as the scope of items to search. This would typically be used if a user was using a .search-ms file to search and then called the default desktop search application from within that search. |
| [inputlocale](search-protocol-localeidentifiers.md)   | No               | Not currently used.                                                                                                                                                                                                                                                         |
| [keywordlocale](search-protocol-localeidentifiers.md) | No               | Not currently used.                                                                                                                                                                                                                                                         |
| [syntax](search-protocol-syntaxargument.md)           | No               | Not currently used.                                                                                                                                                                                                                                                         |
| [stackedby](search-protocol-stackedby.md)             | No               | Not currently used.                                                                                                                                                                                                                                                         |
| displayname                                            | No               | Not currently used.                                                                                                                                                                                                                                                         |



 

## Examples

If a user enters "Microsoft" in the **Start** menu and clicks **Search Everywhere**, the resulting search protocol call is made:


```C++
search:query=microsoft&
```



If a user enters "Seattle" in Windows Explorer within C:\\MyFolder and then clicks **Search Everywhere**, the following call is made, using escape characters for ':' and '\\':


```C++
search:query=seattle&crumb=location:C%3A%5CMyFolder
```



## Registering the Application that Handles the Protocol

Because multiple applications can contend for the search protocol, you should register your application with the [Default Programs](default-programs.md) feature during installation to enable the user to configure the default more easily. In addition to the installation procedures normally practiced under Windows XP, a Windows Vista-based application must register with the Default Programs feature so that the application and users can seamlessly configure defaults.

After installing the necessary binary files on the user's computer, your installation routine should complete these general tasks:

1.  Write ProgIDs to **HKEY\_LOCAL\_MACHINE**, as described below. Note that applications must create application-specific ProgIDs for the search protocol.
2.  Claim machine-level search protocol association.
3.  Register the application with [Default Programs](default-programs.md), as explained in [Registering an Application for Use with Default Programs](default-programs.md), as a contender for the search protocol.

### Registry Entries

The following are examples of the required registry entries for a fictional desktop search application, Contoso Search.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Classes
         contoso-search
            URL Protocol = ""
```

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Classes
         contoso-search
            DefaultIcon
               (Default) = %ProgramFiles%\Contoso\Search\contososearch.exe,-7
```

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Classes
         contoso-search
            shell
               open
                  command
                     (Default) = %ProgramFiles%\Contoso\Search\contososearch.exe %1
```

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      RegisteredApplications
         Contoso Search = "Software\\Contoso\\Search\\Capabilities"
```

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Contoso
         Search
            Capabilities
               ApplicationName = "Contoso Search Test App"
               ApplicationDescription = "Contoso search is a great new desktop search application"
```

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Contoso
         Search
            Capabilities
               UrlAssociations
                  search = "contoso-search"
```

## Related topics

<dl> <dt>

[Advanced Query Syntax](../search/-search-3x-advancedquerysyntax.md)
</dt> <dt>

[Default Programs](default-programs.md)
</dt> </dl>

 

 
