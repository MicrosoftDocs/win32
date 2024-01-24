---
title: WMDMMetadataView structure
description: The WMDMMetadataView structure defines the metadata view. Content is organized based on this definition.
ms.assetid: 787d2295-d433-451d-a1fc-6f73585e10d6
keywords:
- WMDMMetadataView structure windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDMMetadataView
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDMMetadataView structure

The **WMDMMetadataView** structure defines the metadata view. Content is organized based on this definition.

## Syntax


```C++
typedef struct _WMDMMetadataView {
  WCHAR *pwszViewName;
  UINT  nDepth;
  WCHAR **ppwszTags;
} WMDMMetadataView;
```



## Members

<dl> <dt>

**pwszViewName**
</dt> <dd>

Pointer to a wide-character null-terminated string containing the name of the view. This is used as the name of the root node under which this view is presented.

</dd> <dt>

**nDepth**
</dt> <dd>

Integer containing the depth of the view, which indicates how many nested metadata tags are used for the view.

</dd> <dt>

**ppwszTags**
</dt> <dd>

Array of metadata tag strings for the nested tags.

</dd> </dl>

## Examples

The following code creates a metadata view:


```C++
WMDMMetadataView view;
view.pwszName = L"My View";
view.nDepth = 3;  // genre, artist, album
LPCWSTR wszTagArray[3]; 
wszTagArray[0] = g_wszWMDMGenre;
wszTagArray[1] = g_wszWMDMAuthor;
wszTagArray[2] = g_wszWMDMAlbumTitle;
view.ppwszTags = wszTagArray;
```



The preceding code organizes content as follows:

<dl> My View<dl> Genre1<dl> Artist1<dl> Album1<dl> Song1  
Song2  
...  
</dl> </dd> Album2  
...  
</dl> </dd> Artist2<dl> Album1<dl> Song1  
Song2  
...  
</dl> </dd> Album2  
...  
</dl> </dd> </dl> </dd> Genre2<dl> Artist1<dl> Album1<dl> Song1  
Song2  
...  
</dl> </dd> Album2  
...  
</dl> </dd> Artist2<dl> Album1<dl> Song1  
Song2  
...  
</dl> </dd> Album2  
...  
</dl> </dd> ...  
</dl> </dd> ...  
</dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





