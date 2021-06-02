---
description: The EXPERTCONFIG structure contains the configuration data of the expert. The expert overlays the RawConfigData member with an expert-specific structure.
ms.assetid: 6167e846-d58c-40a8-94f7-c6d6185ae724
title: EXPERTCONFIG structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EXPERTCONFIG
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# EXPERTCONFIG structure

The **EXPERTCONFIG** structure contains the configuration data of the expert. The expert overlays the **RawConfigData** member with an expert-specific structure.

## Syntax


```C++
typedef struct {
  DWORD RawConfigLength;
  BYTE  RawConfigData[];
} EXPERTCONFIG, *PEXPERTCONFIG;
```



## Members

<dl> <dt>

**RawConfigLength**
</dt> <dd>

Total length of the structure, including the four bytes used for the member. Network Monitor uses the value when the structure is saved-to and read-from a disk drive.

</dd> <dt>

**RawConfigData**
</dt> <dd>

Configuration data. The expert must add the configuration data. For example, suppose that you had a data structure that looked like this.

``` syntax
typedef struct
{
    DWORD       RawConfigLength;   // Overlay of structure
    DWORD       PickNumEvents;
    DWORD       NumEventsSpecific;
    DWORD       PickSpeedThroughCapture;
    DWORD       PickStartup;
    DWORD       PickAttachProperties;
} TESTEXPERTCONFIG;
typedef TESTEXPERTCONFIG* LPTESTEXPERTCONFIG;
```

Note that **RawConfigLength** ensures that the overlay works correctly. When you use the data, your code might look like this:

``` syntax
BOOL WINAPI Configure( 
    HEXPERTKEY ExpertKey,
    PEXPERTCONFIG * ppConfig,
    PEXPERTSTARTUPINFO pStartupInfo,
    DWORD StartupFlags,
    HWND hWnd
)
{
    LPTESTEXPERTCONFIG  lpConfig;

    //...
    lpConfig = (LPTESTEXPERTCONFIG)(*ppConfig);
    //...
}
```

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




