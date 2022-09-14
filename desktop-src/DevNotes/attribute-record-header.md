---
description: Represents an attribute record.
ms.assetid: f9d9458c-b179-441c-9f62-ff0ac2f75329
title: ATTRIBUTE_RECORD_HEADER structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ATTRIBUTE_RECORD_HEADER
api_type: 
- NA
api_location: 
---

# ATTRIBUTE\_RECORD\_HEADER structure

\[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.\]

Represents an attribute record.

## Syntax


```C++
typedef struct _ATTRIBUTE_RECORD_HEADER {
  ATTRIBUTE_TYPE_CODE TypeCode;
  ULONG               RecordLength;
  UCHAR               FormCode;
  UCHAR               NameLength;
  USHORT              NameOffset;
  USHORT              Flags;
  USHORT              Instance;
  union {
    struct {
      ULONG  ValueLength;
      USHORT ValueOffset;
      UCHAR  Reserved[2];
    } Resident;
    struct {
      VCN      LowestVcn;
      VCN      HighestVcn;
      USHORT   MappingPairsOffset;
      UCHAR    Reserved[6];
      LONGLONG AllocatedLength;
      LONGLONG FileSize;
      LONGLONG ValidDataLength;
      LONGLONG TotalAllocated;
    } Nonresident;
  } Form;
} ATTRIBUTE_RECORD_HEADER, *PATTRIBUTE_RECORD_HEADER;
```



## Members

<dl> <dt>

**TypeCode**
</dt> <dd>

The attribute type code.



| Value                                                                                                                                                                                                                                           | Meaning                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="_STANDARD_INFORMATION"></span><span id="_standard_information"></span><dl> <dt>**$STANDARD\_INFORMATION**</dt> <dt>0x10</dt> </dl> | File attributes (such as read-only and archive), time stamps (such as file creation and last modified), and the hard link count.<br/> |
| <span id="_ATTRIBUTE_LIST"></span><span id="_attribute_list"></span><dl> <dt>**$ATTRIBUTE\_LIST**</dt> <dt>0x20</dt> </dl>                   | A list of attributes that make up the file and the file reference of the MFT file record in which each attribute is located.<br/>     |
| <span id="_FILE_NAME"></span><span id="_file_name"></span><dl> <dt>**$FILE\_NAME**</dt> <dt>0x30</dt> </dl>                                  | The name of the file, in Unicode characters.<br/>                                                                                     |
| <span id="_OBJECT_ID"></span><span id="_object_id"></span><dl> <dt>**$OBJECT\_ID**</dt> <dt>0x40</dt> </dl>                                  | An 64-byte object identifier assigned by the link-tracking service.<br/>                                                              |
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

The size of the attribute record, in bytes. This value reflects the required size for the record variant and is always rounded to the nearest quadword boundary.

</dd> <dt>

**FormCode**
</dt> <dd>

The attribute form code.



| Value                                                                                                                                                                                                                            | Meaning                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <span id="RESIDENT_FORM"></span><span id="resident_form"></span><dl> <dt>**RESIDENT\_FORM**</dt> <dt>0x00</dt> </dl>          | The value is contained in the file record and immediately follows the attribute record header.<br/> |
| <span id="NONRESIDENT_FORM"></span><span id="nonresident_form"></span><dl> <dt>**NONRESIDENT\_FORM**</dt> <dt>0x01</dt> </dl> | The value is contained in other sectors on the disk.<br/>                                           |



 

</dd> <dt>

**NameLength**
</dt> <dd>

The size of the optional attribute name, in characters, or 0 if there is no attribute name. The maximum attribute name length is 255 characters.

</dd> <dt>

**NameOffset**
</dt> <dd>

The offset of the attribute name from the start of the attribute record, in bytes. If the **NameLength** member is 0, this member is undefined.

</dd> <dt>

**Flags**
</dt> <dd>

The attribute flags.

<dl> <dt>

<span id="ATTRIBUTE_FLAG_COMPRESSION_MASK"></span><span id="attribute_flag_compression_mask"></span>**ATTRIBUTE\_FLAG\_COMPRESSION\_MASK** (0x00FF)
</dt> <dt>

<span id="ATTRIBUTE_FLAG_SPARSE"></span><span id="attribute_flag_sparse"></span>**ATTRIBUTE\_FLAG\_SPARSE** (0x8000)
</dt> <dt>

<span id="ATTRIBUTE_FLAG_ENCRYPTED"></span><span id="attribute_flag_encrypted"></span>**ATTRIBUTE\_FLAG\_ENCRYPTED** (0x4000)
</dt> </dl> </dd> <dt>

**Instance**
</dt> <dd>

The unique instance for this attribute in the file record.

</dd> <dt>

**Form**
</dt> <dd>

If the **FormCode** member is RESIDENT\_FORM, the union is a **Resident** structure. If **FormCode** is NONRESIDENT\_FORM, the union is a **Nonresident** structure.

<dl> <dt>

**Resident**
</dt> <dd> <dl> <dt>

**ValueLength**
</dt> <dd>

The size of the attribute value, in bytes.

</dd> <dt>

**ValueOffset**
</dt> <dd>

The offset to the value from the start of the attribute record, in bytes.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**Nonresident**
</dt> <dd> <dl> <dt>

**LowestVcn**
</dt> <dd>

The lowest virtual cluster number (VCN) covered by this attribute record.

</dd> <dt>

**HighestVcn**
</dt> <dd>

The highest VCN covered by this attribute record.

</dd> <dt>

**MappingPairsOffset**
</dt> <dd>

The offset to the mapping pairs array from the start of the attribute record, in bytes. For more information, see Remarks.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**AllocatedLength**
</dt> <dd>

The allocated size of the file, in bytes. This value is an even multiple of the cluster size. This member is not valid if the **LowestVcn** member is nonzero.

</dd> <dt>

**FileSize**
</dt> <dd>

The file size (highest byte that can be read plus 1), in bytes. This member is not valid if **LowestVcn** is nonzero.

</dd> <dt>

**ValidDataLength**
</dt> <dd>

The valid data length (highest initialized byte plus 1), in bytes. This value is rounded to the nearest cluster boundary. This member is not valid if **LowestVcn** is nonzero.

</dd> <dt>

**TotalAllocated**
</dt> <dd>

The total allocated for the file (the sum of the allocated clusters).

</dd> </dl> </dd> </dl> </dd> </dl>

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

Attribute records are always aligned on a quadword boundary.

If the attribute is nonresident, the attribute record header contains a list of retrieval information that provides a mapping between VCN and logical cluster number (LCN) for the attribute. If the retrieval information does not fit in the base file segment, it can be stored in an external file record segment by itself. If it still does not fit into one external file record segment, there is a provision in the attribute list to contain multiple entries for an attribute that requires additional retrieval information.

The mapping pairs array is stored in a compressed form and assumes that the information is decompressed and cached by the system. It consists of a series of NextVcn/CurrentLcn pairs. For example, if a file has a single run of 8 clusters starting at LCN 128 and the file starts at LowestVcn 0, then the mapping pairs array has just one entry, which is NextVcn=8 and CurrentLcn=128. The array is a byte stream that stores the changes to the working variables when processed sequentially. The byte stream is to be interpreted as a zero-terminated stream of triples, as follows:

count byte = *v* + (*l* \* 16)

where *v* is the number of changed low-order VCN bytes and *l* is the number of changed low-order LCN bytes.

The decompression algorithm is as follows:

1.  Initialize NextVcn to `Attribute->LowestVcn` and CurrentLcn to 0.
2.  Initialize the byte stream pointer to `(PCHAR)Attribute + Attribute->AttributeForm->Nonresident->MappingPairsOffset`.
3.  Set CurrentVcn to NextVcn.
4.  Read the next byte from the stream. If it is 0, then break; else extract *v* and *l* as previously described.
5.  Interpret the next *v* bytes as a signed quantity, with the low-order byte first. Unpack it sign-extended into 64 bits and add it to NextVcn.
6.  Interpret the next *l* bytes as a signed quantity, with the low-order byte first. Unpack it sign-extended into 64 bits and add it to CurrentLcn. If this produces a CurrentLcn of 0, then the VCNs from CurrentVcn to NextVcn–1 are unallocated.
7.  Update the cached mapping information from CurrentVcn, NextVcn, and CurrentLcn.
8.  Go to step 3.

## See also

<dl> <dt>

[Master File Table](master-file-table.md)
</dt> </dl>

 

 
