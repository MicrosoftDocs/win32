---
Description: Rob Sinclair and Brendan McKeon
ms.assetid: '0e0a152c-c767-4aa6-9285-1f6657c8c05b'
title: Create More Accessible UI with Dynamic Annotation
---

# Create More Accessible UI with Dynamic Annotation

Rob Sinclair and Brendan McKeon

Microsoft Corporation

September 2000

**Summary:** The first in a series about Microsoft Active Accessibility version 2.0, this article discusses dynamic annotation (DA), a feature that allows developers to improve the accessibility of their user interface. (11 printed pages)

-   [Introduction](#introduction)
-   [What Is Dynamic Annotation?](#what-is-dynamic-annotation)
-   [Alternatives to Dynamic Annotation](#alternatives-to-dynamic-annotation)
-   [Annotating Your UI](#annotating-your-ui)
    -   [Annotation Interfaces](#annotation-interfaces)
    -   [Direct Annotation](#direct-annotation)
    -   [Value-Mapped Annotation](#value-mapped-annotation)
    -   [Callback Annotation](#callback-annotation)
-   [Availability and Additional Resources](#availability-and-additional-resources)

## Introduction

Previous articles have introduced the **IAccessible** interface that is part of Microsoft Active Accessibility version 1.0 and explained that oleacc.dll provides a default implementation of this interface for standard controls (USER and ComCtl). These articles discussed techniques that allow developers to avoid breaking this default implementation when using owner-drawn and custom controls. For more information, see [Microsoft Active Accessibility: Architecture](microsoft-active-accessibility--architecture.md) and [Microsoft Active Accessibility Architecture: Part 2](microsoft-active-accessibility-architecture--part-2.md).

This article is the first in a series that discusses Active Accessibility version 2.0 and the new capabilities it provides. One of these features, dynamic annotation (DA), provides greater flexibility for customizing accessibility information than the techniques discussed in earlier articles and carries a significantly smaller development cost.

## What Is Dynamic Annotation?

The Active Accessibility component, oleacc.dll, creates proxy objects that implement **IAccessible** on behalf of standard Microsoft Windows controls. Because these proxies use standard Windows messages and control-specific functions to collect information about each control, there has been no direct mechanism of customizing the information these proxies expose through **IAccessible**.

Dynamic annotation allows developers to pass hints and other useful information to OLEACC to customize the information it exposes. This capability alone will reduce the cost of supporting Active Accessibility and allow developers to greatly improve the accessibility of their user interface.

## Alternatives to Dynamic Annotation

There are other approaches to providing customized **IAccessible** support for UI elements, and in some scenarios they are the correct solutions. In fact, prior to the introduction of annotation, these other techniques were a developer's only options.

The first alternative is to implement the entire **IAccessible** interface. This approach is often necessary for custom controls or radically different UI elements, but the development and test costs are significant enough that it should be avoided unless truly necessary. If the goal is to modify a single property, the cost is difficult to justify.

The second option is to use subclassing and wrapping techniques to modify the information being exposed for a specific property. This is the technique dynamic annotation is intended to replace. To override a single property using subclassing and wrapping, the developer must:

-   Subclass the HWND of the **IAccessible** object.
-   Intercept WM\_GETOBJECT for the correct lParam/OBJID value.
-   Forward the WM\_GETOBJECT to the base class using CallWndProc(). If zero is returned, call CreateStdAccessibleObject; otherwise, call LresultFromObject on the returned value to obtain the control's native **IAccessible**.
-   Create a wrapper class, which implements **IAccessible** and wraps the **IAccessible** returned from the previous step. This wrapper class forwards all methods and properties to the original **IAccessible**, except those that are to be overridden. This involves writing forwarding code for all 21 properties and methods of **IAccessible**, regardless of how many are actually overridden.
-   The overridden method or property must take care to only handle the required child IDs, and forward all others to the original **IAccessible**.
-   Wrapping must also forward **IEnumVARIANT** and **IOleWindow** interfaces if, and only if, the original object supports them.
-   Care must be taken to ensure that reference counting is handled correctly, especially if other interfaces are supported.
-   Care must be taken to correctly handle **IDispatch**, especially **ITypeLib::Invoke()**, which must be called with an interface pointer to the wrapper interface, not a pointer to the original **IAccessible** interface.

As you can see, a considerable amount of work is involved, even if only one or two properties need to be overridden. The majority of the resulting code is concerned with subclassing and wrapping, and only a small fraction of the resulting code is actually carrying out the real task of providing the overridden information.

## Annotating Your UI

There are three types of dynamic annotation supported in Active Accessibility 2.0: *direct annotation*, *value-mapped annotation*, and *callback annotation*. Each type offers specific advantages, so understanding which approach is appropriate in a given scenario is the first step.

### Annotation Interfaces

Before moving on, it is important to become familiar with the three primary interfaces involved in annotation. Due to the limited space available, we will provide only a high-level description of each. More detailed information, including a discussion of each interface's methods, is available in the Microsoft Windows SDK.

**IAccPropServices** Interface. This is the primary annotation interface that is implemented by a singleton class, **CLSID\_AccPropServices**, which lives in oleacc.dll. This interface contains methods for annotating accessible elements (see Table 1).

**Table 1. IAccPropServices Interface Methods**



|                                                                                              |                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SetPropValue**                                                                             | Requires an IAccessibleIdentity and the annotated value is passed in a VARIANT.                                                                                                                      |
| **SetPropServer**                                                                            | Used for callback annotation.                                                                                                                                                                        |
| **ClearProps**                                                                               | Removes a property's annotated value, but this is usually not required because the annotation service automatically cleans up and releases this information when the annotated element is destroyed. |
| **SetHwndProp**<br/> **SetHwndPropStr**<br/> **SetHwndPropServer**<br/>    | These methods provide HWND-specific annotation.                                                                                                                                                      |
| **SetHmenuProp**<br/> **SetHmenuPropStr**<br/> **SetHmenuPropServer**<br/> | These methods provide HMENU-specific annotation.                                                                                                                                                     |



 

**IAccIdentity** Interface. Implemented by **IAccessible** objects and used internally as a key into the annotation database. All objects wishing to support dynamic annotation must support this interface.

**IAccPropServer** Interface. Implemented by the callback objects used in callback annotation.

### Direct Annotation

The simplest form of dynamic annotation is called *direct annotation*. This style of annotation is most applicable for accessible elements whose annotated property is not dependent on the control's state and therefore does not require the additional support provided by *value-mapped annotation* and *callback annotation*.

To annotate an accessible element using direct annotation:

1.  Obtain an **IAccessible** interface pointer to the accessible element to be annotated.
2.  QI for the **IAccIdentity** interface, and call GetIdentityString() to obtain the accessible element's identity string.
3.  CoCreate the **AccPropServices** object.
4.  Call IAccPropServices::SetPropValue, passing the identity string, a GUID indicating the property to be overridden, and a VARIANT containing the new value of the property.

Instead of calling **SetPropValue** with the accessible element's identity, the developer can call the **SetHwndProp***X* or **SetHmenuProp***X* methods and supply the accessible element's HWND/HMENU, object ID, and child ID. This precludes the need to QI for **IAccIdentity**, call GetIdentityString and package string values in a VARIANT.

The following properties can be annotated using direct annotation. The value must be of the specified type.



|                               |            |
|-------------------------------|------------|
| PROPID\_ACC\_DEFAULTACTION    | (VT\_BSTR) |
| PROPID\_ACC\_DESCRIPTION      | (VT\_BSTR) |
| PROPID\_ACC\_HELP             | (VT\_BSTR) |
| PROPID\_ACC\_KEYBOARDSHORTCUT | (VT\_BSTR) |
| PROPID\_ACC\_NAME             | (VT\_BSTR) |
| PROPID\_ACC\_ROLE             | (VT\_I4)   |
| PROPID\_ACC\_STATE            | (VT\_I4)   |
| PROPID\_ACC\_VALUE            | (VT\_BSTR) |



 

### Example 1: Set the Description property of an icon in a dialog box.

``` syntax
#include <oleacc.h>
...

BOOL CALLBACK DialogProc(   HMENU Hmenu,
                  UINT uMsg,
                  WPARAM wParam,
                  LPARAM lParam )
{
   switch( uMsg )
   {
      case WM_INITDIALOG:
      {
         IAccPropServices * pAccPropSvc = NULL;
         HRESULT hr = CoCreateInstance(   CLSID_AccPropServices,
                  NULL, 
                  CLSCTX_SERVER,
                  IID_IAccPropServices,
                  (void **) & pAccPropSvc );

         if( hr == S_OK && pAccPropSvc )
         {
            HMENU HmenuIcon = GetDlgItem(   Hmenu, IDC_ICON1);
            pAccPropSvc->SetHmenuPropStr(   HandleToLong(HmenuIcon),
                        OBJID_CLIENT,
                        0,
                        PROPID_ACC_DESCRIPTION,
                  L"Picture of a thermometer");
            pAccPropSvc->Release();
         }
         ...
      }
      ...
   }
   ...
}
```

### Value-Mapped Annotation

In addition to directly annotating **IAccessible** properties, there is often a need to convert a control-specific value or index into a string that can be understood by an end user. An example is the screen resolution slider control in the **Display Properties, Settings** tab. Although each slider position corresponds to a different resolution (for example, 640 x 480, 1024 x 768), the control has no knowledge of this relationship and therefore cannot convey this information to Active Accessibility. It is only the developer using this control that can expose this relationship.

Fortunately, with Active Accessibility 2.0's value-mapped annotation, this task is extremely simple. To use this type of annotation, the developer defines a mapping from slider position to display resolution and passes it to the annotation services. Active Accessibility will then map the control's internal value to the property string that should be exposed.

### Supported maps

Because control-specific knowledge is required to support value mapping, there are a limited number of controls and properties that support value-mapped annotation:

<dl> <dt>

<span id="Slider_Value_map__PROPID_ACC_VALUEMAP"></span><span id="slider_value_map__propid_acc_valuemap"></span><span id="SLIDER_VALUE_MAP__PROPID_ACC_VALUEMAP"></span>Slider Value map: PROPID\_ACC\_VALUEMAP
</dt> <dd>

Supported by the OLEACC slider (also known as trackbar) proxy, this property contains a mapping from internal slider positions to human-readable strings. If the current slider value is found in the value map, the corresponding string will be exposed as the value, instead of the default percentage string (for example, "50"). This is useful where sliders are used to select one of a limited set of discrete options.

</dd> <dt>

<span id="ListView_and_TreeView_Value_map__PROPID_ACC_ROLEMAP__PROPID_ACC_STATEMAP"></span><span id="listview_and_treeview_value_map__propid_acc_rolemap__propid_acc_statemap"></span><span id="LISTVIEW_AND_TREEVIEW_VALUE_MAP__PROPID_ACC_ROLEMAP__PROPID_ACC_STATEMAP"></span>ListView and TreeView Value map: PROPID\_ACC\_ROLEMAP, PROPID\_ACC\_STATEMAP
</dt> <dd>

Supported by the OLEACC ListView and TreeView proxies, these maps provide mappings from state image indices to role and state values. Some ListViews and TreeViews use state images that look like check boxes and radio buttons to implement a list or tree of check- and radio- options. These maps allow those state image indices to be mapped to appropriate roles (typically ROLE\_SYSTEM\_RADIOBUTTON or ROLE\_SYSTEM\_CHECKBOX) and additional state bits (typically STATE\_SYSTEM\_CHECKED). The annotated state value is combined with the state bits computed by OLEACC (for example, focus and visibility) using the binary **OR** operator (\|). The map may be keyed by the image index, the state image index, or the overlay image index of the TreeView or ListView item and is indicated by an index-key of 0, 1, or 2, respectively.

</dd> </dl>

### Annotation map format

Annotation maps contain a sequence of *fields* separated by a delimiting character:

-   **Uppercase letter "A".** This indicates that this particular encoding scheme is used. Additional prefixes may be supported for future encoding schemes.
-   **A delimiter character.** Typically a colon (':') is used, but this may be any character other than NUL or space. Because this character will be used as a delimiter for the remaining fields, it may not be used as part of a value in the map.
-   **A value that indicates which key is being used.** For TreeView and ListView role- and state-maps, this key can be 0, 1, or 2, where these indicate the image index, the state image index, or the overlay image index, respectively. For sliders and other controls that do not offer a choice of keys, this value must be 0.
-   The delimiter character.
-   A series of key-value pairs, where each pair consist of:
    -   **A key string.** This is typically a number, and may be in decimal or hexadecimal, with a leading "0x" prefix.
    -   **The delimiter character.**
    -   **A value string.** This is a string in the value map, and a number in the role and state maps. (Either decimal or hexadecimal numbers may be used.)
    -   **The delimiter character.**

Examples of map strings include:

A:0:0:Cold:1:Warm:3:Hot:

If this Value map is applied for a slider control, a value of "Warm" will be exposed when the slider is at position 1. Note that value 2 is absent from this example map, so the default value for that position would be exposed. (In the case of a slider, this would be a percentage value such as "33.")

A:1:0:34:1:0x2C:

The initial '1' in this map indicates that the state image index (instead of the image index or overlay image index) is to be used as the key. When used as the Role map for a TreeView, each item's role will be exposed as ROLE\_SYSTEM\_LISTITEM (corresponding to decimal value 34) if that item has a state image index of 0. For items with a state image index of 1, their role will be exposed as ROLE\_SYSTEM\_CHECKBUTTON (corresponding to hex value 0x2C). TreeView items with other state image indices will have the default role for TreeView items, ROLE\_SYSTEM\_OUTLINEITEM.

### Callback Annotation

Callback annotation is the third type of annotation supported in Active Accessibility 2.0. It allows developers to register a callback object to service client requests for an element's annotated property. This callback object must implement the **IAccPropServer** interface and be registered with the Active Accessibility annotation services. Once registered, it will be asked to service all client requests for that accessible element's property value.

To annotate an object's property using callback annotation:

1.  Obtain an **IAccessible** interface pointer to the accessible element to be annotated.
2.  QI for the **IAccIdentity** interface, and call **GetIdentityString()** to obtain the accessible element's identity string.
3.  CoCreate the **AccPropServices** object.
4.  Create a COM object that implements **IAccPropServer**.
5.  Call **IAccPropServices::SetPropServer**, passing the identity string, a GUID indicating the property to be overridden, and a pointer to the **IAccPropServer** callback object.
6.  When a client requests the annotated property for that accessible element, the callback object will be called to provide the correct value.

As with direct annotation, the **SetHwndPropServer** or **SetHmenuPropServer** methods can be used to specify the HWND/HMENU, object ID, and child ID instead of retrieving the identity string and using it in a call to **SetPropServer**. When using **SetPropServer**, **SetHwndPropServer**, or **SetHmenuPropServer** on a container object, the developer can also specify that the annotation should apply to all element children of that container.

The following properties can only be annotated using callback annotation, and the return type is usually an **IAccessible** inside a VT\_DISPATCH variant:

-   PROPID\_ACC\_FOCUS
-   PROPID\_ACC\_SELECTION
-   PROPID\_ACC\_PARENT
-   PROPID\_ACC\_NAV\_UP
-   PROPID\_ACC\_NAV\_DOWN
-   PROPID\_ACC\_NAV\_LEFT
-   PROPID\_ACC\_NAV\_RIGHT
-   PROPID\_ACC\_NAV\_PREV
-   PROPID\_ACC\_NAV\_NEXT
-   PROPID\_ACC\_NAV\_FIRSTCHILD
-   PROPID\_ACC\_NAV\_LASTCHILD

### Example 2: Supply custom help strings on demand for ListView items.

In this example, the developer needs to supply customized help strings for each item in a ListView and wants to do this only when a client specifically requests it:


```
class ListViewAccServer: public IAccPropServer
{
   ULONG   m_Ref;
   IAccPropServices * m_pAccPropSvc;

public:
   ListViewAccServer( IAccPropServices * pAccPropSvc )
      : m_Ref( 1 ),
        m_pAccPropSvc( pAccPropSvc )
   {
      m_pAccPropSvc->AddRef();
   }

   ~ListViewAccServer()
   {
      m_pAccPropSvc->Release();
   }
```



AddRef(), Release(), QueryInterface() omitted:


```
   HRESULT STDMETHODCALLTYPE GetPropValue ( 
      const BYTE *    pIDString,
      DWORD           dwIDStringLen,
      MSAAPROPID      idProp,
      VARIANT *       pvarValue,
      BOOL *          pfGotProp )
   {
      // Default return values, in case we need to bail out...
      *pfGotProp = FALSE;
      pvarValue->vt = VT_EMPTY;
      // Extract the idChild from the identity string...
      DWORD dwHmenu, idObject, idChild;
      HRESULT hr = m_pAccPropSvc->DecomposeHmenuIdentityString(
                        pIDString, dwIDStringLen, 
                        &amp;dwHmenu, &amp;idObject, &amp;idChild );
      if( hr != S_OK )
      {
         return S_OK;
      }

      HMENU Hmenu = (HMENU)HandleToLong( dwHmenu );
      // Only supply help string for child elements, not the 
      //   listview itself...
      if( idChild == CHILDID_SELF )
      {
         return S_OK;
      }

      // GetHelpString returns a UNICODE string corresponding to
      // the index it is passed.
      LPWSTR pHelpString = GetHelpString( idChild - 1 );
      if( ! pHelpString )
      {
         return S_OK;
      }

      BSTR bstr = SysAllocString( pHelpString );
      pvarValue->vt = VT_BSTR;
      pvarValue->bstrVal = bstr;
      *pfGotProp = TRUE;
      return S_OK;
   }
};
```



Shortly after the ListView, HmenuLV is created:


```
IAccPropServices * pAccPropSvc = NULL;
HRESULT hr = CoCreateInstance( CLSID_PropMgr,
                  NULL, 
                  CLSCTX_SERVER,
                  IID_IAccPropServices,
                  (void **) &amp;pAccPropSvc );
if( hr == S_OK &amp;&amp; pAccPropSvc )
{
   ListViewAccServer * pLVServer = new ListViewAccServer( pAccPropSvc );
   if( pLVServer )
   {
      MSAAPROPID propid = PROPID_ACC_HELP;
      pAccPropSvc->SetHmenuPropServer( DWORD( HmenuLV ),
                  OBJID_CLIENT, 0,
                  1, &amp;propid,
                  pLVServer, ANNO_CONTAINER );
      pLVServer->Release();
      pAccPropSvc->Release();
   }
}
```



## Availability and Additional Resources

Because this functionality is brand new, OLEACC proxies in Active Accessibility 2.0 are the only objects that currently support dynamic annotation. This mechanism, however, can be used to customize the **IAccessible** information exposed for any object that implements the **IAccessibleIdentity** interface.

Active Accessibility 2.0 is built into the next major release of the Microsoft Windows operating system, which is code named Whistler. It might also be made available as an update to existing versions of Windows. See the Microsoft Accessibilitye website, [http://www.microsoft.com/enable/](http://go.microsoft.com/fwlink/p/?linkid=202480), for more information.

 

 




