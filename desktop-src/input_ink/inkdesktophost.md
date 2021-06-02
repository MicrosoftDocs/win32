---
description: Implements the IInkDesktopHost interface.
ms.assetid: 7a577536-405b-400d-89bc-c3b3894b448d
title: InkDesktopHost class
ms.topic: language-reference
ms.date: 02/03/2020
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkDesktopHost
api_type: 
- COM
api_location: 
- InkPresenterDesktop.idl
---

# InkDesktopHost class

Implements the [**IInkDesktopHost**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkdesktophost) interface.

An [**IInkDesktopHost**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkdesktophost) object enables ink input, processing, and rendering through the creation of an app thread to host an [**IInkPresenterDesktop**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkpresenterdesktop) object and insert it into the app's [DirectComposition](../directcomp/directcomposition-portal.md) visual tree.

## Members

The **InkDesktopHost** class inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **InkDesktopHost** also has these types of members:

- [Methods](#methods)

### Methods

The **InkDesktopHost** class has these methods.

| Method | Description |
|---|---|
| [**CreateAndInitializeInkPresenter**](/windows/win32/api/inkpresenterdesktop/nf-inkpresenterdesktop-iinkdesktophost-createandinitializeinkpresenter) | Creates an [**IInkPresenterDesktop**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkpresenterdesktop) object on an application thread, connects it to the app's [DirectComposition](../directcomp/directcomposition-portal.md) visual tree, and sets the size of the object.<br/> |
| [**CreateInkPresenter**](/windows/win32/api/inkpresenterdesktop/nf-inkpresenterdesktop-iinkdesktophost-createinkpresenter) | Creates an [**IInkPresenterDesktop**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkpresenterdesktop) object on an application thread.<br/> |
| [**QueueWorkItem**](/windows/win32/api/inkpresenterdesktop/nf-inkpresenterdesktop-iinkdesktophost-queueworkitem) | Add an ink operation to a work queue for execution on the **InkDesktopHost** thread.<br/> |

## Creation\\Access Functions

Call [<strong>CoCreateInstance</strong>](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) with the class identifier <strong>InkDesktopHost</strong> to retrieve a reference to the object.

``` C++
CoCreateInstance(__uuidof(InkDesktopHost), 
  nullptr, 
  CLSCTX_INPROC_SERVER, 
  IID_PPV_ARGS(&amp;_spInkHost));
```

## Requirements

| Requirement | Value |
|---|---|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/> |
| Header<br/>                   | <dl> <dt>InkPresenterDesktop.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>InkPresenterDesktop.idl</dt> </dl> |
| IID<br/>                      | IID\_IInkDesktopHost is defined as 4ce7d875-a981-4140-a1ff-ad93258e8d59<br/> |

## Related topics

[Ink presenter classes](ink-presenter-classes.md), [Pen and stylus interactions](/windows/uwp/design/input/pen-and-stylus-interactions), [Ink Analysis sample](/samples/microsoft/windows-universal-samples/inkanalysis/), [Simple inking sample](/samples/microsoft/windows-universal-samples/simpleink/), [Complex inking sample](/samples/microsoft/windows-universal-samples/complexink/)
