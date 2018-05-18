---
title: Allocating a DBCOMMANDTREE Structure
description: Allocating a DBCOMMANDTREE Structure
ms.assetid: '0e2afeef-48dc-4b08-a610-b2fde6774b4c'
---

# Allocating a DBCOMMANDTREE Structure

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following example declares a function **PctAllocNode** to allocate a new [**DBCOMMANDTREE**](dbcommandtree.md) structure. An additional example in [Setting Up a Condition Subtree](setting-up-a-condition-subtree.md) uses the function.


```
DBCOMMANDTREE* PctAllocNode(
  DBOP op,
  DBVALUEKIND eKind,
  ULONG cbValueSize
  )
{
  DBCOMMANDTREE* pct;
  //get the OLE IMalloc interface
  IMalloc* pim;
  HRESULT hr = CoGetMalloc(MEMCTX_TASK, &amp;pim);
  if (FAILED(hr))
    return NULL;
 
  // Allocate fixed size part of the node
  pct = (DBCOMMANDTREE*)pim->Alloc((sizeof DBCOMMANDTREE));
 
  //initialize fields
  pct->op = op;
  pct->pctFirstChild = NULL;
  pct->pctNextSibling = NULL;
  pct->hrError = S_OK;
  pct->dwKind = eKind;
 
  // Allocate variable size part of the node 
  if ( 0 != cbValueSize )
    pct.value.pvValue = (void *) pim->Alloc(cbValueSize);
 
  //Initialize value space
  if (0 != cbValueSize)
    memset(pct->value.pvValue, 0, cbValueSize);
 
  return pct;
}
```



 

 




