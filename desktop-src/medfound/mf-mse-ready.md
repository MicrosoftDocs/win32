---
description: Defines the different ready states of the Media Source Extension.
ms.assetid: 7455B92F-CC2D-4743-935D-F5EBFD834397
title: MF_MSE_READY enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MF_MSE_READY
api_type: 
- HeaderDef
api_location: 
- mfmediaengine.h
---

# MF\_MSE\_READY enumeration

Defines the different ready states of the Media Source Extension.

## Syntax


```C++
typedef enum _MF_MSE_READY { 
  MF_MSE_READY_CLOSED  = 1,
  MF_MSE_READY_OPEN    = 2,
  MF_MSE_READY_ENDED   = 3
} MF_MSE_READY;
```



## Constants

<dl> <dt>

<span id="MF_MSE_READY_CLOSED"></span><span id="mf_mse_ready_closed"></span>**MF\_MSE\_READY\_CLOSED**
</dt> <dd>

The media source is closed.

</dd> <dt>

<span id="MF_MSE_READY_OPEN"></span><span id="mf_mse_ready_open"></span>**MF\_MSE\_READY\_OPEN**
</dt> <dd>

The media source is open.

</dd> <dt>

<span id="MF_MSE_READY_ENDED"></span><span id="mf_mse_ready_ended"></span>**MF\_MSE\_READY\_ENDED**
</dt> <dd>

The media source is ended.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Enumerations](media-foundation-enumerations.md)
</dt> </dl>

 

 




