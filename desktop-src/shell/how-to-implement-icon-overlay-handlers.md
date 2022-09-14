---
description: Icon overlay handlers are in-process Component Object Model (COM) objects, implemented as DLLs.
ms.assetid: ADF27BFD-CC96-43F9-9EBB-DEBE0DEA7B92
title: How to Implement Icon Overlay Handlers
ms.topic: article
ms.date: 05/31/2018
---

# How to Implement Icon Overlay Handlers

Icon overlay handlers are in-process Component Object Model (COM) objects, implemented as DLLs. They export one interface in addition to [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown): [**IShellIconOverlayIdentifier**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelliconoverlayidentifier). This interface has three methods: [**IShellIconOverlayIdentifier::GetOverlayInfo**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelliconoverlayidentifier-getoverlayinfo), [**IShellIconOverlayIdentifier::GetPriority**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelliconoverlayidentifier-getpriority), and [**IShellIconOverlayIdentifier::IsMemberOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelliconoverlayidentifier-ismemberof).

## Instructions

### Step 1: Implementing GetOverlayInfo

The [**GetOverlayInfo**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelliconoverlayidentifier-getoverlayinfo) method is first called during initialization. The method returns the fully qualified path of the file that contains the icon overlay image, and its zero-based index within the file. The Shell then adds the image to the system image list. Icon overlays can be contained in any of the standard file types, including .exe, .dll, and .ico.

After initialization is complete, the Shell calls [**GetOverlayInfo**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelliconoverlayidentifier-getoverlayinfo) when it needs to display the handler's icon overlay. The method should return the same file name and index that it did during initialization. Although the Shell uses the image that is cached in the system image list rather than loading the image from the file, an icon overlay is still identified by its file name and index.

### Step 2: Implementing GetPriority

The [**GetPriority**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelliconoverlayidentifier-getpriority) method is called only during initialization. It assigns a priority value to the handler's icon overlay. The value can range from zero to 100, where 100 is the lowest priority. The purpose of this priority value is to help the Shell resolve the conflict that arises when multiple icon overlays are specified for a single object. The Shell first uses an internal set of rules to determine the highest-priority icon overlay. If these rules do not resolve the conflict, the values assigned to the icon overlays by **GetPriority** determine priority.

The priority value set by [**GetPriority**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelliconoverlayidentifier-getpriority) is not a reliable way to resolve conflicts between unrelated icon overlay handlers. There is no way for your handler to determine what priority values other handlers are using. Normally, you should set the value to zero. However, the priority value is useful when you have implemented two or more icon overlay handlers that can request icon overlay icons for the same object. By setting the priority values appropriately, you can specify which of the requested icon overlays will be displayed.

### Step 3: Implementing IsMemberOf

The Shell calls the [**IsMemberOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelliconoverlayidentifier-ismemberof) method to determine whether it should display a handler's icon overlay for a particular object. The Shell specifies the object by passing its name to the method. If a handler wants to have its icon overlay displayed, **IsMemberOf** returns S\_OK. If not, it returns S\_FALSE.

Icon overlay handlers are normally intended to work with a particular group of files. A typical example is a [file type](fa-file-types.md), identified by a specific file name extension. An icon overlay handler can request an icon overlay for all files of the file type. Some handlers request an icon overlay only if a file of the file type is in a particular state. However, icon overlay handlers are free to request their icon overlay for any object that they choose.

 

 
