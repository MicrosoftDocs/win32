---
description: Represents an entry in the attribute list.
ms.assetid: daa0c97d-2ebe-4e14-b1f8-e4be3075b13e
title: ATTRIBUTE_LIST_ENTRY structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ATTRIBUTE_LIST_ENTRY
api_type: 
- NA
api_location: 
---

# ATTRIBUTE\_LIST\_ENTRY structure

\[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.\]

Represents an entry in the attribute list.

## Syntax


```C++
typedef struct _ATTRIBUTE_LIST_ENTRY {
  ATTRIBUTE_TYPE_CODE   AttributeTypeCode;
  USHORT                RecordLength;
  UCHAR                 AttributeNameLength;
  UCHAR                 AttributeNameOffset;
  VCN                   LowestVcn;
  MFT_SEGMENT_REFERENCE SegmentReference;
  USHORT                Reserved;
  WCHAR                 AttributeName[1];
} ATTRIBUTE_LIST_ENTRY, *PATTRIBUTE_LIST_ENTRY;
```



## Members

<dl> <dt>

**AttributeTypeCode**
</dt> <dd>

The attribute type code.



| Value                                                                                                                                                                                                                                           | Meaning                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="_STANDARD_INFORMATION"></span><span id="_standard_information"></span><dl> <dt>**$STANDARD\_INFORMATION**</dt> <dt>0x10</dt> </dl> | File attributes (such as read-only and archive), time stamps (such as file creation and last modified), and the hard link count.<br/> |
| <span id="_ATTRIBUTE_LIST"></span><span id="_attribute_list"></span><dl> <dt>**$ATTRIBUTE\_LIST**</dt> <dt>0x20</dt> </dl>                   | A list of attributes that make up the file and the file reference of the MFT file record in which each attribute is located.<br/>     |
| <span id="_FILE_NAME"></span><span id="_file_name"></span><dl> <dt>**$FILE\_NAME**</dt> <dt>0x30</dt> </dl>                                  | The name of the file, in Unicode characters.<br/>                                                                                     |
| <span id="_OBJECT_ID"></span><span id="_object_id"></span><dl> <dt>**$OBJECT\_ID**</dt> <dt>0x40</dt> </dl>                                  | An 16-byte object identifier assigned by the link-tracking service.<br/>                                                              |
| <span id="_VOLUME_NAME"></span><span id="_volume_name"></span><dl> <dt>**$VOLUME\_NAME**</dt> <dt>0x60</dt> </dl>                            | The volume label. Present in the $Volume file.<br/>                                                                                   |
| <span id="_VOLUME_INFORMATION"></span><span id="_volume_information"></span><dl> <dt>**$VOLUME\_INFORMATION**</dt> <dt>0x70</dt> </dl>       | The volume information. Present in the $Volume file.<br/>                                                                             |
| <span id="_DATA"></span><span id="_data"></span><dl> <dt>**$DATA**</dt> <dt>0x80</dt> </dl>                                                  | The contents of the file.<br/>                                                                                                        |
| <span id="_INDEX_ROOT"></span><span id="_index_root"></span><dl> <dt>**$INDEX\_ROOT**</dt> <dt>0x90</dt> </dl>                               | Used to implement filename allocation for large directories.<br/>                                                                     |
| <span id="_INDEX_ALLOCATION"></span><span id="_index_allocation"></span><dl> <dt>**$INDEX\_ALLOCATION**</dt> <dt>0xA0</dt> </dl>             | Used to implement filename allocation for large directories.<br/>                                                                     |
| <span id="_BITMAP"></span><span id="_bitmap"></span><dl> <dt>**$BITMAP**</dt> <dt>0xB0</dt> </dl>                                            | A bitmap index for a large directory.<br/>                                                                                            |
| <span id="_REPARSE_POINT"></span><span id="_reparse_point"></span><dl> <dt>**$REPARSE\_POINT**</dt> <dt>0xC0</dt> </dl>                      | The reparse point data.<br/>                                                                                                          |



 

</dd> <dt>

**RecordLength**
</dt> <dd>

The size of this structure, plus the optional name buffer, in bytes.

</dd> <dt>

**AttributeNameLength**
</dt> <dd>

The size of the optional attribute name, in characters. If a name exists, this value is nonzero and the structure is followed immediately by a Unicode string of the specified number of characters.

</dd> <dt>

**AttributeNameOffset**
</dt> <dd>

Reserved.

</dd> <dt>

**LowestVcn**
</dt> <dd>

The lowest virtual cluster number (VCN) for this attribute. This member is zero unless the attribute requires multiple file record segments and unless this entry is a reference to a segment other than the first one. In this case, this value is the lowest VCN that is described by the referenced segment.

</dd> <dt>

**SegmentReference**
</dt> <dd>

The master file table (MFT) segment in which the attribute resides. See [**MFT\_SEGMENT\_REFERENCE**](mft-segment-reference.md).

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**AttributeName**
</dt> <dd>

The start of the optional attribute name.

</dd> </dl>

## Remarks

The attributes list is an ordered list of quadword-aligned **ATTRIBUTE\_LIST\_ENTRY** structures. This list is ordered first by the attribute type code and then by the attribute name (if present). No two attributes can have the same type code, name, and lowest VCN. Therefore, there can be at most one attribute for each type code without a name.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

Note that there is no associated header file for this structure.

## See also

<dl> <dt>

[Master File Table](master-file-table.md)
</dt> </dl>

 

 
