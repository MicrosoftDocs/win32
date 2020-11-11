---
title: How to Support Callback Items
description: This topic demonstrates how to provide support for callback items.
ms.assetid: BD32666F-9445-4871-AE21-5DC9F5FC9C1B
ms.topic: article
ms.date: 05/31/2018
---

# How to Support Callback Items

This topic demonstrates how to provide support for callback items.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


If your application is going to use callback items in a ComboBoxEx control, it must be prepared to handle the [CBEN\_GETDISPINFO](cben-getdispinfo.md) notification code. A ComboBoxEx control sends this notification whenever it needs the owner to provide specific item information. For more information about callback items, see [Callback Items](comboboxex-controls.md).

The following application-defined function processes [CBEN\_GETDISPINFO](cben-getdispinfo.md) by providing attributes for a given item. Note that it sets the **mask** member of the incoming [**COMBOBOXEXITEM**](/windows/win32/api/commctrl/ns-commctrl-comboboxexitema) structure to CBEIF\_DI\_SETITEM. Setting **mask** to this value makes the control retain the item information so that it will not need to request the information again.

## Complete example


```C++
// DoItemCallback - Processes CBEN_GETDISPINFO by providing item
// attributes for a given callback item.

void WINAPI DoItemCallback(PNMCOMBOBOXEX pNMCBex)
{
    DWORD dwMask = pNMCBex->ceItem.mask;

    if(dwMask & CBEIF_TEXT)
    {
            // Insert code to provide item text.
    }

    if(dwMask & CBEIF_IMAGE) 
    {
        // Insert code to provide an item image index.
    }

    // Insert code to provide other callback information as desired.

    // Make the ComboBoxEx control hold onto the item information.
    pNMCBex->ceItem.mask = CBEIF_DI_SETITEM;
}
```



## Related topics

<dl> <dt>

[About ComboBoxEx Controls](comboboxex-controls.md)
</dt> <dt>

[ComboBoxEx Control Reference](bumper-comboboxex-comboboxex-control-reference.md)
</dt> <dt>

[Using ComboBoxEx Controls](/windows/desktop/Controls/using-comboboxex)
</dt> <dt>

[ComboBoxEx](comboboxex-control-reference.md)
</dt> </dl>

 

 