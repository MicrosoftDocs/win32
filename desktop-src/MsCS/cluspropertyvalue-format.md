---
title: ClusPropertyValue.Format property
description: The format (data type) of a property value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a53a969b-9269-43c7-81a0-178e61a23058'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Format property Failover Cluster", "Format property Failover Cluster , ClusPropertyValue object", "ClusPropertyValue object Failover Cluster , Format property"]
topic_type:
- apiref
api_name:
- ClusPropertyValue.Format
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusPropertyValue.Format property

\[The **Format** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns or sets the format (data type) of a [*property value*](p-gly.md#-wolf-property-value-gly).

This property is read-only.

## Syntax


```VB
ClusPropertyValue.Format
```



## Property value

**Long** describing the format of the property value. MsClus.h defines the following formats, enumerated by the [**CLUSTER\_PROPERTY\_FORMAT**](cluster-property-format.md) enumeration.

<dt>

<span id="CLUSPROP_FORMAT_BINARY"></span><span id="clusprop_format_binary"></span>

<span id="CLUSPROP_FORMAT_BINARY"></span><span id="clusprop_format_binary"></span>**CLUSPROP\_FORMAT\_BINARY** (1)


</dt> <dd>

Data is a binary value.

</dd> <dt>

<span id="CLUSPROP_FORMAT_DWORD"></span><span id="clusprop_format_dword"></span>

<span id="CLUSPROP_FORMAT_DWORD"></span><span id="clusprop_format_dword"></span>**CLUSPROP\_FORMAT\_DWORD** (2)


</dt> <dd>

Data is a **DWORD** value.

</dd> <dt>

<span id="CLUSPROP_FORMAT_EXPAND_SZ"></span><span id="clusprop_format_expand_sz"></span>

<span id="CLUSPROP_FORMAT_EXPAND_SZ"></span><span id="clusprop_format_expand_sz"></span>**CLUSPROP\_FORMAT\_EXPAND\_SZ** (4)


</dt> <dd>

Data is a null-terminated Unicode string with unexpanded references to environment variables.

</dd> <dt>

<span id="CLUSPROP_FORMAT_EXPANDED_SZ"></span><span id="clusprop_format_expanded_sz"></span>

<span id="CLUSPROP_FORMAT_EXPANDED_SZ"></span><span id="clusprop_format_expanded_sz"></span>**CLUSPROP\_FORMAT\_EXPANDED\_SZ** (8)


</dt> <dd>

Data is a null-terminated Unicode string with expanded references to environment variables.

</dd> <dt>

<span id="CLUSPROP_FORMAT_FILETIME"></span><span id="clusprop_format_filetime"></span>

<span id="CLUSPROP_FORMAT_FILETIME"></span><span id="clusprop_format_filetime"></span>**CLUSPROP\_FORMAT\_FILETIME** (12)


</dt> <dd>

Data is a [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284).

</dd> <dt>

<span id="CLUSPROP_FORMAT_LARGE_INTEGER"></span><span id="clusprop_format_large_integer"></span>

<span id="CLUSPROP_FORMAT_LARGE_INTEGER"></span><span id="clusprop_format_large_integer"></span>**CLUSPROP\_FORMAT\_LARGE\_INTEGER** (10)


</dt> <dd>

Data is a signed large integer.

</dd> <dt>

<span id="CLUSPROP_FORMAT_LONG"></span><span id="clusprop_format_long"></span>

<span id="CLUSPROP_FORMAT_LONG"></span><span id="clusprop_format_long"></span>**CLUSPROP\_FORMAT\_LONG** (7)


</dt> <dd>

Data is an signed **long** value.

</dd> <dt>

<span id="CLUSPROP_FORMAT_MULTI_SZ"></span><span id="clusprop_format_multi_sz"></span>

<span id="CLUSPROP_FORMAT_MULTI_SZ"></span><span id="clusprop_format_multi_sz"></span>**CLUSPROP\_FORMAT\_MULTI\_SZ** (5)


</dt> <dd>

Data is an array of null-terminated Unicode strings.

</dd> <dt>

<span id="CLUSPROP_FORMAT_SECURITY_DESCRIPTOR"></span><span id="clusprop_format_security_descriptor"></span>

<span id="CLUSPROP_FORMAT_SECURITY_DESCRIPTOR"></span><span id="clusprop_format_security_descriptor"></span>**CLUSPROP\_FORMAT\_SECURITY\_DESCRIPTOR** (9)


</dt> <dd>

Data is a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561)

</dd> <dt>

<span id="CLUSPROP_FORMAT_SZ"></span><span id="clusprop_format_sz"></span>

<span id="CLUSPROP_FORMAT_SZ"></span><span id="clusprop_format_sz"></span>**CLUSPROP\_FORMAT\_SZ** (3)


</dt> <dd>

Data is a null-terminated Unicode string.

</dd> <dt>

<span id="CLUSPROP_FORMAT_ULARGE_INTEGER"></span><span id="clusprop_format_ularge_integer"></span>

<span id="CLUSPROP_FORMAT_ULARGE_INTEGER"></span><span id="clusprop_format_ularge_integer"></span>**CLUSPROP\_FORMAT\_ULARGE\_INTEGER** (6)


</dt> <dd>

Data is an unsigned large integer.

</dd> <dt>

<span id="CLUSPROP_FORMAT_UNKNOWN"></span><span id="clusprop_format_unknown"></span>

<span id="CLUSPROP_FORMAT_UNKNOWN"></span><span id="clusprop_format_unknown"></span>**CLUSPROP\_FORMAT\_UNKNOWN** (0)


</dt> <dd>

Data is in an unknown format.

</dd> <dt>

<span id="CLUSPROP_FORMAT_USER"></span><span id="clusprop_format_user"></span>

<span id="CLUSPROP_FORMAT_USER"></span><span id="clusprop_format_user"></span>**CLUSPROP\_FORMAT\_USER** (32768)


</dt> <dd>

Data is in a user-defined format.

</dd> <dt>

<span id="CLUSPROP_FORMAT_WORD"></span><span id="clusprop_format_word"></span>

<span id="CLUSPROP_FORMAT_WORD"></span><span id="clusprop_format_word"></span>**CLUSPROP\_FORMAT\_WORD** (11)


</dt> <dd>

Data is a **WORD** value.

</dd> </dl>

## Remarks

The **Format** property corresponds to the **wFormat** member of a [**CLUSPROP\_SYNTAX**](clusprop-syntax.md) union.

For information on making constants defined by the Cluster Automation Server type library (MsClus.tlb) available to scripts, see [Creating a Cluster Automation Server Script](creating-a-cluster-automation-server-script.md).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>              |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>  |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>  |
| IID<br/>                      | IID\_ISClusPropertyValue is defined as F2E6071A-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusPropertyValue**](cluspropertyvalue-object.md)
</dt> <dt>

[**ClusPropertyValue.Type**](cluspropertyvalue-type.md)
</dt> <dt>

[**CLUSPROP\_SYNTAX**](clusprop-syntax.md)
</dt> </dl>

 

 





