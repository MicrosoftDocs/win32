---
title: PSM\_RESTARTWINDOWS message
description: Indicates that Windows needs to be restarted for the changes to take effect.
ms.assetid: 5bf634ee-7408-45df-adb6-c5b947f6c47b
keywords:
- PSM_RESTARTWINDOWS message Windows Controls
topic_type:
- apiref
api_name:
- PSM_RESTARTWINDOWS
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PSM\_RESTARTWINDOWS message

Indicates that Windows needs to be restarted for the changes to take effect.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

No return value.

## Remarks

An application should send this message only in response to the [PSN\_APPLY](psn-apply.md) or [PSN\_KILLACTIVE](psn-killactive.md) notification code. You can send the **PSM\_RESTARTWINDOWS** message explicitly or by using the [**PropSheet\_RestartWindows**](/windows/win32/Prsht/nf-prsht-propsheet_restartwindows?branch=master) macro.

This message causes the [**PropertySheet**](/windows/win32/Prsht/nf-prsht-propertysheeta?branch=master) function to return the ID\_PSRESTARTWINDOWS value, but only if the user clicks the **OK** button to close the property sheet. It is the application's responsibility to restart Windows, which can be done by using the [**ExitWindowsEx**](https://msdn.microsoft.com/library/windows/desktop/aa376868) function.

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/win32/Prsht/ns-prsht-_propsheetheadera_v2?branch=master)).

 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





