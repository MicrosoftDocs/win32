---
title: Ribbon.ApplicationMenu property
description: Represents the Application Menu. | Ribbon.ApplicationMenu property
ms.assetid: 6945e976-8ac8-40fa-8e71-31812871b496
keywords:
- Ribbon.ApplicationMenu property Windows Ribbon
topic_type:
- apiref
api_name:
- Ribbon.ApplicationMenu
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Ribbon.ApplicationMenu property

Represents the Application Menu.

## Usage

``` syntax
<Ribbon.ApplicationMenu>
  child elements
</Ribbon.ApplicationMenu>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                                     | Description                                    |
|-----------------------------------------------------------------------------|------------------------------------------------|
| [**ApplicationMenu**](windowsribbon-element-applicationmenu.md)<br/> | Must occur exactly once<br/> <br/> |



## Parent elements



| Element                                                   |
|-----------------------------------------------------------|
| [**Ribbon**](windowsribbon-element-ribbon.md)<br/> |



## Remarks

Required.

May occur at most once for each [**Ribbon**](windowsribbon-element-ribbon.md).

## Examples

The following example demonstrates the basic markup for the **Ribbon.ApplicationMenu** element.

This section of code shows the **Ribbon.ApplicationMenu** control declaration.


```XML
<!-- Control declarations for Application Menu items. -->
<Ribbon.ApplicationMenu>
  <ApplicationMenu CommandName="cmdFileMenu">
    <!-- Most recently used items collection. -->
    <ApplicationMenu.RecentItems>
      <RecentItems CommandName="cmdMRUItems"/>
    </ApplicationMenu.RecentItems>
    <!-- Menu items collection. -->
    <MenuGroup>
      <Button CommandName="cmdNew" />
      <Button CommandName="cmdOpen" />
      <Button CommandName="cmdSave" />
    </MenuGroup>
    <MenuGroup>
      <Button CommandName="cmdPrint" />
      <Button CommandName="cmdExit" />
    </MenuGroup>
  </ApplicationMenu>
</Ribbon.ApplicationMenu>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





