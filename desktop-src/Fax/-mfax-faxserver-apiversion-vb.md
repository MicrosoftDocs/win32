---
Description: The APIVersion property is a value that indicates the version of the fax server API.
ms.assetid: 01e5c0d0-ce7c-47f4-949e-887bb8fa1065
title: FaxServer.APIVersion property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.APIVersion property

The **APIVersion** property is a value that indicates the version of the fax server API.

This property is read-only.

## Syntax


```VB
Property APIVersion As Integer
```



## Property value

Value from the [**FAX\_SERVER\_APIVERSION\_ENUM**](-mfax-fax-server-apiversion-enum.md) enumeration that specifies the version of the fax server API.

## Remarks

In general, each new version of the fax server API is fully compatible with previous API versions. When connecting to a fax server using the Component Object Model (COM) objects, the API version of the fax server is not required because the COM layer performs the conversions and mapping to transparently support the fax API version of the server. However, if you want to detect the version of the fax server you are connected to, you can use the **APIVersion** property.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-retrieving-server-properties.md)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxServer**](-mfax-faxserver-cpp.md)
</dt> </dl>

 

 




