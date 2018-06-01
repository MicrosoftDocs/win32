---
Description: Creating a Query in Visual Basic Scripting Edition
ms.assetid: e7d87442-83c9-4a67-bc75-674423bbcd4a
title: Creating a Query in Visual Basic Scripting Edition
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Query in Visual Basic Scripting Edition

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

The VBSQuery.vbs script of the [SQuery Sample](squery-sample.md) executes a query that is embedded in the script. The query produces a parent, chaptered Recordset object (which represents a [hierarchical rowset](https://msdn.microsoft.com/windows/desktop/1844d85b-5197-4824-a254-9b3d63c421c2)) with selected columns forming a child chapter. This script is also translated into the JScript language. For a discussion of the JScript version, see [Creating a Query in JScript](creating-a-query-in-jscript.md).

The following list divides the sample script into segments and shows the structure of the complete script. The individual topic for each segment describes the details of the code for that segment.

-   [Declare Variables](declare-variables.md)
-   [Create a Query Object](create-a-query-object.md)
-   [Set Properties of the Query Object](set-properties-of-the-query-object.md)
-   [Create a Utility Object](create-a-utility-object.md)
-   [Add the Physical Path and All Subdirectories](add-the-physical-path-and-all-subdirectories.md)
-   [Output Query Properties](output-query-properties.md)
-   [Create a Parent Recordset Object for the Query](create-a-parent-recordset-object-for-the-query.md)
-   [Determine the Name of the GroupBy Column](determine-the-name-of-the-groupby-column.md)
-   [Read Through the Parent Recordset Object](read-through-the-parent-recordset-object.md)
-   [Close the Parent Recordset Object](close-the-parent-recordset-object.md)

 

 



