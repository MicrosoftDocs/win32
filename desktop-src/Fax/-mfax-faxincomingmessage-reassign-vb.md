---
Description: 'Reassign the fax to one or more recipients. It also commits changes to the Subject, SenderName, SenderFaxNumber, and HasCoverPage properties.'
ms.assetid: 'c8b0d5c7-9e28-4fc5-9e78-bd7c555d1e7e'
title: 'FaxIncomingMessage.Reassign method'
---

# FaxIncomingMessage.Reassign method

[Reassign](-mfax-glossary.md) the fax to one or more recipients. It also commits changes to the [**Subject**](-mfax-faxincomingmessage-subject-vb.md), [**SenderName**](-mfax-faxincomingmessage-sendername-vb.md), [**SenderFaxNumber**](-mfax-faxincomingmessage-senderfaxnumber-vb.md), and [**HasCoverPage**](-mfax-faxincomingmessage-hascoverpage-vb.md) properties.

> [!Note]  
> This method is supported only in Windows Vista and later.

 

## Syntax


```VB
FaxIncomingMessage.Reassign() As Long
```



## Parameters

This method has no parameters.

## Remarks

To use this method, a user must have the [****far2MANAGE\_RECEIVE\_FOLDER****](-mfax-fax-access-rights-enum-2.md) and [****far2QUERY\_CONFIG****](-mfax-fax-access-rights-enum-2.md) access rights. Also, IFaxConfiguration::IncomingFaxesArePublic must be set to false.

If the [routing assistant](-mfax-glossary.md) application is going to set the [**Subject**](-mfax-faxincomingmessage-subject-vb.md), [**SenderName**](-mfax-faxincomingmessage-sendername-vb.md), [**SenderFaxNumber**](-mfax-faxincomingmessage-senderfaxnumber-vb.md), or [**HasCoverPage**](-mfax-faxincomingmessage-hascoverpage-vb.md) properties, it should do this before calling **Reassign**. **Reassign** will commit those changes, so it is not necessary to call [**Save**](-mfax-faxincomingmessage-save-vb.md).

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

[**IFaxIncomingMessage2**](-mfax-faxincomingmessage2-cpp.md)
</dt> </dl>

 

 




