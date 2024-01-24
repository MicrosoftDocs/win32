---
title: Ribbon.Tabs property
description: Represents a container for all core tabs in a Ribbon.
ms.assetid: b43d0544-c110-4785-85d7-935842b8f03e
keywords:
- Ribbon.Tabs property Windows Ribbon
topic_type:
- apiref
api_name:
- Ribbon.Tabs
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Ribbon.Tabs property

Represents a container for all core tabs in a Ribbon.

## Usage

``` syntax
<Ribbon.Tabs>
  child elements
</Ribbon.Tabs>
```

## Attributes

There are no attributes.

## Child elements



| Element                                             | Description                                     |
|-----------------------------------------------------|-------------------------------------------------|
| [**Tab**](windowsribbon-element-tab.md)<br/> | Must occur at least once<br/> <br/> |



## Parent elements



| Element                                                   |
|-----------------------------------------------------------|
| [**Ribbon**](windowsribbon-element-ribbon.md)<br/> |



## Remarks

Required.

May occur one or more times for each [**Ribbon**](windowsribbon-element-ribbon.md).

## Examples

The following example demonstrates the basic markup for a **Ribbon.Tabs** element with a **Home** [**Tab**](windowsribbon-element-tab.md) declaration.


```C++
<Ribbon Name="ScenicRibbonSampleApp">
  <Ribbon.QuickAccessToolbar>
  ...
  </Ribbon.QuickAccessToolbar>
  <Ribbon.ApplicationMenu>
  ...
  </Ribbon.ApplicationMenu>
  <Ribbon.SizeDefinitions>
  ...
  </Ribbon.SizeDefinitions>
  <Ribbon.Tabs>
  ...
```




```C++
<Tab CommandName="cmdHomeTab">
  <Group CommandName="cmdClipboardGroup" 
         SizeDefinition="ThreeButtons">
    <Button CommandName="cmdCopy"/>
    <Button CommandName="cmdPaste"/>
    <ToggleButton CommandName="cmdMinimize"/>
  </Group>
</Tab>
```




```C++
  ...
  </Ribbon.Tabs>
  <Ribbon.ContextualTabs>
  ...
  </Ribbon.ContextualTabs>
  <Ribbon.HelpButton>
  ...
  </Ribbon.HelpButton>
</Ribbon>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Ribbon.ContextualTabs**](windowsribbon-element-ribbon-contextualtabs.md)
</dt> </dl>

 

 





