---
title: How to Use TOM GUIDs
description: Text Object Model (TOM) GUIDs are given in Tom.h inside the MIDL\_INTERFACE statements. To use the associated interfaces, you must first declare the interface by using the GUID.
ms.assetid: 48FF98C9-D42E-4E7F-874F-8E56F730E24E
ms.topic: article
ms.date: 05/31/2018
---

# How to Use TOM GUIDs

Text Object Model (TOM) GUIDs are given in Tom.h inside the MIDL\_INTERFACE statements. To use the associated interfaces, you must first declare the interface by using the GUID.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use a TOM GUID

The following example code demonstrates how to use the [**ITextDocument**](/windows/desktop/api/Tom/nn-tom-itextdocument) interface.


```C++
#define DEFINE_GUIDXXX(name, l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8) \
        EXTERN_C const GUID CDECL name \
                = { l, w1, w2, { b1, b2,  b3,  b4,  b5,  b6,  b7,  b8 } }

DEFINE_GUIDXXX(IID_ITextDocument,0x8CC497C0,0xA1DF,0x11CE,0x80,0x98,
                0x00,0xAA,0x00,0x47,0xBE,0x5D);
```



## Related topics

<dl> <dt>

[Using The Text Object Model](using-the-text-object-model.md)
</dt> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




