---
title: IMPLTYPEFLAG Constants
description: Specifies implementation type flags.
ms.assetid: 712b7d02-0181-4a21-9221-514c062af171
topic_type:
- apiref
api_name:
- IMPLTYPEFLAG_FDEFAULT
- IMPLTYPEFLAG_FSOURCE
- IMPLTYPEFLAG_FRESTRICTED
- IMPLTYPEFLAG_FDEFAULTVTABLE
api_location:
- OaIdl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMPLTYPEFLAG Constants

Specifies implementation type flags.



| Constant/value                                                                                                                                                                                                                                                   | Description                                                                               |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| <span id="IMPLTYPEFLAG_FDEFAULT"></span><span id="impltypeflag_fdefault"></span><dl> <dt>**IMPLTYPEFLAG\_FDEFAULT**</dt> <dt>0x1</dt> </dl>                   | The interface or dispinterface represents the default for the source or sink. <br/> |
| <span id="IMPLTYPEFLAG_FSOURCE"></span><span id="impltypeflag_fsource"></span><dl> <dt>**IMPLTYPEFLAG\_FSOURCE**</dt> <dt>0x2</dt> </dl>                      | This member of a coclass is called rather than implemented. <br/>                   |
| <span id="IMPLTYPEFLAG_FRESTRICTED"></span><span id="impltypeflag_frestricted"></span><dl> <dt>**IMPLTYPEFLAG\_FRESTRICTED**</dt> <dt>0x4</dt> </dl>          | The member should not be displayed or programmable by users.<br/>                   |
| <span id="IMPLTYPEFLAG_FDEFAULTVTABLE"></span><span id="impltypeflag_fdefaultvtable"></span><dl> <dt>**IMPLTYPEFLAG\_FDEFAULTVTABLE**</dt> <dt>0x8</dt> </dl> | Sinks receive events through the VTBL. <br/>                                        |



## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>OaIdl.h</dt> </dl> |



 

 





