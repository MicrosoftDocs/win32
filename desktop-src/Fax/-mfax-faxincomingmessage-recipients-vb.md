---
Description: 'Contains the recipients associated with the inbound fax message. This property is a null-terminated string.'
ms.assetid: 'f2d624da-b24c-493f-933b-56320b14616d'
title: 'FaxIncomingMessage.Recipients property'
---

# FaxIncomingMessage.Recipients property

Contains the recipients associated with the inbound fax message. This property is a null-terminated string.

> [!Note]  
> This property is supported only in Windows Vista and later.

 

This property is read/write.

## Syntax


```VB
Property Recipients As String
```



## Property value

A list of the recipients of the inbound fax message.

## Remarks

A received message starts with a null value for the recipients when it arrives. A list of recipients can be specified by a [routing assistant](-mfax-glossary.md) when it is reassigned.

Each recipient is identified on the pattern of &lt;DomainName&gt;\\&lt;UserName&gt;. A colon ":" separates each recipient. For local users, &lt;DomainName&gt; is the local computer name.

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

 

 




