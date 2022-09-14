---
description: Starting with Windows Vista, the TextInputPanel supersedes the PenInputPanel for controlling the onscreen appearance and behavior of the Tablet Input Panel.The following sections describe programming the Input Panel using the Text Input Panel application programming interfaces.TextInputPanel for Users of PenInputPanelUsing Input Panel AutoCompleteEnabling Text Correction for Custom Ink CollectorsNote  The Text Input Panel is implemented in an executable file called TabTip.exe. Running TabTip.exe with the /SeekDesktop parameter attempts to run a reduced functionality version of Input Panel on a nonstandard interactive desktop, as created with CreateDesktop. For most created desktops, Input Panel will automatically run in this mode already. This parameter provides the means for launching it in unusual application scenarios that otherwise prevent the automatic launch. If Input Panel is already running on the desktop, this parameter will have no effect and the instance of TabTip.exe will exit immediately.
ms.assetid: af0a2946-88d0-4f2e-98ca-446398aeb6b8
title: Programming the Text Input Panel
ms.topic: article
ms.date: 05/31/2018
---

# Programming the Text Input Panel

Starting with Windows Vista, the [**TextInputPanel**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpanel) supersedes the [**PenInputPanel**](peninputpanel-class.md) for controlling the onscreen appearance and behavior of the Tablet Input Panel.

The following sections describe programming the Input Panel using the Text Input Panel application programming interfaces.

-   [TextInputPanel for Users of PenInputPanel](textinputpanel-for-users-of-peninputpanel.md)
-   [Using Input Panel AutoComplete](using-input-panel-autocomplete.md)
-   [Enabling Text Correction for Custom Ink Collectors](enabling-text-correction-for-custom-ink-collectors.md)

> [!Note]  
> The Text Input Panel is implemented in an executable file called TabTip.exe. Running TabTip.exe with the */SeekDesktop* parameter attempts to run a reduced functionality version of Input Panel on a nonstandard interactive desktop, as created with [**CreateDesktop**](/windows/win32/api/winuser/nf-winuser-createdesktopa). For most created desktops, Input Panel will automatically run in this mode already. This parameter provides the means for launching it in unusual application scenarios that otherwise prevent the automatic launch. If Input Panel is already running on the desktop, this parameter will have no effect and the instance of TabTip.exe will exit immediately.

 

## Related topics

<dl> <dt>

[Programming the Input Panel Using the PenInputPanel Class](programming-the-input-panel-using-the-peninputpanel-class.md)
</dt> </dl>

 

 
