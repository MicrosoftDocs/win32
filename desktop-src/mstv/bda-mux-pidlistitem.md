---
title: BDA\_MUX\_PIDLISTITEM structure
description: Specifies a packet identifier (PID) for the IBDA\_MUX interface.
ms.assetid: 50355317-7133-445c-9990-ab536801e555
keywords:
- BDA_MUX_PIDLISTITEM structure Microsoft TV Technologies
- PBDA_MUX_PIDLISTITEM structure pointer Microsoft TV Technologies
topic_type:
- apiref
api_name:
- BDA_MUX_PIDLISTITEM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
api_location:
- bdatypes.h
api_type:
- HeaderDef
---

# BDA\_MUX\_PIDLISTITEM structure

Specifies a packet identifier (PID) for the [**IBDA\_MUX**](/windows/desktop/api/bdaiface/nn-bdaiface-ibda_mux) interface.

## Syntax


```C++
typedef struct _BDA_MUX_PIDLISTITEM {
  USHORT       usPIDNumber;
  USHORT       usProgramNumber;
  MUX_PID_TYPE ePIDType;
} BDA_MUX_PIDLISTITEM, *PBDA_MUX_PIDLISTITEM;
```



## Members

<dl> <dt>

**usPIDNumber**
</dt> <dd>

The PID number.

</dd> <dt>

**usProgramNumber**
</dt> <dd>

The associated service identifier, if applicable.

</dd> <dt>

**ePIDType**
</dt> <dd>

The stream type, specified as a member of the [**MUX\_PID\_TYPE**](mux-pid-type.md) enumeration.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[**IBDA\_MUX**](/windows/desktop/api/bdaiface/nn-bdaiface-ibda_mux)
</dt> </dl>

 

 





