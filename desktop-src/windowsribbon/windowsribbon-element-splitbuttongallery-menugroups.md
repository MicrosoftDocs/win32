---
title: SplitButtonGallery.MenuGroups property
description: Represents a container for a set of drop-down menu items in a SplitButtonGallery control.
ms.assetid: e30fcf9a-488b-423a-8bc4-fccbc78f74de
keywords:
- SplitButtonGallery.MenuGroups property Windows Ribbon
topic_type:
- apiref
api_name:
- SplitButtonGallery.MenuGroups
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SplitButtonGallery.MenuGroups property

Represents a container for a set of drop-down menu items in a [**SplitButtonGallery**](windowsribbon-element-splitbuttongallery.md) control.

## Usage

``` syntax
<SplitButtonGallery.MenuGroups>
  child elements
</SplitButtonGallery.MenuGroups>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                         | Description                                     |
|-----------------------------------------------------------------|-------------------------------------------------|
| [**MenuGroup**](windowsribbon-element-menugroup.md)<br/> | Must occur at least once<br/> <br/> |



## Parent elements



| Element                                                                           |
|-----------------------------------------------------------------------------------|
| [**SplitButtonGallery**](windowsribbon-element-splitbuttongallery.md)<br/> |



## Remarks

Required.

Must occur exactly once for each [**SplitButtonGallery**](windowsribbon-element-splitbuttongallery.md) element.

## Examples

The following example demonstrates the basic markup for the **SplitButtonGallery.MenuGroups** element.

This section of code shows the **SplitButtonGallery.MenuGroups** control declaration.


```XML
<!-- SplitButtonGallery -->
<Group CommandName="cmdSplitButtonGalleryGroup">
  <SplitButtonGallery CommandName="cmdSplitButtonGallery">
    <SplitButtonGallery.MenuLayout>
      <FlowMenuLayout Rows="2"
                      Columns="3"
                      Gripper="None"/>
    </SplitButtonGallery.MenuLayout>
    <SplitButtonGallery.MenuGroups>
      <MenuGroup>
        <Button CommandName="cmdButton1"></Button>
        <Button CommandName="cmdButton2"></Button>
      </MenuGroup>
      <MenuGroup>
        <Button CommandName="cmdButton3"></Button>
      </MenuGroup>
    </SplitButtonGallery.MenuGroups>
  </SplitButtonGallery>
</Group>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Split Button Gallery control](windowsribbon-controls-splitbuttongallery.md)
</dt> <dt>

[Working with Galleries](ribbon-controls-galleries.md)
</dt> </dl>

 

 





