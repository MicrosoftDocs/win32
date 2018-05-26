---
title: dual
description: Identifies an interface that exposes properties and methods through IDispatch and directly through the VTBL.
ms.assetid: 1d39d64c-e23a-4249-a167-4369d5bd2b65
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# dual

Identifies an interface that exposes properties and methods through [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) and directly through the VTBL.

## Allowed on

Interface.

## Flags

<dl> TYPEFLAG\_FDUAL  
TYPEFLAG\_FOLEAUTOMATION  
</dl>

## Remarks

The interface must be compatible with Automation and derive from [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master). Not allowed on dispinterfaces.

The dual attribute creates an interface that is both a Dispatch interface and a Component Object Model (COM) interface. The first seven entries of the VTBL for a dual interface are the seven members of [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master), and the remaining entries are COM entries for direct access to members of the dual interface. All of the parameters and return types specified for members of a dual interface must be compatible with Automation types.

All members of a dual interface must specify an HRESULT or VOID return value. Members that need to return other values should specify the last parameter as \[[retval](retval.md), [out](out.md)\] indicating an output parameter that returns the value of the function. In addition, members that need to support multiple locales should pass an lcid parameter.

A dual interface provides for both the speed of direct VTBL binding and the flexibility of [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) binding. For this reason, dual interfaces are recommended whenever possible.

> [!Note]  
> If an application accesses object data by casting the THIS pointer in the interface call, the VTBL pointers in the object should be checked against the VTBL pointers to ensure that they are connected to the appropriate proxy.

 

Specifying dual on an interface implies that the interface is compatible with Automation, and therefore causes both the TYPEFLAG\_FDUAL and TYPEFLAG\_FOLEAUTOMATION flags to be set.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




