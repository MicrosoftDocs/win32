---
description: Stores information about link types, and is used by the IItemPreviewerExt interface.
ms.assetid: c1d525ea-ee80-49fb-9447-20465b8f8654
title: LINKINFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LINKINFO
api_type: 
- NA
api_location: 
---

# LINKINFO structure

\[**LINKINFO** and [**IItemPreviewerExt**](-search-iitempreviewerext.md) are supported only on Windows XP and Windows Server 2003, and should no longer be used.\]

Stores information about link types, and is used by the [**IItemPreviewerExt**](-search-iitempreviewerext.md) interface.

## Syntax


```C++
typedef struct _LINKINFO {
  LINKTYPE type;
  BSTR     bstrContentType;
  BSTR     bstrEncoding;
  BSTR     bstrFileExt;
  VARIANT  varData;
  DWORD    dwRelatedParts;
  BSTR     bstrRelatedCid;
  Long     lCodePage;
} LINKINFO;
```



## Members

<dl> <dt>

**type**
</dt> <dd>

Type: **[**LINKTYPE**](-search-linktype.md)**

</dd> <dd>

The type of link specified when crawling or indexing indicated by a [**LINKTYPE**](-search-linktype.md) constant.

</dd> <dt>

**bstrContentType**
</dt> <dd>

Type: **BSTR**

</dd> <dd>

A **BSTR** value that specifies the content type.

</dd> <dt>

**bstrEncoding**
</dt> <dd>

Type: **BSTR**

</dd> <dd>

An EncodingStyle attribute specified in the Web Services Description Language (WSDL) file.

</dd> <dt>

**bstrFileExt**
</dt> <dd>

Type: **BSTR**

</dd> <dd>

A **BSTR** value that specifies the file name extension.

</dd> <dt>

**varData**
</dt> <dd>

Type: **VARIANT**

</dd> <dd>

A variant that specifies the variable value.

</dd> <dt>

**dwRelatedParts**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

A **DWORD** that specifies the related parts.

</dd> <dt>

**bstrRelatedCid**
</dt> <dd>

Type: **BSTR**

</dd> <dd>

A **BSTR** value that specifies a Cid property, a non-padded, signed decimal string.

</dd> <dt>

**lCodePage**
</dt> <dd>

Type: **Long**

</dd> <dd>

The code page to use for encoding the string.

</dd> </dl>

## Remarks

To preview attachments with a third-party protocol handler on computers running Windows XP or Windows Server 2003, it may be necessary to use the **LINKINFO** structure, and the following APIs: the [**IItemPreviewerExt::GetLinkedContent**](-search-iitempreviewerext-getlinkedcontent.md) and [**IItemPreviewerExt::GetRelatedPart**](-search-iitempreviewerext-getrelatedpart.md) methods, and the [**LINKTYPE**](-search-linktype.md) enumeration.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>          |



 

 




