---
title: IAgentPropertySheet GetVisible
description: IAgentPropertySheet GetVisible
ms.assetid: 5e95c4da-28a3-4686-8699-ff7b16b3808f
ms.topic: article
ms.date: 05/31/2018
---

# IAgentPropertySheet::GetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetVisible(
   long * pbVisible  // address of variable for property sheet
);                   // Visible setting
```

Determines whether the Microsoft Agent property sheet is visible or hidden.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbVisible"></span><span id="pbvisible"></span><span id="PBVISIBLE"></span>*pbVisible*
</dt> <dd>

Address of a variable that receives **True** if the property sheet is visible and **False** if hidden.

</dd> </dl>

## See Also

[**IAgentPropertySheet::SetVisible**](iagentpropertysheet--setvisible.md)


 

 




