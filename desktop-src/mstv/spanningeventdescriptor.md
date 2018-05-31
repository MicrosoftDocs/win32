---
title: SpanningEventDescriptor structure
description: Contains information about an MPEG-2 descriptor.
ms.assetid: d394b0c9-a61a-44e8-972d-0c12fd446e59
keywords:
- SpanningEventDescriptor structure Microsoft TV Technologies
topic_type:
- apiref
api_name:
- SpanningEventDescriptor
api_location:
- bdamedia.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# SpanningEventDescriptor structure

Contains information about an MPEG-2 descriptor.

## Syntax


```C++
typedef struct _SpanningEventDescriptor {
  WORD wDataLen;
  WORD wProgNumber;
  WORD wSID;
  BYTE bDescriptor[1];
} SpanningEventDescriptor;
```



## Members

<dl> <dt>

**wDataLen**
</dt> <dd>

Total size of the structure in bytes, including the size of the **bDescriptor** array.

</dd> <dt>

**wProgNumber**
</dt> <dd>

The program number associated with the descriptor.

</dd> <dt>

**wSID**
</dt> <dd>

The service ID associted with the descriptor.

</dd> <dt>

**bDescriptor**
</dt> <dd>

A byte array with the following layout:

-   Byte 0 contains the descriptor tag.
-   Byte 1 contains the length of the descriptor body.
-   The remaining bytes contain the descriptor body.

The array is larger than the size given in the structure declaration. Use the value of **wDataLen** to determine the size.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





