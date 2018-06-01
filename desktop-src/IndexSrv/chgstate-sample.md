---
Description: ChgState Sample
ms.assetid: db0a624b-4788-42b2-aa38-569cfc1d3a9d
title: ChgState Sample
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ChgState Sample

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The ChgState example is a command-line application written in C++ that can either report the current state of a catalog or change the state of the catalog using the [**SetCatalogState**](/windows/desktop/api/Ntquery/nf-ntquery-setcatalogstate) function of the OLE DB Helper API.

Source: mssdk\\samples\\winbase\\indexing\\ChgState\\

**To build the sample**

1.  Set the Lib environment variable to "D:\\mssdk\\Lib;%Lib%" and the Include environment variable to "D:\\mssdk\\Include;%Include%", where D: is the drive on which you installed the Platform SDK.
2.  Correctly set the CPU environment variable to, for example, "i386".
3.  Open a command window and change the directory to the source path of the sample.
4.  Build the sample by entering, at the command-line prompt, "nmake".

**To find or change the catalog state using the sample**

1.  Open a command window and change the directory to the path of the built sample.
2.  Submit a catalog state command by entering, at the command-line prompt, **chgstate /a:&lt;action&gt; \[/c:&lt;catalog&gt;\] \[/m:&lt;machine&gt;\]**

    where the values of the command-line parameters are the following.

    

    | Value                      | Meaning                                                                                                                                                                                                                                                         |
    |----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | &lt;action&gt;<br/>  | is a catalog state action; one of the following: <br/> RO sets read-only (queries only)<br/> RW sets read/write (queries and indexing)<br/> Stop sets stopped (no queries or indexing)<br/> GetState gets current state only<br/> |
    | &lt;catalog&gt;<br/> | is the name of the catalog (default is "system")                                                                                                                                                                                                                |
    | &lt;machine&gt;<br/> | is the name of the machine (default is ".")                                                                                                                                                                                                                     |

    

     

## Programming Notes

The previous state of the specified catalog is always returned in the *dwOldState* parameter of the [**SetCatalogState**](/windows/desktop/api/Ntquery/nf-ntquery-setcatalogstate) function and printed by the sample.

The state of the catalog will change to the new, specified state if that state does not violate read-only rules for the catalog. If the catalog resides on a read-only medium, the catalog is specified as read-only in the registry, or if the file cicat.hsh is set to read-only, the catalog is set to read-only even when the read/write state is requested.

## Parameters

The &lt;action&gt; parameter is the action desired. Four actions are possible:

-   RO (Read-only): Queries are allowed, but no indexing occurs.
-   RW (Read/write): Queries are allowed and indexing occurs.
-   Stop (Stopped): Stops catalog completely (no queries, no indexing).
-   GetState (Get state): Gets the current state of a catalog only. The catalog state prior to any specified action is always returned.

The &lt;catalog&gt; parameter is the name of the catalog on which to perform the action. The default value of the &lt;catalog&gt; parameter is "system", which is the default catalog installed. Additional catalogs can be created with the Indexing Service snap-in of the Microsoft Management Console (MMC).

The &lt;machine&gt; parameter is the name of the computer on which the request is executed. The default is ".", which is the local computer. Computer names should not be preceded by two backslashes.

## Examples

Change the "system" catalog on the local computer to the Read/write state.

**chgstate /a:RW /c:system**

Get the current state of the "system" catalog on machine SERVERNAME.

**chgstate /a:GetState /m:SERVERNAME**

Set the catalog CATALOGNAME on machine SERVERNAME to the Read-only state. (The catalog can be queried, but indexing is stopped.)

**chgstate /a:RO /c:CATALOGNAME /m:SERVERNAME**

 

 




