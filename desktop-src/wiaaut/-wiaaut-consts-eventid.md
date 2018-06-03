---
title: EventID Constants
description: Specifies DeviceManager events as String versions of GUIDs.
ms.assetid: 13e4f850-02c3-4f7e-af38-f2d8a9cff1bf
topic_type:
- apiref
api_name:
- wiaEventDeviceConnected
- wiaEventDeviceDisconnected
- wiaEventItemCreated
- wiaEventItemDeleted
- wiaEventScanImage
- wiaEventScanPrintImage
- wiaEventScanFaxImage
- wiaEventScanOCRImage
- wiaEventScanEmailImage
- wiaEventScanFilmImage
- wiaEventScanImage2
- wiaEventScanImage3
- wiaEventScanImage4
api_location:
- Wiaaut.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EventID Constants

Specifies [**DeviceManager**](-wiaaut-devicemanager.md) events as **String** versions of GUIDs.



| Constant/value                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                       |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| <span id="wiaEventDeviceConnected"></span><span id="wiaeventdeviceconnected"></span><span id="WIAEVENTDEVICECONNECTED"></span><dl> <dt>**wiaEventDeviceConnected**</dt> <dt>{A28BBADE-64B6-11D2-A231-00C04FA31809}</dt> </dl>             | EventID for Device Connected. Fires when a WIA hardware device is connected to the user's computer or started.<br/>         |
| <span id="wiaEventDeviceDisconnected"></span><span id="wiaeventdevicedisconnected"></span><span id="WIAEVENTDEVICEDISCONNECTED"></span><dl> <dt>**wiaEventDeviceDisconnected**</dt> <dt>{143E4E83-6497-11D2-A231-00C04FA31809}</dt> </dl> | EventID for Device Disconnected. Fires when a WIA hardware device is disconnected from the user's computer or stopped.<br/> |
| <span id="wiaEventItemCreated"></span><span id="wiaeventitemcreated"></span><span id="WIAEVENTITEMCREATED"></span><dl> <dt>**wiaEventItemCreated**</dt> <dt>{4C8F4EF5-E14F-11D2-B326-00C04F68CE61}</dt> </dl>                             | EventID for Item Created. Fires when an item is added to a WIA Device.<br/>                                                 |
| <span id="wiaEventItemDeleted"></span><span id="wiaeventitemdeleted"></span><span id="WIAEVENTITEMDELETED"></span><dl> <dt>**wiaEventItemDeleted**</dt> <dt>{1D22A559-E14F-11D2-B326-00C04F68CE61}</dt> </dl>                             | EventID for Item Deleted. Fires when an item is deleted from a WIA Device.<br/>                                             |
| <span id="wiaEventScanImage"></span><span id="wiaeventscanimage"></span><span id="WIAEVENTSCANIMAGE"></span><dl> <dt>**wiaEventScanImage**</dt> <dt>{A6C5A715-8C6E-11D2-977A-0000F87A926F}</dt> </dl>                                     | EventID for Scan Image. Fires when the image button on a scanner is pressed.<br/>                                           |
| <span id="wiaEventScanPrintImage"></span><span id="wiaeventscanprintimage"></span><span id="WIAEVENTSCANPRINTIMAGE"></span><dl> <dt>**wiaEventScanPrintImage**</dt> <dt>{B441F425-8C6E-11D2-977A-0000F87A926F}</dt> </dl>                 | EventID for Scan Print Image. Fires when the print button on a scanner is pressed.<br/>                                     |
| <span id="wiaEventScanFaxImage"></span><span id="wiaeventscanfaximage"></span><span id="WIAEVENTSCANFAXIMAGE"></span><dl> <dt>**wiaEventScanFaxImage**</dt> <dt>{C00EB793-8C6E-11D2-977A-0000F87A926F}</dt> </dl>                         | EventID for Scan Fax Image. Fires when the fax button on a scanner is pressed.<br/>                                         |
| <span id="wiaEventScanOCRImage"></span><span id="wiaeventscanocrimage"></span><span id="WIAEVENTSCANOCRIMAGE"></span><dl> <dt>**wiaEventScanOCRImage**</dt> <dt>{9D095B89-37D6-4877-AFED-62A297DC6DBE}</dt> </dl>                         | EventID for Scan OCR Image. Fires when the OCR button on a scanner is pressed.<br/>                                         |
| <span id="wiaEventScanEmailImage"></span><span id="wiaeventscanemailimage"></span><span id="WIAEVENTSCANEMAILIMAGE"></span><dl> <dt>**wiaEventScanEmailImage**</dt> <dt>{C686DCEE-54F2-419E-9A27-2FC7F2E98F9E}</dt> </dl>                 | EventID for Scan E-mail Image. Fires when the e-mail button on a scanner is pressed.<br/>                                   |
| <span id="wiaEventScanFilmImage"></span><span id="wiaeventscanfilmimage"></span><span id="WIAEVENTSCANFILMIMAGE"></span><dl> <dt>**wiaEventScanFilmImage**</dt> <dt>{9B2B662C-6185-438C-B68B-E39EE25E71CB}</dt> </dl>                     | EventID for Scan Film Image. Fires when the film button on a scanner is pressed.<br/>                                       |
| <span id="wiaEventScanImage2"></span><span id="wiaeventscanimage2"></span><span id="WIAEVENTSCANIMAGE2"></span><dl> <dt>**wiaEventScanImage2**</dt> <dt>{FC4767C1-C8B3-48A2-9CFA-2E90CB3D3590}</dt> </dl>                                 | EventID for Scan Image 2. Fires when the second image button on a scanner is pressed.<br/>                                  |
| <span id="wiaEventScanImage3"></span><span id="wiaeventscanimage3"></span><span id="WIAEVENTSCANIMAGE3"></span><dl> <dt>**wiaEventScanImage3**</dt> <dt>{154E27BE-B617-4653-ACC5-0FD7BD4C65CE}</dt> </dl>                                 | EventID for Scan Image 3. This event fires when the third image button on a scanner is pressed.<br/>                        |
| <span id="wiaEventScanImage4"></span><span id="wiaeventscanimage4"></span><span id="WIAEVENTSCANIMAGE4"></span><dl> <dt>**wiaEventScanImage4**</dt> <dt>{A65B704A-7F3C-4447-A75D-8A26DFCA1FDF}</dt> </dl>                                 | EventID for Scan Image 4. Fires when the fourth image button on a scanner is pressed.<br/>                                  |



## Remarks

Use **EventID Constants** as the value for the *EventID* parameter for the [**RegisterEvent**](-wiaaut-idevicemanager-registerevent.md), [**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md), [**UnregisterEvent**](-wiaaut-idevicemanager-unregisterevent.md), and [**UnregisterPersistentEvent**](-wiaaut-idevicemanager-unregisterpersistentevent.md) methods. The *EventID* parameter in the [**OnEvent**](-wiaaut--idevicemanagerevents-onevent.md) event also takes an EventID constant value.

The following example shows how to register the wiaEventDeviceConnected event for all devices.


```
DeviceManager1.RegisterEvent wiaEventDeviceConnected, wiaAnyDeviceID
```



The following example shows how to handle a wiaEventDeviceConnected event.


```
Private Sub DeviceManager1_OnEvent(EventID, DeviceID, ItemID)
    If EventID = wiaEventDeviceConnected Then
        MsgBox "A Device has connected"
    End If
End Sub
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**EventID**](-wiaaut-ideviceevent-eventid.md)
</dt> </dl>

 

 





