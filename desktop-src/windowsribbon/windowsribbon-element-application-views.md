---
title: Application.Views property
description: Represents a container for each Ribbon framework View, specifically the Ribbon and the ContextPopup.
ms.assetid: e7549b8b-0f95-477a-9024-1a99ee1412c2
keywords:
- Application.Views property Windows Ribbon
topic_type:
- apiref
api_name:
- Application.Views
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Application.Views property

Represents a container for each Ribbon framework View, specifically the [**Ribbon**](windowsribbon-element-ribbon.md) and the [**ContextPopup**](windowsribbon-element-contextpopup.md).

## Usage

``` syntax
<Application.Views>
  child elements
</Application.Views>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                               | Description                                        |
|-----------------------------------------------------------------------|----------------------------------------------------|
| [**ContextPopup**](windowsribbon-element-contextpopup.md)<br/> | May occur one or more times<br/> <br/> |
| [**Ribbon**](windowsribbon-element-ribbon.md)<br/>             | Must occur exactly once<br/> <br/>     |



## Parent elements



| Element                                                             |
|---------------------------------------------------------------------|
| [**Application**](windowsribbon-element-application.md)<br/> |



## Remarks

Required.

Must occur exactly once for each [**Application**](windowsribbon-element-application.md) element.

## Examples

The following example shows an **Application.Views** element that contains a manifest of Ribbon controls, each with a reference to a Command declared in the [**Application.Commands**](windowsribbon-element-application-commands.md) element.


```C++
<Application.Views>
  <Ribbon Name="ScenicRibbonSampleApp">
    <Ribbon.Tabs>
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
    </Ribbon.Tabs>
  </Ribbon>
</Application.Views>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Application.Commands**](windowsribbon-element-application-commands.md)
</dt> </dl>

 

 





