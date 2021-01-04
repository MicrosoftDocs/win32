---
title: DropDownGallery.MenuGroups property
description: Represents a container for a set of drop-down menu items in a Drop-Down Gallery control.
ms.assetid: 594f6ae5-760e-456d-98cd-04ecae0bae99
keywords:
- DropDownGallery.MenuGroups property Windows Ribbon
topic_type:
- apiref
api_name:
- DropDownGallery.MenuGroups
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DropDownGallery.MenuGroups property

Represents a container for a set of drop-down menu items in a [Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md) control.

## Usage

``` syntax
<DropDownGallery.MenuGroups>
  child elements
</DropDownGallery.MenuGroups>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                         | Description                                     |
|-----------------------------------------------------------------|-------------------------------------------------|
| [**MenuGroup**](windowsribbon-element-menugroup.md)<br/> | Must occur at least once<br/> <br/> |



## Parent elements



| Element                                                                     |
|-----------------------------------------------------------------------------|
| [**DropDownGallery**](windowsribbon-element-dropdowngallery.md)<br/> |



## Remarks

Required.

Must occur exactly once for each [**DropDownGallery**](windowsribbon-element-dropdowngallery.md) element.

## Examples

The following example demonstrates the basic markup for the **DropDownGallery.MenuGroups** element.

This section of code shows the **DropDownGallery.MenuGroups** control declaration in a [Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md) Command Space.


```XML
<!-- DropDownGallery -->
<Group CommandName="cmdDropDownGalleryGroup">
  <DropDownGallery CommandName="cmdDropDownGallery"
                   TextPosition="Hide"
                   Type="Commands"
                   ItemHeight="32"
                   ItemWidth="32">
    <DropDownGallery.MenuLayout>
      <FlowMenuLayout Rows="2"
                      Columns="3"
                      Gripper="None"/>
    </DropDownGallery.MenuLayout>
    <DropDownGallery.MenuGroups>
      <MenuGroup>
        <Button CommandName="cmdButton1"></Button>
        <Button CommandName="cmdButton2"></Button>
       </MenuGroup>
       <MenuGroup>
        <Button CommandName="cmdButton3"></Button>
      </MenuGroup>
    </DropDownGallery.MenuGroups>
  </DropDownGallery>
</Group>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Drop-Down Gallery control**](windowsribbon-element-dropdowngallery.md)
</dt> <dt>

[Working with Galleries](ribbon-controls-galleries.md)
</dt> </dl>

 

 





