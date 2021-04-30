---
description: Gets the merit value of a hardware codec.
ms.assetid: 51987a79-78bf-41b2-8349-8c2725dd89d6
title: OPM_GET_CODEC_INFO (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM\_GET\_CODEC\_INFO

Gets the merit value of a hardware codec.



| Requirement | Value |
|--------------|-------------------------------------------------------------------------------------------|
| Request GUID | **OPM\_GET\_CODEC\_INFO**                                                                 |
| Input data   | An [**OPM\_GET\_CODEC\_INFO\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_codec_info_parameters) structure   |
| Return data  | An [**OPM\_GET\_CODEC\_INFO\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_codec_info_information) structure |



 

## Remarks

Although this command uses the [Output Protection Manager](output-protection-manager.md) (OPM) interface, it applies only to hardware encoders and decoders. It does not apply to video output devices.

Generally, you should not use this command directly. To get the merit value for a hardware codec, call the [**MFGetMFTMerit**](/windows/desktop/api/mfapi/nf-mfapi-mfgetmftmerit) function. This function performs all of the OPM calls needed to send the **OPM\_GET\_CODEC\_INFO** command.

## Requirements



| Requirement | Value |
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

[**IOPMVideoOutput::GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation)
</dt> </dl>

 

 




