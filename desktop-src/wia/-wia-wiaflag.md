---
Description: 'Flags used by the IWiaDevMgr::GetImageDlg, IWiaDevMgr2::GetImageDlg, IWiaItem::DeviceDlg, and IWiaItem2::DeviceDlg methods to control the dialog box operation.'
ms.assetid: '468a3c9e-64f8-456d-aad9-fa7c6876fbe6'
title: WiaFlag
---

# WiaFlag

Flags used by the [**IWiaDevMgr::GetImageDlg**](-wia-iwiadevmgr-getimagedlg.md), [**IWiaDevMgr2::GetImageDlg**](-wia-iwiadevmgr2-getimagedlg.md), [**IWiaItem::DeviceDlg**](-wia-iwiaitem-devicedlg.md), and [**IWiaItem2::DeviceDlg**](-wia-iwiaitem2-devicedlg.md) methods to control the dialog box operation.



| Constant                                                                                                                                                                                                                | Description                                                                                                                                                                                                 |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WIA_DEVICE_DIALOG_SINGLE_IMAGE"></span><span id="wia_device_dialog_single_image"></span><dl> <dt>**WIA\_DEVICE\_DIALOG\_SINGLE\_IMAGE**</dt> </dl>     | Restrict image selection to a single image in the device image acquisition dialog box.<br/>                                                                                                           |
| <span id="WIA_DEVICE_DIALOG_USE_COMMON_UI"></span><span id="wia_device_dialog_use_common_ui"></span><dl> <dt>**WIA\_DEVICE\_DIALOG\_USE\_COMMON\_UI**</dt> </dl> | Use the system UI, if available, rather than the vendor-supplied UI. If the system UI is not available, the vendor UI is used. If neither UI is available, the function returns E\_NOTIMPL.<br/>      |
| <span id="WIA_SELECT_DEVICE_NODEFAULT"></span><span id="wia_select_device_nodefault"></span><dl> <dt>**WIA\_SELECT\_DEVICE\_NODEFAULT**</dt> </dl>               | Force the [**IWiaDevMgr::GetImageDlg**](-wia-iwiadevmgr-getimagedlg.md) or [**IWiaDevMgr2::GetImageDlg**](-wia-iwiadevmgr2-getimagedlg.md) method to display the **Select Device** dialog box.<br/> |



## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 




