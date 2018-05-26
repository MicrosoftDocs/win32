---
Description: The ListenToServerEvents method registers the FaxServer object to receive notifications about one or more types of server events, or to stop these notifications.
ms.assetid: 5d7b6c07-5009-48af-933c-1be3e2bde27e
title: FaxServer.ListenToServerEvents method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.ListenToServerEvents method

The **ListenToServerEvents** method registers the [**FaxServer**](-mfax-faxserver.md) object to receive notifications about one or more types of server events, or to stop these notifications.

## Syntax


```VB
FaxServer.ListenToServerEvents( _
  ByVal EventTypes As FAX_SERVER_EVENTS_TYPE_ENUM _
) As Long
```



## Parameters

<dl> <dt>

*EventTypes* \[in\]
</dt> <dd>

Type: **[**FAX\_SERVER\_EVENTS\_TYPE\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master)**

A value that contains a set of bit flags representing the types of events for which the [**FaxServer**](-mfax-faxserver.md) object is registering to receive notifications. For more information, see [**FAX\_SERVER\_EVENTS\_TYPE\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master).

</dd> </dl>

## Remarks

In Microsoft Visual Basic, if you want the fax server to receive notifications, you have to create the [**FaxServer**](-mfax-faxserver.md) object using the following syntax:


```
Dim WithEvents objFaxServer As New FAXCOMEXLib.FaxServer
Set objFaxServer = CreateObject("FaxServer") 
```



In Microsoft Visual C++, the [**IFaxServerNotify**](/windows/previous-versions/FaxComex/?branch=master) interface on the **FaxServer** object receives notifications of the events.

By default, the [**FaxServer**](-mfax-faxserver.md) object does not receive notifications for any server events. If you want the **FaxServer** object to receive notifications, you must call **ListenToServerEvents** and pass to it the event types for which you want to receive notifications. To stop receiving the notification, call this method with *EventTypes* equal to [**fsetNONE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master).

Access rights for this method depend on which events are requested, as shown in the following table.



|                                                                 |                                                                |
|-----------------------------------------------------------------|----------------------------------------------------------------|
| Event                                                           | Required access rights                                         |
| [**fsetINCOMING\_CALL**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master) | [**farQUERY\_IN\_ARCHIVE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)  |
| [**fsetIN\_QUEUE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master)      | [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)         |
|                                                                 | [**farQUERY\_JOBS**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)         |
| [**fsetOUT\_QUEUE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master)     | [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)         |
|                                                                 | [**farQUERY\_JOBS**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)         |
| [**fsetCONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master)         | [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)       |
| [**fsetDEVICE\_STATUS**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master) | [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)       |
| [**fsetACTIVITY**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master)       | [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)       |
| [**fsetIN\_ARCHIVE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master)    | [**farSUBMIT**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)              |
|                                                                 | [**farQUERY\_IN\_ARCHIVE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)  |
| [**fsetOUT\_ARCHIVE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_server_events_type_enum?branch=master)   | [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master)         |
|                                                                 | [**farQUERY\_OUT\_ARCHIVE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-registering-for-fax-events.md)
</dt> <dt>

[Registering for Event Notifications](-mfax-registering-for-event-notifications.md)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxServer**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxserver?branch=master)
</dt> </dl>

 

 




