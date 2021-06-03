---
title: Customizing a Ribbon Through Size Definitions and Scaling Policies
description: Controls hosted in the ribbon Command bar are subject to layout rules that are enforced by the Windows Ribbon framework and based on a combination of default behaviors and layout templates (both framework-defined and custom) as declared in the Ribbon markup. These rules define the adaptive layout behaviors of the Ribbon framework that influence how controls in the Command bar adapt to various ribbon sizes at run time.
ms.assetid: b5869394-3fa9-4817-add9-54487434fc4f
keywords:
- Windows Ribbon,customizing
- Ribbon,customizing
- Windows Ribbon,SizeDefinition templates
- Ribbon,SizeDefinition templates
- Windows Ribbon,custom templates
- Ribbon,custom templates
- customizing Windows Ribbon
ms.topic: article
ms.date: 05/31/2018
---

# Customizing a Ribbon Through Size Definitions and Scaling Policies

Controls hosted in the ribbon Command bar are subject to layout rules that are enforced by the Windows Ribbon framework and based on a combination of default behaviors and layout templates (both framework-defined and custom) as declared in the Ribbon markup. These rules define the adaptive layout behaviors of the Ribbon framework that influence how controls in the Command bar adapt to various ribbon sizes at run time.

-   [Introduction](#introduction)
    -   [Ribbon SizeDefinition Templates](#customizing-a-ribbon-through-size-definitions-and-scaling-policies)
    -   [Custom Templates](#custom-templates)
-   [Related topics](#related-topics)

## Introduction

Adaptive layout, as defined by the Ribbon framework, is the ability of all controls within the ribbon UI to dynamically adjust their organization, size, format, and relative scale based on changes to the size of the ribbon at run time.

The framework exposes adaptive layout functionality through a set of markup elements that are dedicated to specifying and customizing various layout behaviors. A collection of templates, called [**SizeDefinitions**](windowsribbon-element-sizedefinition.md), is defined by the framework, each of which support various control and layout scenarios. However, the framework also supports custom templates should the predefined templates not provide the UI experience or layouts required by an application.

To display controls in a preferred layout at a particular ribbon size, both predefined templates and custom templates work in conjunction with the [**ScalingPolicy**](windowsribbon-element-scalingpolicy.md) element. This element contains a manifest of size preferences that the framework uses as a guide when rendering the ribbon.

> [!Note]  
> The Ribbon framework provides default layout behaviors based on a set of built-in heuristics for the organization and presentation of controls at run time without the need for the predefined [**SizeDefinition**](windowsribbon-element-sizedefinition.md) templates. However, this capability is intended for prototyping purposes only.

 

### Ribbon SizeDefinition Templates

The Ribbon framework provides a comprehensive set of [**SizeDefinition**](windowsribbon-element-sizedefinition.md) templates that specify size and layout behavior for a [Group](windowsribbon-controls-group.md) of Ribbon controls. These templates cover most common scenarios for organizing controls in a Ribbon application.

To enforce a consistent user experience across Ribbon applications, each [**SizeDefinition**](windowsribbon-element-sizedefinition.md) template imposes restrictions on the controls or the family of controls it supports.

For example, the button family of controls includes:

-   [Button](windowsribbon-controls-button.md)
-   [Toggle Button](windowsribbon-controls-togglebutton.md)
-   [Drop-Down Button](windowsribbon-controls-dropdownbutton.md)
-   [Split Button](windowsribbon-controls-splitbutton.md)
-   [Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md)
-   [Split Button Gallery](windowsribbon-controls-splitbuttongallery.md)
-   [Drop-Down Color Picker](windowsribbon-controls-dropdowncolorpicker.md)

While the input family of controls includes:

-   [Combo Box](windowsribbon-controls-combobox.md)
-   [Spinner](windowsribbon-controls-spinner.md)

[Check Box](windowsribbon-controls-checkbox.md) and [In-Ribbon Gallery](windowsribbon-controls-inribbongallery.md) do not belong to either the button family or the input family. These two controls can be used only where explicitly indicated in a [**SizeDefinition**](windowsribbon-element-sizedefinition.md) template.

The following is a list of the [**SizeDefinition**](windowsribbon-element-sizedefinition.md) templates with a description of the layout and controls allowed by each template.

> [!IMPORTANT]
> If the controls declared in markup do not map exactly to control type, order, and quantity defined in the associated template, a [validation error](windowsribbon-compilationerrors.md) is logged by the [markup compiler](windowsribbon-intentcl.md) and compilation is terminated.

 



OneButton

One button-family control.<br/> Only Large group size is supported.<br/>

![picture of onebutton sizedefinition template.](images/overviews/sizedefinition-onebutton.png)

TwoButtons

Two button-family controls.<br/> Only Large and Medium group sizes are supported.<br/>

![picture of twobuttons large sizedefinition template.](images/overviews/sizedefinition-twobuttons-large.png)

![picture of twobuttons medium sizedefinition template.](images/overviews/sizedefinition-twobuttons-medium.png)

ThreeButtons

Three button-family controls.<br/> Only Large and Medium group sizes are supported.<br/>

![picture of threebuttons large sizedefinition template.](images/overviews/sizedefinition-threebuttons-large.png)

![picture of threebuttons medium sizedefinition template.](images/overviews/sizedefinition-threebuttons-medium.png)

ThreeButtons-OneBigAndTwoSmall

Three button-family controls.<br/> The first button is presented prominently in all three sizes.<br/>

![picture of threebuttons-onebigandtwosmall large sizedefinition template.](images/overviews/sizedefinition-threebuttons-onebigandtwosmall-large.png)

![picture of threebuttons-onebigandtwosmall medium sizedefinition template.](images/overviews/sizedefinition-threebuttons-onebigandtwosmall-medium.png)

![picture of threebuttons-onebigandtwosmall small sizedefinition template.](images/overviews/sizedefinition-threebuttons-onebigandtwosmall-small.png)

ThreeButtonsAndOneCheckBox

Three button-family controls accompanied by a single CheckBox control.<br/> Only Large and Medium group sizes are supported.<br/>

![picture of threebuttonsandonecheckbox large sizedefinition template.](images/overviews/sizedefinition-threebuttonsandonecheckbox-large.png)

![picture of threebuttonsandonecheckbox medium sizedefinition template.](images/overviews/sizedefinition-threebuttonsandonecheckbox-medium.png)

FourButtons

Four button-family controls.<br/>

![picture of fourbuttons large sizedefinition template.](images/overviews/sizedefinition-fourbuttons-large.png)

![picture of fourbuttons medium sizedefinition template.](images/overviews/sizedefinition-fourbuttons-medium.png)

![picture of fourbuttons small sizedefinition template.](images/overviews/sizedefinition-fourbuttons-small.png)

FiveButtons

Five button-family controls.<br/>

![picture of fivebuttons large sizedefinition template.](images/overviews/sizedefinition-fivebuttons-large.png)

![picture of fivebuttons medium sizedefinition template.](images/overviews/sizedefinition-fivebuttons-medium.png)

![picture of fivebuttons small sizedefinition template.](images/overviews/sizedefinition-fivebuttons-small.png)

FiveOrSixButtons

Five button-family controls and an optional sixth button.<br/>

![picture of fiveorsixbuttons large sizedefinition template.](images/overviews/sizedefinition-fiveorsixbuttons-large.png)

![picture of fiveorsixbuttons medium sizedefinition template.](images/overviews/sizedefinition-fiveorsixbuttons-medium.png)

![picture of fiveorsixbuttons small sizedefinition template.](images/overviews/sizedefinition-fiveorsixbuttons-small.png)

SixButtons

Six button-family controls.<br/>

![picture of sixbuttons large sizedefinition template.](images/overviews/sizedefinition-sixbuttons-large.png)

![picture of sixbuttons medium sizedefinition template.](images/overviews/sizedefinition-sixbuttons-medium.png)

![picture of sixbuttons small sizedefinition template.](images/overviews/sizedefinition-sixbuttons-small.png)

SixButtons-TwoColumns

Six button-family controls (alternate presentation).<br/>

![picture of sixbuttons-twocolumns large sizedefinition template.](images/overviews/sizedefinition-sixbuttons-twocolumns-large.png)

![sixbuttons-twocolumns medium sizedefinition template.](images/overviews/sizedefinition-sixbuttons-twocolumns-medium.png)

![picture of sixbuttons-twocolumns small sizedefinition template.](images/overviews/sizedefinition-sixbuttons-twocolumns-small.png)

SevenButtons

Seven button-family controls.<br/>

![picture of sevenbuttons large sizedefinition template.](images/overviews/sizedefinition-sevenbuttons-large.png)

![picture of sevenbuttons mediumsizedefinition template.](images/overviews/sizedefinition-sevenbuttons-medium.png)

![picture of sevenbuttons small sizedefinition template.](images/overviews/sizedefinition-sevenbuttons-small.png)

EightButtons

Eight button-family controls.<br/>

![picture of eightbuttons-lastthreesmall large sizedefinition template.](images/overviews/sizedefinition-eightbuttons-lastthreesmall-large.png)

![picture of eightbuttons-lastthreesmall medium sizedefinition template.](images/overviews/sizedefinition-eightbuttons-lastthreesmall-medium.png)

![picture of eightbuttons-lastthreesmall small sizedefinition template.](images/overviews/sizedefinition-eightbuttons-lastthreesmall-small.png)

EightButtons-LastThreeSmall

Eight button-family controls (alternate presentation).<br/>

> [!Note]  
> All control elements declared with this template must be contained in two [**ControlGroup**](windowsribbon-element-controlgroup.md) elements: one for the first five elements and one for the last three elements.

<br/> The following example demonstrates the markup required for this template.<br/>

```
<Group CommandName="cmdSizeDefinitionsGroup" 
       SizeDefinition="EightButtons-LastThreeSmall">
  <ControlGroup>
    <Button CommandName="cmdSDButton1" />
    <Button CommandName="cmdSDButton2" />
    <Button CommandName="cmdSDButton3" />
    <Button CommandName="cmdSDButton4" />
    <Button CommandName="cmdSDButton5" />
  </ControlGroup>
  <ControlGroup>
    <Button CommandName="cmdSDButton6" />
    <Button CommandName="cmdSDButton7" />
    <Button CommandName="cmdSDButton8" />
  </ControlGroup>
</Group>
```



![picture of eightbuttons large sizedefinition template.](images/overviews/sizedefinition-eightbuttons-large.png)

![picture of eightbuttons medium sizedefinition template.](images/overviews/sizedefinition-eightbuttons-medium.png)

![picture of eightbuttons small sizedefinition template.](images/overviews/sizedefinition-eightbuttons-small.png)

NineButtons

Nine button-family controls.

![picture of ninebuttons large sizedefinition template.](images/overviews/sizedefinition-ninebuttons-large.png)

![picture of ninebuttons medium sizedefinition template.](images/overviews/sizedefinition-ninebuttons-medium.png)

![picture of ninebuttons small sizedefinition template.](images/overviews/sizedefinition-ninebuttons-small.png)

TenButtons

Ten button-family controls.

![picture of tenbuttons large sizedefinition template.](images/overviews/sizedefinition-tenbuttons-large.png)

![picture of tenbuttons medium sizedefinition template.](images/overviews/sizedefinition-tenbuttons-medium.png)

![picture of tenbuttons small sizedefinition template.](images/overviews/sizedefinition-tenbuttons-small.png)

ElevenButtons

Eleven button-family controls.

![picture of elevenbuttons large sizedefinition template.](images/overviews/sizedefinition-elevenbuttons-large.png)

![picture of elevenbuttons medium sizedefinition template.](images/overviews/sizedefinition-elevenbuttons-medium.png)

![picture of elevenbuttons small sizedefinition template.](images/overviews/sizedefinition-elevenbuttons-small.png)

OneFontControl

One [**FontControl**](windowsribbon-element-fontcontrol.md).

Only Large and Medium group sizes are supported.

> [!IMPORTANT]
> Including a [**FontControl**](windowsribbon-element-fontcontrol.md) within a custom template definition is not supported by the framework.

 

![picture of onefontcontrol large sizedefinition template.](images/overviews/sizedefinition-onefontcontrol-large.png)

![picture of onefontcontrol medium sizedefinition template.](images/overviews/sizedefinition-onefontcontrol-medium.png)

OneInRibbonGallery

One [**InRibbonGallery**](windowsribbon-element-inribbongallery.md) control.

Only Large and Small group sizes are supported.

![picture of oneinribbongallery large sizedefinition template.](images/overviews/sizedefinition-oneinribbongallery-large.png)

![picture of oneinribbongallery small sizedefinition template.](images/overviews/sizedefinition-oneinribbongallery-small.png)

InRibbonGalleryAndBigButton

One [**InRibbonGallery**](windowsribbon-element-inribbongallery.md) control and a button-family control.

Only Large and Small group sizes are supported.

![picture of inribbongalleryandbigbutton large sizedefinition template.](images/overviews/sizedefinition-inribbongalleryandbigbutton-large.png)

![picture of inribbongalleryandbigbutton small sizedefinition template.](images/overviews/sizedefinition-inribbongalleryandbigbutton-small.png)

InRibbonGalleryAndButtons-GalleryScalesFirst

One [In-Ribbon Gallery](windowsribbon-controls-inribbongallery.md) control and two or three button-family controls.

The gallery collapses to Popup representation in Medium and Small group sizes.

![picture of inribbongalleryandbuttons-galleryscalesfirst large sizedefinition template.](images/overviews/sizedefinition-inribbongalleryandbuttons-galleryscalesfirst-large.png)

![picture of inribbongalleryandbuttons-galleryscalesfirst medium sizedefinition template.](images/overviews/sizedefinition-inribbongalleryandbuttons-galleryscalesfirst-medium.png)

![picture of inribbongalleryandbuttons-galleryscalesfirst small sizedefinition template.](images/overviews/sizedefinition-inribbongalleryandbuttons-galleryscalesfirst-small.png)

ButtonGroups

A complex arrangement of 32 button-family controls (most of which are optional).

> [!Note]  
> Aside from the optional full-sized button of the large ButtonGroups template, all control elements declared with this template must be contained in [**ControlGroup**](windowsribbon-element-controlgroup.md) elements.

 

The following example demonstrates the markup required to display all 32 control elements (required and optional) with this template.


```
<Group CommandName="cmdSizeDefinitionsGroup"
       SizeDefinition="ButtonGroups">
  <!-- Row 1 -->
  <ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton1" />
      <Button CommandName="cmdSDButton2" />
      <Button CommandName="cmdSDButton3" />
      <Button CommandName="cmdSDButton4" />
      <Button CommandName="cmdSDButton5" />
      <Button CommandName="cmdSDButton6" />
      <Button CommandName="cmdSDButton7" />
      <Button CommandName="cmdSDButton8" />
      <Button CommandName="cmdSDButton9" />
      <Button CommandName="cmdSDButton10" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton11" />
      <Button CommandName="cmdSDButton12" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton13" />
      <Button CommandName="cmdSDButton14" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton15" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton16" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton17" />
      <Button CommandName="cmdSDButton18" />
    </ControlGroup>
  </ControlGroup>
  <!-- Row 2 -->
  <ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton19" />
      <Button CommandName="cmdSDButton20" />
      <Button CommandName="cmdSDButton21" />
      <Button CommandName="cmdSDButton22" />
      <Button CommandName="cmdSDButton23" />
      <Button CommandName="cmdSDButton24" />
      <Button CommandName="cmdSDButton25" />
      <Button CommandName="cmdSDButton26" />
      <Button CommandName="cmdSDButton27" />
      <Button CommandName="cmdSDButton28" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton29" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton30" />
      <Button CommandName="cmdSDButton31" />
    </ControlGroup>
  </ControlGroup>
  <Button CommandName="cmdSDButton32" />            
</Group>
```



![picture of buttongroups large sizedefinition template.](images/overviews/sizedefinition-buttongroups-large.png)

![picture of buttongroups medium sizedefinition template.](images/overviews/sizedefinition-buttongroups-medium.png)

![picture of buttongroups small sizedefinition template.](images/overviews/sizedefinition-buttongroups-small.png)

ButtonGroupsAndInputs

Two input-family controls (the second is optional) followed by a complex arrangement of 29 button-family controls (most of which are optional).

Only Large and Medium group sizes are supported.

> [!Note]  
> All control elements declared with this template must be contained in [**ControlGroup**](windowsribbon-element-controlgroup.md) elements.

 

The following example demonstrates the markup required to display all control elements (required and optional) with this template.


```
<Group CommandName="cmdSizeDefinitionsGroup" 
       SizeDefinition="ButtonGroupsAndInputs">
  <!-- Row 1 -->
  <ControlGroup>
    <ControlGroup>
      <ComboBox CommandName="cmdSDComboBox" />
      <Spinner CommandName="cmdSDSpinner" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton1" />
      <Button CommandName="cmdSDButton2" />
      <Button CommandName="cmdSDButton3" />
      <Button CommandName="cmdSDButton4" />
      <Button CommandName="cmdSDButton5" />
      <Button CommandName="cmdSDButton6" />
      <Button CommandName="cmdSDButton7" />
      <Button CommandName="cmdSDButton8" />
      <Button CommandName="cmdSDButton9" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton10" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton11" />
      <Button CommandName="cmdSDButton12" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton13" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton14" />
    </ControlGroup>
  </ControlGroup>
  <!-- Row 2 -->  
  <ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton15" />
      <Button CommandName="cmdSDButton16" />
      <Button CommandName="cmdSDButton17" />
      <Button CommandName="cmdSDButton18" />
      <Button CommandName="cmdSDButton19" />
      <Button CommandName="cmdSDButton20" />
      <Button CommandName="cmdSDButton21" />
      <Button CommandName="cmdSDButton22" />
      <Button CommandName="cmdSDButton23" />
      <Button CommandName="cmdSDButton24" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton25" />
      <Button CommandName="cmdSDButton26" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton27" />
      <Button CommandName="cmdSDButton28" />
    </ControlGroup>
    <ControlGroup>
      <Button CommandName="cmdSDButton29" />
    </ControlGroup>
  </ControlGroup>
</Group>
```



![picture of buttongroupsandinputs large sizedefinition template.](images/overviews/sizedefinition-buttongroupsandinputs-large.png)

![picture of buttongroupsandinputs medium sizedefinition template.](images/overviews/sizedefinition-buttongroupsandinputs-medium.png)

BigButtonsAndSmallButtonsOrInputs

Two button-family controls (both optional) followed by two or three button or input-family controls.

Only Large and Medium group sizes are supported.

![picture of bigbuttonsandsmallbuttonsorinputs large sizedefinition template.](images/overviews/sizedefinition-bigbuttonsandsmallbuttonsorinputs-large.png)

![picture of bigbuttonsandsmallbuttonsorinputs medium sizedefinition template.](images/overviews/sizedefinition-bigbuttonsandsmallbuttonsorinputs-medium.png)



 

### Basic SizeDefinition Example

The following code example provides a basic demonstration of how to declare a [**SizeDefinition**](windowsribbon-element-sizedefinition.md) template in Ribbon markup.

The *OneInRibbonGallery* [**SizeDefinition**](windowsribbon-element-sizedefinition.md) is used for this particular example, but all framework templates are specified in a similar fashion.


```XML
<!-- InRibbonGallery -->
<Group CommandName="cmdInRibbonGalleryGroup" SizeDefinition="OneInRibbonGallery">
  <InRibbonGallery CommandName="cmdInRibbonGallery"
                   MaxColumns="10"
                   MaxColumnsMedium="5"
                   MinColumnsLarge="5"
                   MinColumnsMedium="3"
                   Type="Items">
    <InRibbonGallery.MenuLayout>
      <VerticalMenuLayout Rows="2"
                          Gripper="Vertical"/>
    </InRibbonGallery.MenuLayout>
    <InRibbonGallery.MenuGroups>
      <MenuGroup>
        <Button CommandName="cmdButton1"></Button>
        <Button CommandName="cmdButton2"></Button>
      </MenuGroup>
      <MenuGroup>
        <Button CommandName="cmdButton3"></Button>
      </MenuGroup>
    </InRibbonGallery.MenuGroups>            
  </InRibbonGallery>
</Group>
```



### Complex SizeDefinition Example with Scaling Policies

The collapsing behavior of [**SizeDefinition**](windowsribbon-element-sizedefinition.md) templates can be controlled through the use of scaling policies in the Ribbon markup.

The [**ScalingPolicy**](windowsribbon-element-scalingpolicy.md) element contains a manifest of [**ScalingPolicy.IdealSizes**](windowsribbon-element-scalingpolicy-idealsizes.md) and [**Scale**](windowsribbon-element-scale.md) declarations that specify adaptive layout preferences for one or more [**Group**](windowsribbon-element-group.md) elements when the Ribbon is resized.

> [!Note]  
> It is highly recommended that adequate scaling policy detail be specified such that most, if not all, [**Group**](windowsribbon-element-group.md) elements are associated with a [**Scale**](windowsribbon-element-scale.md) element where the *Size* attribute is equal to `Popup`. Doing so allows the framework to render the ribbon at the smallest size possible, and support the broadest range of display devices, before automatically introducing a scrolling mechanism.

 

The following code example demonstrates a [**ScalingPolicy**](windowsribbon-element-scalingpolicy.md) manifest that specifies a [**ScalingPolicy.IdealSizes**](windowsribbon-element-scalingpolicy-idealsizes.md) [**SizeDefinition**](windowsribbon-element-sizedefinition.md) preference for each of four groups of controls on a **Home** tab. In addition, [**Scale**](windowsribbon-element-scale.md) elements are specified to influence the collapsing behavior, in descending size order, of each group.


```C++
<Tab CommandName="Home">
  <Tab.ScalingPolicy>
    <ScalingPolicy>
      <ScalingPolicy.IdealSizes>
        <Scale Group="GroupClipboard" Size="Medium"/>
        <Scale Group="GroupView" Size="Large"/>
        <Scale Group="GroupFont" Size="Large"/>
        <Scale Group="GroupParagraph" Size="Large"/>
      </ScalingPolicy.IdealSizes>
      <Scale Group="GroupClipboard" Size="Small"/>
      <Scale Group="GroupClipboard" Size="Popup"/>
      <Scale Group="GroupFont" Size="Medium"/>
      <Scale Group="GroupFont" Size="Popup"/>
      <Scale Group="GroupParagraph" Size="Medium"/>
      <Scale Group="GroupParagraph" Size="Popup"/>
      <!-- 
        GroupView group is associated with the OneButton SizeDefinition.
        Since this template is constrained to one size (Large) there
        is no need to declare further scaling preferences.
      -->
    </ScalingPolicy>
  </Tab.ScalingPolicy>

  <Group CommandName="GroupClipboard" SizeDefinition="FourButtons">
    <Button CommandName="Paste"/>
    <Button CommandName="Cut"/>
    <Button CommandName="Copy"/>
    <Button CommandName="SelectAll"/>
  </Group>

  <Group CommandName="GroupFont"  ApplicationModes="1">
    <FontControl CommandName="Font" FontType="FontWithColor" />
  </Group>

  <Group CommandName="GroupParagraph"  ApplicationModes="1" SizeDefinition="ButtonGroups">
    <ControlGroup>
      <ControlGroup>
        <ToggleButton CommandName="Numbered" />
        <ToggleButton CommandName="Bulleted" />
      </ControlGroup>
    </ControlGroup>
    <ControlGroup>
      <ControlGroup>
        <ToggleButton CommandName="LeftJustify" />
        <ToggleButton CommandName="CenterJustify" />
        <ToggleButton CommandName="RightJustify" />
      </ControlGroup>
      <ControlGroup/>
      <ControlGroup>
        <Button CommandName="Outdent" />
        <Button CommandName="Indent" />
      </ControlGroup>
    </ControlGroup>
  </Group>

  <Group CommandName="GroupView" SizeDefinition="OneButton" >
    <ToggleButton CommandName="ViewSource"/>
  </Group>

</Tab>
```



### Custom Templates

If the default layout behaviors and the predefined [**SizeDefinition**](windowsribbon-element-sizedefinition.md) templates do not offer the flexibility or support for a particular layout scenario, custom templates are supported by the Ribbon framework through the [**Ribbon.SizeDefinitions**](windowsribbon-element-ribbon-sizedefinitions.md) element.

Custom templates can be declared in two ways: a standalone method using the [**Ribbon.SizeDefinitions**](windowsribbon-element-ribbon-sizedefinitions.md) element for declaring reusable, named templates or an inline method that is [**Group**](windowsribbon-element-group.md)-specific.

### Standalone Template

The following code example illustrates a basic, reusable custom template.


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



### Inline Template

The following code examples illustrate a basic inline custom template for a group of four buttons.

This section of code shows the Command declarations for a group of buttons. Large and small image resources are also specified here.


```XML
<!-- Button -->
<Command Name="cmdButtonGroup"
         Symbol="cmdButtonGroup"
         Comment="Button Group"
         LabelTitle="ButtonGroup"/>
<Command Name="cmdButton1"
         Symbol="cmdButton1"
         Comment="Button1"
         LabelTitle="Button1"/>
<Command Name="cmdButton2"
         Symbol="cmdButton2"
         Comment="Button2"
         LabelTitle="Button2"/>
<Command Name="cmdButton3"
         Symbol="cmdButton3"
         Comment="Button3"
         LabelTitle="Button3"/>
<Command Name="cmdButtonGroup2"
         Symbol="cmdButtonGroup2"
         Comment="Button Group2"
         LabelTitle="ButtonGroup2"/>
<Command Name="cmdButtonG21"
         Symbol="cmdButtonG21"
         Comment="ButtonG21"
         LabelTitle="ButtonG21">
  <Command.LargeImages>
    <Image Source="res/large.bmp"/>
  </Command.LargeImages>
  <Command.SmallImages>
    <Image Source="res/small.bmp"/>
  </Command.SmallImages>
</Command>
<Command Name="cmdButtonG22"
         Symbol="cmdButtonG22"
         Comment="ButtonG22"
         LabelTitle="ButtonG22">
  <Command.LargeImages>
    <Image Source="res/large.bmp"/>
  </Command.LargeImages>
  <Command.SmallImages>
    <Image Source="res/small.bmp"/>
  </Command.SmallImages>
</Command>
<Command Name="cmdButtonG23"
         Symbol="cmdButtonG23"
         Comment="ButtonG23"
         LabelTitle="ButtonG23">
  <Command.LargeImages>
    <Image Source="res/large.bmp"/>
  </Command.LargeImages>
  <Command.SmallImages>
    <Image Source="res/small.bmp"/>
  </Command.SmallImages>
</Command>
<Command Name="cmdButtonG24"
         Symbol="cmdButtonG24"
         Comment="ButtonG24"
         LabelTitle="ButtonG24">
  <Command.LargeImages>
    <Image Source="res/large.bmp"/>
  </Command.LargeImages>
  <Command.SmallImages>
    <Image Source="res/small.bmp"/>
  </Command.SmallImages>
</Command>
```



This section of code demonstrates how to define large, medium, and small [**GroupSizeDefinition**](windowsribbon-element-groupsizedefinition.md) templates to display the four buttons at various sizes and layouts. The [**ScalingPolicy**](windowsribbon-element-scalingpolicy.md) declaration for the tab defines which template is used for a group of controls based on the ribbon size and space required by the active tab.


```XML
        <Tab CommandName="cmdTab6">
          <Tab.ScalingPolicy>
            <ScalingPolicy>
              <ScalingPolicy.IdealSizes>
                <Scale Group="cmdButtonGroup"
                       Size="Large"/>
                <Scale Group="cmdButtonGroup2"
                       Size="Large"/>
                <Scale Group="cmdToggleButtonGroup"
                       Size="Large"/>
              </ScalingPolicy.IdealSizes>
              <Scale Group="cmdButtonGroup"
                     Size="Medium"/>
              <Scale Group="cmdButtonGroup2"
                     Size="Medium"/>
              <Scale Group="cmdButtonGroup2"
                     Size="Small"/>
              <Scale Group="cmdButtonGroup2"
                     Size="Popup"/>
            </ScalingPolicy>
          </Tab.ScalingPolicy>

          <Group CommandName="cmdButtonGroup2">
            <SizeDefinition>
              <ControlNameMap>
                <ControlNameDefinition Name="button1"/>
                <ControlNameDefinition Name="button2"/>
                <ControlNameDefinition Name="button3"/>
                <ControlNameDefinition Name="button4"/>
              </ControlNameMap>
              <GroupSizeDefinition Size="Large">
                <ControlGroup>
                  <ControlSizeDefinition ControlName="button1"
                                         ImageSize="Large"
                                         IsLabelVisible="true" />
                  <ControlSizeDefinition ControlName="button2"
                                         ImageSize="Large"
                                         IsLabelVisible="true" />
                </ControlGroup>
                <ColumnBreak ShowSeparator="true"/>
                <ControlGroup>
                  <ControlSizeDefinition ControlName="button3"
                                         ImageSize="Large"
                                        IsLabelVisible="true" />
                  <ControlSizeDefinition ControlName="button4"
                                        ImageSize="Large"
                                        IsLabelVisible="true" />
                </ControlGroup>
              </GroupSizeDefinition>
              <GroupSizeDefinition Size="Medium">
                <Row>
                  <ControlSizeDefinition ControlName="button1"
                                         ImageSize="Small"
                                         IsLabelVisible="true" />
                  <ControlSizeDefinition ControlName="button3"
                                         ImageSize="Small"
                                         IsLabelVisible="true" />
                </Row>
                <Row>
                  <ControlSizeDefinition ControlName="button2"
                                         ImageSize="Small"
                                         IsLabelVisible="true" />
                  <ControlSizeDefinition ControlName="button4"
                                         ImageSize="Small"
                                         IsLabelVisible="true" />
                </Row>
              </GroupSizeDefinition>
              <GroupSizeDefinition Size="Small">
                <Row>
                  <ControlSizeDefinition ControlName="button1"
                                         ImageSize="Small"
                                         IsLabelVisible="true" />
                  <ControlSizeDefinition ControlName="button3"
                                         ImageSize="Small"
                                         IsLabelVisible="false" />
                </Row>
                <Row>
                  <ControlSizeDefinition ControlName="button2"
                                         ImageSize="Small"
                                         IsLabelVisible="true" />
                  <ControlSizeDefinition ControlName="button4"
                                         ImageSize="Small"
                                         IsLabelVisible="false" />
                </Row>
              </GroupSizeDefinition>
            </SizeDefinition>
            <Button CommandName="cmdButtonG21"></Button>
            <Button CommandName="cmdButtonG22"></Button>
            <Button CommandName="cmdButtonG23"></Button>
            <Button CommandName="cmdButtonG24"></Button>
          </Group>
          <Group CommandName="cmdCheckBoxGroup">
            <CheckBox CommandName="cmdCheckBox"></CheckBox>
          </Group>
          <Group CommandName="cmdToggleButtonGroup"
                 SizeDefinition="OneButton">
            <ToggleButton CommandName="cmdToggleButton"></ToggleButton>
          </Group>
          <Group CommandName="cmdButtonGroup"
                 SizeDefinition="ThreeButtons">
            <Button CommandName="cmdButton1"></Button>
            <Button CommandName="cmdButton2"></Button>
            <Button CommandName="cmdButton3"></Button>
          </Group>
        </Tab>
```



The following images show how the templates from the previous example are applied to the ribbon UI to accommodate a decrease in ribbon size.



|  Type  |      Image                                                                                         |
|--------|----------------------------------------------------------------------------------------------------|
| Large  | ![picture of an inline large custom template.](images/overviews/sizedefinition-custom-large.png)   |
| Medium | ![picture of an inline medium custom template.](images/overviews/sizedefinition-custom-medium.png) |
| Small  | ![picture of an inline small custom template.](images/overviews/sizedefinition-custom-small.png)   |
| Popup  | ![picture of an inline popup custom template.](images/overviews/sizedefinition-custom-popup.png)   |



 

## Related topics

<dl> <dt>

[**SizeDefinition**](windowsribbon-element-sizedefinition.md)
</dt> <dt>

[**Scale**](windowsribbon-element-scale.md)
</dt> <dt>

[**Group**](windowsribbon-element-group.md)
</dt> </dl>

 

 





