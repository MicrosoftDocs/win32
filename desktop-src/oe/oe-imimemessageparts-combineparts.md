---
title: IMimeMessageParts CombineParts method
description: Combines all the parts in the current collection into a single message.
ms.assetid: 102781df-7759-4567-962a-b74d1eb482ae
keywords:
- CombineParts method Windows Mail (formerly Outlook Express)
- CombineParts method Windows Mail (formerly Outlook Express) , IMimeMessageParts interface
- IMimeMessageParts interface Windows Mail (formerly Outlook Express) , CombineParts method
topic_type:
- apiref
api_name:
- IMimeMessageParts.CombineParts
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMimeMessageParts::CombineParts method

Combines all the parts in the current collection into a single message.

## Syntax


```C++
HRESULT CombineParts(
  [out] IMimeMessage **ppMessage
);
```



## Parameters

<dl> <dt>

*ppMessage* \[out\]
</dt> <dd>

Type: **[**IMimeMessage**](oe-imimemessage.md)\*\***

Receives the address of a pointer to the [**IMimeMessage**](oe-imimemessage.md) object containing the combined message.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppMessage* is **NULL**. <br/>        |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates an attempt to allocate memory failed.<br/> |



 

## Examples

The following sample method combines a group of partial messages into the original message.


```C++
// Combine a group of partial messages into the original.
HRESULT CombineMsgParts(ULONG cParts, IMimeMessage **prgpMsg, IMimeMessage **ppOriginal)
{
   // Local Variables
   IMimeMessageParts *pParts;

   // Create an IMimeMessageParts object.
   CoCreateInstance(CLSID_IMimeMessageParts, NULL, CLSCTX_INPROC_SERVER, IID_IMimeMessageParts, (LPVOID *)&amp;pParts);

   // Tell IMimeMessageParts how many parts to add.
   pParts->SetMaxParts(cParts);

   // Add all the parts into the IMimeMessageParts object.
   for (ULONG i = 0; i < cParts; i++)
      pParts->AddPart(prgpMsg[i]);

   // Combine all the parts into a single IMimeMessage.
   pParts->CombineParts(ppOriginal);

   // Done
   return(S_OK);
}

                
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





