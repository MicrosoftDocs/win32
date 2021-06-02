---
description: Defines a single object of a display filter.
ms.assetid: 865b55f3-9294-43c5-b4dc-eb5128ce3a38
title: FILTEROBJECT structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FILTEROBJECT
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# FILTEROBJECT structure

The **FILTEROBJECT** structure defines a single object of a display filter. The [**FilterAddObject**](filteraddobject.md) function uses **FILTEROBJECT** to build a display filter.

## Syntax


```C++
typedef struct _FILTEROBJECT {
  FILTERACTIONTYPE     Action;
  HPROPERTY            hProperty;
  union {
    VALUETYPE           Value;
    HPROTOCOL           hProtocol;
    LPVOID              lpArray;
    LPPROTOCOLTABLETYPE lpProtocolTable;
    LPADDRESS           lpAddress;
    ULPLARGEINT         lpLargeInt;
    ULPTIME             lpTime;
    LPOBJECT_IDENTIFIER lpOID;
  };
  union {
    WORD ByteCount;
    WORD ByteOffset;
  };
  struct _FILTEROBJECT  *pNext;
} FILTEROBJECT, *LPFILTEROBJECT;
```



## Members

<dl> <dt>

**Action**
</dt> <dd>

Flag that specifies the **FILTEROBJECT** action. A flag can specify a property, value, or operator.

The following table lists Action member property flags.



| Value                                                                                                                                                                                                | Meaning                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="FILTERACTION_PROPERTY"></span><span id="filteraction_property"></span><dl> <dt>**FILTERACTION\_PROPERTY**</dt> </dl>                | Contains this property.<br/>                                     |
| <span id="FILTERACTION_PROPERTYEXIST"></span><span id="filteraction_propertyexist"></span><dl> <dt>**FILTERACTION\_PROPERTYEXIST**</dt> </dl> | Indicates that a filter action property is already defined.<br/> |



 

The following table lists Action member value flags.



| Value                                                                                                                                                                                        | Meaning                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="FILTERACTION_VALUE"></span><span id="filteraction_value"></span><dl> <dt>**FILTERACTION\_VALUE**</dt> </dl>                 | Contains this value.<br/>                                             |
| <span id="FILTERACTION_STRING"></span><span id="filteraction_string"></span><dl> <dt>**FILTERACTION\_STRING**</dt> </dl>              | Contains this string.<br/>                                            |
| <span id="FILTERACTION_ARRAY"></span><span id="filteraction_array"></span><dl> <dt>**FILTERACTION\_ARRAY**</dt> </dl>                 | Contains this array.<br/>                                             |
| <span id="FILTERACTION_CONTAINSNC"></span><span id="filteraction_containsnc"></span><dl> <dt>**FILTERACTION\_CONTAINSNC**</dt> </dl>  | Indicates that a property contains a case-insensitive substring.<br/> |
| <span id="FILTERACTION_CONTAINS"></span><span id="filteraction_contains"></span><dl> <dt>**FILTERACTION\_CONTAINS**</dt> </dl>        | Indicates that a property contains a case sensitive substring.<br/>   |
| <span id="FILTERACTION_ADDRESS"></span><span id="filteraction_address"></span><dl> <dt>**FILTERACTION\_ADDRESS**</dt> </dl>           | Contains the MAC address.<br/>                                        |
| <span id="FILTERACTION_ADDRESSANY"></span><span id="filteraction_addressany"></span><dl> <dt>**FILTERACTION\_ADDRESSANY**</dt> </dl>  | Matches any MAC address.<br/>                                         |
| <span id="FILTERACTION_FROM"></span><span id="filteraction_from"></span><dl> <dt>**FILTERACTION\_FROM**</dt> </dl>                    | Indicates the **From MAC** address.<br/>                              |
| <span id="FILTERACTION_TO"></span><span id="filteraction_to"></span><dl> <dt>**FILTERACTION\_TO**</dt> </dl>                          | Indicates the **To MAC** address.<br/>                                |
| <span id="FILTERACTION_FROMTO"></span><span id="filteraction_fromto"></span><dl> <dt>**FILTERACTION\_FROMTO**</dt> </dl>              | Indicates a **From/To** pairing of MAC addresses.<br/>                |
| <span id="FILTERACTION_LARGEINT"></span><span id="filteraction_largeint"></span><dl> <dt>**FILTERACTION\_LARGEINT**</dt> </dl>        | Contains a large integer.<br/>                                        |
| <span id="FILTERACTION_TIME"></span><span id="filteraction_time"></span><dl> <dt>**FILTERACTION\_TIME**</dt> </dl>                    | Contains a **SYSTEMTIME** structure.<br/>                             |
| <span id="FILTERACTION_ADDR_ETHER"></span><span id="filteraction_addr_ether"></span><dl> <dt>**FILTERACTION\_ADDR\_ETHER**</dt> </dl> | Contains an Ethernet MAC address.<br/>                                |
| <span id="FILTERACTION_ADDR_TOKEN"></span><span id="filteraction_addr_token"></span><dl> <dt>**FILTERACTION\_ADDR\_TOKEN**</dt> </dl> | Contains a token ring MAC address.<br/>                               |
| <span id="FILTERACTION_ADDR_FDDI"></span><span id="filteraction_addr_fddi"></span><dl> <dt>**FILTERACTION\_ADDR\_FDDI**</dt> </dl>    | Contains a FDDI MAC address.<br/>                                     |
| <span id="FILTERACTION_ADDR_IPX"></span><span id="filteraction_addr_ipx"></span><dl> <dt>**FILTERACTION\_ADDR\_IPX**</dt> </dl>       | Contains an IPX MAC address.<br/>                                     |
| <span id="FILTERACTION_ADDR_IP"></span><span id="filteraction_addr_ip"></span><dl> <dt>**FILTERACTION\_ADDR\_IP**</dt> </dl>          | Contains an IP MAC address.<br/>                                      |
| <span id="FILTERACTION_OID"></span><span id="filteraction_oid"></span><dl> <dt>**FILTERACTION\_OID**</dt> </dl>                       | Contains an Object Identifier (OID).<br/>                             |



 

The following table lists Action member operator flags.



| Value                                                                                                                                                                                                        | Meaning                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| <span id="FILTERACTION_INVALID"></span><span id="filteraction_invalid"></span><dl> <dt>**FILTERACTION\_INVALID**</dt> </dl>                           | Indicates an invalid filter action.<br/>                                                                                  |
| <span id="FILTERACTION_AND"></span><span id="filteraction_and"></span><dl> <dt>**FILTERACTION\_AND**</dt> </dl>                                       | Indicates a logical **AND** statement.<br/>                                                                               |
| <span id="FILTERACTION_OR"></span><span id="filteraction_or"></span><dl> <dt>**FILTERACTION\_OR**</dt> </dl>                                          | Indicates a logical **OR** statement.<br/>                                                                                |
| <span id="FILTERACTION_XOR"></span><span id="filteraction_xor"></span><dl> <dt>**FILTERACTION\_XOR**</dt> </dl>                                       | Indicates a logical exclusive **OR** (XOR) statement.<br/>                                                                |
| <span id="FILTERACTION_NOT"></span><span id="filteraction_not"></span><dl> <dt>**FILTERACTION\_NOT**</dt> </dl>                                       | Indicates a logical **NOT** statement.<br/>                                                                               |
| <span id="FILTERACTION_EQUALNC"></span><span id="filteraction_equalnc"></span><dl> <dt>**FILTERACTION\_EQUALNC**</dt> </dl>                           | Filter action is equal and case insensitive.<br/>                                                                         |
| <span id="FILTERACTION_EQUAL"></span><span id="filteraction_equal"></span><dl> <dt>**FILTERACTION\_EQUAL**</dt> </dl>                                 | Filter action is equal and case sensitive.<br/>                                                                           |
| <span id="FILTERACTION_NOTEQUALNC"></span><span id="filteraction_notequalnc"></span><dl> <dt>**FILTERACTION\_NOTEQUALNC**</dt> </dl>                  | Logical **NOT** statement is equal and case insensitive.<br/>                                                             |
| <span id="FILTERACTION_NOTEQUAL"></span><span id="filteraction_notequal"></span><dl> <dt>**FILTERACTION\_NOTEQUAL**</dt> </dl>                        | Logical **NOT** statement is equal and is case sensitive.<br/>                                                            |
| <span id="FILTERACTION_GREATERNC"></span><span id="filteraction_greaternc"></span><dl> <dt>**FILTERACTION\_GREATERNC**</dt> </dl>                     | Filter action is greater than (>) and case insensitive.<br/>                                                           |
| <span id="FILTERACTION_GREATER"></span><span id="filteraction_greater"></span><dl> <dt>**FILTERACTION\_GREATER**</dt> </dl>                           | Filter action is greater than (>) and case sensitive.<br/>                                                             |
| <span id="FILTERACTION_LESSNC"></span><span id="filteraction_lessnc"></span><dl> <dt>**FILTERACTION\_LESSNC**</dt> </dl>                              | Filter action is less than (<) and case insensitive.<br/>                                                              |
| <span id="FILTERACTION_LESS"></span><span id="filteraction_less"></span><dl> <dt>**FILTERACTION\_LESS**</dt> </dl>                                    | Filter action is less than (<) and case sensitive.<br/>                                                                |
| <span id="FILTERACTION_GREATEREQUALNC"></span><span id="filteraction_greaterequalnc"></span><dl> <dt>**FILTERACTION\_GREATEREQUALNC**</dt> </dl>      | Filter action is greater than or equal to (>=) and case insensitive.<br/>                                              |
| <span id="FILTERACTION_GREATEREQUAL"></span><span id="filteraction_greaterequal"></span><dl> <dt>**FILTERACTION\_GREATEREQUAL**</dt> </dl>            | Filter action is greater than or equal to (>=) and case sensitive.<br/>                                                |
| <span id="FILTERACTION_LESSEQUALNC"></span><span id="filteraction_lessequalnc"></span><dl> <dt>**FILTERACTION\_LESSEQUALNC**</dt> </dl>               | Filter action is less than or equal to (<=) and case insensitive.<br/>                                                 |
| <span id="FILTERACTION_LESSEQUAL"></span><span id="filteraction_lessequal"></span><dl> <dt>**FILTERACTION\_LESSEQUAL**</dt> </dl>                     | Filter action is less than or equal to (<=) and is case sensitive.<br/>                                                |
| <span id="FILTERACTION_PLUS"></span><span id="filteraction_plus"></span><dl> <dt>**FILTERACTION\_PLUS**</dt> </dl>                                    | Add operator (+).<br/>                                                                                                    |
| <span id="FILTERACTION_MINUS"></span><span id="filteraction_minus"></span><dl> <dt>**FILTERACTION\_MINUS**</dt> </dl>                                 | Subtract operator (-).<br/>                                                                                               |
| <span id="FILTERACTION_AREBITSON"></span><span id="filteraction_arebitson"></span><dl> <dt>**FILTERACTION\_AREBITSON**</dt> </dl>                     | Indicates a bitwise operation.<br/>                                                                                       |
| <span id="FILTERACTION_AREBITSOFF"></span><span id="filteraction_arebitsoff"></span><dl> <dt>**FILTERACTION\_AREBITSOFF**</dt> </dl>                  | Indicates a non-bitwise operation.<br/>                                                                                   |
| <span id="FILTERACTION_PROTOCOLSEXIST"></span><span id="filteraction_protocolsexist"></span><dl> <dt>**FILTERACTION\_PROTOCOLSEXIST**</dt> </dl>      | Indicates that the selected protocols exist.<br/>                                                                         |
| <span id="FILTERACTION_PROTOCOLEXIST"></span><span id="filteraction_protocolexist"></span><dl> <dt>**FILTERACTION\_PROTOCOLEXIST**</dt> </dl>         | Indicates that the selected protocol exists.<br/>                                                                         |
| <span id="FILTERACTION_ARRAYEQUAL"></span><span id="filteraction_arrayequal"></span><dl> <dt>**FILTERACTION\_ARRAYEQUAL**</dt> </dl>                  | Indicates that array contents are equal. The flag must be used with a **FILTERACTION\_ARRAY** structure.<br/>             |
| <span id="FILTERACTION_DEREFPROPERTY"></span><span id="filteraction_derefproperty"></span><dl> <dt>**FILTERACTION\_DEREFPROPERTY**</dt> </dl>         | Describes a pattern match at an offset (in bytes), from the protocol.<br/>                                                |
| <span id="FILTERACTION_OID_CONTAINS"></span><span id="filteraction_oid_contains"></span><dl> <dt>**FILTERACTION\_OID\_CONTAINS**</dt> </dl>           | Evaluates a substring within an object identifier. The action must be used with the **FILTERACTION\_OID** structure.<br/> |
| <span id="FILTERACTION_OID_BEGINS_WITH"></span><span id="filteraction_oid_begins_with"></span><dl> <dt>**FILTERACTION\_OID\_BEGINS\_WITH**</dt> </dl> | Evaluates a substring that begins an object identifier. The flag must be used with **FILTERACTION\_OID**.<br/>            |
| <span id="FILTERACTION_OID_ENDS_WITH"></span><span id="filteraction_oid_ends_with"></span><dl> <dt>**FILTERACTION\_OID\_ENDS\_WITH**</dt> </dl>       | Evaluates a substring that ends an object identifier. The flag must be used with **FILTERACTION\_OID**.<br/>              |
| <span id="FILTERACTION_ADDR_VINES"></span><span id="filteraction_addr_vines"></span><dl> <dt>**FILTERACTION\_ADDR\_VINES**</dt> </dl>                 | Contains a Vines MAC address.<br/>                                                                                        |
| <span id="FILTERACTION_EXPRESSION"></span><span id="filteraction_expression"></span><dl> <dt>**FILTERACTION\_EXPRESSION**</dt> </dl>                  | Contains an action expression.<br/>                                                                                       |
| <span id="FILTERACTION_BOOL"></span><span id="filteraction_bool"></span><dl> <dt>**FILTERACTION\_BOOL**</dt> </dl>                                    | Contains a **BOOL** data type.<br/>                                                                                       |
| <span id="FILTER_DIRECTION_NEXT"></span><span id="filter_direction_next"></span><dl> <dt>**FILTER\_DIRECTION\_NEXT**</dt> </dl>                       | Controls sequential direction (Next frame) within a capture file.<br/>                                                    |
| <span id="FILTER_DIRECTION_PREV"></span><span id="filter_direction_prev"></span><dl> <dt>**FILTER\_DIRECTION\_PREV**</dt> </dl>                       | Controls sequential direction (Previous frame) within a capture file.<br/>                                                |



 

</dd> <dt>

**hProperty**
</dt> <dd>

Handle to a property key.

</dd> <dt>

**Value**
</dt> <dd>

Value of an object.

</dd> <dt>

**hProtocol**
</dt> <dd>

Handle to display filter protocol.

</dd> <dt>

**lpArray**
</dt> <dd>

Pointer to an array.

</dd> <dt>

**lpProtocolTable**
</dt> <dd>

Pointer to a protocol list designed to test the existence of protocol in a frame.

</dd> <dt>

**lpAddress**
</dt> <dd>

Pointer to the kernel type address. For example, MAC or IP.

</dd> <dt>

**lpLargeInt**
</dt> <dd>

Double **DWORD** used in a Windows NT or Windows 2000 application.

</dd> <dt>

**lpTime**
</dt> <dd>

A pointer to a **SYSTEMTIME** structure.

</dd> <dt>

**lpOID**
</dt> <dd>

A pointer to the **OBJECT\_IDENTIFIER** (OID) structure.

</dd> <dt>

**ByteCount**
</dt> <dd>

The number, in bytes, in the frame.

</dd> <dt>

**ByteOffset**
</dt> <dd>

The offset byte value of the FILTEROBJECT structure used to compare arrays.

</dd> <dt>

**pNext**
</dt> <dd>

Reserved.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




