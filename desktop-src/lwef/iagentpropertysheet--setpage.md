---
title: IAgentPropertySheet SetPage
description: IAgentPropertySheet SetPage
ms.assetid: 52451a45-4f05-4209-ac3a-b4f2d90b3e74
ms.topic: article
ms.date: 05/31/2018
---

# IAgentPropertySheet::SetPage

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetPage(
   BSTR bszPage  // current property page
);
```

Sets the current page of the Microsoft Agent property sheet.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszPage"></span><span id="bszpage"></span><span id="BSZPAGE"></span>*bszPage*
</dt> <dd>

A BSTR that sets the current page of the property. The parameter can be one of the following.



|                 | Description            |
|-----------------|------------------------|
| **"Speech"**    | The Speech Input page. |
| **"Output"**    | The Output page.       |
| **"Copyright"** | The Copyright page.    |



 

</dd> </dl>

## See Also

[**IAgentPropertySheet::GetPage**](iagentpropertysheet--getpage.md)


 

 




