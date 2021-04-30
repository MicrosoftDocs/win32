---
description: An attachment snap-in extension must add itself under the Services node when that node is expanded by a user.
ms.assetid: af853c29-11c2-4fd0-ad81-80aebeb74cc3
title: Adding an Attachment Snap-in Extension Node
ms.topic: article
ms.date: 05/31/2018
---

# Adding an Attachment Snap-in Extension Node

An attachment snap-in extension must add itself under the Services node when that node is expanded by a user.

When a user expands the Services node under one of the Security Configuration snap-ins, MMC uses [**IComponentData::Notify**](/windows/desktop/api/mmc/nf-mmc-icomponentdata-notify) and the MMCN\_EXPAND notification message to notify the Security Configuration snap-in, plus all its extensions.

The Security Configuration snap-in then extracts its internal format from the *lpDataObject*, which is passed in from the MMC main framework as type **LPDATAOBJECT**. It stops processing when it sees the Services node type. The attachment snap-in extension then extracts the node type from the *lpDataObject*. If the node type is one of the service's defined node types, the attachment snap-in extension inserts its root nodes under the specified parent node.

Note that in this example, ExtractNodeType, is a private function that the extension implements. The extension examines the data object to get the node type. The implementation of ExtractNodeType is not shown.


```C++
//  Detect which extension node to expand.
GUID* nodeType = ExtractNodeType(lpdataObject);

if (NULL == nodeType)
{
  return S_OK;
}

if (TRUE == ::IsEqualGUID(*nodeType, cNodetypeSceTemplateServices))
{
  folderType = ATTACHMENT_STATIC;  // defined by attachment writer
}

else if (TRUE == ::IsEqualGUID
    (*nodeType, cNodetypeSceAnalysisServices))
{
  folderType = ATTACHMENT_STATIC_ANALYSIS;
               // defined by attachment writer
}

//  Free resources.
::GlobalFree(reinterpret_cast<HANDLE>(nodeType));

//  Add service attachment root node and remember it as the
//  root of the SMB extension namespace.
//  ...
```



 

 
