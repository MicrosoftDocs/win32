---
title: Creating a Query in JScript
description: Creating a Query in JScript
ms.assetid: 10137b57-2815-405b-84b7-869912b9981f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Query in JScript

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The JSQuery.js script of the [SQuery Sample](squery-sample.md) executes a query that is embedded in the script. The query produces a parent, chaptered recordset (which represents a [hierarchical rowset](1844d85b-5197-4824-a254-9b3d63c421c2)) that contains selected columns forming a child chapter. The JSQuery.js script is a translation of the VBScript.vbs script into the JScript language. For a discussion of the VBScript version, see [Creating a Query in Visual Basic Scripting Edition](creating-a-query-in-visual-basic-scripting-edition.md).

The following list divides the sample script into segments and shows the structure of the complete script. The individual topic for each segment describes the details of the code for that segment.

-   [Declare Variables](declare-variables-jscript.md)
-   [Create a Query Object](create-a-query-object-jscript.md)
-   [Set Properties of the Query Object](set-properties-of-the-query-object-jscript.md)
-   [Create a Utility Object](create-a-utility-object-jscript.md)
-   [Add the Physical Path and All Subdirectories](add-the-physical-path-and-all-subdirectories-jscript.md)
-   [Output Query Properties](output-query-properties-jscript.md)
-   [Create a Parent Recordset Object for the Query](create-a-parent-recordset-object-for-the-query-jscript.md)
-   [Determine the Name of the GroupBy Column](determine-the-name-of-the-groupby-column-jscript.md)
-   [Read Through the Parent Recordset Object](read-through-the-parent-recordset-object-jscript.md)
-   [Close the Parent Recordset Object](close-the-parent-recordset-object-jscript.md)

 

 




