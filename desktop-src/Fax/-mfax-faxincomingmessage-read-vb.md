---
Description: A flag that indicates if the fax has been read.
ms.assetid: 4ad2446d-a453-41f6-a891-8779a26e8d3a
title: FaxIncomingMessage.Read property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessage.Read property

A flag that indicates if the fax has been read.

> [!Note]  
> This property is supported only in Windows Vista and later.

 

This property is read/write.

## Syntax


```VB
Property Read As Boolean
```



## Property value

A flag indicating whether the inbound fax message has been read.

## Remarks

Possible values are VARIANT\_TRUE and VARIANT\_FALSE.

A change to this value is not committed to the server until [**Save**](-mfax-faxincomingmessage-save-vb.md) is called.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxIncomingMessage**](-mfax-faxincomingmessage.md)
</dt> <dt>

[**IFaxIncomingMessage2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingmessage2)
</dt> </dl>

 

 




