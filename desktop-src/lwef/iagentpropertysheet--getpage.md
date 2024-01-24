---
title: IAgentPropertySheet GetPage
description: IAgentPropertySheet GetPage
ms.assetid: 40d00e9b-dd81-4e23-907a-6ca24a28fa95
ms.topic: article
ms.date: 05/31/2018
---

# IAgentPropertySheet::GetPage

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetPage(
BSTR * pbszPage  // address of variable for current property page
);
```

Retrieves the current page of the Microsoft Agent property sheet.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszPage"></span><span id="pbszpage"></span><span id="PBSZPAGE"></span>*pbszPage*
</dt> <dd>

Address of a variable that receives the current page of the property sheet (last viewed page if the window is not open). The parameter can be one of the following:



|                 | Description            |
|-----------------|------------------------|
| **"Speech"**    | The Speech Input page. |
| **"Output"**    | The Output page.       |
| **"Copyright"** | The Copyright page.    |



 

</dd> </dl>

## See Also

[**IAgentPropertySheet::SetPage**](iagentpropertysheet--setpage.md)


 

 




