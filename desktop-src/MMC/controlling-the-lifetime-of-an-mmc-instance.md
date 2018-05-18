---
title: Controlling the Lifetime of an MMC Instance
description: A script (or other automation program) controls the lifetime of the MMC instance by maintaining the UserControl and Visible properties of the Application object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '039453b2-736d-4c24-9783-75a30596f3a0'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Controlling the Lifetime of an MMC Instance

A script (or other automation program) controls the lifetime of the MMC instance by maintaining the [**UserControl**](application-usercontrol.md) and [**Visible**](application-visible.md) properties of the [**Application**](application-object.md) object. The UserControl property is read/write, and is set by directly assigning it a value. The Visible property is read-only, and is set by the [**Application.Hide**](application-hide.md) and [**Application.Show**](application-show.md) methods. By default, when MMC is started by the script, the MMC instance is hidden (the Visible property is 0) and control is maintained by the script (the UserControl property is 0).

If the script places the user in control (by setting UserControl to 1), then when the script exits, the instance of MMC remains in user control (that is, the instance of MMC does not exit). Be aware that if MMC is hidden and the script sets UserControl to 1, then MMC is displayed (not hidden).

If the script does not place the user in control, but does make the application visible (by calling the [**Application.Show**](application-show.md) method), then when the script finishes, the instance of MMC will be placed into user control and the MMC console will try to exit (this behavior is identical to the user closing MMC by selecting Close from the Console menu, or by clicking the **Close** button). Before the MMC console exits, the user may be prompted to save any changes to the document or to close open property sheets. If the user cancels the save operation, or if there were any open property sheets, the MMC console will not exit—the MMC console will continue running under user control.

If the script does not place the user in control and does not make the application visible, then when the script finishes; unsaved document changes will be discarded and the instance of MMC will quit. However, if the hidden instance of MMC contains any open property sheets, then the instance of MMC will not quit until the last property sheet is closed.

## Related topics

<dl> <dt>

[**Application object**](application-object.md)
</dt> <dt>

[**Application.Hide method**](application-hide.md)
</dt> <dt>

[**Application.Show method**](application-show.md)
</dt> <dt>

[**Application.UserControl property**](application-usercontrol.md)
</dt> <dt>

[**Application.Visible property**](application-visible.md)
</dt> </dl>

 

 




