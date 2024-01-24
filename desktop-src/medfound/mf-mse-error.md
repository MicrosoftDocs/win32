---
description: Defines the different error states of the Media Source Extension.
ms.assetid: 8FD54833-F60B-49E8-A673-6130F3B06160
title: MF_MSE_ERROR enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MF_MSE_ERROR
api_type: 
- HeaderDef
api_location: 
- mfmediaengine.h
---

# MF\_MSE\_ERROR enumeration

Defines the different error states of the Media Source Extension.

## Syntax


```C++
typedef enum _MF_MSE_ERROR { 
  MF_MSE_ERROR_NOERROR        =  0,
  MF_MSE_ERROR_NETWORK        = 1,
  MF_MSE_ERROR_DECODE         = 2,
  MF_MSE_ERROR_UNKNOWN_ERROR  =  3
} MF_MSE_ERROR;
```



## Constants

<dl> <dt>

<span id="MF_MSE_ERROR_NOERROR"></span><span id="mf_mse_error_noerror"></span>**MF\_MSE\_ERROR\_NOERROR**
</dt> <dd>

Specifies no error.

</dd> <dt>

<span id="MF_MSE_ERROR_NETWORK"></span><span id="mf_mse_error_network"></span>**MF\_MSE\_ERROR\_NETWORK**
</dt> <dd>

Specifies an error with the network.

</dd> <dt>

<span id="MF_MSE_ERROR_DECODE"></span><span id="mf_mse_error_decode"></span>**MF\_MSE\_ERROR\_DECODE**
</dt> <dd>

Specifies an error with decoding.

</dd> <dt>

<span id="MF_MSE_ERROR_UNKNOWN_ERROR"></span><span id="mf_mse_error_unknown_error"></span>**MF\_MSE\_ERROR\_UNKNOWN\_ERROR**
</dt> <dd>

Specifies an unknown error.

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

 

 




