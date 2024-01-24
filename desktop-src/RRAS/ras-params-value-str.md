---
title: RAS_PARAMS_VALUE union (Rassapi.h)
description: The RAS\_PARAMS\_VALUE union is used in the RAS\_PARAMETERS structure to store the data associated with a media-specific parameter.
ms.assetid: 43284ee4-9bd4-4019-860f-0fb7ff3f38ee
keywords:
- RAS_PARAMS_VALUE union RAS
topic_type:
- apiref
api_name:
- RAS_PARAMS_VALUE
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_PARAMS\_VALUE union

\[The **RAS\_PARAMS\_VALUE** union is not supported as of Windows Vista.\]

The **RAS\_PARAMS\_VALUE** union is used in the [**RAS\_PARAMETERS**](ras-parameters-str.md) structure to store the data associated with a media-specific parameter. The **P\_Type** member of the **RAS\_PARAMETERS** structure uses a value from the [**RAS\_PARAMS\_FORMAT**](ras-params-format-str.md) enumeration to indicate the type of value currently stored in **RAS\_PARAMS\_VALUE**.

## Syntax


```C++
typedef union RAS_PARAMS_VALUE {
  DWORD  Number;
  struct {
    DWORD Length;
    PCHAR Data;
  } String;
} RAS_PARAMS_VALUE;
```



## Members

<dl> <dt>

**Number**
</dt> <dd>

If the **P\_Type** member of the [**RAS\_PARAMETERS**](ras-parameters-str.md) structure is ParamNumber, the **Number** member contains the value of the media-specific parameter. For example, the MAXCONNECTBPS parameter is of type ParamNumber, and the value might be 19200.

If the **P\_Type** member of the [**RAS\_PARAMETERS**](ras-parameters-str.md) structure is ParamNumber, the **Number** member contains the value of the media-specific parameter. For example, the MAXCONNECTBPS parameter is of type ParamNumber, and the value might be 19200.

</dd> <dt>

**String**
</dt> <dd>

If the **P\_Type** member of the [**RAS\_PARAMETERS**](ras-parameters-str.md) structure is ParamString, the **String** member contains the value of the media-specific parameter.

<dl> <dt>

**Length**
</dt> <dd>

Specifies the length, in characters, of the string pointed to by the **Data** member.

</dd> <dt>

**Data**
</dt> <dd>

Pointer to a buffer that contains the string value of a media-specific parameter.

</dd> </dl> </dd> </dl>

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

[RAS Server Administration Union](ras-server-administration-union.md)
</dt> <dt>

[**RAS\_PARAMETERS**](ras-parameters-str.md)
</dt> <dt>

[**RAS\_PARAMS\_FORMAT**](ras-params-format-str.md)
</dt> </dl>

 

 





