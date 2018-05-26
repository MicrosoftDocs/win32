---
Description: The Item property returns a FaxRecipient object from the FaxRecipients collection.
ms.assetid: efb17932-40c9-4903-9c6e-80e4e684d063
title: FaxRecipients.Item property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxRecipients.Item property

The **Item** property returns a [**FaxRecipient**](-mfax-faxrecipient.md) object from the [**FaxRecipients**](-mfax-faxrecipients.md) collection.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal lIndex As Long _
) As IFaxRecipient
```



## Property value

A variable of type [**IFaxRecipient**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxrecipient?branch=master) that receives A [**FaxRecipient**](-mfax-faxrecipient.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxRecipients**](-mfax-faxrecipients.md)
</dt> <dt>

[**IFaxRecipients**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxrecipients?branch=master)
</dt> <dt>

[Broadcasting a Fax](-mfax-broadcasting-a-fax.md)
</dt> </dl>

 

 




