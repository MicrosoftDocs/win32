---
Description: The Security2 property returns a IFaxSecurity2 object used to configure security on the fax server.
ms.assetid: 2e030439-3edd-49b2-99bf-56cc3900beef
title: FaxServer.Security2 property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.Security2 property

The **Security2** property returns a [**IFaxSecurity2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxsecurity2?branch=master) object used to configure security on the fax server.

This property is read-only.

## Syntax


```VB
Property Security2 As IFaxSecurity2
```



## Property value

The address of a pointer to an [**IFaxSecurity2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxsecurity2?branch=master) object.

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

 

 




