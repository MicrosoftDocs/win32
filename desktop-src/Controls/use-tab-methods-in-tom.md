---
title: How to Use Tab Methods in TOM
description: The following example provides C functions that illustrate the use of the tab methods in the Text Object Model (TOM).
ms.assetid: C74B4E43-615D-48B9-9884-F626BAF31F74
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Tab Methods in TOM

The following example provides C functions that illustrate the use of the tab methods in the Text Object Model (TOM). It is assumed that most applications include a toolbar that shows the current position and type of the tabs for the currently selected paragraph.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use a Tab Method

The following code example demonstrates how to update a toolbar with the current tab details.


```C++
HRESULT UpdateToolbar(ITextSelection *pSel)
{
    HRESULT hr       = S_OK;        
    ITextPara *pPara = 0;
    
    float f;
    long tbt;            // tab type
    long tbp;

    hr = pSel->GetPara(&pPara);
    
    if (FAILED(hr))
        goto cleanup;    // Paragraph properties are not supported
    
    f = (float) -1.0;    // Start at beginning
    
    while (pPara->GetTab(tbgoNext, &f, &tbt, NULL) == S_OK)
    {
            // Do something like draw tab icon on toolbar here
            // DrawTabPicture(f, tbt);
    }
    
cleanup:

    if (pPara)
        pPara->Release();
        
    return hr;
    
}
```



### Copy Tab Information

The following example shows how to copy only the tab information from one [**ITextPara**](/windows/desktop/api/Tom/nn-tom-itextpara) interface to another. It takes two parameters: **ITextPara** \* *pParaFrom* (the paragraph from which to copy tabs) and **ITextPara** \* *pParaFrom* (the paragraph to which to copy tabs).


```C++
HRESULT CopyOnlyTabs(ITextPara *pParaFrom, ITextPara *pParaTo)
{
    float f;
    short tbt;
    short style;
     
    pParaTo->ClearAllTabs();
    
    f = (float) -1.0;
    
    while (pParaFrom->GetTab(tbgoNext, &f, &tbt, &style) == S_OK)
        pParaTo->AddTab(f, tbt, style);
        
    return S_OK;                
    
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

 

 




