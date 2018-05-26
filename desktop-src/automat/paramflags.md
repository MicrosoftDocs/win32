---
title: PARAMFLAG Constants
description: Specifies parameter flags.
ms.assetid: 0273322a-1ba6-48eb-8eb7-f273f5240bdd
topic_type:
- apiref
api_name:
- PARAMFLAG_NONE
- PARAMFLAG_FIN
- PARAMFLAG_FOUT
- PARAMFLAG_FLCID
- PARAMFLAG_FRETVAL
- PARAMFLAG_FOPT
- PARAMFLAG_FHASDEFAULT
- PARAMFLAG_FHASCUSTDATA
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

# PARAMFLAG Constants

Specifies parameter flags.



| Constant/value                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                   |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PARAMFLAG_NONE"></span><span id="paramflag_none"></span><dl> <dt>**PARAMFLAG\_NONE**</dt> <dt>0</dt> </dl>                            | Whether the parameter passes or receives information is unspecified. [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interfaces can use this flag. <br/>                                                                                                 |
| <span id="PARAMFLAG_FIN"></span><span id="paramflag_fin"></span><dl> <dt>**PARAMFLAG\_FIN**</dt> <dt>0x1</dt> </dl>                             | Parameter passes information from the caller to the callee. <br/>                                                                                                                                                                       |
| <span id="PARAMFLAG_FOUT"></span><span id="paramflag_fout"></span><dl> <dt>**PARAMFLAG\_FOUT**</dt> <dt>0x2</dt> </dl>                          | Parameter returns information from the callee to the caller. <br/>                                                                                                                                                                      |
| <span id="PARAMFLAG_FLCID"></span><span id="paramflag_flcid"></span><dl> <dt>**PARAMFLAG\_FLCID**</dt> <dt>0x4</dt> </dl>                       | Parameter is the LCID of a client application.<br/>                                                                                                                                                                                     |
| <span id="PARAMFLAG_FRETVAL"></span><span id="paramflag_fretval"></span><dl> <dt>**PARAMFLAG\_FRETVAL**</dt> <dt>0x8</dt> </dl>                 | Parameter is the return value of the member.<br/>                                                                                                                                                                                       |
| <span id="PARAMFLAG_FOPT"></span><span id="paramflag_fopt"></span><dl> <dt>**PARAMFLAG\_FOPT**</dt> <dt>0x10</dt> </dl>                         | Parameter is optional. The pPARAMDescEx field contains a pointer to a VARIANT describing the default value for this parameter, if the PARAMFLAG\_FOPT and PARAMFLAG\_FHASDEFAULT bit of wParamFlags is set. <br/>                       |
| <span id="PARAMFLAG_FHASDEFAULT"></span><span id="paramflag_fhasdefault"></span><dl> <dt>**PARAMFLAG\_FHASDEFAULT**</dt> <dt>0x20</dt> </dl>    | Parameter has default behaviors defined. The pPARAMDescEx field contains a pointer to a VARIANT that describes the default value for this parameter, if the PARAMFLAG\_FOPT and PARAMFLAG\_FHASDEFAULT bit of wParamFlags is set. <br/> |
| <span id="PARAMFLAG_FHASCUSTDATA"></span><span id="paramflag_fhascustdata"></span><dl> <dt>**PARAMFLAG\_FHASCUSTDATA**</dt> <dt>0x40</dt> </dl> | Parameter has custom data.<br/>                                                                                                                                                                                                         |



## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>OaIdl.h</dt> </dl> |



 

 





