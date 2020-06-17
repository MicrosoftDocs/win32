---
title: How to Use a Font Duplicate
description: This section explains how to use a font duplicate to apply a number of changes to a text range, all at once.
ms.assetid: CF0123E5-313F-4583-872F-6FE954F1C9E8
ms.topic: article
ms.date: 05/31/2018
---

# How to Use a Font Duplicate

This section explains how to use a font duplicate to apply a number of changes to a text range, all at once.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use a Font Duplicate

The following example shows how a font duplicate can be used to apply a number of changes to a range at once.


```C++
void ChangeFontNameSizeBold(ITextSelection *pSel)
{
    ITextFont *pFontSel      = NULL
    ITextFont *FontDuplicate = NULL;
    
    // Get ITextFont version of non-duplicated font.
    if (FAILED(pSel->GetFont( &pFontSel))
        return;

    // Duplicate the font.
    pFontSel->GetValue(&pFontDuplicate);
    pFontSel->Release();
    
    if(!pFontDuplicate)
        return;

   // Changes here happen only to the underlying data structure, 
   // such as a CHARFORMAT, in the duplicate - NOT to the actual story text.

    BSTR bstrTemp = UnicodeBstrFromAnsi("Times New Roman");   // Font name
    
    pFontDuplicate->SetName(bstrTemp);
    SysFreeString(bstrTemp);
    
    pFontDuplicate->SetBold(tomTrue);                        // Bold
    pFontDuplicate->SetSize(10.5);                           // 10.5 point font.
    pFontDuplicate->SetAnimation(tomBlackMarchingAnts);

    // Apply the change to text as one change: one screen update, one undo. 
    // You can also apply the font object to different ranges before you free it.
    
    pSel->SetFont(pFontDuplicate);
    
    pFontDuplicate->Release();
    
}
```



## Related topics

<dl> <dt>

[Using The Text Object Model](using-the-text-object-model.md)
</dt> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




