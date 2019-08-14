---
title: Exposing Owner-Drawn Menu Items
description: Exposing Owner-Drawn Menu Items
ms.assetid: 93b51cbb-b7b4-4a38-ba69-d6345a269944
ms.topic: article
ms.date: 05/31/2018
---

# Exposing Owner-Drawn Menu Items

Application developers can use the [**MSAAMENUINFO**](/windows/win32/api/oleacc/ns-oleacc-msaamenuinfo) structure to expose the names of owner-drawn menu items. By associating this structure with the owner-drawn menu item data, you do not need to expose the menu items with [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible).

When creating an owner-drawn menu, define a class or structure for the owner-drawn menu item data and create instances of this class for each menu item. Pass in a pointer to the item data when adding items to the menu.

To expose the names of the menu items, the [**MSAAMENUINFO**](/windows/win32/api/oleacc/ns-oleacc-msaamenuinfo) structure must be the first member of the structure that defines the application-specific item data, as shown in the following example:


```C++
// Application-specific owner-drawn menu info struct. Owner-drawn data 
// is a pointer to one of these.
struct MenuEntry
{
    MSAAMENUINFO m_MSAA;       // MSAA info - must be first member
    LPTSTR       m_pName;      // Displayed menu text or NULL for 
                               //   separator item 
    int          m_CmdID;      // Menu command ID 
    int          m_IconIndex;  // Index of icon in bitmap or -1 for
                               //   for separator 
};
```



The [**MSAAMENUINFO**](/windows/win32/api/oleacc/ns-oleacc-msaamenuinfo) structure cannot be a member in a class that contains virtual functions. When the code is compiled, the first member of the class is always a compiler-generated pointer to a table of the virtual functions. To work around this problem, create an item data structure that contains **MSAAMENUINFO** as the first member. The second member is a pointer to an instance of the class that defines the owner-drawn data. The following example demonstrates this technique.


```C++
// Application-defined class that contains the owner-drawn data and 
//  virtual functions that operate on that data.  
class MenuEntry
{
    LPTSTR       m_pName;      // Displayed menu text or NULL for 
                               //  separator item. 
    int          m_CmdID;      // Menu command ID 
    int          m_IconIndex;  // Index of icon in bitmap or -1 for
                               //  separator item 
    virtual void m_AnimateIcon();  
    virtual void m_ChangeIconColor();
}

// Application-defined struct that contains MSAAMENUINFO as first 
//  member. Second member points to owner-drawn data. 
struct MenuInfo
{
    MSAAMENUINFO m_MSAA;       // MSAA info - must be first member
    MenuEntry *pMenuData;      // Points to the owner-drawn data 
}
```



When adding items to the menu, pass a pointer to an instance of the structure that contains [**MSAAMENUINFO**](/windows/win32/api/oleacc/ns-oleacc-msaamenuinfo) to expose the names of the menu items.

 

 




