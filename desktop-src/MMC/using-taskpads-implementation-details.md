---
title: Using Taskpads Implementation Details
description: Using Taskpads Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4b1ae691-12df-486e-a760-5613e13d9476
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- taskpads MMC , implementation details
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Taskpads: Implementation Details

## To implement a standard taskpad

1.  Implement a mechanism for storing the selected view type (standard list view or taskpad). This allows a standard list view or the appropriate taskpad to be loaded when MMC calls [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) to display the result pane for your snap-in.

    The recommended method is to create a member variable in your [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) object. In the CComponent class below, the **m\_ViewType** member stores the view type.

    ```C++
    // CComponent
    class CComponent : 
      public IComponent,
      public IExtendContextMenu,
      public IExtendTaskPad
     
    {
    public:
      CComponent()
      {
        // Default to standard view
        m_ViewType=0;
      }
      ~CComponent();
     
    public:
      // Store the view type: standard or taskpad
      long m_ViewType;
    };
    ```

    

2.  If your snap-in has taskpads as well as list and/or custom views for a particular scope item, the snap-in should by default display a taskpad for the item when it is selected. If the item has more than one taskpad view, the snap-in should display the default taskpad or whatever taskpad the snap-in determines to be appropriate. On subsequent visits to that item (using the **Back** and **Forward** buttons), the view type last selected by the user will be displayed (for more information, see [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md)).
3.  Implement access to the taskpads. There are three ways to do this:
    -   Add one or more taskpad menu items to the **View** menu. You can add a single menu item to use it as an additional view type option on an item in the scope pane. You can use multiple menu items if you want access to specific taskpads, or if an item has multiple taskpads.

        Be aware that MMC calls the [**IExtendContextMenu::AddMenuItems**](/windows/desktop/api/Mmc/nf-mmc-iextendcontextmenu-addmenuitems) method implemented by the [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) that owns the view to allow it to add items to the **View** menu.

    -   Add tasks that link to other taskpads.
    -   Use only taskpad views.

4.  If your snap-in uses context menus to switch to taskpad view, or if a taskpad task links to a taskpad on another item, the snap-in must set the view type member to the appropriate taskpad and then call the [**IConsole2::SelectScopeItem**](https://www.bing.com/search?q=**IConsole2::SelectScopeItem**) method. This forces a call to [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) to load the appropriate taskpad.
5.  Handle selection of a taskpad in [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype).

    For a taskpad view that uses MMC taskpad templates, ppViewType should point to the address of a string that contains the resource path to the taskpad template and a group name that identifies the taskpad. Be aware that MMC passes the group name in calls to [**IExtendTaskPad**](/windows/desktop/api/Mmc/nn-mmc-iextendtaskpad) methods to enable the snap-in to identify the particular taskpad that is being displayed (this is important if the snap-in has multiple taskpads).

    The string should have the form **res://filepath/template\#groupname**.

    where filepath is the full path to the MMC executable (MMC.exe), template is the file name of the template that is stored as a resource within the file specified by filepath, and groupname is the name that identifies the taskpad.

The following table lists HTML files supplied by MMC:



| Resource file  | Description                                  |
|----------------|----------------------------------------------|
| default.htm    | Template for standard taskpad.               |
| listpad.htm    | Template for "vertical" list view taskpad.   |
| horizontal.htm | Template for "horizontal" list view taskpad. |



 

For example, the following string specifies that MMC.exe has a path of "c:/windows/system32/mmc.exe", the standard taskpad is displayed (default.htm), and the group name is tpad1.


```C++
res://c:\\windows\\system32\\mmc.exe/default.htm#tpad1
```



For a taskpad view that uses a custom HTML page, ppViewType should point to the address of a string that contains the resource path to the custom taskpad's HTML file and a group name that identifies the taskpad. The string has the same form as the string for an MMC taskpad template — except the filepath should specify the path to the snap-in's DLL that stores the custom HTML page as a resource.

1.  Implement the [**IExtendTaskPad**](/windows/desktop/api/Mmc/nn-mmc-iextendtaskpad) interface on your snap-in's **IComponent** object.

    If your snap-in owns the item that displays the taskpad, [**IExtendTaskPad**](/windows/desktop/api/Mmc/nn-mmc-iextendtaskpad) is used by MMC to set up the taskpad, to get a pointer to the [**IEnumTASK**](/windows/desktop/api/Mmc/nn-mmc-ienumtask) interface, and to send notifications from the taskpad to your snap-in.

    If the taskpad is a list view taskpad, MMC calls [**IExtendTaskPad::GetListPadInfo**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-getlistpadinfo) to get the title text for the list control, text for an optional button, and the command ID passed to [**IExtendTaskPad::TaskNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-tasknotify) when the button is clicked.

    MMC calls the [**IExtendTaskPad::EnumTasks**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-enumtasks) method to get a pointer to the [**IEnumTASK**](/windows/desktop/api/Mmc/nn-mmc-ienumtask) interface of an object that specifies the tasks your snap-in must add to the taskpad. If a taskpad extension snap-in has been added to your snap-in, MMC gets a pointer to the [**IExtendTaskPad**](/windows/desktop/api/Mmc/nn-mmc-iextendtaskpad) interface on that snap-in and calls the **IExtendTaskPad::EnumTasks** method to get a pointer to the **IEnumTASK** interface for that snap-in.

    MMC calls the [**IExtendTaskPad::TaskNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-tasknotify) method to notify the snap-in when a task or a list view button has been clicked. The list view button applies only to list view taskpads — it is the optional button specified in the [**IExtendTaskPad::GetListPadInfo**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-getlistpadinfo) method. The command ID for the specific task or list view button is passed as a VARIANT.

2.  Implement the [**IEnumTASK**](/windows/desktop/api/Mmc/nn-mmc-ienumtask) interface. MMC calls methods on this interface to get the tasks for the taskpad.

    MMC calls the [**IEnumTASK::Next**](/windows/desktop/api/Mmc/nf-mmc-ienumtask-next) method to iterate the tasks. Each task is returned as an [**MMC\_TASK**](/windows/desktop/api/Mmc/ne-mmc-_mmc_task_display_type) structure.

3.  If the taskpad is a list view taskpad, handle the [**MMCN\_LISTPAD**](mmcn-listpad.md) notification in [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify).

    When a list view taskpad is displayed, MMC clears the items in the result pane, attaches the list control used in the taskpad, and sends this notification with the arg set to **TRUE**. The snap-in must handle this notification by populating the list with items using the [**IResultData**](/windows/desktop/api/Mmc/nn-mmc-iresultdata) or [**IResultOwnerData**](/windows/desktop/api/Mmc/nn-mmc-iresultownerdata) interfaces.

    When the view is switched from the list view taskpad to another view, MMC sends this notification with the arg set to **FALSE**. When the snap-in handles this notification, it can free any resources used to populate the list.

## Related topics

<dl> <dt>

[Using Taskpads: Interfaces](using-taskpads-interfaces.md)
</dt> </dl>

 

 




