---
title: IMessenger3 Property property
description: get\_Property retrieves the Messenger client version and the locale ID (LCID). put\_Property is reserved. Do not use.
ms.assetid: 12654942-862f-4724-af38-6b98567a7a6f
keywords:
- Property property Windows Messenger
- Property property Windows Messenger , IMessenger3 interface
- IMessenger3 interface Windows Messenger , Property property
topic_type:
- apiref
api_name:
- IMessenger3.Property
- IMessenger3.get_Property
- IMessenger3.put_Property
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMessenger3::Property property

\[**Property** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

`get_Property` retrieves the Messenger client version and the locale ID (LCID). `put_Property` is reserved. Do not use.

This property is read/write.

## Syntax


```C++
HRESULT put_Property(
  [in]          MMESSENGERPROPERTY ePropType,
  [in]          VARIANT            vPropVal
);

HRESULT get_Property(
  [in]          MMESSENGERPROPERTY ePropType,
  [out, retval] VARIANT            *pvPropVal
);
```



## Property value

A pointer to a **VARIANT** that contains the property value. (Variant type differs depending on the property being set or retrieved.)

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                                                                                                                                                                                    |
| <dl> <dt>E\_INVALIDARG</dt> </dl>              | For `get_Property`, *ePropType* is out of range (not within [**MMESSENGERPROPERTY**](im-mmessengerproperty.md) range). For `put_Property`, E\_INVALIDARG is returned in all cases. This method is reserved.<br/> |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pvPropVal* is a **NULL** pointer. <br/>                                                                                                                                                                          |



## Remarks

The following table contains the country code, LCID, code pate, and language supported by Messenger.



| Country Code | LCID (Hexadecimal) | Code Page (Decimal) | Language                     |
|--------------|--------------------|---------------------|------------------------------|
| EN           | 0x0409             | 1252                | English                      |
| DE           | 0x0407             | 1252                | German                       |
| JA           | 0x0411             | 932                 | Japanese                     |
| KO           | 0x0412             | 949                 | Korean                       |
| TW           | 0x0404             | 950                 | Traditional Chinese (Taiwan) |
| CN           | 0x0804             | 936                 | Simplified Chinese (PRC)     |
| FR           | 0x040c             | 1252                | French                       |
| ES           | 0x0c0a             | 1252                | Spanish                      |
| SV           | 0x041d             | 1252                | Swedish                      |
| IT           | 0x0410             | 1252                | Italian                      |
| NO           | 0x0414             | 1252                | Norwegian                    |
| BR           | 0x0416             | 1252                | Brazilian                    |
| NL           | 0x0413             | 1252                | Dutch                        |
| DA           | 0x0406             | 1252                | Danish                       |
| FI           | 0x040b             | 1252                | Finnish                      |
| PT           | 0x0816             | 1252                | Portuguese                   |
| CS           | 0x0405             | 1250                | Czech                        |
| PL           | 0x0415             | 1250                | Polish                       |
| HU           | 0x040e             | 1250                | Hungarian                    |
| RU           | 0x0419             | 1251                | Russian                      |
| tr           | 0x041f             | 1254                | Turkish                      |
| EL           | 0x0408             | 1253                | Greek                        |
| SK           | 0x041b             | 1250                | Slovak                       |
| SL           | 0x0424             | 1250                | Slovenian                    |
| AR           | 0x0401             | 1256                | Arabic                       |
| HE           | 0x040d             | 1255                | Hebrew                       |



 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





