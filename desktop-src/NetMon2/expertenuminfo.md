---
description: The EXPERTENUMINFO structure provides information about the expert.
ms.assetid: f745997b-d753-4c4d-88b6-6978f5eaa91c
title: EXPERTENUMINFO structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EXPERTENUMINFO
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# EXPERTENUMINFO structure

The **EXPERTENUMINFO** structure provides information about the expert. Network Monitor allocates memory for the structure, and passes it to the expert when it calls the [**Register Expert**](register-expert.md) function. When the expert receives the structure, it must then fill-in all the information that Network Monitor requests.

## Syntax


```C++
typedef struct {
  char                szName[EXPERTSTRINGLENGTH];
  char                szVendor[EXPERTSTRINGLENGTH];
  char                szDescription[EXPERTSTRINGLENGTH];
  DWORD               Version;
  DWORD               Flags;
  HEXPERT             hExpert;
  char                szDllName[MAX_PATH];
  HINSTANCE           hModule;
  PEXPERTREGISTERPROC pRegisterProc;
  PEXPERTCONFIGPROC   pConfigProc;
  PEXPERTRUNPROC      pRunProc;
} EXPERTENUMINFO, *PEXPERTENUMINFO;
```



## Members

<dl> <dt>

**szName**
</dt> <dd>

Name of the expert.

</dd> <dt>

**szVendor**
</dt> <dd>

Name of the vendor that creates the expert.

</dd> <dt>

**szDescription**
</dt> <dd>

Description of the expert. The value of the **szDescription** member may be **NULL**. If the name is too long, it is truncated in the default viewer configuration.

</dd> <dt>

**Version**
</dt> <dd>

The value must be zero.

</dd> <dt>

**Flags**
</dt> <dd>

The following flags describe the expert.



| Value                                                                                                                                                                                                                                                    | Meaning                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| <span id="EXPERT_ENUM_FLAG_CONFIGURABLE"></span><span id="expert_enum_flag_configurable"></span><dl> <dt>**EXPERT\_ENUM\_FLAG\_CONFIGURABLE**</dt> </dl>                                          | The expert supports calls to the [**Configure**](configure.md) method. <br/>        |
| <span id="EXPERT_ENUM_FLAG_VIEWER_PRIVATE"></span><span id="expert_enum_flag_viewer_private"></span><dl> <dt>**EXPERT\_ENUM\_FLAG\_VIEWER\_PRIVATE**</dt> </dl>                                   | The expert requires a private (non-shared) Event Viewer. <br/>                       |
| <span id="EXPERT_ENUM_FLAG_NO_VIEWER"></span><span id="expert_enum_flag_no_viewer"></span><dl> <dt>**EXPERT\_ENUM\_FLAG\_NO\_VIEWER**</dt> </dl>                                                  | The expert does not send event notifications. <br/>                                  |
| <span id="EXPERT_ENUM_FLAG_ADD_ME_TO_RMC_IN_SUMMARY"></span><span id="expert_enum_flag_add_me_to_rmc_in_summary"></span><dl> <dt>**EXPERT\_ENUM\_FLAG\_ADD\_ME\_TO\_RMC\_IN\_SUMMARY**</dt> </dl> | When the focus is in the summary pane, the expert appears on the context menu. <br/> |
| <span id="EXPERT_ENUM_FLAG_ADD_ME_TO_RMC_IN_DETAIL"></span><span id="expert_enum_flag_add_me_to_rmc_in_detail"></span><dl> <dt>**EXPERT\_ENUM\_FLAG\_ADD\_ME\_TO\_RMC\_IN\_DETAIL**</dt> </dl>    | When the focus is in the detail pane, the expert appears on the context menu. <br/>  |



 

</dd> <dt>

**hExpert**
</dt> <dd>

Handle to the expert. When the **EXPERTENUMINFO** structure is used to register an expert, the parameter is ignored.

</dd> <dt>

**szDllName**
</dt> <dd>

Private member; do not use.

</dd> <dt>

**hModule**
</dt> <dd>

Private member; do not use.

</dd> <dt>

**pRegisterProc**
</dt> <dd>

Private member; do not use.

</dd> <dt>

**pConfigProc**
</dt> <dd>

Private member; do not use.

</dd> <dt>

**pRunProc**
</dt> <dd>

Private member; do not use.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




