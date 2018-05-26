---
Description: .
ms.assetid: 53f71cab-9d5a-431b-92f8-a0172856a94f
title: Software
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Software

## In this section



| Topic                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [System.AppUserModel.ExcludeFromShowInNewInstall](properties.props_system_appusermodel_excludefromshowinnewinstall)<br/> | Prevents a **Start** menu entry for a newly installed application shortcut from receiving a highlight.<br/>                                                                                                                                                                                                            |
| [System.AppUserModel.ID](properties.props_system_appusermodel_id)<br/>                                                   | An explicit Application User Model ID (AppUserModelID) used to associate processes, files, and windows with a particular application.<br/>                                                                                                                                                                             |
| [System.AppUserModel.IsDestListSeparator](properties.props_system_appusermodel_isdestlistseparator)<br/>                 | Inserts a separator in the **Tasks** section of a Jump List.<br/>                                                                                                                                                                                                                                                      |
| [System.AppUserModel.IsDualMode](props-system-appusermodel-isdualmode.md)<br/>                                          | Indicates that an application supports dual desktop and immersive modes. In Windows 8, this property is only applicable for web browsers.<br/>                                                                                                                                                                         |
| [System.AppUserModel.PreventPinning](properties.props_system_appusermodel_preventpinning)<br/>                           | Disables the ability of a shortcut or window to be pinned to the taskbar or the **Start** menu. This property also makes the item ineligible for inclusion in the **Start** menu's Most Frequently Used (MFU) list.<br/>                                                                                               |
| [System.AppUserModel.RelaunchCommand](properties.props_system_appusermodel_relaunchcommand)<br/>                         | Specifies a command that can be executed through [**ShellExecute**](shell.ShellExecute) to launch an application when it is pinned to the taskbar or when a new instance of the application is launched through the application's Jump List.<br/>                                                                      |
| [System.AppUserModel.RelaunchDisplayNameResource](properties.props_system_appusermodel_relaunchdisplaynameresource)<br/> | Specifies the display name used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button's Jump List.<br/>                                                                                                                       |
| [System.AppUserModel.RelaunchIconResource](properties.props_system_appusermodel_relaunchiconresource)<br/>               | Specifies the icon used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button's Jump List. This is the icon used for the taskbar group and is shown for a pinned application whether that application is running or not.<br/> |
| [System.AppUserModel.StartPinOption](props-system-appusermodel-startpinoption.md)<br/>                                  | Set this property on a shortcut to (1) prevent an application from being automatically pinned to Start screen upon installation; or(2) indicate that an item is programmatically added to launcher via user action (which implies automatically pin to Start and delete on unpin).<br/>                                |
| [System.AppUserModel.ToastActivatorCLSID](props-system-appusermodel-toastactivatorclsid.md)<br/>                        | Used to CoCreate an INotificationActivationCallback interface to notify about toast activations.<br/>                                                                                                                                                                                                                  |
| [System.EdgeGesture.DisableTouchWhenFullscreen](props-system-edgegesture-disabletouchwhenfullscreen.md)<br/>            | Prevents edge gesture behaviors when an application window is active and in full-screen mode (or an owned window is active). <br/>                                                                                                                                                                                     |
| [System.Software.DateLastUsed](properties.props_system_software_datelastused)<br/>                                       |                                                                                                                                                                                                                                                                                                                              |
| [System.Software.ProductName](properties.props_system_software_productname)<br/>                                         |                                                                                                                                                                                                                                                                                                                              |



 

 

 




