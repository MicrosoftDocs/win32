---
title: TV Ratings Broadcast Events
description: This topic applies to Windows XP Service Pack 1 or later.
ms.assetid: 73a6a4fd-cca2-4143-91f9-37f4f6d952b8
keywords:
- TV Ratings Broadcast Events Microsoft TV Technologies
topic_type:
- apiref
api_name:
- TV Ratings Broadcast Events
api_location:
- Encdec.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TV Ratings Broadcast Events

This topic applies to Windows XP Service Pack 1 or later.

The TV Ratings components fire the following broadcast events. These events are fired through the [**IBroadcastEvent Interface**](/windows/previous-versions/tuner/nn-tuner-ibroadcastevent?branch=master) interface.



| Event                              | Description                                                                                                  |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| EVENTID\_DTFilterDataFormatFailure | Sent by the Decrypter/Detagger filter if the data format is unreadable.                                      |
| EVENTID\_DTFilterRatingChange      | The current rating has changed. (Sent by the Decrypter/Detagger filter.)                                     |
| EVENTID\_ETDTFilterLicenseFailure  | The Encrypter/Tagger filter or the Decrypter/Detagger filter failed to get an encryption/decryption license. |
| EVENTID\_ETFilterCopyNever         | Sent by the Encrypter/Tagger filter when the content has the Copy Never flag.                                |
| EVENTID\_ETFilterCopyOnce          | Sent by the Encrypter/Tagger filter when the content has the Copy Once flag.                                 |
| EVENTID\_ETFilterEncryptionOff     | Sent by the Encrypter/Tagger filter when it stops encrypting content.                                        |
| EVENTID\_ETFilterEncryptionOn      | Sent by the Encrypter/Tagger filter when it starts to encrypt content.                                       |
| EVENTID\_XDSCodecNewXDSRating      | Sent by the XDS Codec filter when it receives a new rating.                                                  |



 

The Decrypter/Detagger filter sends the following event through the [**IBroadcastEventEx**](/windows/previous-versions/tuner/nn-tuner-ibroadcasteventex?branch=master) interface.



| Event                      | Description                                    |
|----------------------------|------------------------------------------------|
| EVENTID\_EncDecFilterEvent | Generic content protection event. See remarks. |



 

The EVENTID\_EncDecFilterEvent event has the following event parameters.

-   *Param1*: ENCDEC\_CPEVENT. Indicates a copy protection event.
-   *Param2*: Member of the [**CPEvents**](/windows/previous-versions/EncDec/ne-encdec-cpevents?branch=master) enumeration.
-   *Param3*: Unused (0).
-   *Param4*: Unused (0).

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Encdec.h</dt> </dl> |



## See also

<dl> <dt>

[TV Ratings Components](tv-ratings-components.md)
</dt> </dl>

 

 





