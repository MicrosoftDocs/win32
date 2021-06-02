---
title: RAS_PARAMETERS structure (Rassapi.h)
description: The RAS\_PARAMETERS structure is used by the RasAdminPortGetInfo function to return the name and value of a media-specific parameter associated with a port on a RAS server.
ms.assetid: b46b6176-9a0c-4d9b-b961-b20fdc41653b
keywords:
- RAS_PARAMETERS structure RAS
topic_type:
- apiref
api_name:
- RAS_PARAMETERS
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_PARAMETERS structure

\[The **RAS\_PARAMETERS** structure is not supported as of Windows Vista.\]

The **RAS\_PARAMETERS** structure is used by the [**RasAdminPortGetInfo**](rasadminportgetinfo.md) function to return the name and value of a media-specific parameter associated with a port on a RAS server.

## Syntax


```C++
typedef struct RAS_PARAMETERS {
  CHAR              P_Key[RASSAPI_MAX_PARAM_KEY_SIZE];
  RAS_PARAMS_FORMAT P_Type;
  BYTE              P_Attributes;
  RAS_PARAMS_VALUE  P_Value;
} RAS_PARAMETERS;
```



## Members

<dl> <dt>

**P\_Key**
</dt> <dd>

Specifies the name of the key that represents the media-specific parameter, such as MAXCONNECTBPS.

</dd> <dt>

**P\_Type**
</dt> <dd>

Identifies the type of data associated with the parameter. This member can be one of the following values from the [**RAS\_PARAMS\_FORMAT**](ras-params-format-str.md) enumeration.



| Value                                                                                                                                                                                | Meaning                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <span id="ParamNumber"></span><span id="paramnumber"></span><span id="PARAMNUMBER"></span><dl> <dt>**ParamNumber**</dt> </dl> | Indicates that the data associated with the key is a number.<br/> |
| <span id="ParamString"></span><span id="paramstring"></span><span id="PARAMSTRING"></span><dl> <dt>**ParamString**</dt> </dl> | Indicates that the data associated with the key is a string.<br/> |



 

</dd> <dt>

**P\_Attributes**
</dt> <dd>

Reserved.

</dd> <dt>

**P\_Value**
</dt> <dd>

Specifies the value associated with the parameter. This member is a [**RAS\_PARAMS\_VALUE**](ras-params-value-str.md) union. If the **P\_Type** member is ParamNumber, the **Number** member of the union contains the value. If **P\_Type** is ParamString, the **String** member of the union contains the value.

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

[RAS Server Administration Structures](ras-server-administration-structures.md)
</dt> <dt>

[**RasAdminAcceptNewConnection**](rasadminacceptnewconnection.md)
</dt> <dt>

[**RasAdminConnectionHangupNotification**](rasadminconnectionhangupnotification.md)
</dt> <dt>

[**RasAdminPortGetInfo**](rasadminportgetinfo.md)
</dt> </dl>

 

 





