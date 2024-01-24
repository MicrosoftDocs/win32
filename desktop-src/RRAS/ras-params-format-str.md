---
title: RAS_PARAMS_FORMAT enumeration (Rassapi.h)
description: The RAS\_PARAMS\_FORMAT enumeration type is used in the RAS\_PARAMETERS structure to indicate the type of data associated with a media-specific key.
ms.assetid: dd2c0110-1f27-4a8f-bc61-f15588ebc4ca
keywords:
- RAS_PARAMS_FORMAT enumeration RAS
topic_type:
- apiref
api_name:
- RAS_PARAMS_FORMAT
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_PARAMS\_FORMAT enumeration

\[The **RAS\_PARAMS\_FORMAT** enumeration is not supported as of Windows Vista.\]

The **RAS\_PARAMS\_FORMAT** enumeration type is used in the [**RAS\_PARAMETERS**](ras-parameters-str.md) structure to indicate the type of data associated with a media-specific key.

## Syntax


```C++
typedef enum RAS_PARAMS_FORMAT { 
  ParamNumber  = 0,
  ParamString  = 1
} RAS_PARAMS_FORMAT;
```



## Constants

<dl> <dt>

<span id="ParamNumber"></span><span id="paramnumber"></span><span id="PARAMNUMBER"></span>**ParamNumber**
</dt> <dd>

Indicates that the data associated with the key is a number.

</dd> <dt>

<span id="ParamString"></span><span id="paramstring"></span><span id="PARAMSTRING"></span>**ParamString**
</dt> <dd>

Indicates that the data associated with the key is a string.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP<br/>                                                                |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>Rassapi.h</dt> </dl> |



## See also

<dl> <dt>

[Remote Access Service (RAS) Overview](about-remote-access-service.md)
</dt> <dt>

[RAS Server Administration Enumerations](ras-server-administration-enumerations.md)
</dt> <dt>

[**RAS\_PARAMETERS**](ras-parameters-str.md)
</dt> </dl>

 

 





