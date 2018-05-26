---
Description: Sets the protection level for an output protection mechanism.
ms.assetid: f4e63bf5-0749-4054-9f86-7fd88f2881ad
title: OPM\_SET\_PROTECTION\_LEVEL
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OPM\_SET\_PROTECTION\_LEVEL

Sets the protection level for an output protection mechanism.



|              |                                                                                                     |
|--------------|-----------------------------------------------------------------------------------------------------|
| Command GUID | OPM\_SET\_PROTECTION\_LEVEL                                                                         |
| Input data   | An [**OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS**](/windows/win32/opmapi/ns-opmapi-_opm_set_protection_level_parameters?branch=master) structure |



 

## Remarks

Some connectors can support multiple protection mechanisms. With that type of connector, you can apply several protection mechanisms to the same connector, with different settings for each.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::Configure**](/windows/win32/opmapi/nf-opmapi-iopmvideooutput-configure?branch=master)
</dt> <dt>

[OPM Commands](opm-commands.md)
</dt> </dl>

 

 




