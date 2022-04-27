---
title: Calling WDS from the Command Line
description: You can launch the Microsoft Windows Desktop Search (WDS) user interface with a specific filter, store, and query from another application or a webpage that uses the Browser Helper Object (BHO) by using the windowssearch.exe command line syntax.
ms.assetid: fd62f7c9-08a9-4e05-b0bc-e2215cfff59e
ms.topic: article
ms.date: 05/31/2018
---

# Calling WDS from the Command Line

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

You can launch the Microsoft Windows Desktop Search (WDS) user interface with a specific filter, store, and query from another application or a webpage that uses the Browser Helper Object (BHO) by using the windowssearch.exe command line syntax. When calling WDS from the command line, no information about the user's actions or selection in the WDS window is returned to the calling application or webpage.

The WDS installation path is specified in the InstallDir registry setting under HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows Desktop Search. The default path that windowssearch.exe is installed to is Program Files\\Windows Desktop Search.

## Command Line Syntax

The following syntax applies to the Windows Desktop Search 2.x command-line interface.

| Options | Parameter | Meaning | 
|-|-|-|
| /startup | | Initializes Windows Desktop Search |
| /indexnow | | Turns off indexing back-off and rescans all index locations |
| /showstatusv | | Shows the indexing status window |
| /launchsearchwindow or /url | | Opens a WDS window with an empty query |
| /url | search:[store\|show\|query] query string | Opens a WDS window with a query and filter based on the following parameters:<ul><li><p>store - Specifies the data source to query: files, outlook, outlookexpress. If not specified all stores will be searched. <br /></p><blockquote>[!Note]<br />While Advanced Query Syntax supports referencing Microsoft Outlook as 'oe', the store parameter on the command line must be 'outlookexpress'.</blockquote><p><br /></p></li><li><p>show - Specifies which perceived type of results to return. See <a href="-search-2x-wds-perceivedtype.md">Perceived Types</a> for a complete list of types. If not specified, all types will be returned. <br /></p><blockquote>[!Note]<br />There are three differences between the perceived type values and the values for show. For <code>show</code>, use 'documents' instead of 'doc', 'pictures' instead of 'pics', and 'textdocuments' instead of 'text'.</blockquote><p><br /></p></li><li>query - Specifies the search criteria. This value supports <a href="-search-2x-wds-aqsreference.md">Advanced Query Syntax</a> parameters to refine the results. The query parameter must be the last parameter in the URL.</li></ul> |

## Example

For example, to search all files for pictures matching the criteria 'wallpaper' use the following command:

```cmd
WindowsSearch.exe /url search:store=files&show=pictures&query=wallpaper
```

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Advanced Query Syntax](-search-2x-wds-aqsreference.md)
</dt> <dt>

[Perceived Types](-search-2x-wds-perceivedtype.md)
</dt> <dt>

[Calling WDS from Web Pages](-search-2x-wds-browserhelpobject.md)
</dt> </dl>

 

 





