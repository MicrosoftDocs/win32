---
title: MFC and Snap-in Development
description: You can use Microsoft Foundation Classes (MFC) in your snap-in code.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e217db44-4a0e-402a-b850-75940f63ed10
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MFC and snap-in development MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MFC and Snap-in Development

You can use Microsoft Foundation Classes (MFC) in your snap-in code. However, snap-ins that use the MFC library can make no assumptions other than those provided by the MMC interfaces. The only connection between a snap-in and MMC are the COM interfaces that the snap-in exposes to MMC.

Snap-in DLLs can be either statically or dynamically linked to MFC libraries. When statically linking to MFC, follow the guidelines for using AFX\_MANAGE\_STATE that are available on the MSDN library.

## MFC and Property Pages

MFC must have the correct module state set from exported functions or COM interfaces. This includes calls made from the operating system to the module. For exported functions or COM interfaces, this is done by adding the AFX\_MANAGE\_STATE macro at the beginning of all exported functions in snap-in DLLs that dynamically link to MFC.


```C++
AFX_MANAGE_STATE(AfxGetStaticModuleState( ))
```



For an operating system call, MFC does this automatically. Because MMC's property sheet is not an MFC CPropertySheet object, the operating system call due to the callback is in the wrong module state. As a result, you must verify that the module state is correctly set during the page creation. This is the purpose of the [**MMCPropPageCallback**](mmcproppagecallback.md) function declared in the Mmc.idl file. After the module state has been set, the only AFX\_MANAGE\_STATE calls that must be made are those exposed by the COM interfaces implemented by the snap-in (for example, [**IExtendPropertySheet2::CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md)).

The [**MMCPropPageCallback**](mmcproppagecallback.md) function is declared as follows.


```C++
STDAPI MMCPropPageCallback(
  void * vpsp,  // A pointer to the PROPSHEETPAGE structure.
);
```



The vpsp argument is the pointer to a Windows [**PROPSHEETPAGE**](/windows/win32/Prsht/nc-prsht-lpfnaddpropsheetpage?branch=master) structure. By default, MFC specifies its own callback function in the pfnCallback member of the structure. Therefore, for each page you create derived from the MFC class CPropertyPage, you must call [**MMCPropPageCallback**](mmcproppagecallback.md) with a pointer to the page's callback.

Be aware that [**MMCPropPageCallback**](mmcproppagecallback.md) should not be called by snap-ins that statically link MFC libraries. A call to this function by such a snap-in will not link correctly.

For each page derived from CPropertyPage, call [**MMCPropPageCallback**](mmcproppagecallback.md) with a pointer to the page callback. The following list contains the recommended guidelines:

-   All pages for a particular property sheet must use the same callback pointer.
-   If you replace the MFC callback with your own, your callback must call the MFC callback.
-   You must call this function with each CPropertyPage derived class.

## Displaying OCX Controls on Property Pages

If you have property pages that use MFC to display an OCX control, Windows will fail to create the page because it does not know how to create the OCX control. As a result, you must manually create the OCX control. Additionally, your control will be ignored by the dialog manager for TAB key operation.

 

 




