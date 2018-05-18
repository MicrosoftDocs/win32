---
Description: Rob Sinclair
ms.assetid: 'b5af7646-ae36-45ba-8442-497847c7422c'
title: 'Microsoft Active Accessibility Architecture: Part 2'
---

# Microsoft Active Accessibility Architecture: Part 2

Rob Sinclair

Microsoft Corporation

July 2000

**Summary**: This is the second of two articles that describe Microsoft Active Accessibility and explain how to use it to develop accessible controls, modules, and applications. This second article explains how to write an accessibility server (a control, module, or application) and implement the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface. Detailed sections are included on working with OLEACC proxies, custom controls, and other controls that require implementation of the **IAccessible** interface. (12 printed pages)

[Microsoft Active Accessibility: Architecture](microsoft-active-accessibility--architecture.md) presents the basic Microsoft Active Accessibility architecture and outlines Active Accessibility server requirements.

For more detailed information about Microsoft Active Accessibility, see [Microsoft Active Accessibility](https://msdn.microsoft.com/library/windows/desktop/dd373592).

-   [Writing an Active Accessibility Server](#writing-an-active-accessibility-server)
    -   [Cooperating with OLEACC Proxies](#cooperating-with-oleacc-proxies)
    -   [Advanced Active Accessibility Implementation](#advanced-active-accessibility-implementation)
    -   [Common Pitfalls](#common-pitfalls)
    -   [Testing Your Active Accessibility Server](#testing-your-active-accessibility-server)
-   [Additional Resources and Information](#additional-resources-and-information)

## Writing an Active Accessibility Server

The recommended approach to writing an accessibility server is to:

-   Build the application UI with as many standard UI elements as possible. This approach minimizes development cost by leveraging the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) proxies provided by OLEACC and the default WinEvents provided by USER.
-   For standard UI elements, such as owner-drawn controls, that cannot be fully proxied, employ any available workarounds to cooperate with OLEACC proxies and improve their ability to expose the information in your UI. For information on the available workarounds, see the next section, [Cooperating with OLEACC Proxies](#cooperating-with-oleacc-proxies).
-   Implement the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface for custom controls or subclassed standard controls that cannot be proxied. For information on how to do this, see the section [Advanced Active Accessibility Implementation](#advanced-active-accessibility-implementation).
-   Ensure appropriate WinEvents are being sent for all UI elements. If they are not, add the appropriate calls to the [**NotifyWinEvent**](https://msdn.microsoft.com/library/windows/desktop/dd373603) function.

### Cooperating with OLEACC Proxies

The next sections describe Active Accessibility workarounds that enable OLEACC to provide a proxy for a UI element that would otherwise require native [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) support:

-   [Unnamed controls](#msaa-sa-unmcntrls), which do not properly expose the **Name** property.
-   [Orphaned static text](#msaa-sa-orphtxt) in which one static text control labels another static text control.
-   [Upside-down slider controls](#msaa-sa-slidecntrls) in which minimum and maximum slider values are not where OLEACC expects them to be.
-   [Owner-drawn controls](#msaa-sa-owncntrls), which might store a control's text separately from the control.

Becoming familiar with the techniques to handle these controls will save time and simplify the process of supporting Active Accessibility.

### Unnamed controls

Many dialog boxes contain one or more controls that do not properly expose the **Name** property. To retrieve this name, OLEACC examines the control immediately preceding the unnamed control in the dialog box's tabbing order. If the preceding control is a static text control, OLEACC uses that control's text for the control's **Name** value.

Therefore, in many cases, the **Name** property can be changed by adding a static text control to the dialog box and setting its text to the desired name. Sometimes the unnamed control is already labeled by a static text control, but the tabbing order is incorrect. The label must immediately precede the control in the tabbing order.

Because OLEACC supports both visible and invisible static text controls, it is possible to add an invisible label to improve Active Accessibility support without changing the visible UI.

### Orphaned static text

In unnamed controls OLEACC uses static text controls to label other UI elements, but OLEACC cannot detect a situation in which one static text control labels another static text control. Therefore, Active Accessibility clients have no way to associate the two pieces of information with each other.

For example, the **General** tab on the **File Properties** dialog box uses two static text controls for the file size. One control, Size, acts as a label. The other contains the information being labeled, such as 24.0 KB (24,576 bytes). If the information portion were contained in a read-only edit control instead, Active Accessibility could expose a single UI element with a name of Size and value of 24.0 KB (24,576 bytes).

Because of the way OLEACC works in this case, servers should not use static text controls to label other static text. Instead, servers should use a read-only edit control for the information portion and a static text control for the label.

In addition to improving the Active Accessibility support in the server's UI, this solution also allows users to highlight and copy the text in the edit field and adds tabbing capability so they can navigate to the text. This improves accessibility for screen reader users.

### Upside-down slider controls

Standard slider controls, sometimes known as the trackbar controls, can be fully proxied by OLEACC. It always exposes a slider's **Value** property as a percentage representing the thumb's position along the slide. Therefore, regardless of the minimum and maximum values of a slider control, **Value** will always be 50 percent when the thumb is in the middle of the slide.

However, OLEACC cannot determine the meaning of the slider's minimum and maximum values. It assumes that zero (0) percent is at the top of a vertical slider and at the left of a horizontal slider. This causes a problem when the slider's maximum (100 percent) is at the top or left side.

Fortunately, OLEACC supports the TBS\_REVERSED style, which the application designer can use to indicate that OLEACC should switch the values for the minimum and maximum slider positions.

The Volume setting, located in the Taskbar, uses this flag to indicate that Active Accessibility should expose 100 percent for its value when the slider is at the top, and should expose zero (0) percent when it is at the bottom.

The TBS\_DOWNISLEFT style, although not specifically designed for use with Active Accessibility, is useful. By default, the down or right button (depending on whether the control is oriented vertically or horizontally) increments the value in a slider control. When TBS\_DOWNISLEFT is set, either button decrements the value. By using these two styles (TBS\_DOWNISLEFT and TBS\_REVERSED) together, the application developer can customize how slider controls are exposed to Active Accessibility clients.

### Owner-drawn controls

In general, owner-drawn controls cause accessibility problems because they store a control's text separately from the control. When writing an owner-drawn control, many developers assume that only the drawing code needs to access the control's strings. Unfortunately, this assumption is flawed. Active Accessibility and its clients need to be able to retrieve these strings through [**WM\_GETTEXT**](https://msdn.microsoft.com/library/windows/desktop/ms632627) messages or other standard mechanisms.

Correcting this problem is often very easy. For example, using the LBS\_HASSTRINGS style or calling [**SetWindowText**](https://msdn.microsoft.com/library/windows/desktop/ms633546) can cause a dramatic change in a control's accessibility.

The following sections describe specific workarounds designed to restore OLEACC's ability to proxy support for an owner-drawn control:

-   [Owner-drawn button controls](#msaa-sa-btncntrls)
-   [Owner-drawn list box items](#msaa-sa-listbxcntrls)
-   [Owner-drawn combo box items](#msaa-sa-cmbobxcntrls)
-   [Owner-drawn menu items](#msaa-sa-menitms)

> [!Note]  
> If these techniques are not sufficient, it may be necessary to implement the entire [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface.

 

### Owner-drawn button controls

The leading cause of problems for owner-drawn buttons is that the **Name** property is blank or contains garbage text. To work around this problem, set the button text by specifying a name in the resource file or by sending it a [**WM\_SETTEXT**](https://msdn.microsoft.com/library/windows/desktop/ms632644) message. Although it is likely this text will not be shown on the screen (because it is owner-drawn), OLEACC can expose this text as the button's Name value.

### Owner-drawn list box items

OLEACC is unable to retrieve the **Name** property for owner-drawn list items unless the LBS\_HASSTRINGS style is specified and appropriate text has been set for each item. When the LBS\_HASSTRINGS style is set, the list box maintains the memory and pointers for each list item's string. Thus, OLEACC can send a [**LB\_GETTEXT**](https://msdn.microsoft.com/library/windows/desktop/bb761313) message and retrieve the text for each item.

To re-enable OLEACC proxy support, set the LBS\_HASSTRINGS style and use the [**LB\_ADDSTRING**](https://msdn.microsoft.com/library/windows/desktop/bb775181) message to add the text for each item. If additional owner-drawn data is needed for each item, use the [**LB\_SETITEMDATA**](https://msdn.microsoft.com/library/windows/desktop/bb761346) message.

When using this technique, note the following:

-   If you use the LBS\_SORT style, the list box is sorted by using the supplied strings and not the [**WM\_COMPAREITEM**](https://msdn.microsoft.com/library/windows/desktop/bb775921) callback procedure.
-   With owner-drawn variable list boxes (that is, list boxes created with the style LBS\_OWNERDRAWVARIABLE), a global variable or some other mechanism must be used to keep track of when the **itemData** member of [**MEASUREITEMSTRUCT**](https://msdn.microsoft.com/library/windows/desktop/bb775804) is valid. A global variable is needed because the system sends the [**WM\_MEASUREITEM**](https://msdn.microsoft.com/library/windows/desktop/bb775925) message as soon as the string is added but before the item data has been attached, and at this point the **itemData** member is not valid.
-   To change the string for an item in a list box with the LBS\_HASSTRINGS style, you must delete the item with the [**LB\_DELETESTRING**](https://msdn.microsoft.com/library/windows/desktop/bb775181) message and add the new string with the **LB\_ADDSTRING** message.

### Owner-drawn combo box items

Owner-drawn combo boxes have the same problem as list boxes when the LBS\_HASSTRINGS style is not specified. To resolve this problem and enable OLEACC to provide a proxy, follow the same advice given for list boxes in the preceding section, [Owner-drawn list box items](#msaa-sa-listbxcntrls).

### Owner-drawn menu items

Server developers can use the [**MSAAMENUINFO**](https://msdn.microsoft.com/library/windows/desktop/dd373594) structure to expose the names of owner-drawn menu items. By associating this structure with the owner-drawn menu item data, OLEACC can provide proxies for these menu items.

Typically, when creating an owner-drawn menu, developers define a class (or structure) for the owner-drawn menu item data and create instances of this class for each menu item. Then, a pointer to the item data is used when adding items to the menu.

To expose the names of the menu items, the [**MSAAMENUINFO**](https://msdn.microsoft.com/library/windows/desktop/dd373594) structure must be the first member of the structure that defines the server's menu item data, as the following example shows:

``` syntax
// Owner-drawn menu info struct. Owner-drawn data is a 
// pointer to one of these.
struct MenuEntry{
    MSAAMENUINFO m_MSAA;       // Active Accessibility info 
                               //   - must be 1<SUP>st</SUP> member    LPTSTR       
m_pName;      // Displayed menu text or NULL for                               
//   separator item    int          m_CmdID;      // Menu command ID    int          
m_IconIndex;  // Index of icon in bitmap or                               
//   -1 for separator};
```

The [**MSAAMENUINFO**](https://msdn.microsoft.com/library/windows/desktop/dd373594) structure cannot be a member in a class that contains virtual functions because, when the code is compiled, the first member of the class is always a compiler-generated pointer to a table of the virtual functions.

To work around this problem, create an item data structure that contains [**MSAAMENUINFO**](https://msdn.microsoft.com/library/windows/desktop/dd373594) as the first member. The second member is a pointer to an instance of the class that defines the owner-drawn data. The following example demonstrates this technique:

``` syntax
// Application-defined class that contains the owner-drawn data // and 
virtual functions that operate on that data. 
class MenuEntry{    LPTSTR       m_pName;      // Displayed menu text or 
NULL for                               //  separator item.    int          
m_CmdID;      // Menu command ID    int          m_IconIndex;  // Index of 
icon in bitmap or -1                                //  for separator item    
virtual void m_AnimateIcon();      virtual void m_ChangeIconColor();}
// Application-defined struct that contains MSAAMENUINFO as first //  member. 
Second member points to owner-drawn data.
struct MenuInfo{    MSAAMENUINFO m_MSAA;       // Active Accessibility info 
                               //   - must be 1<SUP>st</SUP> member    MenuEntry 
*pMenuData;      // Points to the owner-drawn data}
```

When adding items to the menu, pass a pointer to an instance of the structure that contains [**MSAAMENUINFO**](https://msdn.microsoft.com/library/windows/desktop/dd373594) to expose the names of the menu items.

### Leveraging CreateStdAccessibleProxy and CreateStdAccessibleObject

If all or most of the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) properties for a UI element are the same as a standard UI element, it may be possible to use [**CreateStdAccessibleProxy**](https://msdn.microsoft.com/library/windows/desktop/dd318028) or [**CreateStdAccessibleObject**](https://msdn.microsoft.com/library/windows/desktop/dd318027) to expose the correct information through an existing OLEACC proxy. In effect, this provides a default **IAccessible** implementation for a control but allows the server to customize the information that is exposed.

Both functions retrieve an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface pointer for the specified system control. The difference in these functions is that [**CreateStdAccessibleObject**](https://msdn.microsoft.com/library/windows/desktop/dd318027) uses the window class name obtained from its *hwnd* parameter, whereas [**CreateStdAccessibleProxy**](https://msdn.microsoft.com/library/windows/desktop/dd318028) uses the window class name specified in its *szClassName* parameter.

For more information, see [Developer's Guide for Active Accessibility Servers](https://msdn.microsoft.com/library/windows/desktop/dd318053).

### Advanced Active Accessibility Implementation

When writing an advanced Active Accessibility server implementation, there are two primary design challenges: how to implement [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) properties and methods for UI elements, and how to respond to client requests for access to UI elements in the form of [**WM\_GETOBJECT**](https://msdn.microsoft.com/library/windows/desktop/dd373892) messages.

### How to implement IAccessible

To successfully implement [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466), server developers need to make design decisions in the following areas:

-   Will [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) be implemented directly on the object or on a helper object? (See [Direct implementation or lifetime manager object?](#msaa-sa-directimpl))
-   Will each [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface be created on demand or during initialization? (See [Create IAccessible on demand or one per request?](#msaa-sa-createiaccess))
-   Will the server create a new [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object for every request (for the same object) or reuse the same **IAccessible** object? (See [One IAccessible interface per object or one per request?](#msaa-sa-oneiaccess))
-   Will the server use accessible objects or simple elements? (See [Accessible objects or simple elements?](#msaa-sa-accessobjs))

### Direct implementation or lifetime manager object?

Early in the design process, developers need to decide how they will implement [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466)directly on the UI element or indirectly on a lightweight helper object that monitors the UI element's lifetime.

It is recommended that server developers use a helper object, because it provides a clean method of managing the UI element's lifetime and handling client requests after the UI element is destroyed. These helper objects can be extremely simple, containing as little as a single member that is a pointer to the UI element, or they can include the full [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) implementation for that element.

When [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) is implemented directly on the UI element, there is no way to disconnect the **IAccessible** object pointer from the UI element when it needs to be destroyed. If there is not a mechanism to do this, the UI element cannot be destroyed until all clients release their references to the **IAccessible** object.

Therefore, it is recommended that servers create lifetime management objects to handle all incoming client requests and to determine whether the specified UI element is still accepting requests. If it is not, the server can gracefully return an error message. Because all client references are actually on the helper object instead of the UI element, it remains until the last client releases its reference.

### Create IAccessible on demand or during initialization?

Servers may choose to either create an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface for each UI element when it creates that element or create the **IAccessible** interface when the first request is made for that object. Although either approach is acceptable, performance is enhanced when the **IAccessible** interface is created on demand. By using this approach, the server can create as few **IAccessible** interfaces as possible and avoid Active Accessibility overhead when no Active Accessibility clients are running.

### One IAccessible per object or one per request?

Some servers cache the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) pointer for each control and return it for all requests for that particular UI element. Other servers create a new **IAccessible**object each time they receive a request, even if a client has already received an **IAccessible** object for that UI element.

Although both approaches are used, it is recommended that servers return the same [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object pointer for each request for a particular UI element. This approach simplifies object tracking by clients and fits well with the lifetime management scheme discussed elsewhere in this article.

### Accessible objects or simple elements?

In some situations, servers implement the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface on each UI element (accessible objects). Others create a parent object that handles client requests on behalf of its children (simple elements).

Although the use of simple elements offers some benefits, we recommend exposing all UI elements as accessible objects. Some advantages of this approach are:

-   There are fewer problems with consistency and it is easier for clients to use.
-   It is safer and easier to implement. Servers do not need to handle all the special cases involved with child IDs.
-   The likelihood of introducing navigation problems, such as failing to correctly respond to the child ID, is greatly reduced.
-   A parent object does not have to simultaneously handle requests for its children and for its own properties.
-   Accessible objects are easier to debug.

### How to respond to WM\_GETOBJECT messages

A server's response to [**WM\_GETOBJECT**](https://msdn.microsoft.com/library/windows/desktop/dd373892) depends on the design of its accessible objects. In this discussion, assume the server does not return zero. A return value of zero means the server requested that OLEACC create a proxy for the object.

Whatever the design of its objects, the server must pass an interface pointer for the corresponding accessible object to [**LresultFromObject**](https://msdn.microsoft.com/library/windows/desktop/dd318557). This function generates a reference to the accessible object. This reference is then used by OLEACC and the COM library to perform the appropriate marshaling, if needed, and pass the interface pointer back to the client. **LresultFromObject** increments the object's reference count by means of **AddRef** as necessary, and the server is responsible for releasing any references it holds.

The *lParam* received in the [**WM\_GETOBJECT**](https://msdn.microsoft.com/library/windows/desktop/dd373892) message handler is an Object ID that indicates which type of object is being requested. In most cases, servers should handle the message only if it is a request for a client object, OBJID\_CLIENT.

The most common way for a server to handle a [**WM\_GETOBJECT**](https://msdn.microsoft.com/library/windows/desktop/dd373892) message is:

1.  If the Object ID is not OBJID\_CLIENT, ignore the message; otherwise, determine which UI element corresponds to the request.
2.  Then, create an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface for the UI element by either:
    -   Creating a new accessible object.

        –or–

    -   Reusing an existing pointer to an object.

        –or–

    -   Creating a new interface to the same object.

For more information, see [Developer's Guide for Active Accessibility Servers](https://msdn.microsoft.com/library/windows/desktop/dd318053).

### Common Pitfalls

This section discusses the following common pitfalls server developers have encountered in the past and explains how to avoid them:

-   Incorrect proxying of child objects (See [Overriding an HWND IAccessible implementation](#overriding-an-hwnd-iaccessible-implementation))
-   Improper lifetime management of [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) objects (See [Implementing IAccessible directly on UI elements](#implementing-iaccessible-directly-on-ui-elements))
-   Failing to leverage existing Active Accessibility support (See [Reinventing the wheel](#reinventing-the-wheel))
-   Inconsistently implementing server support (See [Inconsistent server support](#inconsistent-server-support))
-   Testing improperly (See [Improper testing](#improper-testing))

### Overriding an HWND IAccessible implementation

To modify the default proxy provided by OLEACC, the server must handle the WM\_GETOBJECT message sent to that window. Only by using this technique can the server intercept all forms of requests for the element's [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface.

### Implementing IAccessible directly on UI elements

Another common pitfall is for server developers to implement [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) directly on the UI element instead of using a lightweight proxy object that monitors the lifetime of the UI element.

It is recommended that all Active Accessibility servers use lightweight proxies to manage a UI element's lifetime and avoid the stability problems introduced by direct [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) implementations.

For more information, see the section, [Direct implementation or lifetime manager object?](#msaa-sa-directimpl) earlier in this article.

### Reinventing the wheel

OLEACC proxies provide a great deal of Active Accessibility support for standard UI elements, and USER provides most of the necessary WinEvent support. Therefore, server developers should become familiar with this default support before writing any server-specific support.

The Windows SDK provides information regarding the default [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) and WinEvent support that is provided for each type of UI element. Use the Inspect tool in the SDK to see what information is exposed by OLEACC for each user interface. Use the Accessible Event Watcher tool to see which WinEvents are automatically generated. These tools and the information in the Windows SDK can help developers avoid reinventing the wheel.

### Inconsistent server support

Possibly the most significant problem faced by Active Accessibility clients is the lack of consistency between Active Accessibility server implementations. To avoid this, before implementing [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) for any UI element, be sure to examine the existing support for comparable UI elements in other applications or in OLEACC-provided proxies. Then, design further **IAccessible** implementation to provide consistent support.

### Improper testing

It is critical to understand how to properly test for Active Accessibility support. Insufficient and improper testing leads to wasted time and higher maintenance costs.

For more information, see the section immediately to follow, "Testing Your Active Accessibility Server."

### Testing Your Active Accessibility Server

Every Active Accessibility server application needs to be tested, both for Active Accessibility support and for general accessibility. This section focuses on testing Active Accessibility support.

Your Active Accessibility testing should cover all areas discussed in the section Active Accessibility Server Requirements in the [first article](microsoft-active-accessibility--architecture.md), including three specific areas of Active Accessibility functionality:

-   [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) properties
-   WinEvents
-   [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) navigation

The easiest way to test Active Accessibility support is by using the accessibility tools found in the [Microsoft Windows Software Development Kit (SDK)](http://go.microsoft.com/fwlink/p/?linkid=208210).

## Additional Resources and Information

There are many sources of information that can assist in the development of accessible software.

Resources mentioned in this article:

-   [Microsoft Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=208210)

Additional information is available from the Microsoft Accessibility website at [http://www.microsoft.com/enable/](http://go.microsoft.com/fwlink/p/?linkid=202480).

 

 



