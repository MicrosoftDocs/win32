---
description: Specifies the type of link when crawling or indexing.
ms.assetid: 2a0ddb31-df35-4da5-9950-b091cd461556
title: LINKTYPE enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LINKTYPE
api_type: 
- NA
api_location: 
---

# LINKTYPE enumeration

\[The **LINKTYPE** enumeration is supported only on Windows XP and Windows Server 2003, and should no longer be used.\]

Specifies the type of link when crawling or indexing.

## Syntax


```C++
typedef enum _LINKTYPE { 
  LINKTYPE_URL      = 0x00000000,
  LINKTYPE_CONTENT  = 0x00000001,
  LINKTYPE_RELATED  = 0x00000002
} LINKTYPE;
```



## Constants

<dl> <dt>

<span id="LINKTYPE_URL"></span><span id="linktype_url"></span>**LINKTYPE\_URL**
</dt> <dd>

Specifies whether the URLs link type should be indexed.

</dd> <dt>

<span id="LINKTYPE_CONTENT"></span><span id="linktype_content"></span>**LINKTYPE\_CONTENT**
</dt> <dd>

Specifies whether the link content should be indexed.

</dd> <dt>

<span id="LINKTYPE_RELATED"></span><span id="linktype_related"></span>**LINKTYPE\_RELATED**
</dt> <dd>

Specifies a related link.

</dd> </dl>

## Remarks

To preview attachments with a third-party protocol handler on computers running Windows XP or Windows Server 2003, it may be necessary to use the **LINKTYPE** flags, and the following other APIs: the [**IItemPreviewerExt::GetLinkedContent**](-search-iitempreviewerext-getlinkedcontent.md) and [**IItemPreviewerExt::GetRelatedPart**](-search-iitempreviewerext-getrelatedpart.md) methods, and the [**LINKINFO**](-search-linkinfo.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



 

 




