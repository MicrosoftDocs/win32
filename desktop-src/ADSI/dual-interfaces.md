---
title: Dual Interfaces (ADSI)
description: Use COM interfaces to access the properties and methods on any provider ADSI objects.
ms.assetid: 6f3fd725-d660-4cc3-8de2-8ed7800b1141
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Dual Interfaces (ADSI)

Use COM interfaces to access the properties and methods on any provider ADSI objects. A read-only property maps to an interface entry of the form **get\_&lt;PropertyName&gt;**. A read/write property maps to two interface entries of the form **get\_&lt;PropertyName&gt;** and **put\_&lt;PropertyName&gt;**.

All methods on a COM interface must:

-   Return an HRESULT value to indicate success or failure. The **HRESULT** type is discussed in the COM specification.
-   On calls to **QueryInterface**, return **E\_NOINTERFACE** for unimplemented interfaces.
-   Return **E\_NOTIMPL** for unimplemented methods on interfaces that are otherwise implemented.
-   Return **E\_ADS\_PROPERTY\_NOT\_SUPPORTED** for interface properties that are not supported.

To retain compatibility with Automation controllers, all parameters and return types should be within the subset defined by the Automation VARIANT data type. For more information, see **VARIANT** and **VARIANTARG** in the Platform Software Development Kit (SDK).

A provider Active Directory object can expose interfaces that use data types other than those in the **VARIANT** subset. However, Automation controllers such as Visual Basic are not able to call those interfaces. Most ADSI provider interfaces are derived from [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) and can be used as **IDispatch** interface pointers. However, the [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject), [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch), and [**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension) ADSI interfaces are not derived from **IDispatch**.

 

 
