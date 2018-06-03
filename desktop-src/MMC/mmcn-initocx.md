---
title: MMCN\_INITOCX message
description: The MMCN\_INITOCX notification message is sent to snap-ins having an OCX as the result pane. The notification is sent when the custom OCX is initialized for the first time.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 79256d4a-a936-419e-a953-80d743d05290
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_INITOCX message MMC
topic_type:
- apiref
api_name:
- MMCN_INITOCX
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_INITOCX message

The **MMCN\_INITOCX** notification message is sent to snap-ins having an OCX as the result pane. The notification is sent when the custom OCX is initialized for the first time.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

Not used.

</dd> <dt>

*arg* 
</dt> <dd>

Not used.

</dd> <dt>

*param* 
</dt> <dd>

The [**IUnknown**](https://www.bing.com/search?q=**IUnknown**) to the OCX, the result pane. This is the same **IUnknown** you would get from [**IConsole::QueryResultView**](https://www.bing.com/search?q=**IConsole::QueryResultView**).

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The snap-in successfully handled the notification.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The snap-in does not handle the notification. MMC then performs a default operation for the notification.

</dd> </dl>

## Remarks

When an OCX is created for the first time, and must be initialized, the snap-in is sent an **MMCN\_INITOCX** notification.

### Note

If a snap-in implements [**IComponent2**](/windows/desktop/api/Mmc/nn-mmc-icomponent2) and uses an OCX for the result pane, then the **MMCN\_INITOCX** notification will not be sent; instead, the snap-in should initialize the OCX during the call to [**IComponent2::GetResultViewType2**](/windows/desktop/api/Mmc/nf-mmc-icomponent2-getresultviewtype2).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IConsole::QueryResultView**](https://www.bing.com/search?q=**IConsole::QueryResultView**)
</dt> </dl>

 

 





