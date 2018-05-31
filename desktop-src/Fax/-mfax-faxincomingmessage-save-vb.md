---
Description: Saves the FaxIncomingMessage object's data.
ms.assetid: b62f318f-76e6-4902-9b8b-a45d56bc067b
title: FaxIncomingMessage.Save method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessage.Save method

Saves the [**FaxIncomingMessage**](-mfax-faxincomingmessage.md) object's data.

> [!Note]  
> This method is supported only in Windows Vista and later.

 

## Syntax


```VB
FaxIncomingMessage.Save() As Long
```



## Parameters

This method has no parameters.

## Remarks

To use this method, a user must have the [****far2MANAGE\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum_2) and [****far2QUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum_2) access rights.

It is not necessary to call this method to commit changes to the [**Subject**](-mfax-faxincomingmessage-subject-vb.md), [**SenderName**](-mfax-faxincomingmessage-sendername-vb.md), [**SenderFaxNumber**](-mfax-faxincomingmessage-senderfaxnumber-vb.md), and [**HasCoverPage**](-mfax-faxincomingmessage-hascoverpage-vb.md) properties. They are committed with the [**Reassign**](-mfax-faxincomingmessage-reassign-vb.md) method.

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

[**IFaxIncomingMessage**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingmessage)
</dt> </dl>

 

 




