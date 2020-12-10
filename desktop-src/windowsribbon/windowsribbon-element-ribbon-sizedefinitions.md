---
title: Ribbon.SizeDefinitions property
description: Represents a container for custom layout templates of Ribbon controls.
ms.assetid: 1f5fcffc-7f2e-4763-b0a7-4e8f46534da8
keywords:
- Ribbon.SizeDefinitions property Windows Ribbon
topic_type:
- apiref
api_name:
- Ribbon.SizeDefinitions
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Ribbon.SizeDefinitions property

Represents a container for custom layout templates of Ribbon controls.

## Usage

``` syntax
<Ribbon.SizeDefinitions>
  child elements
</Ribbon.SizeDefinitions>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                                   | Description                                        |
|---------------------------------------------------------------------------|----------------------------------------------------|
| [**SizeDefinition**](windowsribbon-element-sizedefinition.md)<br/> | May occur one or more times<br/> <br/> |



## Parent elements



| Element                                                   |
|-----------------------------------------------------------|
| [**Ribbon**](windowsribbon-element-ribbon.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**Ribbon**](windowsribbon-element-ribbon.md).

## Examples

The following code example illustrates a basic custom template.


```
<Ribbon.SizeDefinitions>
  <SizeDefinition Name="CustomTemplate">
    <GroupSizeDefinition Size="Large">
      <ControlSizeDefinition ImageSize="Large" IsLabelVisible="true" />
    </GroupSizeDefinition>
    <GroupSizeDefinition Size="Medium">
      <ControlSizeDefinition ImageSize="Small" IsLabelVisible="false" />
    </GroupSizeDefinition>
    <GroupSizeDefinition Size="Small">
      <ControlSizeDefinition ImageSize="Small" IsLabelVisible="false" />
    </GroupSizeDefinition>
  </SizeDefinition>
</Ribbon.SizeDefinitions>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Customizing a Ribbon Through Size Definitions and Scaling Policies](windowsribbon-templates.md)
</dt> </dl>

 

 





