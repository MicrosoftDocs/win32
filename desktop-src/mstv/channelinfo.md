---
title: ChannelInfo structure
description: Contains information about the cable television channel.
ms.assetid: 4d4c8e5b-5b9f-4cff-98c7-6d3645e677e1
keywords:
- ChannelInfo structure Microsoft TV Technologies
topic_type:
- apiref
api_name:
- ChannelInfo
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
api_location:
- bdamedia.h
api_type:
- HeaderDef
---

# ChannelInfo structure

Contains information about the cable television channel.

## Syntax


```C++
typedef struct _ChannelInfo {
  LONG  lFrequency;
  union {
    struct {
      LONG lONID;
      LONG lTSID;
      LONG lSID;
    } DVB;
    struct {
      LONG lProgNumber;
    } DC;
    struct {
      LONG lProgNumber;
    } ATSC;
  };
} ChannelInfo;
```



## Members

<dl> <dt>

**lFrequency**
</dt> <dd>

The tuning frequency.

</dd> <dt>

**DVB**
</dt> <dd>

Contains information for DVB tuning.

<dl> <dt>

**lONID**
</dt> <dd>

The original network ID.

</dd> <dt>

**lTSID**
</dt> <dd>

The transport stream ID.

</dd> <dt>

**lSID**
</dt> <dd>

The service ID for the network.

</dd> </dl> </dd> <dt>

**DC**
</dt> <dd>

Contains information the digital cable tuning.

<dl> <dt>

**lProgNumber**
</dt> <dd>

The program number.

</dd> </dl> </dd> <dt>

**ATSC**
</dt> <dd>

Contains information for ATSC tuning.

<dl> <dt>

**lProgNumber**
</dt> <dd>

The program number.

</dd> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





