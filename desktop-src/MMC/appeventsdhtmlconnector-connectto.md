---
title: EventConnector ConnectTo method
description: The ConnectTo method provides a way for an Application object to receive event notification.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '04360c43-0fad-4b5e-8167-5a7b42aee351'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["ConnectTo method MMC", "ConnectTo method MMC , AppEventsDHTMLConnector object", "AppEventsDHTMLConnector object MMC , ConnectTo method", "ConnectTo method MMC , EventConnector interface", "EventConnector interface MMC , ConnectTo method"]
topic_type:
- apiref
api_name:
- AppEventsDHTMLConnector.ConnectTo
- EventConnector.ConnectTo
api_location:
- Mmcndmgr.dll
api_type:
- COM
---

# EventConnector::ConnectTo method

The **ConnectTo** method provides a way for an [**Application object**](application-object.md) to receive event notification.

## Syntax


```VB
AppEventsDHTMLConnector.ConnectTo( _
  ByVal Application As Application _
)
```



## Parameters

<dl> <dt>

*Application* 
</dt> <dd>

The [**Application**](application-object.md) object that will receive event notification.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To close the connection, call [**AppEventsDHTMLConnector.Disconnect**](appeventsdhtmlconnector-disconnect.md).

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                               |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>          |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>        |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl>      |
| CLSID<br/>                    | CLSID\_AppEventsDHTMLConnector is defined as ADE6444B-C91F-4e37-92A4-5BB430A33340<br/> |
| IID<br/>                      | IID\_\_EventConnector is defined as C0BCCD30-DE44-4528-8403-A05A6A1CC8EA<br/>          |



## See also

<dl> <dt>

[**Application object**](application-object.md)
</dt> <dt>

[**AppEventsDHTMLConnector.Disconnect**](appeventsdhtmlconnector-disconnect.md)
</dt> </dl>

 

 





