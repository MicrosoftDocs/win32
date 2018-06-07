---
title: Windowless ActiveX Control Accessibility
description: This section describes how to use the Windows Accessibility API to ensure that windowless Microsoft ActiveX controls are accessible.
ms.assetid: 93CBCF20-DADF-4A63-BE60-F2A0D8810C62
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windowless ActiveX Control Accessibility

This section describes how to use the Windows Accessibility API to ensure that windowless Microsoft ActiveX controls are accessible.

Windows 8 includes new Windows Accessibility API interfaces that simplify the task of implementing accessibility for windowless ActiveX controls. The API includes interfaces that are implemented on a windowless control and on the control container, enabling the windowless control and its container to work together to provide accessibility information about the windowless control. The API supports the following scenarios:

-   Microsoft Active Accessibility windowless controls hosted in a Microsoft Active Accessibility control container.
-   Microsoft Active Accessibility windowless controls hosted in a Microsoft UI Automation control container.
-   UI Automation windowless controls hosted in a Microsoft Active Accessibility control container.
-   UI Automation windowless controls hosted in a UI Automation control container.

The following table lists the interfaces that support windowless ActiveX controls and identifies the objects that implement the interfaces.



| Object              | MSAA                                                                             | UI automation                                                                                     |
|---------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Control object      | [**IAccessibleHandler**](/windows/desktop/api/oleacc/nn-oleacc-iaccessiblehandler)                                 |                                                                                                   |
| Control site        | [**IAccessibleWindowlessSite**](https://msdn.microsoft.com/library/windows/desktop/hh448752)        | [**IRawElementProviderWindowlessSite**](https://msdn.microsoft.com/library/windows/desktop/hh448787)         |
| Root of host window | [**IAccessibleHostingElementProviders**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessiblehostingelementproviders) | [**IRawElementProviderHostingAccessibles**](https://msdn.microsoft.com/library/windows/desktop/hh448785) |



 

## In this section

-   [How to Use UI Automation to Make a Windowless ActiveX Control Accessible](use-ui-automation-to-make-an-windowless-activex-control-accessible.md)
-   [How to Use MSAA to Make a Windowless ActiveX Control Accessible](use-msaa-to-make-an-windowless-activex-control-accessible.md)
-   [How to Host a UI Automation Windowless ActiveX Control](host-a-ui-automation-windowless-activex-control.md)
-   [How to Host an MSAA Windowless ActiveX Control](host-an-msaa-windowless-activex-control.md)

 

 




