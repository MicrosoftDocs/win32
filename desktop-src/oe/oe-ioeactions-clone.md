---
title: IOEActions Clone method
description: IOEActions Clone is no longer available for use as of Windows Vista.
ms.assetid: 1d9f9db7-7e4d-4cc9-8247-558e68ad07df
keywords:
- Clone method Windows Mail (formerly Outlook Express)
- Clone method Windows Mail (formerly Outlook Express) , IOEActions interface
- IOEActions interface Windows Mail (formerly Outlook Express) , Clone method
topic_type:
- apiref
api_name:
- IOEActions.Clone
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

# IOEActions::Clone method

\[**IOEActions::Clone** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT Clone(
  [out] IOEActions **ppIActions
);
```



## Parameters

<dl> <dt>

*ppIActions* \[out\]
</dt> <dd>

Type: **[**IOEActions**](oe-ioeactions.md)\*\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





