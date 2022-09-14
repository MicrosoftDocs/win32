---
title: IMAPIv1 Result Codes (Imapierror.h)
description: The methods of the IMAPI interfaces return S\_OK if the method was successful. Otherwise, they return one of the following result codes.
ms.assetid: 0143ad10-9b65-4621-9bed-71dadd38c3fc
topic_type:
- apiref
api_name:
- IMAPI_S_PROPERTIESIGNORED
- IMAPI_S_BUFFER_TO_SMALL
- IMAPI_E_NOTOPENED
- IMAPI_E_NOTINITIALIZED
- IMAPI_E_USERABORT
- IMAPI_E_GENERIC
- IMAPI_E_MEDIUM_NOTPRESENT
- IMAPI_E_MEDIUM_INVALIDTYPE
- IMAPI_E_DEVICE_NOPROPERTIES
- IMAPI_E_DEVICE_NOTACCESSIBLE
- IMAPI_E_DEVICE_NOTPRESENT
- IMAPI_E_DEVICE_INVALIDTYPE
- IMAPI_E_INITIALIZE_WRITE
- IMAPI_E_INITIALIZE_ENDWRITE
- IMAPI_E_FILESYSTEM
- IMAPI_E_FILEACCESS
- IMAPI_E_DISCINFO
- IMAPI_E_TRACKNOTOPEN
- IMAPI_E_TRACKOPEN
- IMAPI_E_DISCFULL
- IMAPI_E_BADJOLIETNAME
- IMAPI_E_INVALIDIMAGE
- IMAPI_E_NOACTIVEFORMAT
- IMAPI_E_NOACTIVERECORDER
- IMAPI_E_WRONGFORMAT
- IMAPI_E_ALREADYOPEN
- IMAPI_E_WRONGDISC
- IMAPI_E_FILEEXISTS
- IMAPI_E_STASHINUSE
- IMAPI_E_DEVICE_STILL_IN_USE
- IMAPI_E_LOSS_OF_STREAMING
- IMAPI_E_COMPRESSEDSTASH
- IMAPI_E_ENCRYPTEDSTASH
- IMAPI_E_NOTENOUGHDISKFORSTASH
- IMAPI_E_REMOVABLESTASH
- IMAPI_E_CANNOT_WRITE_TO_MEDIA
- IMAPI_E_TRACK_NOT_BIG_ENOUGH
api_location:
- Imapierror.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# IMAPIv1 Result Codes

The methods of the IMAPI interfaces return S\_OK if the method was successful. Otherwise, they return one of the following result codes.



| Constant/value                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                  |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="IMAPI_S_PROPERTIESIGNORED"></span><span id="imapi_s_propertiesignored"></span><dl> <dt>**IMAPI\_S\_PROPERTIESIGNORED**</dt> <dt>0x40200</dt> </dl>                   | An unknown property was passed in a property set and it was ignored.<br/>                                                                                                                                                                              |
| <span id="IMAPI_S_BUFFER_TO_SMALL"></span><span id="imapi_s_buffer_to_small"></span><dl> <dt>**IMAPI\_S\_BUFFER\_TO\_SMALL**</dt> <dt>0x40201</dt> </dl>                       | The output buffer is too small.<br/>                                                                                                                                                                                                                   |
| <span id="IMAPI_E_NOTOPENED"></span><span id="imapi_e_notopened"></span><dl> <dt>**IMAPI\_E\_NOTOPENED**</dt> <dt>0x8004020b</dt> </dl>                                        | A call to [**IDiscMaster::Open**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-open) has not been made.<br/>                                                                                                                                                                        |
| <span id="IMAPI_E_NOTINITIALIZED"></span><span id="imapi_e_notinitialized"></span><dl> <dt>**IMAPI\_E\_NOTINITIALIZED**</dt> <dt>0x8004020c</dt> </dl>                         | A recorder object has not been initialized.<br/>                                                                                                                                                                                                       |
| <span id="IMAPI_E_USERABORT"></span><span id="imapi_e_userabort"></span><dl> <dt>**IMAPI\_E\_USERABORT**</dt> <dt>0x8004020d</dt> </dl>                                        | The user canceled the operation.<br/>                                                                                                                                                                                                                  |
| <span id="IMAPI_E_GENERIC"></span><span id="imapi_e_generic"></span><dl> <dt>**IMAPI\_E\_GENERIC**</dt> <dt>0x8004020e</dt> </dl>                                              | A generic error occurred.<br/>                                                                                                                                                                                                                         |
| <span id="IMAPI_E_MEDIUM_NOTPRESENT"></span><span id="imapi_e_medium_notpresent"></span><dl> <dt>**IMAPI\_E\_MEDIUM\_NOTPRESENT**</dt> <dt>0x8004020f</dt> </dl>               | There is no disc in the device.<br/>                                                                                                                                                                                                                   |
| <span id="IMAPI_E_MEDIUM_INVALIDTYPE"></span><span id="imapi_e_medium_invalidtype"></span><dl> <dt>**IMAPI\_E\_MEDIUM\_INVALIDTYPE**</dt> <dt>0x80040210</dt> </dl>            | The media is not a type that can be used.<br/>                                                                                                                                                                                                         |
| <span id="IMAPI_E_DEVICE_NOPROPERTIES"></span><span id="imapi_e_device_noproperties"></span><dl> <dt>**IMAPI\_E\_DEVICE\_NOPROPERTIES**</dt> <dt>0x80040211</dt> </dl>         | The recorder does not support any properties.<br/>                                                                                                                                                                                                     |
| <span id="IMAPI_E_DEVICE_NOTACCESSIBLE"></span><span id="imapi_e_device_notaccessible"></span><dl> <dt>**IMAPI\_E\_DEVICE\_NOTACCESSIBLE**</dt> <dt>0x80040212</dt> </dl>      | The device cannot be used or is already in use.<br/>                                                                                                                                                                                                   |
| <span id="IMAPI_E_DEVICE_NOTPRESENT"></span><span id="imapi_e_device_notpresent"></span><dl> <dt>**IMAPI\_E\_DEVICE\_NOTPRESENT**</dt> <dt>0x80040213</dt> </dl>               | The device is not present or has been removed.<br/>                                                                                                                                                                                                    |
| <span id="IMAPI_E_DEVICE_INVALIDTYPE"></span><span id="imapi_e_device_invalidtype"></span><dl> <dt>**IMAPI\_E\_DEVICE\_INVALIDTYPE**</dt> <dt>0x80040214</dt> </dl>            | The recorder does not support an operation.<br/>                                                                                                                                                                                                       |
| <span id="IMAPI_E_INITIALIZE_WRITE"></span><span id="imapi_e_initialize_write"></span><dl> <dt>**IMAPI\_E\_INITIALIZE\_WRITE**</dt> <dt>0x80040215</dt> </dl>                  | The drive interface could not be initialized for writing.<br/>                                                                                                                                                                                         |
| <span id="IMAPI_E_INITIALIZE_ENDWRITE"></span><span id="imapi_e_initialize_endwrite"></span><dl> <dt>**IMAPI\_E\_INITIALIZE\_ENDWRITE**</dt> <dt>0x80040216</dt> </dl>         | The drive interface could not be initialized for closing.<br/>                                                                                                                                                                                         |
| <span id="IMAPI_E_FILESYSTEM"></span><span id="imapi_e_filesystem"></span><dl> <dt>**IMAPI\_E\_FILESYSTEM**</dt> <dt>0x80040217</dt> </dl>                                     | An error occurred while enabling/disabling file system access or during auto-insertion detection.<br/>                                                                                                                                                 |
| <span id="IMAPI_E_FILEACCESS"></span><span id="imapi_e_fileaccess"></span><dl> <dt>**IMAPI\_E\_FILEACCESS**</dt> <dt>0x80040218</dt> </dl>                                     | An error occurred while writing the image file.<br/>                                                                                                                                                                                                   |
| <span id="IMAPI_E_DISCINFO"></span><span id="imapi_e_discinfo"></span><dl> <dt>**IMAPI\_E\_DISCINFO**</dt> <dt>0x80040219</dt> </dl>                                           | An error occurred while trying to read disc data from the device.<br/>                                                                                                                                                                                 |
| <span id="IMAPI_E_TRACKNOTOPEN"></span><span id="imapi_e_tracknotopen"></span><dl> <dt>**IMAPI\_E\_TRACKNOTOPEN**</dt> <dt>0x8004021a</dt> </dl>                               | An audio track is not open for writing.<br/>                                                                                                                                                                                                           |
| <span id="IMAPI_E_TRACKOPEN"></span><span id="imapi_e_trackopen"></span><dl> <dt>**IMAPI\_E\_TRACKOPEN**</dt> <dt>0x8004021b</dt> </dl>                                        | An open audio track is already being staged.<br/>                                                                                                                                                                                                      |
| <span id="IMAPI_E_DISCFULL"></span><span id="imapi_e_discfull"></span><dl> <dt>**IMAPI\_E\_DISCFULL**</dt> <dt>0x8004021c</dt> </dl>                                           | The disc cannot hold any more data.<br/>                                                                                                                                                                                                               |
| <span id="IMAPI_E_BADJOLIETNAME"></span><span id="imapi_e_badjolietname"></span><dl> <dt>**IMAPI\_E\_BADJOLIETNAME**</dt> <dt>0x8004021d</dt> </dl>                            | The application tried to add a badly named element to a disc.<br/>                                                                                                                                                                                     |
| <span id="IMAPI_E_INVALIDIMAGE"></span><span id="imapi_e_invalidimage"></span><dl> <dt>**IMAPI\_E\_INVALIDIMAGE**</dt> <dt>0x8004021e</dt> </dl>                               | The staged image is not suitable for a burn. It has been corrupted or cleared and has no usable content.<br/>                                                                                                                                          |
| <span id="IMAPI_E_NOACTIVEFORMAT"></span><span id="imapi_e_noactiveformat"></span><dl> <dt>**IMAPI\_E\_NOACTIVEFORMAT**</dt> <dt>0x8004021f</dt> </dl>                         | An active format master has not been selected using [**IDiscMaster::SetActiveDiscMasterFormat**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-setactivediscmasterformat).<br/>                                                                                                      |
| <span id="IMAPI_E_NOACTIVERECORDER"></span><span id="imapi_e_noactiverecorder"></span><dl> <dt>**IMAPI\_E\_NOACTIVERECORDER**</dt> <dt>0x80040220</dt> </dl>                   | An active disc recorder has not been selected using [**IDiscMaster::SetActiveDiscRecorder**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-setactivediscrecorder).<br/>                                                                                                              |
| <span id="IMAPI_E_WRONGFORMAT"></span><span id="imapi_e_wrongformat"></span><dl> <dt>**IMAPI\_E\_WRONGFORMAT**</dt> <dt>0x80040221</dt> </dl>                                  | A call to [**IJolietDiscMaster**](/windows/desktop/api/Imapi/nn-imapi-ijolietdiscmaster) has been made when [**IRedbookDiscMaster**](/windows/desktop/api/Imapi/nn-imapi-iredbookdiscmaster) is the active format, or vice versa. To use a different format, change the format and clear the image file contents.<br/> |
| <span id="IMAPI_E_ALREADYOPEN"></span><span id="imapi_e_alreadyopen"></span><dl> <dt>**IMAPI\_E\_ALREADYOPEN**</dt> <dt>0x80040222</dt> </dl>                                  | A call to [**IDiscMaster::Open**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-open) has already been made against this object by your application.<br/>                                                                                                                            |
| <span id="IMAPI_E_WRONGDISC"></span><span id="imapi_e_wrongdisc"></span><dl> <dt>**IMAPI\_E\_WRONGDISC**</dt> <dt>0x80040223</dt> </dl>                                        | The IMAPI multi-session disc has been removed from the active recorder.<br/>                                                                                                                                                                           |
| <span id="IMAPI_E_FILEEXISTS"></span><span id="imapi_e_fileexists"></span><dl> <dt>**IMAPI\_E\_FILEEXISTS**</dt> <dt>0x80040224</dt> </dl>                                     | The file to add is already in the image file and the overwrite flag was not set.<br/>                                                                                                                                                                  |
| <span id="IMAPI_E_STASHINUSE"></span><span id="imapi_e_stashinuse"></span><dl> <dt>**IMAPI\_E\_STASHINUSE**</dt> <dt>0x80040225</dt> </dl>                                     | Another application is already using the IMAPI stash file required to stage a disc image. Try again later.<br/>                                                                                                                                        |
| <span id="IMAPI_E_DEVICE_STILL_IN_USE"></span><span id="imapi_e_device_still_in_use"></span><dl> <dt>**IMAPI\_E\_DEVICE\_STILL\_IN\_USE**</dt> <dt>0x80040226</dt> </dl>       | Another application is already using this device, so IMAPI cannot access the device.<br/>                                                                                                                                                              |
| <span id="IMAPI_E_LOSS_OF_STREAMING"></span><span id="imapi_e_loss_of_streaming"></span><dl> <dt>**IMAPI\_E\_LOSS\_OF\_STREAMING**</dt> <dt>0x80040227</dt> </dl>              | Content streaming was lost; a buffer under-run may have occurred.<br/>                                                                                                                                                                                 |
| <span id="IMAPI_E_COMPRESSEDSTASH"></span><span id="imapi_e_compressedstash"></span><dl> <dt>**IMAPI\_E\_COMPRESSEDSTASH**</dt> <dt>0x80040228</dt> </dl>                      | The stash is located on a compressed volume and cannot be read.<br/>                                                                                                                                                                                   |
| <span id="IMAPI_E_ENCRYPTEDSTASH"></span><span id="imapi_e_encryptedstash"></span><dl> <dt>**IMAPI\_E\_ENCRYPTEDSTASH**</dt> <dt>0x80040229</dt> </dl>                         | The stash is located on an encrypted volume and cannot be read.<br/>                                                                                                                                                                                   |
| <span id="IMAPI_E_NOTENOUGHDISKFORSTASH"></span><span id="imapi_e_notenoughdiskforstash"></span><dl> <dt>**IMAPI\_E\_NOTENOUGHDISKFORSTASH**</dt> <dt>0x8004022a</dt> </dl>    | There is not enough free space to create the stash file on the specified volume.<br/>                                                                                                                                                                  |
| <span id="IMAPI_E_REMOVABLESTASH"></span><span id="imapi_e_removablestash"></span><dl> <dt>**IMAPI\_E\_REMOVABLESTASH**</dt> <dt>0x8004022b</dt> </dl>                         | The selected stash location is on a removable media.<br/>                                                                                                                                                                                              |
| <span id="IMAPI_E_CANNOT_WRITE_TO_MEDIA"></span><span id="imapi_e_cannot_write_to_media"></span><dl> <dt>**IMAPI\_E\_CANNOT\_WRITE\_TO\_MEDIA**</dt> <dt>0x8004022c</dt> </dl> | The media cannot be written to.<br/>                                                                                                                                                                                                                   |
| <span id="IMAPI_E_TRACK_NOT_BIG_ENOUGH"></span><span id="imapi_e_track_not_big_enough"></span><dl> <dt>**IMAPI\_E\_TRACK\_NOT\_BIG\_ENOUGH**</dt> <dt>0x8004022d</dt> </dl>    | The track is not big enough.<br/>                                                                                                                                                                                                                      |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Imapierror.h</dt> </dl> |



 

 





