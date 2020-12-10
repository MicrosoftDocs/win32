---
title: PSM_GETRESULT message (Prsht.h)
description: Used by modeless property sheets to retrieve the information returned to modal property sheets by PropertySheet. You can send this message explicitly or use the PropSheet\_GetResult macro.
ms.assetid: e0f609ea-5d7e-4c17-ade1-3c1051c5a5bf
keywords:
- PSM_GETRESULT message Windows Controls
topic_type:
- apiref
api_name:
- PSM_GETRESULT
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_GETRESULT message

Used by modeless property sheets to retrieve the information returned to modal property sheets by [**PropertySheet**](/windows/desktop/api/Prsht/nf-prsht-propertysheeta). You can send this message explicitly or use the [**PropSheet\_GetResult**](/windows/desktop/api/Prsht/nf-prsht-propsheet_getresult) macro.

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

Returns a positive value if successful, or -1 otherwise. The following return values have a special meaning.



| Return code                                                                                         | Description                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ID\_PSREBOOTSYSTEM**</dt> </dl>   | A page sent a [**PSM\_REBOOTSYSTEM**](psm-rebootsystem.md) message to the property sheet. The computer must be restarted for the user's changes to take effect.<br/> |
| <dl> <dt>**ID\_PSRESTARTWINDOWS**</dt> </dl> | A page sent a [**PSM\_RESTARTWINDOWS**](psm-restartwindows.md) message to the property sheet. Windows must be restarted for the user's changes to take effect.<br/>  |



 

## Remarks

To retrieve extended error information, call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

The return value for this message is identical to what [**PropertySheet**](/windows/desktop/api/Prsht/nf-prsht-propertysheeta) returns for a modal property sheet.

[Version 5.80.](common-control-versions.md) The [**PropertySheet**](/windows/desktop/api/Prsht/nf-prsht-propertysheeta) return value carries different information for modal and modeless property sheets. In some cases, modeless property sheets may need the information they would have received from **PropertySheet** if they had been modal. In particular, they may need to know whether ID\_PSREBOOTSYSTEM or ID\_PSRESTARTWINDOWS would have been returned.

For a modeless property sheet, your message loop should use [**PSM\_ISDIALOGMESSAGE**](psm-isdialogmessage.md) to pass messages to the property sheet dialog box, and [**PSM\_GETCURRENTPAGEHWND**](psm-getcurrentpagehwnd.md) to determine when to destroy the dialog box. When the user clicks the **OK** or **Cancel** button, **PSM\_GETCURRENTPAGEHWND** returns **NULL**. You can then retrieve the value that a modal property sheet would have received from [**PropertySheet**](/windows/desktop/api/Prsht/nf-prsht-propertysheeta) by sending a **PSM\_GETRESULT** message.

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

