---
Description: The Debug property is a Boolean value that indicates whether the fax server was created in a debug environment.
ms.assetid: 5f3f6951-8687-47ad-b173-5afbcd9fd189
title: FaxServer.Debug property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.Debug property

The **Debug** property is a Boolean value that indicates whether the fax server was created in a debug environment.

This property is read-only.

## Syntax


```VB
Property Debug As Boolean
```



## Property value

A **Boolean** that receives the fax server was created in a debug environment.

## Remarks

If this property is equal to **True**, the fax server was created in a debug environment. If this property is equal to **False**, the fax server was not created in a debug environment.

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

[**IFaxServer**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxserver?branch=master)
</dt> </dl>

 

 




