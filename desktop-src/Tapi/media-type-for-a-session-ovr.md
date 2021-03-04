---
description: The media type (or mode) describes the type of information being exchanged, such as interactive voice. A given communications session may involve several media types.
ms.assetid: 2eb140f0-ca07-4e60-b9f3-be2f466f4fca
title: Media Type for a Session
ms.topic: article
ms.date: 05/31/2018
---

# Media Type for a Session

The media type (or mode) describes the type of information being exchanged, such as interactive voice. A given communications session may involve several media types.

Service providers expose to TAPI and to applications the media type or types they support. See the device [media type](media-type-ovr.md) overview for information on acquiring this data.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo), [**lineSetMediaMode**](/windows/win32/api/tapi/nf-tapi-linesetmediamode), [**lineMonitorMedia**](/windows/win32/api/tapi/nf-tapi-linemonitormedia), [**LINE\_MONITORMEDIA**](./line-monitormedia.md) message, [LINEMEDIAMODE\_ Constants](./linemediamode--constants.md).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong) with **CIL\_MEDIATYPESAVAILABLE**, [**ITCallInfo::put\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-put_callinfolong) with **CIL\_MEDIATYPESAVAILABLE**, [**ITCallInfoChangeEvent::get\_Cause**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfochangeevent-get_cause) (returns [**CALLINFOCHANGE\_CAUSE**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfochange_cause) of **CIC\_MEDIATYPE**), [TAPIMEDIATYPE\_ Constants](tapimediatype--constants.md).

 

 
