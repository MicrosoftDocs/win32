---
title: AppEventsDHTMLConnector Object object
description: The AppEventsDHTMLConnector object provides a way for automation clients to receive events from MMC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: aad88657-cc94-4710-8179-b8500fd88dda
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- AppEventsDHTMLConnector Object object MMC
- AppEventsDHTMLConnector Object object MMC , described
topic_type:
- apiref
api_name:
- AppEventsDHTMLConnector Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# AppEventsDHTMLConnector Object object

The AppEventsDHTMLConnector object provides a way for automation clients to receive events from MMC. This object is used by scripts running on DHTML pages created by view extensions; in this situation, there is a need to connect to the [**Application object**](application-object.md) of an existing MMC instance in order to receive its events.

## Members

The **AppEventsDHTMLConnector Object** object has these types of members:

-   [Methods](#methods)

### Methods

The **AppEventsDHTMLConnector Object** object has these methods.



| Method                                                   | Description                                                                                                               |
|:---------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| [**ConnectTo**](appeventsdhtmlconnector-connectto.md)   | Connects to and provides an event sink for an instance of an [**Application object**](application-object.md).<br/> |
| [**Disconnect**](appeventsdhtmlconnector-disconnect.md) | Disconnects from an [**Application object**](application-object.md) instance.<br/>                                 |



 

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                               |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>          |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>        |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl>      |
| CLSID<br/>                    | CLSID\_AppEventsDHTMLConnector is defined as ADE6444B-C91F-4e37-92A4-5BB430A33340<br/> |



## See also

<dl> <dt>

[**Application object**](application-object.md)
</dt> <dt>

[Extending a Primary Snap-in's View](extending-a-primary-snap-ins-view.md)
</dt> </dl>

 

 





