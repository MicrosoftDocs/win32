---
title: IAgentPropertySheet SetVisible
description: IAgentPropertySheet SetVisible
ms.assetid: 53520a64-e99f-4d03-aa36-bcbb4547990c
ms.topic: article
ms.date: 05/31/2018
---

# IAgentPropertySheet::SetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetVisible(
   long bVisible  // property sheet Visible setting 
);
```

Sets the [**Visible**](visible-property.md) property for the Microsoft Agent property sheet.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bVisible"></span><span id="bvisible"></span><span id="BVISIBLE"></span>*bVisible*
</dt> <dd>

Visible property setting. A value of **True** displays the property sheet; a value of **False** hides it.

</dd> </dl>

## See Also

[**IAgentPropertySheet::GetVisible**](iagentpropertysheet--getvisible.md)


 

 




