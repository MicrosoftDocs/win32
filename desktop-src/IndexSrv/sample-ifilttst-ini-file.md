---
Description: Sample IFiltTst.ini File
ms.assetid: 13a1ae88-56b8-4018-bc3b-a980ac42ae12
title: Sample IFiltTst.ini File
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sample IFiltTst.ini File

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

``` syntax
; Only extract text from the object
[Test1]
Flags = 
cAttributes = 0
 
; Get all attributes (text-type and internal value-type properties)
[Test2]
Flags = IFILTER_INIT_APPLY_INDEX_ATTRIBUTES
cAttributes = 0
 
; This also extracts just text from the object (the GUID is PSGUID_STORAGE, and the propid is 
; PID_STG_CONTENTS)
[Test3]
Flags = IFILTER_INIT_CANON_PARAGRAPHS IFILTER_INIT_HARD_LINE_BREAKS 
cAttributes = 1
aAttributes1 = b725f130-47ef-101a-a5f1-02608c9eebac 13
 
; Only extract requested attribute from the html object (the GUID corresponds to the html filter)
[Test4]
Flags = IFILTER_INIT_CANON_HYPHENS IFILTER_INIT_CANON_SPACES 
cAttributes = 1
aAttributes1 = 70eb7a10-55d9-11cf-b75b-00aa0051fe20 2
 
; What happens if cAttributes is nonzero, but aAttributes is empty?
[Test5]
Flags = IFILTER_INIT_CANON_SPACES IFILTER_INIT_APPLY_INDEX_ATTRIBUTES IFILTER_INIT_APPLY_OTHER_ATTRIBUTES
cAttributes = 1
 
; Here is an attribute with a lpwstr instead of a propid (the lpwstr is enclosed in quotes)
; The GUID corresponds to the meta tag clsid for the HTML filter.
[Test6]
Flags = 
cAttributes = 1
aAttributes1 = D1B5D3F0-C0B3-11CF-9A92-00A0C908DBF1 "GENERATOR"
```

 

 



