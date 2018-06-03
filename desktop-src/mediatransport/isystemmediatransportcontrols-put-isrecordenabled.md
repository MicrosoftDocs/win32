---
title: ISystemMediaTransportControls put\_IsRecordEnabled method
description: Sets a value that specifies if the record button should be enabled.
ms.assetid: 0B385A05-2551-4C32-9FEC-3E080B23AC36
keywords:
- put_IsRecordEnabled method
- put_IsRecordEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, put_IsRecordEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_IsRecordEnabled
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISystemMediaTransportControls::put\_IsRecordEnabled method

Sets a value that specifies if the record button should be enabled.

## Syntax


```C++
HRESULT put_IsRecordEnabled(
   boolean value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **boolean**

Set to true to enable the record button. Set to false to disable it.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Windows.Media.SystemMediaTransportControls.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.Media.SystemMediaTransportControls.idl</dt> </dl> |



## See also

<dl> <dt>

[**ISystemMediaTransportControls**](isystemmediatransportcontrols.md)
</dt> </dl>

 

 





