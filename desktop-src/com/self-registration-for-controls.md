---
title: Self Registration for Controls
description: Self Registration for Controls
ms.assetid: 0fff07e5-10bb-4052-8eb1-021efcb66d6c
ms.topic: article
ms.date: 05/31/2018
---

# Self Registration for Controls

ActiveX controls must support self-registration by implementing the [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver) and [**DllUnregisterServer**](/windows/win32/api/olectl/nf-olectl-dllunregisterserver) functions. ActiveX controls must register all of the standard registry entries for embeddable objects and automation servers.

ActiveX controls must use the component categories API to register themselves as a control and register the component categories that they require a host to support and any categories that the control implements, see [Component Categories](component-categories.md).

ActiveX controls should also register the [ToolBoxBitmap32](toolboxbitmap32.md) registry key, although this is not mandatory.

The Insertable component category should be registered only if the control is suitable for use as a compound document object. It is important to note that a compound document object must support certain interfaces beyond the minimum [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) required for an ActiveX control. Although an ActiveX control may qualify as a compound document object, the control's documentation should clearly state what behavior to expect under these circumstances.

## Related topics

<dl> <dt>

[Controls](controls.md)
</dt> </dl>

 

 