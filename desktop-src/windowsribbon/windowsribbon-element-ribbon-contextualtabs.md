---
title: Ribbon.ContextualTabs property
description: Represents a container for contextual tabs.
ms.assetid: 1f57a8d7-97ac-4007-8a36-c6aec5b85e6c
keywords:
- Ribbon.ContextualTabs property Windows Ribbon
topic_type:
- apiref
api_name:
- Ribbon.ContextualTabs
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Ribbon.ContextualTabs property

Represents a container for contextual tabs.

## Usage

``` syntax
<Ribbon.ContextualTabs>
  child elements
</Ribbon.ContextualTabs>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                       | Description                                     |
|---------------------------------------------------------------|-------------------------------------------------|
| [**TabGroup**](windowsribbon-element-tabgroup.md)<br/> | Must occur at least once<br/> <br/> |



## Parent elements



| Element                                                   |
|-----------------------------------------------------------|
| [**Ribbon**](windowsribbon-element-ribbon.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**Ribbon**](windowsribbon-element-ribbon.md).

Contextual tabs are useful for displaying functionality that is relevant only to a specific application context, such as an image formatting tab in a text editor that is displayed only when an image is highlighted. Typically, contextual tabs are not visible until a specific application context occurs, and the application notifies the Ribbon framework.

When displayed, contextual tabs are color coded to differentiate them from regular tabs.

## Examples

The following example demonstrates the basic markup for the **Ribbon.ContextualTabs** element.

This section of code shows a [**TabGroup**](windowsribbon-element-tabgroup.md) Command declaration and two contextual [**Tab**](windowsribbon-element-tab.md) Command declarations.


```XML
<!-- Contextual Tabs -->
<Command Name='cmdContextualTab1'
         LabelTitle='Contextual Tab 1'
         Symbol='ID_CONTEXTUALTAB1'/>
<Command Name='cmdContextualTab2'
         LabelTitle='Contextual Tab 2'
         Symbol='ID_CONTEXTUALTAB2'/>
<Command Name='cmdContextualTabGroup'
         LabelTitle='Contextual Tabs'
         Symbol='ID_CONTEXTUALTAB_GROUP'/>
```



This section of code shows the **Ribbon.ContextualTabs** control declaration with a [**TabGroup**](windowsribbon-element-tabgroup.md) and two contextual [**Tab**](windowsribbon-element-tab.md) controls.


```XML
      <Ribbon.ContextualTabs>
        <TabGroup CommandName='cmdContextualTabGroup'>
          <Tab CommandName='cmdContextualTab1'>
            <!--InRibbonGallery Group-->
            <Group CommandName='cmdInRibbonGalleryGroup'
                   SizeDefinition='OneInRibbonGallery'>
              <InRibbonGallery CommandName='cmdTextSizeGallery3'
                               HasLargeItems='true'
                               ItemHeight='32'
                               ItemWidth='32'
                               MaxColumns='3' >
                <InRibbonGallery.MenuLayout>
                  <FlowMenuLayout Columns='3'
                                  Gripper ='Corner'/>
                </InRibbonGallery.MenuLayout>
              </InRibbonGallery>
            </Group>
            <!--Command Galleries Group-->
            <Group CommandName='cmdCommandGalleriesGroup'
                   SizeDefinition='OneInRibbonGallery'>
              <InRibbonGallery CommandName='cmdCommandGallery1'
                               Type='Commands'
                               MaxRows='3'
                               MaxColumns='3'>
                <InRibbonGallery.MenuLayout>
                  <FlowMenuLayout Columns='3'
                                  Gripper ='Corner'/>
                </InRibbonGallery.MenuLayout>
              </InRibbonGallery>
            </Group>
          </Tab>
          <Tab CommandName='cmdContextualTab2'></Tab>
        </TabGroup>
      </Ribbon.ContextualTabs> 
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Ribbon.Tabs**](windowsribbon-element-ribbon-tabs.md)
</dt> </dl>

 

 





