---
Description: The CurrentAccount property returns the fax account for the user account that has connected to the fax server.
ms.assetid: 20f93d2a-3f3c-4086-8574-98a11b4bf0e4
title: FaxServer.CurrentAccount property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.CurrentAccount property

The **CurrentAccount** property returns the fax account for the user account that has connected to the fax server.

This property is read-only.

## Syntax


```VB
Property CurrentAccount As IFaxAccount
```



## Property value

An address of a pointer to an [**IFaxAccount**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccount?branch=master) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**IFaxServer2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxserver2?branch=master)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> </dl>

 

 




