---
title: AdvQuery Sample
description: AdvQuery is an example of a command-line application written in C++ that executes a query using OLE DB Provider interfaces such as ICommand and ICommandTree.
ms.assetid: 288d6adc-56ac-4f81-b992-48446b917e9f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AdvQuery Sample

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

AdvQuery is an example of a command-line application written in C++ that executes a query using OLE DB Provider interfaces such as [**ICommand**](089427ad-5ba3-4613-b89e-8e86420ccc30) and [**ICommandTree**](/previous-versions/windows/desktop/api/cmdtree/nn-cmdtree-icommandtree). It shows how to specify a catalog, machine name, and scope. It can also display the OLE DB command tree for the query.

Source: mssdk\\samples\\winbase\\indexing\\AdvQuery\\

**To build the sample**

1.  Set the *Lib* environment variable to "D:\\mssdk\\Lib;%Lib%" and the *Include* environment variable to "D:\\mssdk\\Include;%Include%", where D: is the drive on which you installed the Platform SDK.
2.  Correctly set the *CPU* environment variable to, for example, "i386".
3.  Open a command window and change the directory to the source path of the sample.
4.  Build the sample by entering, at the command-line prompt, "nmake".

**To issue a query to Indexing Service using the sample**

1.  Open a command window and change the directory to the path of the built sample.
2.  Formulate a query that you know will succeed. You need to know the machine, catalog, scope, and query text.
3.  Submit the query by entering, at the command-line prompt, **advquery &lt;query&gt; \[/c:&lt;catalog&gt;\] \[/m:&lt;machine&gt;\] \[/s:&lt;scope&gt;\] \[/d\]**

    where the values of the command-line parameters are the following.

    

    | Value           | Meaning                                                                    |
    |-----------------|----------------------------------------------------------------------------|
    | &lt;query&gt;   | is a query in an Indexing Service query language                           |
    | &lt;catalog&gt; | is the name of the catalog (default is "system")                           |
    | &lt;machine&gt; | is the name of the machine (default is ".")                                |
    | &lt;scope&gt;   | is the root path (default is entire catalog)                               |
    | /d              | displays the [DBCOMMANDTREE](dbcommandtree.md) (default is don't display) |

    

     

## Programming Notes

The sample prints the rank, size, and path of each file that matches the query. The query results are sorted by rank (how well the file matches the query).

This sample is more complex than the Simple (QSample) sample because it creates a command tree and use the low-level [**ICommandTree**](/previous-versions/windows/desktop/api/cmdtree/nn-cmdtree-icommandtree) interface instead of using the OLE DB Helper functions [CICreateCommand](/windows/desktop/api/Ntquery/nf-ntquery-cicreatecommand) and [CITextToFullTree](/windows/desktop/api/Ntquery/nf-ntquery-citexttofulltree).

## Parameters

The &lt;query&gt; parameter can be a word or a phrase. Files that contain the word or phrase are listed in the result. To include a space in a query, enclose the query in quotes.

The &lt;catalog&gt; parameter is the name of the catalog to be queried. The default is "system", which is the default catalog installed. Additional catalogs can be created with the Indexing Service snap-in of the Microsoft Management Console (MMC).

The &lt;machine&gt; parameter is the name of the computer on which the query is executed. The default is ".", which is the local machine. Machine names should not be preceded by two backslashes.

The &lt;scope&gt; parameter is the file path where files must be located in order to be included in the results. The default is "\\", which includes all scopes in the catalog.

The "/d" parameter displays the [DBCOMMANDTREE](dbcommandtree.md) structure built to execute the query.

## Examples

Finds all files in the "system" catalog on the local computer that contain the word "abc".

**advquery abc**

Finds all files in the "system" catalog on the local computer that contain the phrase "abc def" that are in the specified directory or any subdirectory.

**advquery "abc def" "/s:c:\\my directory"**

Finds all files in the "system" catalog on computer "servername" that contain the word "abc".

**advquery abc /m:SERVERNAME**

 

 




