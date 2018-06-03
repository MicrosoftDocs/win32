---
title: IMimePropertySet IsContentType method
description: Queries the Content-Type of a property set.
ms.assetid: 401bbddb-2918-41a8-b2e9-55f86f6ca0dd
keywords:
- IsContentType method Windows Mail (formerly Outlook Express)
- IsContentType method Windows Mail (formerly Outlook Express) , IMimePropertySet interface
- IMimePropertySet interface Windows Mail (formerly Outlook Express) , IsContentType method
topic_type:
- apiref
api_name:
- IMimePropertySet.IsContentType
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

# IMimePropertySet::IsContentType method

Queries the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) of a property set.

## Syntax


```C++
HRESULT IsContentType(
  [in] LPCSTR pszPriType,
  [in] LPCSTR pszSubType
);
```



## Parameters

<dl> <dt>

*pszPriType* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the primary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp), for example, multipart or text.

</dd> <dt>

*pszSubType* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the secondary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp), for example, mixed or html.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) matches the specified types or that both *pszPriType* and *pszSubType* are **NULL**.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) does not match the specified types. <br/>                                                 |



 

## Remarks

This method is more efficient than fetching the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) property, comparing against it, and then freeing that value. If a property set does not have a Content-Type, the Content-Type defaults to text/plain according to [RFC 1521](http://www.ietf.org/rfc/rfc1521.txt).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





