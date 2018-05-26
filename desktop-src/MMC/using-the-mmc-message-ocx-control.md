---
title: Using the MMC 2.0 Message OCX Control
description: This feature is introduced in MMC 1.2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bc6db308-d8dd-4868-803d-45c64b951192
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMC 2.0 message OCX control
- message OCX control MMC 2.0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using the MMC 2.0 Message OCX Control

This feature is introduced in MMC 1.2.

MMC provides a message OCX control that snap-ins can use for that displays messages in the result pane. The message OCX control optimizes the performance of snap-in error and warning messages and is therefore the recommended way for a snap-in to display such messages.

Snap-ins can also display messages using a modal message box. However, snap-ins should only use modal message boxes in response to a context menu action, or to alert the user of some error condition that is serious enough to warrant their use.

For messages that need only be displayed when a snap-in is selected, the best choice is to use the MMC message OCX control. The OCX control is displayed in the result pane of a snap-in, so the snap-in can only display a message using the control when it has the focus.

Typically, the message OCX should be used to inform the user of any problems the snap-in encounters when enumerating and that displays items in the result pane of the selected scope item.

The [**IMessageView**](/windows/win32/Mmc/nn-mmc-imessageview?branch=master) interface allows snap-ins to interact with the message OCX control. Its methods can be used to set the text and icon of the error message displayed by the OCX control.

**To use the MMC message OCX control**

1.  If a snap-in wants to display a message (error message or other) for a particular scope item, it should call [**IConsole2::SelectScopeItem**](iconsole2-selectscopeitem.md) to select the item and force a call to its [**IComponent::GetResultViewType**](/windows/win32/Mmc/nf-mmc-icomponent-getresultviewtype?branch=master) method.
2.  Handle selection of the OCX view in the [**IComponent::GetResultViewType**](/windows/win32/Mmc/nf-mmc-icomponent-getresultviewtype?branch=master) method.

    For the MMC message OCX control, the *ppViewType* parameter should be computed with the following:

    ```C++
    StringFromCLSID (CLSID_MessageView, ppViewType);
    ```

    

    The [**StringFromCLSID**](_com_stringfromclsid) function allocates the buffer and formats the string in the correct manner required by [**GetResultViewType**](/windows/win32/Mmc/nf-mmc-icomponent-getresultviewtype?branch=master).

3.  Handle the [**MMCN\_SHOW**](mmcn-show.md) notification message sent to the snap-in's [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) implementation. To obtain the message OCX control's [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface pointer, call [**IConsole2::QueryResultView**](iconsole2-queryresultview.md) and query for the [**IMessageView**](/windows/win32/Mmc/nn-mmc-imessageview?branch=master) interface.

    Using the OCX control's [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface pointer, call the methods of the [**IMessageView**](/windows/win32/Mmc/nn-mmc-imessageview?branch=master) interface to modify the text and icon of the message. Be aware that the snap-in can delete the text strings and icon immediately after the calls are made to **IMessageView** methods.

    Upon deselection of the result pane, the *arg* parameter of MMCN\_SHOW is set to **FALSE**, indicating that the OCX view is being torn down. At this time, the snap-in can do any necessary clean-up.

## Related topics

<dl> <dt>

[Using Custom OCX Controls](using-custom-ocx-controls.md)
</dt> <dt>

[Using List Views](using-list-views.md)
</dt> </dl>

 

 




