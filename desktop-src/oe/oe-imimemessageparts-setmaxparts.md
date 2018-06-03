---
title: IMimeMessageParts SetMaxParts method
description: Specifies how many partial messages are to be added to the collection through the IMimeMessageParts AddPart method.
ms.assetid: 25d9c371-7169-400a-bc36-f696cf5445cb
keywords:
- SetMaxParts method Windows Mail (formerly Outlook Express)
- SetMaxParts method Windows Mail (formerly Outlook Express) , IMimeMessageParts interface
- IMimeMessageParts interface Windows Mail (formerly Outlook Express) , SetMaxParts method
topic_type:
- apiref
api_name:
- IMimeMessageParts.SetMaxParts
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeMessageParts::SetMaxParts method

Specifies how many partial messages are to be added to the collection through the [**IMimeMessageParts::AddPart**](oe-imimemessageparts-addpart.md) method.

## Syntax


```C++
HRESULT SetMaxParts(
  [in] ULONG cParts
);
```



## Parameters

<dl> <dt>

*cParts* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the predicted number of partial messages to be added.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates an attempt to allocate memory failed.<br/> |



 

## Remarks

This method improves performance when adding a large number of partial messages to the collection. A client does not need to call it.

## Examples

The following sample method combines a group of partial messages into the original message.


```C++
// Combine a group of partial messages into the original
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



 

 





