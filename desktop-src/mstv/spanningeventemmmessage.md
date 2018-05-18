---
title: SpanningEventEmmMessage structure
description: Contains information about an Entitlement Management Message (EMM). For more information, refer to ARIB STD-B25, Conditional Access System Specifications for Digital Broadcasting. (This resource may not be available in some languages and countries.).
ms.assetid: 'e362a3b5-db4a-4a58-adf9-d799f83c9f36'
keywords: ["SpanningEventEmmMessage structure Microsoft TV Technologies"]
topic_type:
- apiref
api_name:
- SpanningEventEmmMessage
api_location:
- bdamedia.h
api_type:
- HeaderDef
---

# SpanningEventEmmMessage structure

Contains information about an Entitlement Management Message (EMM). For more information, refer to ARIB STD-B25, *Conditional Access System Specifications for Digital Broadcasting*. (This resource may not be available in some languages and countries.)

## Syntax


```C++
typedef struct _SpanningEventEmmMessage {
  BYTE  bCAbroadcasterGroupId;
  BYTE  bMessageControl;
  WORD  wServiceId;
  WORD  wTableIdExtension;
  BYTE  bDeletionStatus;
  BYTE  bDisplayingDuration1;
  BYTE  bDisplayingDuration2;
  BYTE  bDisplayingDuration3;
  BYTE  bDisplayingCycle;
  BYTE  bFormatVersion;
  BYTE  bDisplayPosition;
  WORD  wMessageLength;
  WCHAR szMessageArea[MIN_DIMENSION];
} SpanningEventEmmMessage;
```



## Members

<dl> <dt>

**bCAbroadcasterGroupId**
</dt> <dd>

The value of the ca\_broadcaster\_group\_ID field from the Condition Access (CA) service descriptor.

</dd> <dt>

**bMessageControl**
</dt> <dd>

The value of the message\_control field from the CA service descriptor.

</dd> <dt>

**wServiceId**
</dt> <dd>

The service ID for the network.

</dd> <dt>

**wTableIdExtension**
</dt> <dd>

The table ID extension. If this value is zero, the remaining structure members are ignored.

</dd> <dt>

**bDeletionStatus**
</dt> <dd>

The value of the deletion\_status field.

</dd> <dt>

**bDisplayingDuration1**
</dt> <dd>

The value of the displaying\_duration1 field.

</dd> <dt>

**bDisplayingDuration2**
</dt> <dd>

The value of the displaying\_duration2 field.

</dd> <dt>

**bDisplayingDuration3**
</dt> <dd>

The value of the displaying\_duration3 field.

</dd> <dt>

**bDisplayingCycle**
</dt> <dd>

The value of the displaying\_cycle field.,

</dd> <dt>

**bFormatVersion**
</dt> <dd>

The value of the format\_version field.

</dd> <dt>

**bDisplayPosition**
</dt> <dd>

The display position.

</dd> <dt>

**wMessageLength**
</dt> <dd>

The number of bytes of data in the **szMessageArea** array.

</dd> <dt>

**szMessageArea**
</dt> <dd>

The contents of the message. This array might be larger than the size given in the structure declaration. Use the value of **szMessageArea** to determine the size.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





