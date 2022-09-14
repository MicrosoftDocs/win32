---
description: The search-ms ?application protocol is a convention for querying the Windows Search index.
ms.assetid: e8b18018-c712-4007-bb0a-af90a75780d6
title: Getting Started with Parameter-Value Arguments
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with Parameter-Value Arguments

The **search-ms** ?[application protocol](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767916(v=vs.85)) is a convention for querying the Windows Search index. The protocol enables applications, like Windows Explorer, to query the index with parameter-value arguments, including property arguments, previously saved searches, Advanced Query Syntax (AQS), Natural Query Syntax (NQS), and language code identifiers (LCIDs) for both the indexer and the query itself.

This topic is organized as follows:

- [About Parameter-Value Arguments](#about-parameter-value-arguments)
- [Examples](#examples)
- [Related topics](#related-topics)

## About Parameter-Value Arguments

The search-ms protocol uses the following standard URL-encoded syntax:

```
search-ms:parameter=value[&parameter=value]&
```

The syntax begins by identifying the protocol itself (search-ms:). The parameter/value pairs are arguments passed to the Search engine, as described in the following table.

| Parameter                                                    | Value                                                         | Description                                                                                                                                                                                                                                                                | Version                  |
|--------------------------------------------------------------|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| query                                                        | URL-encoded text                                              | The query text entered by the user.                                                                                                                                                                                                                                        | Windows XP, and later    |
| [inputlocale](-search-3x-wds-qryidx-localeidentifiers.md)   | Any valid LCID                                                | The LCID that identifies the input language for the query.                                                                                                                                                                                                                 | Windows XP, and later    |
| [keywordlocale](-search-3x-wds-qryidx-localeidentifiers.md) | Any valid LCID                                                | The LCID that identifies the language of the international version of the Indexer. The default is 1033 (en-us).                                                                                                                                                            | Windows XP, and later    |
| [crumb](-search-3x-wds-qryidx-crumb.md)                     | AQS statement                                                 | This argument restricts the scope being searched. In Windows Vista and later, search-ms supports full AQS as well as a special implementation for a `location` argument. In Windows XP, search-ms also supports full AQS, except for a special implementation of `kind` and `store`. | Windows XP, and later    |
| [syntax](-search-3x-wds-qryidx-syntaxargument.md)           | NQS, AQS (not case sensitive)                                 | The query syntax to use to search the index: either Natural Query Syntax or Advanced Query Syntax (AQS). AQS is the default and is always assumed parsed and supported.                                                                                                    | Windows Vista, and later |
| [stackedby](-search-3x-wds-qryidx-stackedby.md)             | Any valid property from the property system                   | A property that specifies the column to stack results by.                                                                                                                                                                                                                  | Windows Vista, and later |
| [subquery](-search-3x-wds-qryidx-subquery.md)               | A fully specified path for a Saved Search file (\*.search-ms) | The results of the subquery are used as the source for the query. That is, the query terms are searched for against the results of the subquery.                                                                                                                           | Windows Vista, and later |
| displayname                                                  | URL-encoded string                                            | The name of the current search.                                                                                                                                                                                                                                            | Windows Vista, and later |


For related information, see [Registering an Application to a URL Protocol](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767914(v=vs.85)).

## Examples

```
search-ms:query=microsoft&
search-ms:query=vacation&subquery=mydepartment.search-ms&
search-ms:query=seattle&crumb=kind:pics&
search-ms:query=seattle&crumb=folder:C:\MyFolder&
```

## Related topics

[Locale Identifier Arguments](-search-3x-wds-qryidx-localeidentifiers.md)

[CRUMB Argument](-search-3x-wds-qryidx-crumb.md)

[SYNTAX Argument](-search-3x-wds-qryidx-syntaxargument.md)

[STACKEDBY Argument](-search-3x-wds-qryidx-stackedby.md)

[SUBQUERY Argument](-search-3x-wds-qryidx-subquery.md)
