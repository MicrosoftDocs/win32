---
title: IStoreFolder GetMessageClose method
description: Frees memory associated with a message enumeration handle.
ms.assetid: 9ef435d2-ffc1-476f-a40f-d6a85e293365
keywords:
- GetMessageClose method Windows Mail (formerly Outlook Express)
- GetMessageClose method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , GetMessageClose method
topic_type:
- apiref
api_name:
- IStoreFolder.GetMessageClose
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

# IStoreFolder::GetMessageClose method

Frees memory associated with a message enumeration handle.

## Syntax


```C++
HRESULT GetMessageClose(
  [in] HENUMSTORE hEnum
);
```



## Parameters

<dl> <dt>

*hEnum* \[in\]
</dt> <dd>

Type: **HENUMSTORE**

Specifies an enumeration handle to close.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or the following error value.



| Return code                                                                                  | Description                                                            |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The handle represented by the *hEnum* parameter is invalid.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IStoreFolder**](oe-istorefolder.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**GetFirstMessage**](oe-istorefolder-getfirstmessage.md)
</dt> <dt>

[**GetNextMessage**](oe-istorefolder-getnextmessage.md)
</dt> </dl>

 

 





