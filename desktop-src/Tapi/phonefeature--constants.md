---
description: The PHONEFEATURE\_ constants list the operations that can be invoked on a phone using this API. Each of the PHONEFEATURE\_ values (except PHONEFEATURE\_GENERICPHONE) corresponds to a TAPI function with an identical or similar name.
ms.assetid: 361b3080-3650-48a2-a1b7-f05d72777f9a
title: PHONEFEATURE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONEFEATURE\_ Constants

The **PHONEFEATURE\_** constants list the operations that can be invoked on a phone using this API. Each of the PHONEFEATURE\_ values (except PHONEFEATURE\_GENERICPHONE) corresponds to a TAPI function with an identical or similar name.



| Constant/value                                                                                                                                                                                                                                                                            | Description                                                                             |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| <span id="PHONEFEATURE_GETBUTTONINFO"></span><span id="phonefeature_getbuttoninfo"></span><dl> <dt>**PHONEFEATURE\_GETBUTTONINFO**</dt> <dt>0x00000001</dt> </dl>                      | [**phoneGetButtonInfo**](/windows/desktop/api/Tapi/nf-tapi-phonegetbuttoninfo)<br/>                             |
| <span id="PHONEFEATURE_GETDATA"></span><span id="phonefeature_getdata"></span><dl> <dt>**PHONEFEATURE\_GETDATA**</dt> <dt>0x00000002</dt> </dl>                                        | [**phoneGetData**](/windows/desktop/api/Tapi/nf-tapi-phonegetdata)<br/>                                         |
| <span id="PHONEFEATURE_GETDISPLAY"></span><span id="phonefeature_getdisplay"></span><dl> <dt>**PHONEFEATURE\_GETDISPLAY**</dt> <dt>0x00000004</dt> </dl>                               | [**phoneGetDisplay**](/windows/desktop/api/Tapi/nf-tapi-phonegetdisplay)<br/>                                   |
| <span id="PHONEFEATURE_GETGAINHANDSET"></span><span id="phonefeature_getgainhandset"></span><dl> <dt>**PHONEFEATURE\_GETGAINHANDSET**</dt> <dt>0x00000008</dt> </dl>                   | [**phoneGetGain**](/windows/desktop/api/Tapi/nf-tapi-phonegetgain) PHONEHOOKSWITCHDEV\_HANDSET<br/>             |
| <span id="PHONEFEATURE_GETGAINSPEAKER"></span><span id="phonefeature_getgainspeaker"></span><dl> <dt>**PHONEFEATURE\_GETGAINSPEAKER**</dt> <dt>0x00000010</dt> </dl>                   | [**phoneGetGain**](/windows/desktop/api/Tapi/nf-tapi-phonegetgain) PHONEHOOKSWITCHDEV\_SPEAKER<br/>             |
| <span id="PHONEFEATURE_GETGAINHEADSET"></span><span id="phonefeature_getgainheadset"></span><dl> <dt>**PHONEFEATURE\_GETGAINHEADSET**</dt> <dt>0x00000020</dt> </dl>                   | [**phoneGetGain**](/windows/desktop/api/Tapi/nf-tapi-phonegetgain) PHONEHOOKSWITCHDEV\_HEADSET<br/>             |
| <span id="PHONEFEATURE_GETHOOKSWITCHHANDSET"></span><span id="phonefeature_gethookswitchhandset"></span><dl> <dt>**PHONEFEATURE\_GETHOOKSWITCHHANDSET**</dt> <dt>0x00000040</dt> </dl> | [**phoneGetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonegethookswitch) PHONEHOOKSWITCHDEV\_HANDSET<br/> |
| <span id="PHONEFEATURE_GETHOOKSWITCHSPEAKER"></span><span id="phonefeature_gethookswitchspeaker"></span><dl> <dt>**PHONEFEATURE\_GETHOOKSWITCHSPEAKER**</dt> <dt>0x00000080</dt> </dl> | [**phoneGetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonegethookswitch) PHONEHOOKSWITCHDEV\_HANDSET<br/> |
| <span id="PHONEFEATURE_GETHOOKSWITCHHEADSET"></span><span id="phonefeature_gethookswitchheadset"></span><dl> <dt>**PHONEFEATURE\_GETHOOKSWITCHHEADSET**</dt> <dt>0x00000100</dt> </dl> | [**phoneGetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonegethookswitch) PHONEHOOKSWITCHDEV\_HANDSET<br/> |
| <span id="PHONEFEATURE_GETLAMP"></span><span id="phonefeature_getlamp"></span><dl> <dt>**PHONEFEATURE\_GETLAMP**</dt> <dt>0x00000200</dt> </dl>                                        | [**phoneGetLamp**](/windows/desktop/api/Tapi/nf-tapi-phonegetlamp)<br/>                                         |
| <span id="PHONEFEATURE_GETRING"></span><span id="phonefeature_getring"></span><dl> <dt>**PHONEFEATURE\_GETRING**</dt> <dt>0x00000400</dt> </dl>                                        | [**phoneGetRing**](/windows/desktop/api/Tapi/nf-tapi-phonegetring)<br/>                                         |
| <span id="PHONEFEATURE_GETVOLUMEHANDSET"></span><span id="phonefeature_getvolumehandset"></span><dl> <dt>**PHONEFEATURE\_GETVOLUMEHANDSET**</dt> <dt>0x00000800</dt> </dl>             | [**phoneGetVolume**](/windows/desktop/api/Tapi/nf-tapi-phonegetvolume) PHONEHOOKSWITCHDEV\_HANDSET<br/>         |
| <span id="PHONEFEATURE_GETVOLUMESPEAKER"></span><span id="phonefeature_getvolumespeaker"></span><dl> <dt>**PHONEFEATURE\_GETVOLUMESPEAKER**</dt> <dt>0x00001000</dt> </dl>             | [**phoneGetVolume**](/windows/desktop/api/Tapi/nf-tapi-phonegetvolume) PHONEHOOKSWITCHDEV\_SPEAKER<br/>         |
| <span id="PHONEFEATURE_GETVOLUMEHEADSET"></span><span id="phonefeature_getvolumeheadset"></span><dl> <dt>**PHONEFEATURE\_GETVOLUMEHEADSET**</dt> <dt>0x00002000</dt> </dl>             | [**phoneGetVolume**](/windows/desktop/api/Tapi/nf-tapi-phonegetvolume) PHONEHOOKSWITCHDEV\_HEADSET<br/>         |
| <span id="PHONEFEATURE_SETBUTTONINFO"></span><span id="phonefeature_setbuttoninfo"></span><dl> <dt>**PHONEFEATURE\_SETBUTTONINFO**</dt> <dt>0x00004000</dt> </dl>                      | [**phoneSetButtonInfo**](/windows/desktop/api/Tapi/nf-tapi-phonesetbuttoninfo)<br/>                             |
| <span id="PHONEFEATURE_SETDATA"></span><span id="phonefeature_setdata"></span><dl> <dt>**PHONEFEATURE\_SETDATA**</dt> <dt>0x00008000</dt> </dl>                                        | [**phoneSetData**](/windows/desktop/api/Tapi/nf-tapi-phonesetdata)<br/>                                         |
| <span id="PHONEFEATURE_SETDISPLAY"></span><span id="phonefeature_setdisplay"></span><dl> <dt>**PHONEFEATURE\_SETDISPLAY**</dt> <dt>0x00010000</dt> </dl>                               | [**phoneSetDisplay**](/windows/desktop/api/Tapi/nf-tapi-phonesetdisplay)<br/>                                   |
| <span id="PHONEFEATURE_SETGAINHANDSET"></span><span id="phonefeature_setgainhandset"></span><dl> <dt>**PHONEFEATURE\_SETGAINHANDSET**</dt> <dt>0x00020000</dt> </dl>                   | [**phoneSetGain**](/windows/desktop/api/Tapi/nf-tapi-phonesetgain) PHONEHOOKSWITCHDEV\_HANDSET<br/>             |
| <span id="PHONEFEATURE_SETGAINSPEAKER"></span><span id="phonefeature_setgainspeaker"></span><dl> <dt>**PHONEFEATURE\_SETGAINSPEAKER**</dt> <dt>0x00040000</dt> </dl>                   | [**phoneSetGain**](/windows/desktop/api/Tapi/nf-tapi-phonesetgain) PHONEHOOKSWITCHDEV\_SPEAKER<br/>             |
| <span id="PHONEFEATURE_SETGAINHEADSET"></span><span id="phonefeature_setgainheadset"></span><dl> <dt>**PHONEFEATURE\_SETGAINHEADSET**</dt> <dt>0x00080000</dt> </dl>                   | [**phoneSetGain**](/windows/desktop/api/Tapi/nf-tapi-phonesetgain) PHONEHOOKSWITCHDEV\_HEADSET<br/>             |
| <span id="PHONEFEATURE_SETHOOKSWITCHHANDSET"></span><span id="phonefeature_sethookswitchhandset"></span><dl> <dt>**PHONEFEATURE\_SETHOOKSWITCHHANDSET**</dt> <dt>0x00100000</dt> </dl> | [**phoneSetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonesethookswitch) PHONEHOOKSWITCHDEV\_HANDSET<br/> |
| <span id="PHONEFEATURE_SETHOOKSWITCHSPEAKER"></span><span id="phonefeature_sethookswitchspeaker"></span><dl> <dt>**PHONEFEATURE\_SETHOOKSWITCHSPEAKER**</dt> <dt>0x00200000</dt> </dl> | [**phoneSetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonesethookswitch) PHONEHOOKSWITCHDEV\_SPEAKER<br/> |
| <span id="PHONEFEATURE_SETHOOKSWITCHHEADSET"></span><span id="phonefeature_sethookswitchheadset"></span><dl> <dt>**PHONEFEATURE\_SETHOOKSWITCHHEADSET**</dt> <dt>0x00400000</dt> </dl> | [**phoneSetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonesethookswitch) PHONEHOOKSWITCHDEV\_HEADSET<br/> |
| <span id="PHONEFEATURE_SETLAMP"></span><span id="phonefeature_setlamp"></span><dl> <dt>**PHONEFEATURE\_SETLAMP**</dt> <dt>0x00800000</dt> </dl>                                        | [**phoneSetLamp**](/windows/desktop/api/Tapi/nf-tapi-phonesetlamp)<br/>                                         |
| <span id="PHONEFEATURE_SETRING"></span><span id="phonefeature_setring"></span><dl> <dt>**PHONEFEATURE\_SETRING**</dt> <dt>0x01000000</dt> </dl>                                        | [**phoneSetRing**](/windows/desktop/api/Tapi/nf-tapi-phonesetring)<br/>                                         |
| <span id="PHONEFEATURE_SETVOLUMEHANDSET"></span><span id="phonefeature_setvolumehandset"></span><dl> <dt>**PHONEFEATURE\_SETVOLUMEHANDSET**</dt> <dt>0x02000000</dt> </dl>             | [**phoneSetVolume**](/windows/desktop/api/Tapi/nf-tapi-phonesetvolume) PHONEHOOKSWITCHDEV\_HANDSET<br/>         |
| <span id="PHONEFEATURE_SETVOLUMESPEAKER"></span><span id="phonefeature_setvolumespeaker"></span><dl> <dt>**PHONEFEATURE\_SETVOLUMESPEAKER**</dt> <dt>0x04000000</dt> </dl>             | [**phoneSetVolume**](/windows/desktop/api/Tapi/nf-tapi-phonesetvolume) PHONEHOOKSWITCHDEV\_SPEAKER<br/>         |
| <span id="PHONEFEATURE_SETVOLUMEHEADSET"></span><span id="phonefeature_setvolumeheadset"></span><dl> <dt>**PHONEFEATURE\_SETVOLUMEHEADSET**</dt> <dt>0x08000000</dt> </dl>             | [**phoneSetVolume**](/windows/desktop/api/Tapi/nf-tapi-phonesetvolume) PHONEHOOKSWITCHDEV\_HEADSET<br/>         |
| <span id="PHONEFEATURE_GENERICPHONE"></span><span id="phonefeature_genericphone"></span><dl> <dt>**PHONEFEATURE\_GENERICPHONE**</dt> <dt>0x10000000</dt> </dl>                         | (relevant only to applications using TAPI 3.0 and later)<br/>                     |



## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




