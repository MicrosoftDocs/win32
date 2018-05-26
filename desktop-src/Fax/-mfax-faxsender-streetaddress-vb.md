---
Description: The StreetAddress property is a null-terminated string that contains the street address associated with the sender.
ms.assetid: 3d978556-01f7-477e-a9b3-66b8adf56c5d
title: FaxSender.StreetAddress property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxSender.StreetAddress property

The **StreetAddress** property is a null-terminated string that contains the street address associated with the sender.

This property is read/write.

## Syntax


```VB
Property StreetAddress As String
```



## Property value

A **String** that specifies or receives the street address associated with the sender.

## Remarks

The street address should also include the city, state, zip code (postal code) and country/region for the sender.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-sending-a-fax.md)
</dt> <dt>

[**FaxSender**](-mfax-faxsender.md)
</dt> <dt>

[**IFaxSender**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxsender?branch=master)
</dt> </dl>

 

 




