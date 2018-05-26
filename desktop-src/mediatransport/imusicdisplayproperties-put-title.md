---
title: IMusicDisplayProperties put\_Title method
description: Sets the title of the music item.
ms.assetid: 9807ED5F-E942-4941-B255-0449138CD333
keywords:
- put_Title method
- put_Title method, IMusicDisplayProperties interface
- IMusicDisplayProperties interface, put_Title method
topic_type:
- apiref
api_name:
- IMusicDisplayProperties.put_Title
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMusicDisplayProperties::put\_Title method

Sets the title of the music item.

## Syntax


```C++
HRESULT put_Title(
   HSTRING value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **[**HSTRING**](https://msdn.microsoft.com/library/windows/desktop/br205775)**

The title of the music item.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

[**IMusicDisplayProperties**](imusicdisplayproperties.md)
</dt> </dl>

 

 





