---
description: Contains Apphelp data information.
ms.assetid: 31b305e9-1f38-4952-b4fd-963df79b1346
title: APPHELP_DATA structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- APPHELP_DATA
api_type: 
- NA
api_location: 
---

# APPHELP\_DATA structure

Contains Apphelp data information.

## Syntax


```C++
typedef struct tagAPPHELP_DATA {
  DWORD  dwFlags;
  DWORD  dwSeverity;
  DWORD  dwHTMLHelpID;
  LPTSTR szAppName;
  TAGREF trExe;
  LPTSTR szURL;
  LPTSTR szLink;
  LPTSTR szAppTitle;
  LPTSTR szContact;
  LPTSTR szDetails;
  DWORD  dwData;
  BOOL   bSPEntry;
} APPHELP_DATA, *PAPPHELP_DATA;
```



## Members

<dl> <dt>

**dwFlags**
</dt> <dd>

This parameter can be one of more of the following values.

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

**dwSeverity**
</dt> <dd>

This parameter can be APPTYPE\_NONE (0).

</dd> <dt>

**dwHTMLHelpID**
</dt> <dd>

The HTML Help identifier.

</dd> <dt>

**szAppName**
</dt> <dd>

The application name.

</dd> <dt>

**trExe**
</dt> <dd>

The [**TAGREF**](tagref.md) of the corresponding executable file.

</dd> <dt>

**szURL**
</dt> <dd>

The URL for Apphelp online link.

</dd> <dt>

**szLink**
</dt> <dd>

The link text for **szURL**.

</dd> <dt>

**szAppTitle**
</dt> <dd>

The title for the Apphelp message.

</dd> <dt>

**szContact**
</dt> <dd>

The vendor contact information.

</dd> <dt>

**szDetails**
</dt> <dd>

The detailed Apphelp message.

</dd> <dt>

**dwData**
</dt> <dd>

User-defined data managed by the application.

</dd> <dt>

**bSPEntry**
</dt> <dd>

This member is **TRUE** if this entry is in the service pack database and **FALSE** otherwise.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SdbReadApphelpDetailsData**](sdbreadapphelpdetailsdata.md)
</dt> </dl>

 

 




