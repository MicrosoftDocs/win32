---
description: Understand how to use the CRUMB argument in Windows Search as a means of controlling the scope of a search.
ms.assetid: b0b974ae-0573-45e4-888e-07138604b62e
title: CRUMB Argument (Windows Search)
ms.topic: article
ms.date: 05/31/2018
---

# CRUMB Argument (Windows Search)

The `crumb` argument supports full Advanced Query Syntax (AQS) statements and is especially useful as a means of controlling the scope of a search. In addition to AQS ements, the `crumb` argument can take a special `location` parameter on Windows Vista and `kind` and `store` parameters on XP, as described later in this topic.

This topic is organized as follows:

-   [Crumb Syntax](#crumb-syntax)
    -   [General Examples](#general-examples)
-   [Using crumb with Vista (location)](#using-crumb-with-vista-location)
    -   [Vista Examples](#vista-examples)
    -   [Constants for Common Folders](#constants-for-common-folders)
-   [Using crumb with Windows XP (kind and store)](#using-crumb-with-windows-xp-kind-and-store)
    -   [XP Examples](#xp-examples)
-   [Related topics](#related-topics)

 

## Crumb Syntax

The crumb syntax is as follows:


```
crumb=<column>:<value>[,<label>][,<column>:<value>[,<label>]]& 
```



The &lt;column&gt; portion is any property in the property system, and the &lt;value&gt; portion is a valid value for that property. The <label> portion is an optional alias for the property that displays as a user interface hint.

### General Examples


```
crumb=System.Author:paolo&
crumb=store:mapi&
crumb=location:c%3a%5cMyVacationPix,Vacation&
```



 

## Using crumb with Vista (location)

In the crumb parameter, Windows Vista supports full AQS and also the `location` property, which has a special implementation available only on Windows Vista. You can use either an AQS string or the `location` property within a single crumb parameter, but not both. If the crumb parameter includes AQS, everything else in that crumb parameter is ignored.

The `location` property enables you to specify a path to search. Windows Vista can bypass the Indexer and traverse the directory directly if the location is outside the Indexer's crawl scope. Consequently, these searches may be slower than searches that use the Indexer.

When you specify a `location` property, two additional parameters are supported and optional:



| Parameter | Values                  | Description                                                                                                                                                                       |
|-----------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| inclusion | include, exclude        | Specifies whether the query should include or exclude items from that path. "Include" is the default. Windows Vista does not support exclusions without inclusions. (See example) |
| recursion | recursive, nonrecursive | Specifies whether the search should recurse all subfolders starting from the value defined in the location:&lt;value&gt;. "Recursive" is the default.                             |



 

To scope a search using the search-ms: protocol, you have different options depending on the target of the scope.

Folder on a local machine:

-   Use AQS (crumb=folder:<URL-encoded path>)
-   Use location argument (crumb=location:<URL-encoded path>)

Folder on a remote machine/network:

-   Use location argument (crumb=location:<URL-encoded path>)

Folder accessed via a known UNC protocol handler:

-   Use AQS (crumb=store:<UNC protocol handler name>)
-   Use location argument (crumb=location:<URL-encoded path>)

### Vista Examples


```
search-ms:query=vacation&crumb=location:shell%3aPersonal,include,recursive&

search-ms:crumb=location:c%3a%5cPictures&crumb=location:c%3a%5cPictures%5cDuplicates,,exclude& 

search-ms:crumb=location:c%3a%5cDocuments&crumb=kind:pics&
```



The first example executes a search for "vacation" starting at the shell://Personal location (a special shortcut to the user's My Documents folder), including that folder and all subfolders. See table below.

The second example executes a search within C:\\Pictures, but not in C:\\Pictures\\Duplicates.

The third example executes a search within C:\\Documents, limited to files with the kind property set to pics.

### Constants for Common Folders

Windows Vista enables the use of [KNOWNFOLDERID](/previous-versions//bb762584(v=vs.85)) values that provide a unique system-independent way to identify special folders used frequently by applications, but which may not have the same name or location on any given system. For example, the system folder may be "C:\\Windows" on one system and "C:\\Winnt" on another. Prior to Windows Vista, [CSIDLs](/windows/desktop/shell/csidl) were used.

Use these locations with this syntax:


```
crumb=location:shell%3a<LocationName>&
```



 

## Using crumb with Windows XP (kind and store)

For Windows Search on Windows XP (WDS 3.x), the AQS terms "kind" and "store" have a special implementation. The "kind" values are the same [values used in WDS 2.x](../lwef/-search-2x-wds-perceivedtype.md). The "store" values include the following:

-   mapi
-   file
-   outlookexpress
-   any

### XP Examples


```
search-ms:query=from:john&crumb=store:outlookexpress,OE%20Mail&
search-ms:query=from:john&crumb=kind:communications&
```



The first example returns Microsoft Outlook Express emails from John with the custom label, "OE Mail". The second example executes a search for any communication from John.

## Related topics

<dl> <dt>

[Getting Started with Parameter-Value Arguments](getting-started-with-parameter-value-arguments.md)
</dt> <dt>

[Locale Identifier Arguments](-search-3x-wds-qryidx-localeidentifiers.md)
</dt> <dt>

[SYNTAX Argument](-search-3x-wds-qryidx-syntaxargument.md)
</dt> <dt>

[STACKEDBY Argument](-search-3x-wds-qryidx-stackedby.md)
</dt> <dt>

[SUBQUERY Argument](-search-3x-wds-qryidx-subquery.md)
</dt> </dl>

 

 
