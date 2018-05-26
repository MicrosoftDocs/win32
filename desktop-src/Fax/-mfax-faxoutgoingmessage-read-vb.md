---
Description: Indicates if the fax has been read.
ms.assetid: c0591f83-d8ea-4fb5-a8cb-e13fa44b638f
title: FaxOutgoingMessage.Read property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingMessage.Read property

Indicates if the fax has been read.

> [!Note]  
> This property is supported only on Windows Vista and later.

 

This property is read/write.

## Syntax


```VB
Property Read As Boolean
```



## Property value

A flag indicating whether the inbound fax message has been read.

## Remarks

Possible values are VARIANT\_TRUE and VARIANT\_FALSE.

A change to this value is not committed to the server until [**Save**](-mfax-faxoutgoingmessage-save-vb.md) is called.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md)
</dt> <dt>

[**IFaxOutgoingMessage2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingmessage2?branch=master)
</dt> </dl>

 

 




