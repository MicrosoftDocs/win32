---
title: RESOURCEHEADER structure
description: Contains information about the resource header itself and the data specific to this resource.
ms.assetid: e0eba7b3-a275-4ffe-9347-46361213cf48
keywords:
- RESOURCEHEADER structure Menus and Other Resources
topic_type:
- apiref
api_name:
- RESOURCEHEADER
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RESOURCEHEADER structure

Contains information about the resource header itself and the data specific to this resource. This structure is not a true C-language structure, because it contains variable-length members. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  DWORD DataSize;
  DWORD HeaderSize;
  DWORD TYPE;
  DWORD NAME;
  DWORD DataVersion;
  WORD  MemoryFlags;
  WORD  LanguageId;
  DWORD Version;
  DWORD Characteristics;
} RESOURCEHEADER;
```



## Members

<dl> <dt>

**DataSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size, in bytes, of the data that follows the resource header for this particular resource. It does not include any file padding between this resource and any resource that follows it in the resource file.

</dd> <dt>

**HeaderSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size, in bytes, of the resource header data that follows.

</dd> <dt>

**TYPE**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The resource type. The **TYPE** member can either be a numeric value or a null-terminated Unicode string that specifies the name of the type. See the following Remarks section for a description of **Name** or **Ordinal** type members.

If the **TYPE** member is a numeric value, it can specify either a standard or a user-defined resource type. If the member is a string, then it is a user-defined resource type. For a list of the predefined resource types, see [Resource Types](/windows/desktop/menurc/resource-types).

Values less than 256 are reserved for system use.

</dd> <dt>

**NAME**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

A name that identifies the particular resource. The **NAME** member, like the **TYPE** member, can either be a numeric value or a null-terminated Unicode string. See the following Remarks section for a description of **Name** or **Ordinal** type members.

You do not need to add padding for **DWORD** alignment between the **TYPE** and **NAME** members because they contain **WORD** data. However, you may need to add a **WORD** of padding after the **NAME** member to align the rest of the header on **DWORD** boundaries.

</dd> <dt>

**DataVersion**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

A predefined resource data version. This will determine which version of the resource data the application should use.

</dd> <dt>

**MemoryFlags**
</dt> <dd>

Type: **WORD**

</dd> <dd>

A set of attribute flags that can describe the state of the resource. Modifiers in the .RC script file assign these attributes to the resource. The script identifiers can assign the following flag values.

Applications do not use any of these attributes. The attributes are permitted in the script for backward compatibility with existing scripts, but they are ignored. Resources are loaded when the corresponding module is loaded, and are freed when the module is unloaded.

<dt>

<span id="MOVEABLE"></span><span id="moveable"></span>

**MOVEABLE** (0x0010)


</dt> <dd></dd> <dt>

<span id="FIXED"></span><span id="fixed"></span>

**FIXED** (~MOVEABLE)


</dt> <dd></dd> <dt>

<span id="PURE"></span><span id="pure"></span>

**PURE** (0x0020)


</dt> <dd></dd> <dt>

<span id="IMPURE"></span><span id="impure"></span>

**IMPURE** (~PURE)


</dt> <dd></dd> <dt>

<span id="PRELOAD"></span><span id="preload"></span>

**PRELOAD** (0x0040)


</dt> <dd></dd> <dt>

<span id="LOADONCALL"></span><span id="loadoncall"></span>

**LOADONCALL** (~PRELOAD)


</dt> <dd></dd> <dt>

<span id="DISCARDABLE"></span><span id="discardable"></span>

**DISCARDABLE** (0x1000)


</dt> <dd></dd> </dl> </dd> <dt>

**LanguageId**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The language for the resource or set of resources. Set the value for this member with the optional [LANGUAGE](./language-statement.md) resource definition statement. The parameters are constants from the Winnt.h file.

Each resource includes a language identifier so the system or application can select a language appropriate for the current locale of the system. If there are multiple resources of the same type and name that differ only in the language of the strings within the resources, you will need to specify a **LanguageId** for each one.

</dd> <dt>

**Version**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

A user-defined version number for the resource data that tools can use to read and write resource files. Set this value with the optional [VERSION](./version-statement.md) resource definition statement.

</dd> <dt>

**Characteristics**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Specifies user-defined information about the resource that tools can use to read and write resource files. Set this value with the optional [CHARACTERISTICS](./characteristics-statement.md) resource definition statement.

</dd> </dl>

## Remarks

A variable type member is called a **Name** or **Ordinal** member, and it is used in most places in the resource file where an identifier appears. The first **WORD** of a **Name** or **Ordinal** type member indicates whether the member is a numeric value or a string. If the first **WORD** in the member is equal to the value 0xffff, which is an invalid Unicode character, then the following **WORD** is a type number. Otherwise, the member contains a Unicode string and the first **WORD** in the member is the first character in the name string. For additional information about resource definition statements, see [Resource-Definition Statements](./resource-definition-statements.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[CHARACTERISTICS Statement](./characteristics-statement.md)
</dt> <dt>

[LANGUAGE Statement](./language-statement.md)
</dt> <dt>

[VERSION Statement](./version-statement.md)
</dt> </dl>

 

