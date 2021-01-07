---
description: Defines the Network Monitor header file structure.
ms.assetid: 944980c9-ebaa-4042-a112-d32b7a28ba21
title: CAPTUREFILE_HEADER_VALUES structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPTUREFILE_HEADER_VALUES
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# CAPTUREFILE\_HEADER\_VALUES structure

The **CAPTUREFILE\_HEADER\_VALUES** structure defines the Network Monitor header file structure.

## Syntax


```C++
typedef struct _CAPTUREFILE_HEADER_VALUES {
  DWORD      Signature;
  BYTE       BCDVerMinor;
  BYTE       BCDVerMajor;
  WORD       MacType;
  SYSTEMTIME TimeStamp;
  DWORD      FrameTableOffset;
  DWORD      FrameTableLength;
  DWORD      UserDataOffset;
  DWORD      UserDataLength;
  DWORD      CommentDataOffset;
  DWORD      CommentDataLength;
  DWORD      StatisticsOffset;
  DWORD      StatisticsLength;
  DWORD      NetworkInfoOffset;
  DWORD      NetworkInfoLength;
  DWORD      ConversationStatsOffset;
  DWORD      ConversationStatsLength;
} CAPTUREFILE_HEADER_VALUES, *LPCAPTUREFILE_HEADER_VALUES;
```



## Members

<dl> <dt>

**Signature**
</dt> <dd>

Unique identifier: 'GMBU.

</dd> <dt>

**BCDVerMinor**
</dt> <dd>

Binary, coded decimal (minor). The value of this member should be zero (0).

</dd> <dt>

**BCDVerMajor**
</dt> <dd>

Binary coded decimal (major). This value should be 2.

</dd> <dt>

**MacType**
</dt> <dd>

Topology type.

</dd> <dt>

**TimeStamp**
</dt> <dd>

Time of capture.

</dd> <dt>

**FrameTableOffset**
</dt> <dd>

Frame index table.

</dd> <dt>

**FrameTableLength**
</dt> <dd>

Frame index table size.

</dd> <dt>

**UserDataOffset**
</dt> <dd>

User data offset.

</dd> <dt>

**UserDataLength**
</dt> <dd>

User data length.

</dd> <dt>

**CommentDataOffset**
</dt> <dd>

Comment data offset.

</dd> <dt>

**CommentDataLength**
</dt> <dd>

Length of comment data.

</dd> <dt>

**StatisticsOffset**
</dt> <dd>

Offset to the **STATISTICS** structure.

</dd> <dt>

**StatisticsLength**
</dt> <dd>

Length of the **STATISTICS** structure.

</dd> <dt>

**NetworkInfoOffset**
</dt> <dd>

Offset to the **NETWORKINFO** structure.

</dd> <dt>

**NetworkInfoLength**
</dt> <dd>

Length of the **NETWORKINFO** structure.

</dd> <dt>

**ConversationStatsOffset**
</dt> <dd>

This member is not used.

</dd> <dt>

**ConversationStatsLength**
</dt> <dd>

This member is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




