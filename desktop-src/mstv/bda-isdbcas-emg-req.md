---
title: BDA\_ISDBCAS\_EMG\_REQ structure
description: Contains the data for an EMG command.
ms.assetid: 'c622a840-9a08-40da-8fa5-6a0d668d23db'
keywords: ["BDA_ISDBCAS_EMG_REQ structure Microsoft TV Technologies", "PBDA_ISDBCAS_EMG_REQ structure pointer Microsoft TV Technologies"]
topic_type:
- apiref
api_name:
- BDA_ISDBCAS_EMG_REQ
api_location:
- bdatypes.h
api_type:
- HeaderDef
---

# BDA\_ISDBCAS\_EMG\_REQ structure

Contains the data for an EMG command.

For more information, refer to ARIB STD-B25, *Conditional Access System Specifications For Digital Broadcasting*. (This resource may not be available in some languages and countries.)

## Syntax


```C++
typedef struct _BDA_ISDBCAS_EMG_REQ {
  BYTE bCLA;
  BYTE bINS;
  BYTE bP1;
  BYTE bP2;
  BYTE bLC;
  BYTE bCardId;
  BYTE bProtocol;
  BYTE bCABroadcasterGroupId;
  BYTE bMessageControl;
  BYTE bMessageCode[MIN_DIMENSION];
} BDA_ISDBCAS_EMG_REQ, *PBDA_ISDBCAS_EMG_REQ;
```



## Members

<dl> <dt>

**bCLA**
</dt> <dd>

The CLA (Class) byte. The value must be 0x90.

</dd> <dt>

**bINS**
</dt> <dd>

The INS (Instruction) byte. The value must be 0x38.

</dd> <dt>

**bP1**
</dt> <dd>

The P1 (Parameter 1) byte.

</dd> <dt>

**bP2**
</dt> <dd>

The P2 (Parameter 2) byte.

</dd> <dt>

**bLC**
</dt> <dd>

The size, in bytes, of the data that follows this structure member.

</dd> <dt>

**bCardId**
</dt> <dd>

Card ID.

</dd> <dt>

**bProtocol**
</dt> <dd>

Protocol number.

</dd> <dt>

**bCABroadcasterGroupId**
</dt> <dd>

Broadcaster group identifier.

</dd> <dt>

**bMessageControl**
</dt> <dd>

Message control.

</dd> <dt>

**bMessageCode**
</dt> <dd>

Message code region. This array might be larger than the size given in the structure declaration. Use the value of **bLC** to determine the size.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[**IBDA\_ISDBConditionalAccess::SetIsdbCasRequest**](ibda-isdbconditionalaccess-setisdbcasrequest.md)
</dt> </dl>

 

 





