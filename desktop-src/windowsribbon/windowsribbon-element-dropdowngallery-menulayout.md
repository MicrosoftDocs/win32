---
title: DropDownGallery.MenuLayout property
description: Represents a container for DropDownGallery drop-down menu layouts.
ms.assetid: 7251e889-377d-4d7f-b049-bd81a202774d
keywords:
- DropDownGallery.MenuLayout property Windows Ribbon
topic_type:
- apiref
api_name:
- DropDownGallery.MenuLayout
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DropDownGallery.MenuLayout property

Represents a container for [**DropDownGallery**](windowsribbon-element-dropdowngallery.md) drop-down menu layouts.

## Usage

``` syntax
<DropDownGallery.MenuLayout>
  child elements
</DropDownGallery.MenuLayout>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                                           | Description                                    |
|-----------------------------------------------------------------------------------|------------------------------------------------|
| [**FlowMenuLayout**](windowsribbon-element-flowmenulayout.md)<br/>         | Must occur exactly once<br/> <br/> |
| [**VerticalMenuLayout**](windowsribbon-element-verticalmenulayout.md)<br/> | Must occur exactly once<br/> <br/> |



## Parent elements



| Element                                                                     |
|-----------------------------------------------------------------------------|
| [**DropDownGallery**](windowsribbon-element-dropdowngallery.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**DropDownGallery**](windowsribbon-element-dropdowngallery.md) element.

> [!Note]  
> A maximum of one child element ([**VerticalMenuLayout**](windowsribbon-element-verticalmenulayout.md) or [**FlowMenuLayout**](windowsribbon-element-flowmenulayout.md)) is allowed.

 

## Examples

The following example demonstrates the basic markup for the [**DropDownGallery**](windowsribbon-element-dropdowngallery.md).

This section of code shows the **DropDownGallery.MenuLayout** control declaration.


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

 

 





