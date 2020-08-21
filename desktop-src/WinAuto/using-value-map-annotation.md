---
title: Using Value Map Annotation
description: For sample code, see Value Map Annotation Sample.
ms.assetid: 29be74c7-a7c2-41f4-8b94-5771988b74ff
ms.topic: article
ms.date: 05/31/2018
---

# Using Value Map Annotation

**To create a value map**

1.  **Create a mapping string.**

    A mapping string is a list of a control's numeric values corresponding to a human-readable string in Unicode. It starts with "A:" followed by a number that indicates the type of index used. Only image indexes are supported; therefore the index type is always 0.

    The string is followed by :index:result pairs. The "index" is a number representing an image index for a List-View or Tree-View, or the value for a slider control.

    The resulting value is a number obtained when you map the Role or State property for a list view or tree view control. Such numbers are expressed in decimal or hexadecimal with an "0x" prefix.

    The mapping string is always terminated with a final colon (":").

    The following is an example of an annotation map for the State and Role properties of a check box in a list view or tree view control. There are two items in the view that represent check boxes, and each has images corresponding to the checked and unchecked state.

    ```C++
    LPCWSTR g_ListOrTreeStateMap = 
    L"A:0"     // Index type; always 0. !
    L":0:0x00" // Image 0 is normal !
    L":1:0x10" // Image 1 is checked - STATE_SYSTEM_CHECKED (0x10) !
    L":";

    LPCWSTR g_ListOrTreeRoleMap = 
    L"A:0"     // Index type; always 0. !
    L":0:0x2C" // Image 0 is a check box - ROLE_SYSTEM_CHECKBUTTON
    (0x2c) !
    L":1:0x2C" // image 1 is also a check box !
    L":";
    ```

    

    For valid Role and State values, see [Object Roles](object-roles.md) and [Object State Constants](object-state-constants.md).

    The index value may be negative when you map properties for a slider control.

    When you map a Value or Description property, the result is a string. Strings are not quoted and the colons act as delimiters.

    For more information, see [Annotation Map Format](value-map-annotation.md).

2.  **Create the annotation manager and obtain a pointer to its**[**IAccPropServices**](/windows/desktop/api/oleacc/nn-oleacc-iaccpropservices)**interface.**

    The following is an example of how to create the annotation manager.

    ```C++
    IAccPropServices * pAccPropSvc = NULL;
    HRESULT hr = CoCreateInstance(CLSID_AccPropServices, NULL,
    CLSCTX_SERVER, IID_IAccPropServices, (void**) & pAccPropSvc));
    
    ```

    

3.  **Attach the mapping string to the control.**

    Call [**IAccPropServices::SetHwndPropStr**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-sethwndpropstr), passing the **HWND** of the control and a pointer to the mapping string.

    The *IdProp* parameter will be one of the following.

    

    | Parameter                   | Used for                                                |
    |-----------------------------|---------------------------------------------------------|
    | MSAAPROPID\_ROLEMAP         | To set a role map for list view or tree view controls.  |
    | MSAAPROPID\_STATEMAP        | To set a state map for list view or tree view controls. |
    | PROPID\_ACC\_DESCRIPTIONMAP | To set a description map for list view or tree views.   |
    | MSAAPROPID\_VALUEMAP        | To set a value map on slider controls.                  |

    

     

4.  **Clean up.**

    Before you destroy any value map annotated controls (for example, when handling [WM\_DESTROY](../winmsg/wm-destroy.md)), you must clear previously registered properties and release the annotation manager.

    To do this, call [**IAccPropServices::ClearHwndProps**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-clearhwndprops) as appropriate and release your pointer to [**IAccPropServices**](/windows/desktop/api/oleacc/nn-oleacc-iaccpropservices).

For sample code, see [Value Map Annotation Sample](value-map-annotation-sample.md).

 

 