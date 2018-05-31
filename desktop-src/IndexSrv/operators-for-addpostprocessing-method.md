---
title: Operators for AddPostProcessing Method
description: Operators for AddPostProcessing Method
ms.assetid: 89c9da65-83bd-43a9-8c6a-27606098560d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Operators for AddPostProcessing Method

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the operators for the **IQuery::AddPostProcessing** method.

<dl> <dt>

<span id="DBOP_prior_command_tree"></span><span id="dbop_prior_command_tree"></span><span id="DBOP_PRIOR_COMMAND_TREE"></span>DBOP\_prior\_command\_tree
</dt> <dd>

Used when adding post-processing operations. This operator occurs in the post-processing tree but never in a complete command tree. It has either no inputs, or no table- or scalar-valued expressions, depending on the previous command tree.

</dd> <dt>

<span id="DBOP_add_columns"></span><span id="dbop_add_columns"></span><span id="DBOP_ADD_COLUMNS"></span>DBOP\_add\_columns
</dt> <dd>

Used when adding post-processing operations, this operation is the only operation that can add columns "projected away" by earlier operations, such as columns from tables that already participate in the query. The inputs are a table and a projection list; output is a table.

</dd> </dl>

 

 




