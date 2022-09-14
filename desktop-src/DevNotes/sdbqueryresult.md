---
description: Contains the results from querying the shim database for a matching executable.
ms.assetid: 6e6df118-fb64-4a97-9280-050e3b4e3a4b
title: SDBQUERYRESULT structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SDBQUERYRESULT
api_type: 
- NA
api_location: 
---

# SDBQUERYRESULT structure

Contains the results from querying the shim database for a matching executable.

## Syntax


```C++
typedef struct tagSDBQUERYRESULT {
  TAGREF atrExes[SDB_MAX_EXES];
  DWORD  adwExeFlags[SDB_MAX_EXES];
  TAGREF atrLayers[SDB_MAX_LAYERS];
  DWORD  dwLayerFlags;
  TAGREF trApphelp;
  DWORD  dwExeCount;
  DWORD  dwLayerCount;
  GUID   guidID;
  DWORD  dwFlags;
  DWORD  dwCustomSDBMap;
  GUID   rgGuidDB[SDB_MAX_SDBS];
} SDBQUERYRESULT, *PSDBQUERYRESULT;
```



## Members

<dl> <dt>

**atrExes**
</dt> <dd>

The **TAGREF** values of the matching executable files. Note that **SDB\_MAX\_EXES** is defined as 16.

</dd> <dt>

**adwExeFlags**
</dt> <dd>

This parameter can be one or more of the following values.

<dl> <dt>

<span id="SHIMREG_DISABLE_SHIM"></span><span id="shimreg_disable_shim"></span>**SHIMREG\_DISABLE\_SHIM** (0x00000001)
</dt> <dt>

<span id="SHIMREG_DISABLE_APPHELP"></span><span id="shimreg_disable_apphelp"></span>**SHIMREG\_DISABLE\_APPHELP** (0x00000002)
</dt> <dt>

<span id="SHIMREG_APPHELP_NOUI"></span><span id="shimreg_apphelp_noui"></span>**SHIMREG\_APPHELP\_NOUI** (0x00000004)
</dt> <dt>

<span id="SHIMREG_APPHELP_CANCEL"></span><span id="shimreg_apphelp_cancel"></span>**SHIMREG\_APPHELP\_CANCEL** (0x10000000)
</dt> <dt>

<span id="SHIMREG_DISABLE_SXS"></span><span id="shimreg_disable_sxs"></span>**SHIMREG\_DISABLE\_SXS** (0x00000010)
</dt> <dt>

<span id="SHIMREG_DISABLE_LAYER"></span><span id="shimreg_disable_layer"></span>**SHIMREG\_DISABLE\_LAYER** (0x00000020)
</dt> <dt>

<span id="SHIMREG_DISABLE_DRIVER"></span><span id="shimreg_disable_driver"></span>**SHIMREG\_DISABLE\_DRIVER** (0x00000040)
</dt> </dl> </dd> <dt>

**atrLayers**
</dt> <dd>

The **TAGREF** values of the matching layers. Note that **SDB\_MAX\_LAYERS** is defined as 8.

</dd> <dt>

**dwLayerFlags**
</dt> <dd>

This parameter can be one or more of the following values.

<dl> <dt>

<span id="SHIMREG_DISABLE_SHIM"></span><span id="shimreg_disable_shim"></span>**SHIMREG\_DISABLE\_SHIM** (0x00000001)
</dt> <dt>

<span id="SHIMREG_DISABLE_APPHELP"></span><span id="shimreg_disable_apphelp"></span>**SHIMREG\_DISABLE\_APPHELP** (0x00000002)
</dt> <dt>

<span id="SHIMREG_APPHELP_NOUI"></span><span id="shimreg_apphelp_noui"></span>**SHIMREG\_APPHELP\_NOUI** (0x00000004)
</dt> <dt>

<span id="SHIMREG_APPHELP_CANCEL"></span><span id="shimreg_apphelp_cancel"></span>**SHIMREG\_APPHELP\_CANCEL** (0x10000000)
</dt> <dt>

<span id="SHIMREG_DISABLE_SXS"></span><span id="shimreg_disable_sxs"></span>**SHIMREG\_DISABLE\_SXS** (0x00000010)
</dt> <dt>

<span id="SHIMREG_DISABLE_LAYER"></span><span id="shimreg_disable_layer"></span>**SHIMREG\_DISABLE\_LAYER** (0x00000020)
</dt> <dt>

<span id="SHIMREG_DISABLE_DRIVER"></span><span id="shimreg_disable_driver"></span>**SHIMREG\_DISABLE\_DRIVER** (0x00000040)
</dt> </dl> </dd> <dt>

**trApphelp**
</dt> <dd>

The **TAGREF** value of the apphelp message of the corresponding executable.

</dd> <dt>

**dwExeCount**
</dt> <dd>

The number of elements in **atrExes**.

</dd> <dt>

**dwLayerCount**
</dt> <dd>

The number of elements in **atrLayers**.

</dd> <dt>

**guidID**
</dt> <dd>

The GUID of the last executable file.

</dd> <dt>

**dwFlags**
</dt> <dd>

This parameter can be one or more of the following values.

<dl> <dt>

<span id="SHIMREG_DISABLE_SHIM"></span><span id="shimreg_disable_shim"></span>**SHIMREG\_DISABLE\_SHIM** (0x00000001)
</dt> <dt>

<span id="SHIMREG_DISABLE_APPHELP"></span><span id="shimreg_disable_apphelp"></span>**SHIMREG\_DISABLE\_APPHELP** (0x00000002)
</dt> <dt>

<span id="SHIMREG_APPHELP_NOUI"></span><span id="shimreg_apphelp_noui"></span>**SHIMREG\_APPHELP\_NOUI** (0x00000004)
</dt> <dt>

<span id="SHIMREG_APPHELP_CANCEL"></span><span id="shimreg_apphelp_cancel"></span>**SHIMREG\_APPHELP\_CANCEL** (0x10000000)
</dt> <dt>

<span id="SHIMREG_DISABLE_SXS"></span><span id="shimreg_disable_sxs"></span>**SHIMREG\_DISABLE\_SXS** (0x00000010)
</dt> <dt>

<span id="SHIMREG_DISABLE_LAYER"></span><span id="shimreg_disable_layer"></span>**SHIMREG\_DISABLE\_LAYER** (0x00000020)
</dt> <dt>

<span id="SHIMREG_DISABLE_DRIVER"></span><span id="shimreg_disable_driver"></span>**SHIMREG\_DISABLE\_DRIVER** (0x00000040)
</dt> </dl> </dd> <dt>

**dwCustomSDBMap**
</dt> <dd>

A map of the custom shim databases. The corresponding bits are set if **rgGuidDB** is valid.

</dd> <dt>

**rgGuidDB**
</dt> <dd>

The GUIDs of the shim databases. Note that **SDB\_MAX\_SDBS** is defined as 16.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SdbGetMatchingExe**](sdbgetmatchingexe.md)
</dt> </dl>

 

 




