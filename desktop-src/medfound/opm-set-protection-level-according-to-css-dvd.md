---
description: Sets the HDCP protection level for DVD playback, following DVD Content Scramble System (CSS) rules.
ms.assetid: 8d9ecb9b-8528-4b23-ab2f-234ba2cb7ed0
title: OPM_SET_PROTECTION_LEVEL_ACCORDING_TO_CSS_DVD (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD

Sets the HDCP protection level for DVD playback, following DVD Content Scramble System (CSS) rules.



| Requirement | Value |
|--------------|-----------------------------------------------------------------------------------------------------|
| Command GUID | OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD                                                |
| Input data   | An [**OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_set_protection_level_parameters) structure |



 

## Remarks

This command is used to set High-Bandwidth Digital Content Protection (HDCP) when playing standard DVDs. Unlike the [**OPM\_SET\_PROTECTION\_LEVEL**](opm-set-protection-level.md) command, if HDCP cannot be set for some reason, this command does not stop playback. (DVD CSS rules contain a "best effort" provision for players.) Otherwise, this command is identical to the **OPM\_SET\_PROTECTION\_LEVEL** command.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::Configure**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-configure)
</dt> <dt>

[OPM Commands](opm-commands.md)
</dt> </dl>

 

 




