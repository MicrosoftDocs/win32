---
description: Contains data that describes an expert when it starts.
ms.assetid: 9ecd5395-d10c-411b-a6bd-fbac724d8603
title: EXPERTSTARTUPINFO structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EXPERTSTARTUPINFO
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# EXPERTSTARTUPINFO structure

The **EXPERTSTARTUPINFO** structure contains data that describes an expert when it starts.

## Syntax


```C++
typedef struct _EXPERTSTARTUPINFO {
  DWORD          Flags;
  HCAPTURE       hCapture;
  char           szCaptureFile[MAX_PATH];
  DWORD          dwFrameNumber;
  HPROTOCOL      hProtocol;
  LPPROPERTYINST lpPropertyInst;
  struct {
    BYTE BitNumber;
    BOOL bOn;
  } sBitfield;
} EXPERTSTARTUPINFO, *PEXPERTSTARTUPINFO;
```



## Members

<dl> <dt>

**Flags**
</dt> <dd>

Flags that describe the expert.

</dd> <dt>

**hCapture**
</dt> <dd>

Handle to a capture.

</dd> <dt>

**szCaptureFile**
</dt> <dd>

Name of the capture file.

</dd> <dt>

**dwFrameNumber**
</dt> <dd>

Frame number.

</dd> <dt>

**hProtocol**
</dt> <dd>

Handle to the protocol.

</dd> <dt>

**lpPropertyInst**
</dt> <dd>

Pointer to a [**PROPERTYINST**](propertyinst.md) structure.

</dd> <dt>

**sBitfield**
</dt> <dd> <dl> <dt>

**BitNumber**
</dt> <dd>

Used only if the **DataQualifier** member of the [**PROPERTYINST**](propertyinst.md) structure is set to PROP\_QUAL\_FLAGS.

</dd> <dt>

**bOn**
</dt> <dd>

Used only if the **DataQualifier** member of the [**PROPERTYINST**](propertyinst.md) structure is set to PROP\_QUAL\_FLAGS.

</dd> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




