---
title: How to Host an MSAA Windowless ActiveX Control
description: Learn how to create a control container that can host windowless Microsoft ActiveX controls that implement Microsoft Active Accessibility.
ms.assetid: 9497561C-37ED-4094-A6B0-C219F63C04B6
keywords:
- MSAA, Windowless ActiveX control
- Windowless ActiveX control, MSAA
ms.topic: article
ms.date: 05/31/2018
---

# How to Host an MSAA Windowless ActiveX Control

Learn how to create a control container that can host windowless Microsoft ActiveX controls that implement Microsoft Active Accessibility. By following the steps described here, you can ensure that any Microsoft Active Accessibility-based windowless controls that are hosted in your control container are accessible to assistive technology (AT) client applications.

## What you need to know

### Technologies

-   [ActiveX Controls](/windows/desktop/com/activex-controls)
-   [Microsoft Active Accessibility](microsoft-active-accessibility.md)

### Prerequisites

-   C/C++
-   Microsoft Win32 and Component Object Model (COM) programming
-   Windowless ActiveX controls
-   Microsoft Active Accessibility servers

## Instructions

### Step 1: Provide the root IAccessible interface on behalf of the windowless control.

Whenever the system needs the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) pointer for the root of a windowless control, the system queries the control container. To retrieve the pointer, the container calls the windowless control's implementation of the [**IServiceProvider::QueryService**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/cc678966(v=vs.85)) method.

If the control container has a Microsoft Active Accessibility implementation, it can return the windowless control's [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) pointer to the system.

If the control container has a Microsoft UI Automation implementation, call the [**UiaProviderFromIAccessible**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaproviderfromiaccessible) function to obtain an [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple) interface pointer that represents the control, and then return the **IRawElementProviderSimple** interface pointer to the system.

### Step 2: Respond to the WM\_GETOBJECT message on behalf of the windowless control.

When a client application responds to a WinEvent raised by a windowless control, the control container receives a [**WM\_GETOBJECT**](wm-getobject.md) message on behalf of the control. The message includes the object ID of the windowless control that raised the event.

The control container responds by looking up the windowless control that "owns" the object ID, and then calling that control's [**IAccessibleHandler::AccessibleObjectFromID**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessiblehandler-accessibleobjectfromid) method. The **AccessibleObjectFromID** method returns the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer for the UI item, and the control container returns the pointer to the system, which forwards it to the client application.

### Step 3: Implement the IAccessibleWindowlessSite interface.

1.  Implement the [**IAccessibleWindowlessSite::GetParentAccessible**](/windows/desktop/api/oleacc/nf-oleacc-iaccessiblewindowlesssite-getparentaccessible) method.

    When a client application needs accessibility information about the parent of the windowless control's root provider, the system calls the windowless control's [**IAccessible::get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent) method. The control responds by calling the control container's [**IAccessibleWindowlessSite::GetParentAccessible**](/windows/desktop/api/oleacc/nf-oleacc-iaccessiblewindowlesssite-getparentaccessible) method, which provides the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) pointer of the windowless control's parent.

2.  Implement the [**IAccessibleWindowlessSite::AcquireObjectIdRange**](/windows/desktop/api/oleacc/nf-oleacc-iaccessiblewindowlesssite-acquireobjectidrange), [**QueryObjectIdRange**](/windows/desktop/api/oleacc/nf-oleacc-iaccessiblewindowlesssite-queryobjectidranges), and [**ReleaseObjectIdRange**](/windows/desktop/api/oleacc/nf-oleacc-iaccessiblewindowlesssite-releaseobjectidrange) methods.

    Your control container must maintain a mapping of object ID ranges to windowless controls. The mapping enables the control container to identify the control that should respond to a particular request for an object ID. The following table shows an example of mapping object ID ranges to windowless controls.

    

    | Range base | Range size | Control   |
    |------------|------------|-----------|
    | 1000       | 500        | Control 1 |
    | 1500       | 1000       | Control 2 |
    | 2500       | 2000       | Control 1 |

    

     

    The control container must maintain the mapping of object ID ranges to windowless controls for itself and all windowless children. The object ID ranges do not need to be adjacent to one another. Also, to avoid denial-of-service attacks, the control container can place limits on the number of ranges that are granted to a particular control. However, it is useful to allow more than one range per control, to enable a control to grow.

### Step 4: Optional: Implement the IAccessibleHostingElementProviders interface.

Implement the [**IAccessibleHostingElementProviders**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessiblehostingelementproviders) interface if your control container has a Microsoft Active Accessibility server implementation and the server is the root of an accessibility tree that includes windowless ActiveX controls that support UI Automation. The **IAccessibleHostingElementProviders** interface has a single method, [**GetEmbeddedFragmentRoots**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-getembeddedfragmentroots), which retrieves the [**IRawElementProviderFragmentRoot**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragmentroot) interface pointers of all UI Automation windowless ActiveX controls that are hosted by your control container.

## Related topics

<dl> <dt>

[How to Host a UI Automation Windowless ActiveX Control](host-a-ui-automation-windowless-activex-control.md)
</dt> <dt>

[Windowless ActiveX Control Accessibility](windowless-activex-control-accessibility.md)
</dt> </dl>

 

 