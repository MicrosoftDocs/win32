---
description: The PROPERTYINFO data structure defines one property of the protocol.
ms.assetid: '878777ab-141d-4cc5-b0c1-f2ac8f770bf0'
title: PROPERTYINFO structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PROPERTYINFO
api_type:
- HeaderDef
api_location:
- Netmon.h
---

# PROPERTYINFO structure

The **PROPERTYINFO** data structure defines one property of the protocol.

## Syntax


```C++
typedef struct _PROPERTYINFO {
  HPROPERTY hProperty;
  DWORD     Version;
  LPSTR     Label;
  LPSTR     Comment;
  BYTE      DataType;
  BYTE      DataQualifier;
  union {
    LPVOID  lpExtendedInfo;
    LPRANGE lpRange;
    LPSET   lpSet;
    DWORD   Bitmask;
    DWORD   Value;
  };
  WORD      FormatStringSize;
  LPVOID    InstanceData;
} PROPERTYINFO, *LPPROPERTYINFO;
```



## Members

<dl> <dt>

**hProperty**
</dt> <dd>

Set this field to zero. On output, Network Monitor returns a handle to the property after the property is added to the property database.

</dd> <dt>

**Version**
</dt> <dd>

Reserved. Must be set to zero.

</dd> <dt>

**Label**
</dt> <dd>

Name of the property.

</dd> <dt>

**Comment**
</dt> <dd>

Description of the property. The description appears on the Network Monitor status bar.

</dd> <dt>

**DataType**
</dt> <dd>

Data type of the property. This member can have one of the following values.



| Value                                                                                                                                                                                                       | Meaning                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PROP_TYPE_VOID"></span><span id="prop_type_void"></span><dl> <dt>**PROP\_TYPE\_VOID**</dt> </dl>                                           | Property type is unknown. There is no implied length or format.<br/>                                                                                                                                                                                                                                  |
| <span id="PROP_TYPE_SUMMARY"></span><span id="prop_type_summary"></span><dl> <dt>**PROP\_TYPE\_SUMMARY**</dt> </dl>                                  | Summarizing property type. Indicates the first property instance that the parser attaches to a frame. PROP\_TYPE\_SUMMARY can serve as a placeholder for groups of properties. This value indicates that the property is not defined in the protocol *RFC*.<br/> |
| <span id="PROP_TYPE_BYTE"></span><span id="prop_type_byte"></span><dl> <dt>**PROP\_TYPE\_BYTE**</dt> </dl>                                           | Numeric data with a size of one byte (8-bit entity).<br/>                                                                                                                                                                                                                                             |
| <span id="PROP_TYPE_WORD"></span><span id="prop_type_word"></span><dl> <dt>**PROP\_TYPE\_WORD**</dt> </dl>                                           | Numeric data with a size of two bytes (16-bit entity).<br/>                                                                                                                                                                                                                                           |
| <span id="PROP_TYPE_DWORD"></span><span id="prop_type_dword"></span><dl> <dt>**PROP\_TYPE\_DWORD**</dt> </dl>                                        | Numeric data with a size of four bytes (32-bit entity).<br/>                                                                                                                                                                                                                                          |
| <span id="PROP_TYPE_LARGEINT"></span><span id="prop_type_largeint"></span><dl> <dt>**PROP\_TYPE\_LARGEINT**</dt> </dl>                               | Numeric data with a size of eight bytes (64-bit entity).<br/>                                                                                                                                                                                                                                         |
| <span id="PROP_TYPE_ADDR"></span><span id="prop_type_addr"></span><dl> <dt>**PROP\_TYPE\_ADDR**</dt> </dl>                                           | MAC address (6-byte entity).<br/>                                                                                                                                                                                                                                                                     |
| <span id="PROP_TYPE_TIME"></span><span id="prop_type_time"></span><dl> <dt>**PROP\_TYPE\_TIME**</dt> </dl>                                           | **SYSTEMTIME** structure.<br/>                                                                                                                                                                                                                                                                        |
| <span id="PROP_TYPE_STRING"></span><span id="prop_type_string"></span><dl> <dt>**PROP\_TYPE\_STRING**</dt> </dl>                                     | ASCII text data. This data type is not NULL-terminated. <br/> For Unicode data, when ASCII text data is specified, the IFLAG\_UNICODE flag must also be set when the attach property instance function is called.<br/>                                                                          |
| <span id="PROP_TYPE_IP_ADDRESS"></span><span id="prop_type_ip_address"></span><dl> <dt>**PROP\_TYPE\_IP\_ADDRESS**</dt> </dl>                        | IP Address. (4-byte entity).<br/>                                                                                                                                                                                                                                                                     |
| <span id="PROP_TYPE_IPX_ADDRESS"></span><span id="prop_type_ipx_address"></span><dl> <dt>**PROP\_TYPE\_IPX\_ADDRESS**</dt> </dl>                     | IPX Address. (10-byte entity).<br/>                                                                                                                                                                                                                                                                   |
| <span id="PROP_TYPE_BYTESWAPPED_WORD"></span><span id="prop_type_byteswapped_word"></span><dl> <dt>**PROP\_TYPE\_BYTESWAPPED\_WORD**</dt> </dl>      | Obsolete. For byte-swapped WORD data, set **DataType** to PROP\_TYPE\_WORD and set the IFLAG\_SWAPPED flag when calling an **Attach** property instance function.<br/>                                                                                                                                |
| <span id="PROP_TYPE_BYTESWAPPED_DWORD"></span><span id="prop_type_byteswapped_dword"></span><dl> <dt>**PROP\_TYPE\_BYTESWAPPED\_DWORD**</dt> </dl>   | Obsolete. For byte-swapped DWORD data, set **DataType** to PROP\_TYPE\_DWORD and set the IFLAG\_SWAPPED flag when calling an **Attach** property instance function.<br/>                                                                                                                              |
| <span id="PROP_TYPE_TYPED_STRING"></span><span id="prop_type_typed_string"></span><dl> <dt>**PROP\_TYPE\_TYPED\_STRING**</dt> </dl>                  | Obsolete. For variable-type string data, set **DataType** to PROP\_TYPE\_STRING and set the IFLAG\_UNICODE flag when calling an **Attach** property instance function.<br/>                                                                                                                           |
| <span id="PROP_TYPE_RAW_DATA"></span><span id="prop_type_raw_data"></span><dl> <dt>**PROP\_TYPE\_RAW\_DATA**</dt> </dl>                              | Raw data of unknown length and format.<br/>                                                                                                                                                                                                                                                           |
| <span id="PROP_TYPE_COMMENT"></span><span id="prop_type_comment"></span><dl> <dt>**PROP\_TYPE\_COMMENT**</dt> </dl>                                  | Same as PROP\_TYPE\_VOID.<br/>                                                                                                                                                                                                                                                                        |
| <span id="PROP_TYPE_SRCFRIENDLYNAME"></span><span id="prop_type_srcfriendlyname"></span><dl> <dt>**PROP\_TYPE\_SRCFRIENDLYNAME**</dt> </dl>          | Address of source-friendly name. Network Monitor does not provide built-in formatting support for this data type.<br/>                                                                                                                                                                                |
| <span id="PROP_TYPE_DSTFRIENDLYNAME"></span><span id="prop_type_dstfriendlyname"></span><dl> <dt>**PROP\_TYPE\_DSTFRIENDLYNAME**</dt> </dl>          | Address of destination friendly name. Network Monitor does not provide built-in formatting support for this data type.<br/>                                                                                                                                                                           |
| <span id="PROP_TYPE_TOKENRING_ADDRESS"></span><span id="prop_type_tokenring_address"></span><dl> <dt>**PROP\_TYPE\_TOKENRING\_ADDRESS**</dt> </dl>   | Token-ring address. Network Monitor does not provide built-in formatting support for this data type.<br/>                                                                                                                                                                                             |
| <span id="PROP_TYPE_FDDI_ADDRESS"></span><span id="prop_type_fddi_address"></span><dl> <dt>**PROP\_TYPE\_FDDI\_ADDRESS**</dt> </dl>                  | FDDI address. Network Monitor does not provide built-in formatting support for this data type.<br/>                                                                                                                                                                                                   |
| <span id="PROP_TYPE_ETHERNET_ADDRESS"></span><span id="prop_type_ethernet_address"></span><dl> <dt>**PROP\_TYPE\_ETHERNET\_ADDRESS**</dt> </dl>      | Ethernet address. Network Monitor does not provide built-in formatting support for this data type.<br/>                                                                                                                                                                                               |
| <span id="PROP_TYPE_OBJECT_IDENTIFIER"></span><span id="prop_type_object_identifier"></span><dl> <dt>**PROP\_TYPE\_OBJECT\_IDENTIFIER**</dt> </dl>   | BER-encoded SNMP object identifier.<br/>                                                                                                                                                                                                                                                              |
| <span id="PROP_TYPE_VINES_IP_ADDRESS"></span><span id="prop_type_vines_ip_address"></span><dl> <dt>**PROP\_TYPE\_VINES\_IP\_ADDRESS**</dt> </dl>     | Vines IP address (6-byte entity).<br/>                                                                                                                                                                                                                                                                |
| <span id="PROP_TYPE_VAR_LEN_SMALL_INT"></span><span id="prop_type_var_len_small_int"></span><dl> <dt>**PROP\_TYPE\_VAR\_LEN\_SMALL\_INT**</dt> </dl> | Numeric value without a pre-determined length, but no more than 8 bytes long. The length of the attached data determines the length of the value.<br/>                                                                                                                                                |



 

</dd> <dt>

**DataQualifier**
</dt> <dd>

The data qualifier of a property. This member provides precise information about the data type.

**DataQualifier** can have one of the following values.



| Value                                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PROP_QUAL_NONE"></span><span id="prop_qual_none"></span><dl> <dt>**PROP\_QUAL\_NONE**</dt> </dl>                                      | The property data type is the only specification of the property. <br/> When this value is set, the union member of the structure is set to **NULL**, and then ignored.<br/>                                                                                                                                        |
| <span id="PROP_QUAL_RANGE"></span><span id="prop_qual_range"></span><dl> <dt>**PROP\_QUAL\_RANGE**</dt> </dl>                                   | The numeric value is expected to be within a given range. Define the range in the **lpRange** member.<br/>                                                                                                                                                                                                                |
| <span id="PROP_QUAL_SET"></span><span id="prop_qual_set"></span><dl> <dt>**PROP\_QUAL\_SET**</dt> </dl>                                         | The value of a property is compared to a set of values that are specified in the **lpSet** member of the structure's union. The value of a property can be a **BYTE**, **WORD**, **DWORD**, **LARGEINT** or **TIME**.<br/>                                                                                                |
| <span id="PROP_QUAL_BITFIELD"></span><span id="prop_qual_bitfield"></span><dl> <dt>**PROP\_QUAL\_BITFIELD**</dt> </dl>                          | Obsolete.<br/>                                                                                                                                                                                                                                                                                                            |
| <span id="PROP_QUAL_LABELED_SET"></span><span id="prop_qual_labeled_set"></span><dl> <dt>**PROP\_QUAL\_LABELED\_SET**</dt> </dl>                | The value of a property is compared to a value in a set of value label pairs. The value label pairs are specified in the **lpSet** member of the structure's union. <br/> At display time, if the value of the property matches a value in the set, then both a value, and the associated label are displayed.<br/> |
| <span id="PROP_QUAL_LABELED_BITFIELD"></span><span id="prop_qual_labeled_bitfield"></span><dl> <dt>**PROP\_QUAL\_LABELED\_BITFIELD**</dt> </dl> | Obsolete. Use PROP\_QUAL\_FLAGS instead.<br/>                                                                                                                                                                                                                                                                             |
| <span id="PROP_QUAL_CONST"></span><span id="prop_qual_const"></span><dl> <dt>**PROP\_QUAL\_CONST**</dt> </dl>                                   | The value of a property is compared to a constant that is specified in the **Value** member of the union. <br/> At display time, if the property values and constant do not match, a formatted error message appears with the value set as Normal.<br/>                                                             |
| <span id="PROP_QUAL_FLAGS"></span><span id="prop_qual_flags"></span><dl> <dt>**PROP\_QUAL\_FLAGS**</dt> </dl>                                   | The value of the property is compared to specific BITs identified in the **lpSet** member of the union.<br/>                                                                                                                                                                                                              |
| <span id="PROP_QUAL_ARRAY"></span><span id="prop_qual_array"></span><dl> <dt>**PROP\_QUAL\_ARRAY**</dt> </dl>                                   | The value of a property specifies an array of values. The length of attached data determines the length of an array. <br/> When the PROP\_QUAL\_ARRAY value is set, the union member of the **PROPERTYINFO** data structure is set to **NULL** and ignored.<br/>                                                    |



 

</dd> <dt>

**lpExtendedInfo**
</dt> <dd>

Reserved (member of union).

</dd> <dt>

**lpRange**
</dt> <dd>

Pointer to a [RANGE](range.md) structure that defines a range of values. This member must be set if the **DataQualifier** member of this structure is set to PROP\_QUAL\_RANGE (member of union).

</dd> <dt>

**lpSet**
</dt> <dd>

Pointer to a [SET](set.md) structure that specifies a set of values or labels. This member must be set if the **DataQualifier** member of the structure is set to PROP\_QUAL\_SET, PROP\_QUAL\_LABELED\_SET, or PROP\_QUAL\_FLAGS (member of union).

</dd> <dt>

**Bitmask**
</dt> <dd>

Obsolete (member of union).

</dd> <dt>

**Value**
</dt> <dd>

Constant value used when the **DataQualifier** is set to PROP\_QUAL\_CONST (member of union).

</dd> <dt>

**FormatStringSize**
</dt> <dd>

Maximum size used only for the property description.

</dd> <dt>

**InstanceData**
</dt> <dd>

Specify the format function that is called to format the displayed data for the property. To use the generic formatter, specify the **FormatPropertyInstance** function.

</dd> </dl>

## Remarks

The **PROPERTYINFO** structure is used in calls to the [AddProperty](/previous-versions/bb251873(v=msdn.10)) function. The **AddProperty** function adds a single property definition to the parser [*property database*](p.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[AddProperty](/previous-versions/bb251873(v=msdn.10))
</dt> <dt>

[RANGE](range.md)
</dt> <dt>

[SET](set.md)
</dt> </dl>

 

