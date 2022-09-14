---
description: The AutoReconnect property of the SWbemRefresher object is a Boolean value that indicates whether the refresher automatically reconnects to a remote provider if the connection is broken.
ms.assetid: 3be24128-8a35-44b0-befd-8b8937eff1b7
ms.tgt_platform: multiple
title: SWbemRefresher.AutoReconnect property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemRefresher.AutoReconnect
- ISWbemRefresher.AutoReconnect
- ISWbemRefresher.get_AutoReconnect
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemRefresher.AutoReconnect property

The **AutoReconnect** property of the [**SWbemRefresher**](swbemrefresher.md) object is a Boolean value that indicates whether the refresher automatically reconnects to a remote provider if the connection is broken.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemRefresher.AutoReconnect As Boolean
```



## Property value

## Remarks

Modifying this property affects only objects in the refresher that are backed by a high-performance provider. If the provider is not a high-performance provider, then setting the **AutoReconnect** property to **TRUE** has no effect because the [**SWbemRefresher**](swbemrefresher.md) object never reconnects.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemRefresher<br/>                                                        |
| IID<br/>                      | IID\_ISWbemRefresher<br/>                                                         |



## See also

<dl> <dt>

[**SWbemRefresher**](swbemrefresher.md)
</dt> </dl>

 

 




