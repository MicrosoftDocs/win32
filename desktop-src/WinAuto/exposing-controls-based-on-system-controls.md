---
title: Exposing Controls Based on System Controls
description: Exposing Controls Based on System Controls
ms.assetid: 9291b79e-3ed0-4f3c-a610-38215d84f5ff
ms.topic: article
ms.date: 05/31/2018
---

# Exposing Controls Based on System Controls

You should consider using some form of Dynamic Annotation—Direct, Value Map, or Server—before attempting the technique described in this section. For more information, see [Dynamic Annotation API](dynamic-annotation-api.md).

In most cases, Microsoft Active Accessibility exposes information about superclassed or subclassed controls. Superclassing and subclassing allow an application developer to create a custom control with the basic functionality of a system control and include enhancements provided by the application. A superclassed control has a different window class name than the system control on which it is based. A subclassed control has the same window class name. For more information about superclassing and subclassing, see the Windows Software Development Kit (SDK) documentation.

Because Microsoft Active Accessibility exposes information about system-provided controls, Microsoft Active Accessibility exposes the modified control unless a superclassed or subclassed control is significantly different from the base control. To determine if the modified control is accessible, application developers should use utilities such as [Inspect](inspect-objects.md) and [Accessible Event Watcher](accessible-event-watcher.md) to compare the behavior of the modified control with the base control.

If after using these utilities you determine that the modified control is not accessible, you must treat the control as any other custom control. The control must trigger events, and the application's window procedure must respond to the [**WM\_GETOBJECT**](wm-getobject.md)message by supplying an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface that client applications use to obtain information about the control.

## CreateStdAccessibleProxy and CreateStdAccessibleObject

If all or most of the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties for the modified control are the same as the base control, use [**CreateStdAccessibleProxy**](/windows/desktop/api/Oleacc/nf-oleacc-createstdaccessibleproxya) or [**CreateStdAccessibleObject**](/windows/desktop/api/Oleacc/nf-oleacc-createstdaccessibleobject) to simplify the implementation of the control's **IAccessible** interface.

> [!Note]  
> When superclassing or subclassing an accessible control, be aware that the object retrieved by the [**CreateStdAccessibleObject**](/windows/desktop/api/Oleacc/nf-oleacc-createstdaccessibleobject) function may implement more than just the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface. It may include other interfaces such as [IEnumVARIANT](/windows/win32/api/oaidl/nn-oaidl-ienumvariant). You might need to wrap these additional interfaces to retain the accessibility support provided by the original implemenation of the control.

 

The [**CreateStdAccessibleProxy**](/windows/desktop/api/Oleacc/nf-oleacc-createstdaccessibleproxya) and [**CreateStdAccessibleObject**](/windows/desktop/api/Oleacc/nf-oleacc-createstdaccessibleobject) functions retrieve an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer for the specified system control. The difference in these functions is that **CreateStdAccessibleObject** uses the window class name obtained from its *hwnd* parameter whereas **CreateStdAccessibleProxy** uses the window class name specified in its *szClassName* parameter. Therefore, if you decide to use these functions, use **CreateStdAccessibleProxy** to expose information about superclassed controls, and either function with subclassed controls.

After obtaining an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer to the system control, use the pointer in your implementation of the **IAccessible** interface for the modified control. If a property or method for the modified control is the same as the base control, use the **IAccessible** pointer to return the information provided by the base control. If a property for the modified control is different from the base control, override the base control's property.

In the following example, **CAccCustomButton** is the application-defined class derived from [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible). The member variable **m\_pAccDefaultButton** is a pointer to an **IAccessible** interface that was retrieved from [**CreateStdAccessibleObject**](/windows/desktop/api/Oleacc/nf-oleacc-createstdaccessibleobject) during the initialization procedure for the control. In this example, the **Role** property for the custom control is the same as the **Role** property of the system control, so the **Role** property of the base control is returned. However, the **Description** property is different from that of the base control, so this property is overridden.


```C++
HRESULT CAccCustomButton::Initialize( HWND hWnd, HINSTANCE hInst )
{
.
.
.
    hr = CreateStdAccessibleObject( m_hWnd, 
                                    OBJID_CLIENT, 
                                    IID_IAccessible, 
                                    (void **) &m__pAccDefaultButton );
.
.
.
}

STDMETHODIMP CAccCustomButton::get_accRole( VARIANT varID )
{
    return m_pAccDefaultButton->get_accRole(varID);
}


STDMETHODIMP CAccCustomButton::get_accDescription( VARIANT varChild,
                                                   BSTR* pszDesc )
{
    TCHAR   szString[256];
    OLECHAR wszString[256];

    LoadString( m_hInst, ID_DESCRIPTION, szString, 256 );
    MultiByteToWideChar( CP_ACP, 0, szString, -1, wszString, 256 );
   *pszDesc = SysAllocString( wszString );
   if ( !pszDesc )
       return S_OK;
   else
       return E_OUTOFMEMORY;
}
```



For more information about the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties and methods of system controls, see [Appendix A: Supported User Interface Elements Reference](appendix-a--supported-user-interface-elements-reference.md).

 

 