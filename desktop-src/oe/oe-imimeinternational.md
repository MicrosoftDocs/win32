---
title: IMimeInternational interface
description: Do not use. Performs character-set conversions and queries information about character sets and codepages.
ms.assetid: '22eaa889-928e-4b78-b874-7841f03dc66a'
keywords: ["IMimeInternational interface Windows Mail (formerly Outlook Express)", "IMimeInternational interface Windows Mail (formerly Outlook Express) , described"]
topic_type:
- apiref
api_name:
- IMimeInternational
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeInternational interface

Do not use. Performs character-set conversions and queries information about character sets and codepages.

## Members

The **IMimeInternational** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Remarks

For the most part, other interfaces such as [**IMimeMessage**](oe-imimemessage.md), [**IMimeMessageTree**](oe-imimemessagetree.md), [**IMimeBody**](oe-imimebody.md), and [**IMimePropertySet**](oe-imimepropertyset.md) internally handle character-set conversions. A client might use this interface to get information about a character set or to decode or encode a single piece of data like a message subject downloaded from an Network News Transport Protocol (NNTP) or Internet Message Access Protocol (IMAP) server. Internally, **IMimeInternational** uses [MLang](https://msdn.microsoft.com/library/aa767865) (Mlang.dll) to implement most of its functionality.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





