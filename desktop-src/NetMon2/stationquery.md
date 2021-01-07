---
description: The STATIONQUERY structure provides information about a specific computer using Network Monitor.
ms.assetid: b7202c6b-e2b9-4a6f-8b87-3d11879f1d69
title: STATIONQUERY structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- STATIONQUERY
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# STATIONQUERY structure

The **STATIONQUERY** structure provides information about a specific computer using Network Monitor.

## Syntax


```C++
typedef struct _STATIONQUERY {
  DWORD Flags;
  BYTE  BCDVerMinor;
  BYTE  BCDVerMajor;
  DWORD LicenseNumber;
  BYTE  MachineName[MACHINE_NAME_LENGTH];
  BYTE  UserName[USER_NAME_LENGTH];
  BYTE  Reserved[32];
  BYTE  AdapterAddress[6];
  WCHAR WMachineName[MACHINE_NAME_LENGTH];
  WCHAR WUserName[USER_NAME_LENGTH];
} STATIONQUERY, *LPSTATIONQUERY;
```



## Members

<dl> <dt>

**Flags**
</dt> <dd>

Flags that Identify the current state of Network Monitor.



| Value                                                                                                                                                                                                                | Meaning                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <span id="STATIONQUERY_FLAGS_LOADED"></span><span id="stationquery_flags_loaded"></span><dl> <dt>**STATIONQUERY\_FLAGS\_LOADED**</dt> </dl>                   | The driver is loaded, but the kernel is not.<br/> |
| <span id="STATIONQUERY_FLAGS_RUNNING"></span><span id="stationquery_flags_running"></span><dl> <dt>**STATIONQUERY\_FLAGS\_RUNNING**</dt> </dl>                | The driver is loaded but not capturing data.<br/> |
| <span id="STATIONQUERY_FLAGS_CAPTURING"></span><span id="stationquery_flags_capturing"></span><dl> <dt>**STATIONQUERY\_FLAGS\_CAPTURING**</dt> </dl>          | The driver is actively engaged in a capture.<br/> |
| <span id="STATIONQUERY_FLAGS_TRANSMITTING"></span><span id="stationquery_flags_transmitting"></span><dl> <dt>**STATIONQUERY\_FLAGS\_TRANSMITTING**</dt> </dl> | This flag is obsolete.<br/>                       |



 

</dd> <dt>

**BCDVerMinor**
</dt> <dd>

Minor version number of Network Monitor installed on the computer.

</dd> <dt>

**BCDVerMajor**
</dt> <dd>

Major version number of Network Monitor installed on the computer.

</dd> <dt>

**LicenseNumber**
</dt> <dd>

Software license number.

</dd> <dt>

**MachineName**
</dt> <dd>

Computer manufacturer name, if any.

</dd> <dt>

**UserName**
</dt> <dd>

User name or system identifier.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**AdapterAddress**
</dt> <dd>

NIC address.

</dd> <dt>

**WMachineName**
</dt> <dd>

Unicode computer name. This member applies to Network Monitor 2.0 or later.

</dd> <dt>

**WUserName**
</dt> <dd>

Unicode user name. This member applies to Network Monitor 2.0 or later.

</dd> </dl>

## Remarks

An array of these structures is used by the [QUERYTABLE](querytable.md) structure to provide a list of the computers that are currently using Network Monitor to capture data.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[QUERYTABLE](querytable.md)
</dt> </dl>

 

 




