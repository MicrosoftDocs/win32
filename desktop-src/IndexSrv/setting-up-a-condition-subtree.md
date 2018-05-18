---
title: Setting Up a Condition Subtree
description: Setting Up a Condition Subtree
ms.assetid: '6a17cec8-f5f3-44bd-b12d-b30d73fd736b'
---

# Setting Up a Condition Subtree

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following example illustrates how to set up a condition subtree representing content search restriction. It uses the **PctAllocNode** function declared in [Allocating a DBCOMMANDTREE Structure](allocating-a-dbcommandtree-structure.md). The condition searches for the occurrence of the word "Database" within a column named "Text".


```
DBCOMMANDTREE *pct1, pct2;
DBCONTENT* pdbc;
 
//Allocate content node
pct1 = PctAllocNode(DBOP_content, DBVALUEKIND_CONTENT, (sizeof DBCONTENT));
 
//set up value field
pdbc = (DBCONTENT*)(pct1->value.pvValue);
pdbc->dwGenerateMethod = GENERATE_METHOD_PREFIX;
pdbc->lWeight = 200;
pdbc->lcid = DEFAULT_LCID;
pdbc->pwszPhrase = L"Database";
 
//allocate column node
pct2 = PctAllocNode(DBOP_simple_name, DBVALUEKIND_WSTR,
  (sizeof LPWSTR));
pct2->value.pwszValue = L"Text";
 
//Make the column node a child of the Content node
pct1->pctFirstChild = pct2;
```



 

 




