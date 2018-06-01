---
Description: CiHiliteType
ms.assetid: 695a4c6a-f170-494a-95d3-7546e9aa1cd4
title: CiHiliteType
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CiHiliteType

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Format: **CiHiliteType**=\[Full\|Summary\]

This parameter is optional. If not specified, Summary is the default value.

<dl> <dt>

<span id="Summary"></span><span id="summary"></span><span id="SUMMARY"></span>Summary
</dt> <dd>

When this parameter is set to Summary it generates small excerpts of a document around the words that match the query specification.

</dd> <dt>

<span id="Full"></span><span id="full"></span><span id="FULL"></span>Full
</dt> <dd>

When this parameter is set to Full it generates the full text of a document, highlighting the words that match the query. Mainly for documents that contain mostly text, this option does not do full-fidelity highlighting. Only the text part of the document is extracted and highlighted. In addition, this option tags the highlighted text (hits) with bookmarks, allowing navigation between the hits. The first hit is bookmarked as \#CiTag0 and the top of the generated document is tagged as \#CiTag-1. To help navigate, double-angle bracket tags (&lt;&lt; and &gt;&gt;) surround each hit. Click the &lt;&lt; tag to go to the previous hit, and click the &gt;&gt; tag to go to the next hit.

</dd> </dl>

 

 



