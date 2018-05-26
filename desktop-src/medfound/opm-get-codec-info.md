---
Description: Gets the merit value of a hardware codec.
ms.assetid: 51987a79-78bf-41b2-8349-8c2725dd89d6
title: OPM\_GET\_CODEC\_INFO
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OPM\_GET\_CODEC\_INFO

Gets the merit value of a hardware codec.



|              |                                                                                           |
|--------------|-------------------------------------------------------------------------------------------|
| Request GUID | **OPM\_GET\_CODEC\_INFO**                                                                 |
| Input data   | An [**OPM\_GET\_CODEC\_INFO\_PARAMETERS**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_get_codec_info_parameters?branch=master) structure   |
| Return data  | An [**OPM\_GET\_CODEC\_INFO\_INFORMATION**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_get_codec_info_information?branch=master) structure |



 

## Remarks

Although this command uses the [Output Protection Manager](output-protection-manager.md) (OPM) interface, it applies only to hardware encoders and decoders. It does not apply to video output devices.

Generally, you should not use this command directly. To get the merit value for a hardware codec, call the [**MFGetMFTMerit**](/windows/win32/mfapi/nf-mfapi-mfgetmftmerit?branch=master) function. This function performs all of the OPM calls needed to send the **OPM\_GET\_CODEC\_INFO** command.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[OPM Status Requests](opm-status-requests.md)
</dt> <dt>

[Output Protection Manager](output-protection-manager.md)
</dt> <dt>

[**IOPMVideoOutput::GetInformation**](/windows/win32/opmapi/nf-opmapi-iopmvideooutput-getinformation?branch=master)
</dt> </dl>

 

 




